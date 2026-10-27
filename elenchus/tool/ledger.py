#!/usr/bin/env python3
"""The claim ledger and its gate. Roadmap M1 (T-11, T-13, T-14, T-16, T-64).

A claim not in the ledger has no tier and may not be cited. The ledger is machine-readable, and this
module is the gate over it. Like every gate here it can say *no* and cannot say *yes*: a clean run
means the bookkeeping holds, and says nothing about whether any claim is true.

Tiers, weakest to strongest:  X < C < L < B < A.

Checks (severity in brackets):
  LEDGER_SCHEMA            malformed record, unknown schema version, unknown tier or kind     [block]
  LEDGER_DUPLICATE_ID      two records with one identifier                                    [block]
  LEDGER_ID_TIER_MISMATCH  the tier letter inside the identifier disagrees with the tier      [block]
  LEDGER_ORPHAN            depends_on names a claim that is not in the ledger                 [block]
  LEDGER_KIND_OVERCLAIM    tier above the cap for the declared evidence kind                  [block]
  LEDGER_TIER_INVERSION    claim filed above the EFFECTIVE tier of something it rests on      [block]
  LEDGER_CYCLE             a claim rests on itself                                            [block]
  LEDGER_NO_EVIDENCE       evidence is not a sha256 digest                                    [block]
  LEDGER_EVIDENCE_MISSING  (with --evidence-dir) the digest names a blob that is not there    [block]
  LEDGER_EVIDENCE_MISMATCH (with --evidence-dir) the blob does not hash to its digest         [block]
  LEDGER_NO_PROVENANCE     (with --evidence-dir) a solver_reading blob lacks its provenance   [block]
  LEDGER_UNAUDITED_TIER_A  a Tier A row nobody has audited for statement adequacy             [flag]

Absence assertion: an empty ledger is INCOMPLETE (exit 2), never a clean pass. "No findings" and
"never looked" must not be the same output.

Exit codes: 0 no findings, 1 findings, 2 the check could not run or looked at nothing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

TIERS = "XCLBA"
RANK = {t: i for i, t in enumerate(TIERS)}
SCHEMA_VERSION = 1

# R-12: a claim's tier is capped by how it was established.
KIND_CAP = {
    "lean_axioms": "A",
    "exact_harness": "B",
    "citation": "L",
    "argument": "C",
    "numeric": "X",
    "llm_output": "X",
    "solver_reading": "X",  # an external instrument's reading, filed by the bridge. Never above X.
}

SEVERITY = {
    "LEDGER_SCHEMA": "block",
    "LEDGER_DUPLICATE_ID": "block",
    "LEDGER_ID_TIER_MISMATCH": "block",
    "LEDGER_ORPHAN": "block",
    "LEDGER_KIND_OVERCLAIM": "block",
    "LEDGER_TIER_INVERSION": "block",
    "LEDGER_CYCLE": "block",
    "LEDGER_NO_EVIDENCE": "block",
    "LEDGER_EVIDENCE_MISSING": "block",
    "LEDGER_EVIDENCE_MISMATCH": "block",
    "LEDGER_NO_PROVENANCE": "block",
    "LEDGER_UNAUDITED_TIER_A": "flag",
}

DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
ID_TIER = re.compile(r"^[A-Z0-9]{1,16}-([XCLBA])-[0-9]{1,12}$")
WEAKEN_RULES = ("kindcap", "closure")


def digest_of(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


PROVENANCE_TEXT = ("producer", "producer_version", "tool", "library", "library_revision")


def provenance_problem(raw: bytes) -> str | None:
    """R-64, from the gate's side. Written separately from the bridge's check so the two are independent
    implementations of one rule (tests/unit/test_provenance.py requires them to agree)."""
    try:
        body = json.loads(raw)
    except ValueError:
        return "the evidence blob is not JSON"
    p = body.get("provenance") if isinstance(body, dict) else None
    if not isinstance(p, dict):
        return "no provenance object"
    for k in PROVENANCE_TEXT:
        if not isinstance(p.get(k), str) or not p[k].strip():
            return f"provenance.{k} missing or empty"
    tc = p.get("toolchain")
    if not isinstance(tc, dict) or not tc or not all(isinstance(v, str) and v.strip() for v in tc.values()):
        return "provenance.toolchain missing or empty"
    if "input" not in p:
        return "provenance.input missing"
    return None


def _finding(code: str, cid: str, message: str) -> dict:
    return {"code": code, "severity": SEVERITY[code], "claim": cid, "message": message}


def _schema_errors(c) -> list[str]:
    if not isinstance(c, dict):
        return ["record is not an object"]
    errs = []
    if not isinstance(c.get("id"), str) or not ID_TIER.fullmatch(c["id"]):
        errs.append("id must look like PREFIX-<tier letter>-<digits>")
    if not isinstance(c.get("statement"), str) or not c.get("statement", "").strip():
        errs.append("statement must be a non-empty string")
    if not isinstance(c.get("tier"), str) or c["tier"] not in RANK:
        errs.append(f"tier {c.get('tier')!r} is not one of {list(TIERS)}")
    if not isinstance(c.get("kind"), str) or c["kind"] not in KIND_CAP:
        errs.append(f"kind {c.get('kind')!r} is not one of {sorted(KIND_CAP)}")
    deps = c.get("depends_on")
    if not isinstance(deps, list) or not all(isinstance(d, str) for d in deps):
        errs.append("depends_on must be a list of identifiers")
    if "evidence" not in c:
        errs.append("evidence field is absent")
    if "audit" in c and c["audit"] is not None and not isinstance(c["audit"], dict):
        errs.append("audit must be an object or null; it is never a model")
    return errs


def _sccs(edges: dict[str, list[str]]) -> list[list[str]]:
    """Tarjan, iterative. Components come out dependencies-first."""
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []
    out: list[list[str]] = []
    counter = 0
    for root in edges:
        if root in index:
            continue
        index[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        work = [(root, iter(edges[root]))]
        while work:
            v, it = work[-1]
            for w in it:
                if w not in index:
                    index[w] = low[w] = counter
                    counter += 1
                    stack.append(w)
                    on_stack.add(w)
                    work.append((w, iter(edges[w])))
                    break
                if w in on_stack:
                    low[v] = min(low[v], index[w])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        w = stack.pop()
                        on_stack.discard(w)
                        comp.append(w)
                        if w == v:
                            break
                    out.append(comp)
    return out


def check(ledger: dict, weaken: list[str] | None = None, evidence_dir: str | None = None) -> dict:
    """Returns {"findings": [...], "skipped": [...], "claims": n}."""
    weaken = weaken or []
    findings: list[dict] = []

    if not isinstance(ledger, dict):
        return {"findings": [], "skipped": ["ledger is not a JSON object: nothing was checked"], "claims": 0}
    sv = ledger.get("schema_version")
    if type(sv) is not int or sv != SCHEMA_VERSION:
        # A consumer refuses a version it does not know rather than guessing (T-11).
        return {"findings": [_finding("LEDGER_SCHEMA", "-", f"unsupported schema_version "
                                      f"{ledger.get('schema_version')!r}; this reader knows {SCHEMA_VERSION}")],
                "skipped": [], "claims": 0}

    claims = ledger.get("claims")
    if not isinstance(claims, list) or not claims:
        return {"findings": [], "skipped": ["ledger holds no claims: nothing was checked"], "claims": 0}

    by_id: dict[str, dict] = {}
    valid: list[dict] = []
    for i, c in enumerate(claims):
        errs = _schema_errors(c)
        cid = c.get("id", f"#{i}") if isinstance(c, dict) else f"#{i}"
        if errs:
            findings.append(_finding("LEDGER_SCHEMA", str(cid), "; ".join(errs)))
            continue
        if c["id"] in by_id:
            findings.append(_finding("LEDGER_DUPLICATE_ID", c["id"], "identifier appears more than once"))
            continue
        by_id[c["id"]] = c
        valid.append(c)

    # Effective tier = min(own tier, effective tier of everything it rests on, transitively). This is the
    # closure (T-14): a claim is judged against what its ancestors are worth, not what they claim.
    # Computed over strongly connected components, iteratively: a cycle's members all reach one another,
    # so they share one effective tier, and a 5000-deep chain is judged rather than crashing the gate.
    edges = {i: [d for d in c["depends_on"] if d in by_id] for i, c in by_id.items()}
    effective: dict[str, tuple[int, str]] = {}   # id -> (rank, id of the limiting claim)
    cyclic: set[str] = set()
    for comp in _sccs(edges):                    # dependencies are emitted before their dependants
        members = set(comp)
        best = min((RANK[by_id[m]["tier"]], m) for m in comp)
        for m in comp:
            for d in edges[m]:
                if d not in members and effective[d] < best:
                    best = effective[d]
        for m in comp:
            effective[m] = best
        if len(comp) > 1 or comp[0] in edges[comp[0]]:
            cyclic.update(comp)
    for cid in sorted(cyclic):
        findings.append(_finding("LEDGER_CYCLE", cid, "claim rests on itself, directly or transitively"))

    for c in valid:
        cid, tier = c["id"], c["tier"]

        m = ID_TIER.fullmatch(cid)
        if m and m.group(1) != tier:
            findings.append(_finding("LEDGER_ID_TIER_MISMATCH", cid,
                                     f"identifier says tier {m.group(1)} but the record says {tier}"))

        cap = KIND_CAP[c["kind"]]
        if "kindcap" not in weaken and RANK[tier] > RANK[cap]:
            findings.append(_finding("LEDGER_KIND_OVERCLAIM", cid,
                                     f"tier {tier} exceeds cap {cap} for evidence kind '{c['kind']}'"))

        worst = None
        for d in c["depends_on"]:
            if d not in by_id:
                findings.append(_finding("LEDGER_ORPHAN", cid, f"rests on '{d}', which is not in the ledger"))
                continue
            if "closure" in weaken:
                seen = (RANK[by_id[d]["tier"]], d)      # direct tier only: the naive check
            else:
                seen = effective[d]                     # effective tier: the closure
            if RANK[tier] > seen[0] and (worst is None or seen[0] < worst[0]):
                worst = seen
        if worst is not None:
            findings.append(_finding("LEDGER_TIER_INVERSION", cid,
                                     f"tier {tier} exceeds effective tier {TIERS[worst[0]]} of its "
                                     f"ancestor {worst[1]}"))

        ev = c.get("evidence")
        if not isinstance(ev, str) or not DIGEST.fullmatch(ev):
            findings.append(_finding("LEDGER_NO_EVIDENCE", cid,
                                     "evidence must be a 'sha256:<64 hex>' digest, never a path or null"))
        elif evidence_dir is not None:
            blob = os.path.join(evidence_dir, ev.split(":", 1)[1] + ".json")
            if not os.path.isfile(blob):
                findings.append(_finding("LEDGER_EVIDENCE_MISSING", cid, f"no blob for {ev}"))
            else:
                with open(blob, "rb") as fh:
                    raw = fh.read()
                got = digest_of(raw)
                if got != ev:
                    findings.append(_finding("LEDGER_EVIDENCE_MISMATCH", cid,
                                             f"blob hashes to {got}, the record says {ev}"))
                elif c["kind"] == "solver_reading":
                    problem = provenance_problem(raw)
                    if problem:
                        findings.append(_finding("LEDGER_NO_PROVENANCE", cid, f"{problem} [R-64]"))

        if tier == "A" and c.get("audit") is None:
            findings.append(_finding("LEDGER_UNAUDITED_TIER_A", cid,
                                     "Tier A with audit null: the kernel checked the proof, and no person "
                                     "has yet certified the statement means what its gloss claims"))

    return {"findings": findings, "skipped": [], "claims": len(valid),
            "evidence_verified": evidence_dir is not None}


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def next_id(ledger: dict, prefix: str, tier: str) -> str:
    n = 0
    pat = re.compile(rf"^{re.escape(prefix)}-{tier}-([0-9]{{1,12}})$")
    for c in ledger.get("claims", []):
        m = pat.match(c.get("id", ""))
        if m:
            n = max(n, int(m.group(1)))
    return f"{prefix}-{tier}-{n + 1:04d}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
                                 allow_abbrev=False)
    ap.add_argument("ledger")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--weaken", action="append", default=[], choices=WEAKEN_RULES,
                    help="negative control for the ratchet: disable one rule")
    ap.add_argument("--evidence-dir", help="verify every digest against a content-addressed blob store")
    args = ap.parse_args()

    if args.weaken and os.environ.get("ELENCHUS_RATCHET_SELFTEST") != "1":
        # --weaken exists only so the ratchet can prove it notices a weakened gate. A gate someone can
        # weaken from the command line and still read as clean is not a gate.
        print("REFUSED: --weaken is reserved for the ratchet self-test.", file=sys.stderr)
        return 2

    try:
        ledger = load(args.ledger)
    except (OSError, json.JSONDecodeError) as e:
        msg = f"cannot read ledger: {e}"
        print(json.dumps({"findings": [], "skipped": [msg], "claims": 0}) if args.json else msg,
              file=sys.stdout if args.json else sys.stderr)
        return 2

    try:
        res = check(ledger, args.weaken, args.evidence_dir)
    except Exception as e:  # noqa: BLE001 - a gate that crashed has not looked, and must say so as exit 2
        print(f"INCOMPLETE: the ledger check crashed: {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    if args.weaken:
        print(f"WEAKENED RUN ({', '.join(args.weaken)}): a negative control, not a verdict.", file=sys.stderr)
    if args.json:
        print(json.dumps(res, indent=2))
    else:
        for f in res["findings"]:
            print(f"  {f['severity']:5} {f['code']:26} {f['claim']}: {f['message']}")
        for s in res["skipped"]:
            print(f"  INCOMPLETE: {s}")
        if not res["findings"] and not res["skipped"]:
            print(f"  {res['claims']} claims checked, no findings. (Bookkeeping only: this licenses nothing.)")
        if not res.get("evidence_verified", True):
            print("  note: evidence digests were NOT checked against blobs (no --evidence-dir).")
    if res["skipped"]:
        return 2
    return 1 if res["findings"] else 0


if __name__ == "__main__":
    sys.exit(main())
