#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Xavier Callens (SocrateAI Lab). See NOTICE.
"""Consistency check for elenchus/ (public copy), run from this repository alone.

Checks, each reported separately in CONSISTENCY_REPORT.md:
  1. Zenodo   every REGISTRY.json DOI resolves on the public Zenodo API, its DOI matches, and its title matches the
              registry title and the copied publication_meta*.json title (exact, then whitespace/HTML/case-normalised).
  2. Ledger   every discoveries/*/ledger/ledger.json goes through the Elenchus gate (ledger.py, run with
              --evidence-dir), shipped in elenchus/tool/ledger.py, so every evidence digest is re-hashed. If that
              file is missing, the gate is reported as SKIPPED and a built-in integrity check runs instead (every
              claim's `sha256:` evidence digest must name a blob in evidence/ whose bytes hash to it). That check is
              not the gate.
              Exit 1 with only LEDGER_UNAUDITED_TIER_A flags is the expected state (no human statement audit yet);
              any 'block' finding, an exit code 2, or a disagreement with REGISTRY.json is an inconsistency.
  3. Lean     every copied lean/ file is re-hashed and compared with the hashes recorded for it in the ledger
              evidence blobs, in STATEMENT_LOCK.json, and in lean_manifest.json. Hash pairs quoted in
              publication_meta notes are cross-checked too (informational: notes sometimes quote an earlier version).
  4. Kernel   code-only scan (comments stripped) of every copied Lean file for sorry, axiom declarations,
     escapes  debug.skipKernelTC, addDecl, native_decide, implemented_by, #exit. Hits in files whose name marks
              them as planted controls are expected; any other hit is reported.
  5. Replay   which copied modules appear in the kernel-replay snapshot (kernel_replay_2026-10-26/), per paper.
  6. Secrets  byte-level scan of every file for token patterns.

What this does NOT check: the ledger evidence blobs name compile transcripts and data by (redacted) paths on the
producing machine; those files are not in this repository, so a clean ledger run here certifies blob integrity
and bookkeeping, not the transcripts behind the blobs. Nothing here re-runs Lean.

Exit codes: 0 no inconsistency, 1 inconsistencies found, 2 a check could not run (e.g. no network for Zenodo).
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from typing import Any

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GATE = os.path.join(ROOT, "tool", "ledger.py")
GATE_PRESENT = os.path.isfile(GATE)
ALLOWED_FLAG = "LEDGER_UNAUDITED_TIER_A"
CONTROL_NAME = re.compile(r"(Control|Reject|Forg|Plant|Mutation|Tamper|Cheat|EnvControl|plants)", re.I)
ESCAPES = {
    "sorry": re.compile(r"\bsorry\b"),
    "axiom_decl": re.compile(r"^\s*(private\s+|protected\s+)?axiom\s", re.M),
    "skipKernelTC": re.compile(r"skipKernelTC"),
    "addDecl": re.compile(r"\baddDecl\b"),
    "native_decide": re.compile(r"\bnative_decide\b"),
    "implemented_by": re.compile(r"\bimplemented_by\b"),
    "#exit": re.compile(r"^\s*#exit\b", re.M),
}
SECRETS = {
    "github_token": re.compile(rb"gh[pousr]_[A-Za-z0-9]{30,}"),
    "github_pat": re.compile(rb"github" + rb"_pat_[A-Za-z0-9_]{30,}"),
    "hugging_face_tok": re.compile(rb"\bhf_[A-Za-z0-9]{30,}"),
    "openai_or_anthropic_key": re.compile(rb"\bsk-(ant-)?[A-Za-z0-9_-]{30,}"),
    "aws_key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "private_key": re.compile(rb"-----BEGIN [A-Z ]*" + rb"PRIV" + rb"ATE KEY-----"),
    "bearer": re.compile(rb"Bearer [A-Za-z0-9._~+/-]{30,}"),
    "token_assignment": re.compile(rb"(ZEN" + rb"ODO|HUGGING" + rb"FACE|HF|GITHUB)_TOK" + rb"EN\s*[=:]\s*['\"]?[A-Za-z0-9._-]{16,}"),
}


def sha256_file(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def norm(t: str) -> str:
    return " ".join(html.unescape(t).split()).casefold()


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def meta_title(m: dict) -> str | None:
    return m.get("title") or (m.get("metadata") or {}).get("title")


def fetch_zenodo(rec: str) -> dict:
    url = f"https://zenodo.org/api/records/{rec}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
    except Exception as e:  # noqa: BLE001 - reported, never swallowed
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}
    return {"ok": True, "title": (d.get("metadata") or {}).get("title"), "doi": d.get("doi"),
            "date": (d.get("metadata") or {}).get("publication_date"),
            "pdf_md5": sorted(f.get("checksum") for f in d.get("files", []) if str(f.get("key", "")).endswith(".pdf"))}


def check_zenodo(reg: dict, offline: bool) -> tuple[list[dict], int]:
    rows: list[dict] = []
    bad = 0
    for e in reg["entries"]:
        rec = e["doi"].rsplit(".", 1)[1]
        z = {"ok": None, "error": "skipped (--offline)"} if offline else fetch_zenodo(rec)
        if not offline:
            time.sleep(1.0)
        meta_t = None
        pdf_status = None
        if e.get("discovery_dir"):
            pdf = os.path.join(ROOT, e["discovery_dir"], "main_v1.pdf" if e["id"] == "ED-06" else "main.pdf")
            if not os.path.isfile(pdf):
                pdf_status = "not copied (on Zenodo only)"
            elif z.get("ok"):
                md5 = "md5:" + hashlib.md5(open(pdf, "rb").read()).hexdigest()
                pdf_status = "identical to the Zenodo upload" if md5 in z.get("pdf_md5", []) else "DIFFERS from the Zenodo upload"
            mf = "publication_meta_v2.json" if e.get("version") == "v2" else "publication_meta.json"
            mp = os.path.join(ROOT, e["discovery_dir"], mf)
            if os.path.isfile(mp):
                meta_t = meta_title(load_json(mp))
        zt = z.get("title")
        row = {"id": e["id"], "doi": e["doi"], "resolves": z.get("ok"), "doi_match": z.get("doi") == e["doi"] if z.get("ok") else None,
               "title_exact": (zt == e["title"]) if zt else None,
               "title_normalised": (norm(zt) == norm(e["title"])) if zt else None,
               "meta_title_match": (norm(meta_t) == norm(e["title"])) if meta_t else None,
               "date": z.get("date"), "error": z.get("error"), "pdf": pdf_status}
        if z.get("ok") and not (row["doi_match"] and row["title_normalised"]):
            bad += 1
        if z.get("ok") is False:
            bad += 1
        if row["meta_title_match"] is False:
            bad += 1
        if pdf_status and pdf_status.startswith("DIFFERS"):
            bad += 1
        rows.append(row)
    return rows, bad


def parse_committed_exit(path: str) -> int | None:
    if not os.path.isfile(path):
        return None
    txt = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"exit[ _]code\W{0,3}(\d)", txt, re.I)
    return int(m.group(1)) if m else None


def check_ledgers(reg: dict) -> tuple[list[dict], int]:
    by_slug = {e["slug"]: e for e in reg["entries"]}
    rows: list[dict] = []
    bad = 0
    disc = os.path.join(ROOT, "discoveries")
    for slug in sorted(os.listdir(disc)):
        ld = os.path.join(disc, slug, "ledger")
        lj = os.path.join(ld, "ledger.json")
        if not os.path.isfile(lj):
            rows.append({"slug": slug, "ledger": False})
            continue
        tiers: dict[str, int] = {}
        for c in load_json(lj).get("claims", []):
            tiers[c.get("tier")] = tiers.get(c.get("tier"), 0) + 1
        committed = parse_committed_exit(os.path.join(ld, "gate_output.txt"))
        if not GATE_PRESENT:
            integ = integrity_check(lj, os.path.join(ld, "evidence"))
            problems = list(integ["problems"])
            bad += 1 if problems else 0
            rows.append({"slug": slug, "ledger": True, "claims": integ["claims"], "tiers": tiers, "exit": "SKIPPED",
                         "blocks": "-", "flags": "-", "committed_exit": committed, "digests_ok": integ["ok"],
                         "problems": problems})
            continue
        r = subprocess.run([sys.executable, "-I", GATE, lj, "--json", "--evidence-dir", os.path.join(ld, "evidence")],
                           capture_output=True, text=True)
        try:
            res = json.loads(r.stdout)
        except ValueError:
            res = {"findings": [], "skipped": [r.stderr.strip() or "no JSON output"], "claims": 0}
        blocks = [f for f in res["findings"] if f["severity"] == "block"]
        flags = [f for f in res["findings"] if f["severity"] == "flag"]
        other_flags = [f for f in flags if f["code"] != ALLOWED_FLAG]
        rg = (by_slug.get(slug) or {}).get("ledger_gate") or {}
        problems = []
        if r.returncode == 2 or res.get("skipped"):
            problems.append("gate could not run / looked at nothing")
        if blocks:
            problems.append(f"{len(blocks)} blocking finding(s): {sorted({f['code'] for f in blocks})}")
        if other_flags:
            problems.append(f"unexpected flags {sorted({f['code'] for f in other_flags})}")
        if rg and rg.get("gate_exit") != r.returncode:
            problems.append(f"exit {r.returncode} differs from REGISTRY.json ({rg.get('gate_exit')})")
        if rg and rg.get("flags") != len(flags):
            problems.append(f"{len(flags)} flags differ from REGISTRY.json ({rg.get('flags')})")
        if committed is not None and committed != r.returncode:
            problems.append(f"exit {r.returncode} differs from committed gate_output.txt ({committed})")
        if not res.get("evidence_verified"):
            problems.append("evidence digests were not verified")
        bad += 1 if problems else 0
        rows.append({"slug": slug, "ledger": True, "claims": res.get("claims"), "tiers": tiers, "exit": r.returncode,
                     "blocks": len(blocks), "flags": len(flags), "committed_exit": committed, "problems": problems})
    return rows, bad


def integrity_check(ledger_json: str, evidence_dir: str) -> dict[str, Any]:
    """Built-in check used when the Elenchus gate is absent: digests resolve to blobs with matching bytes."""
    claims = load_json(ledger_json).get("claims", [])
    problems: list[str] = []
    ok = 0
    for c in claims:
        ev = c.get("evidence") or ""
        if not ev.startswith("sha256:"):
            problems.append(f"{c.get('id')}: evidence is not a sha256 digest")
            continue
        h = ev.split(":", 1)[1]
        p = os.path.join(evidence_dir, h + ".json")
        if not os.path.isfile(p):
            problems.append(f"{c.get('id')}: blob {h[:16]}... missing")
        elif sha256_file(p) != h:
            problems.append(f"{c.get('id')}: blob {h[:16]}... bytes do not hash to its name")
        else:
            ok += 1
    if not claims:
        problems.append("empty ledger")
    return {"claims": len(claims), "ok": ok, "problems": problems}


def recorded_from_evidence(ledger_dir: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}

    def walk(o: Any) -> None:
        if isinstance(o, dict):
            p = o.get("path")
            h = o.get("sha256")
            if isinstance(p, str) and p.endswith(".lean") and isinstance(h, str):
                out.setdefault(p, set()).add(h)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    ev = os.path.join(ledger_dir, "evidence")
    if os.path.isdir(ev):
        for f in os.listdir(ev):
            try:
                walk(load_json(os.path.join(ev, f)))
            except ValueError:
                continue
    return out


def recorded_from_lock(lock: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}

    def walk(o: Any) -> None:
        if isinstance(o, dict):
            for k, v in o.items():
                if k.endswith(".lean") and isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v):
                    out.setdefault(k, set()).add(v)
                elif isinstance(v, str) and v.endswith(".lean") and isinstance(o.get(k + "_sha256"), str):
                    out.setdefault(v, set()).add(o[k + "_sha256"])
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    if os.path.isfile(lock):
        walk(load_json(lock))
    return out


def strip_lean_comments(src: str) -> str:
    out: list[str] = []
    i, depth, n = 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and src.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            out.append("\n" if src[i] == "\n" else " ")
            i += 1
        elif src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
        elif src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append('""')
            i = j + 1
        else:
            out.append(src[i])
            i += 1
    return "".join(out)


PLANTED = "planted control file (expected)"
CHALLENGE = "challenge statement file: sorry is the statement hole by design (expected)"
INLINE = ("planted control declared inline (ctl_*) in an axiom-audit file: breaches the programme's own "
          "'controls live in separate *Controls.lean files' rule; #print axioms is per declaration, so the audited "
          "theorems are unaffected")
REVIEW = "NOT a control: review"


def classify_escape(base: str, lines: list[str], line: int) -> str:
    if CONTROL_NAME.search(base):
        return PLANTED
    if re.search(r"Challenge", base):
        return CHALLENGE
    window = " ".join(lines[max(0, line - 3):line])
    if re.search(r"\b(theorem|lemma|axiom|def)\s+ctl_\w*", window):
        return INLINE
    return REVIEW


def check_lean(reg: dict) -> tuple[list[dict], list[dict], list[dict], int]:
    rows: list[dict] = []
    escapes: list[dict] = []
    notes: list[dict] = []
    bad = 0
    disc = os.path.join(ROOT, "discoveries")
    for slug in sorted(os.listdir(disc)):
        d = os.path.join(disc, slug)
        mp = os.path.join(d, "lean_manifest.json")
        if not os.path.isfile(mp):
            continue
        man = load_json(mp)["files"]
        ev = recorded_from_evidence(os.path.join(d, "ledger"))
        lk = recorded_from_lock(os.path.join(d, "STATEMENT_LOCK.json"))
        stats = {"copied": 0, "match": 0, "pub_commit_match": 0, "mismatch": 0, "no_record": 0, "upstream_listed": 0, "missing_copy": 0, "withheld": 0}
        mism: list[str] = []
        by_base: dict[str, list[str]] = {}
        for f in man:
            if not f.get("copied_to"):
                key = "withheld" if f.get("withheld_in_public_release") else ("upstream_listed" if f.get("upstream") else "missing_copy")
                stats[key] += 1
                continue
            path = os.path.join(d, f["copied_to"])
            if not os.path.isfile(path):
                stats["missing_copy"] += 1
                mism.append(f"{f['copied_to']}: listed but absent")
                continue
            stats["copied"] += 1
            h = sha256_file(path)
            by_base.setdefault(os.path.basename(path), []).append(h)
            names = set(f.get("aliases") or []) | {f["ref"]}
            rec = set(f.get("recorded_sha256") or [])
            for a in names:
                rec |= ev.get(a, set())
            for k, v in lk.items():
                if any(a == k or a.endswith("/" + k) for a in names):
                    rec |= v
            if not rec and f.get("pub_sha256"):
                if h == f["pub_sha256"]:
                    stats["pub_commit_match"] += 1
                else:
                    stats["mismatch"] += 1
                    mism.append(f"{f['copied_to']}: sha256 {h[:16]}... differs from the publication-commit version")
            elif not rec:
                stats["no_record"] += 1
            elif h in rec:
                stats["match"] += 1
            else:
                stats["mismatch"] += 1
                mism.append(f"{f['copied_to']}: sha256 {h[:16]}... not in recorded {sorted(x[:16] for x in rec)}")
            code = strip_lean_comments(open(path, encoding="utf-8", errors="replace").read())
            lines = code.split("\n")
            for kind, rx in ESCAPES.items():
                for m in rx.finditer(code):
                    line = code.count("\n", 0, m.start()) + 1
                    escapes.append({"slug": slug, "file": f["copied_to"], "line": line, "kind": kind,
                                    "classification": classify_escape(os.path.basename(path), lines, line)})
        # hash pairs quoted in publication_meta notes (informational)
        for mf in ("publication_meta.json", "publication_meta_v2.json"):
            p = os.path.join(d, mf)
            if not os.path.isfile(p):
                continue
            txt = json.dumps(load_json(p))
            for m in re.finditer(r"([\w./{},-]+\.lean)\W{1,20}(?:sha256\W{1,4})?([0-9a-f]{64})", txt):
                base = os.path.basename(m.group(1))
                hs = by_base.get(base, [])
                notes.append({"slug": slug, "meta": mf, "file": base, "sha": m.group(2),
                              "status": "matches copied file" if m.group(2) in hs
                              else ("no copied file with this name" if not hs else "differs from copied file")})
        if stats["mismatch"] or stats["missing_copy"]:
            bad += 1
        rows.append({"slug": slug, **stats, "problems": mism})
    return rows, escapes, notes, bad


def check_replay(reg: dict) -> dict:
    kd = os.path.join(ROOT, "kernel_replay_2026-10-26")
    out: dict[str, Any] = {"present": os.path.isdir(kd), "replayed": {}, "built": {}, "per_paper": {}}
    if not out["present"]:
        return out
    rj = os.path.join(kd, "replay.jsonl")
    if os.path.isfile(rj):
        for line in open(rj, encoding="utf-8"):
            line = line.strip()
            if line:
                r = json.loads(line)
                out["replayed"][r["module"]] = r.get("rc")
    bj = os.path.join(kd, "build.json")
    if os.path.isfile(bj):
        b = load_json(bj)
        for r in b.get("built", []):
            out["built"][r["module"]] = r.get("build_rc")
    snap = os.path.join(kd, "SNAPSHOT.json")
    res = os.path.join(kd, "result.json")
    out["snapshot"] = load_json(snap) if os.path.isfile(snap) else None
    out["result"] = load_json(res) if os.path.isfile(res) else None
    disc = os.path.join(ROOT, "discoveries")
    for slug in sorted(os.listdir(disc)):
        mp = os.path.join(disc, slug, "lean_manifest.json")
        if not os.path.isfile(mp):
            continue
        mods_set: set[str] = set()
        for f in load_json(mp)["files"]:
            c = f.get("copied_to") or ""
            m = re.match(r"lean/formal_cert/(.+)\.lean$", c)
            if m:
                mods_set.add(m.group(1).replace("/", "."))
        mods = sorted(mods_set)
        rep = sorted(x for x in mods if x in out["replayed"])
        out["per_paper"][slug] = {"modules": len(mods), "replayed": rep,
                                  "replayed_rc0": sum(1 for x in rep if out["replayed"][x] == 0),
                                  "built_only": sorted(x for x in mods if x in out["built"] and x not in out["replayed"])}
    return out


def check_secrets() -> tuple[list[dict], int, int]:
    hits: list[dict] = []
    total = 0
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in (".git", "__pycache__")]
        for f in files:
            p = os.path.join(root, f)
            total += os.path.getsize(p)
            if os.path.abspath(p) == os.path.abspath(__file__):
                continue
            data = open(p, "rb").read()
            for kind, rx in SECRETS.items():
                for m in rx.finditer(data):
                    hits.append({"file": os.path.relpath(p, ROOT), "kind": kind, "offset": m.start()})
    return hits, len(hits), total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true", help="skip the Zenodo check (reported as not run)")
    ap.add_argument("--report", default=os.path.join(ROOT, "CONSISTENCY_REPORT.md"))
    args = ap.parse_args()
    reg = load_json(os.path.join(ROOT, "REGISTRY.json"))

    z_rows, z_bad = check_zenodo(reg, args.offline)
    l_rows, l_bad = check_ledgers(reg)
    f_rows, esc, notes, f_bad = check_lean(reg)
    rp = check_replay(reg)
    s_hits, s_bad, total = check_secrets()
    esc_review = [x for x in esc if x["classification"] == REVIEW]
    esc_inline = [x for x in esc if x["classification"] == INLINE]
    esc_chal = [x for x in esc if x["classification"] == CHALLENGE]
    unresolved = sum(1 for r in z_rows if r["resolves"] is not True)

    L: list[str] = ["# Consistency report", "",
                    f"Generated by `tools/check_consistency.py` on {time.strftime('%Y-%m-%d %H:%M:%SZ', time.gmtime())}, "
                    "from this repository alone (plus the public Zenodo API).", "",
                    "## Summary", "",
                    f"- Zenodo: {sum(1 for r in z_rows if r['resolves'])}/{len(z_rows)} DOIs resolve; "
                    f"{sum(1 for r in z_rows if r['title_exact'])} exact title matches, "
                    f"{sum(1 for r in z_rows if r['title_normalised'])} normalised; "
                    f"{sum(1 for r in z_rows if (r['pdf'] or '').startswith('identical'))} PDFs identical to the upload, "
                    f"{sum(1 for r in z_rows if (r['pdf'] or '').startswith('not copied'))} PDFs not copied (on Zenodo only); inconsistencies: {z_bad}"
                    + (" (NOT RUN: --offline)" if args.offline else ""),
                    (f"- Ledger gate: {sum(1 for r in l_rows if r['ledger'])} ledgers run with --evidence-dir; "
                     f"blocking findings: {sum(r.get('blocks', 0) for r in l_rows)}; "
                     f"LEDGER_UNAUDITED_TIER_A flags: {sum(r.get('flags', 0) for r in l_rows)}; ledgers with a problem: {l_bad}"
                     if GATE_PRESENT else
                     f"- Ledger gate: SKIPPED (tool/ledger.py not found). "
                     f"Built-in integrity check instead: {sum(1 for r in l_rows if r['ledger'])} ledgers, "
                     f"{sum(r.get('digests_ok', 0) for r in l_rows)}/{sum(r.get('claims', 0) or 0 for r in l_rows if r['ledger'])} claim digests resolve to a blob with matching bytes; "
                     f"ledgers with a problem: {l_bad}"),
                    f"- Lean copies: {sum(r['copied'] for r in f_rows)} files re-hashed; {sum(r['match'] for r in f_rows)} match a recorded hash, "
                    f"{sum(r['pub_commit_match'] for r in f_rows)} match their publication-commit version (no hash was recorded), "
                    f"{sum(r['mismatch'] for r in f_rows)} mismatch, {sum(r['no_record'] for r in f_rows)} have neither, "
                    f"{sum(r['upstream_listed'] for r in f_rows)} upstream files listed (not copied), "
                    f"{sum(r['withheld'] for r in f_rows)} withheld from the public copy (see REDACTION.md)",
                    f"- Kernel-escape scan: {len(esc)} hits: {sum(1 for x in esc if x['classification'] == PLANTED)} in planted-control files, "
                    f"{len(esc_chal)} in challenge-statement files, {len(esc_inline)} inline ctl_* controls in axiom-audit files "
                    f"(convention breach, listed), {len(esc_review)} unexplained",
                    f"- Kernel replay snapshot: {'present' if rp['present'] else 'absent'}; "
                    f"{sum(1 for v in rp['replayed'].values() if v == 0)}/{len(rp['replayed'])} replayed modules rc 0",
                    f"- Secrets: {s_bad} pattern hits",
                    f"- Size of elenchus/: {total / 1e6:.1f} MB", ""]

    L += ["## 1. Zenodo", "", "The PDF column compares the md5 of a copied PDF with the checksum Zenodo publishes for the uploaded PDF. "
          "The public copy holds no PDF, so it reads 'not copied (on Zenodo only)'.", "",
          "| id | DOI | resolves | DOI match | title exact | title normalised | meta title | date | PDF |", "|---|---|---|---|---|---|---|---|---|"]
    for r in z_rows:
        L.append(f"| {r['id']} | {r['doi']} | {r['resolves']} | {r['doi_match']} | {r['title_exact']} | {r['title_normalised']} | "
                 f"{r['meta_title_match']} | {r['date']} | {r['pdf'] or '-'} |" + (f" {r['error']}" if r.get("error") and not args.offline else ""))

    L += ["", "## 2. Elenchus ledger gate" + (" (`--evidence-dir`)" if GATE_PRESENT else ": SKIPPED in this release"), "",
          ("Exit 1 with only `LEDGER_UNAUDITED_TIER_A` flags = 0 blocking findings and no human statement audit yet. "
           "This is the expected state of every paper with Tier A rows; it is not a publication-gate pass in the Elenchus sense (which needs exit 0)."
           if GATE_PRESENT else
           "The Elenchus `tool/ledger.py` was not found, so the gate did not run. "
           "The 'exit' column says SKIPPED; 'committed gate_output exit' is the gate's own exit code recorded at publication "
           "(1 with only `LEDGER_UNAUDITED_TIER_A` flags = no blocking finding, and no human statement audit yet). "
           "'problems' reports the built-in integrity check: every claim digest must name a blob whose bytes hash to it. That check is bookkeeping, not the gate."), "",
          "| paper | claims | tiers | exit | blocks | flags | committed gate_output exit | problems |", "|---|---|---|---|---|---|---|---|"]
    for r in l_rows:
        if not r["ledger"]:
            L.append(f"| {r['slug']} | - | no ledger in this paper's folder | - | - | - | - | - |")
            continue
        t = " ".join(f"{k}{v}" for k, v in sorted(r["tiers"].items()))
        ce = "absent" if r["committed_exit"] is None else r["committed_exit"]
        L.append(f"| {r['slug']} | {r['claims']} | {t} | {r['exit']} | {r['blocks']} | {r['flags']} | {ce} | {'; '.join(r['problems']) or 'none'} |")
    if not GATE_PRESENT:
        L += ["", f"Integrity check: {sum(r.get('digests_ok', 0) for r in l_rows if r['ledger'])} claim digests verified; "
              "the evidence blobs were re-hashed for the public copy after path redaction (REDACTION.md maps old to new digests)."]

    L += ["", "## 3. Lean file hashes", "",
          "`match` = equals a hash recorded in the ledger evidence or STATEMENT_LOCK.json. `pub commit` = no hash was recorded "
          "(ED-03 to ED-08); the copy equals the version last committed before the Zenodo record was created (a proxy, not a lock).", "",
          "| paper | copied | match | pub commit | mismatch | no recorded hash | upstream listed | withheld | problems |", "|---|---|---|---|---|---|---|---|---|"]
    for r in f_rows:
        L.append(f"| {r['slug']} | {r['copied']} | {r['match']} | {r['pub_commit_match']} | {r['mismatch']} | {r['no_record']} | {r['upstream_listed']} | {r['withheld']} | "
                 f"{'; '.join(r['problems']) or 'none'} |")
    nm = [n for n in notes if n["status"] != "matches copied file"]
    L += ["", f"Hash pairs quoted in `publication_meta` notes: {len(notes)} found, {len(notes) - len(nm)} match a copied file. "
          "The rest are listed; a note may quote an earlier version of a file or a file that is not copied (informational, not counted as an inconsistency).", ""]
    for n in nm:
        L.append(f"- {n['slug']} `{n['meta']}`: `{n['file']}` {n['sha'][:16]}... — {n['status']}")

    L += ["", "## 4. Kernel-escape scan (code only, comments and strings stripped)", ""]
    if esc_review:
        L += ["Unexplained hits (each needs a human look):", ""]
        for x in esc_review:
            L.append(f"- {x['slug']}: `{x['file']}` line {x['line']}: `{x['kind']}`")
    else:
        L.append("No unexplained hit.")
    L += ["", f"Inline planted controls in axiom-audit files ({INLINE}):", ""]
    L += [f"- {x['slug']}: `{x['file']}` line {x['line']}: `{x['kind']}`" for x in esc_inline] or ["- none"]
    L += ["", "Challenge-statement files (the statement to be proved, with `sorry` as its hole):", ""]
    L += [f"- {x['slug']}: `{x['file']}` line {x['line']}: `{x['kind']}`" for x in esc_chal] or ["- none"]
    ctl = {}
    for x in esc:
        if x["classification"] == PLANTED:
            ctl.setdefault(x["file"], set()).add(x["kind"])
    L += ["", f"Planted-control files with expected hits: {len(ctl)}", ""]
    for f, k in sorted(ctl.items()):
        L.append(f"- `{f}`: {', '.join(sorted(k))}")

    L += ["", "## 5. Kernel replay snapshot", ""]
    if rp["present"]:
        snap = rp.get("snapshot") or {}
        res = rp.get("result") or {}
        L += ([f"Final record (`result.json`): {json.dumps(res.get('counts', res.get('summary', '')))}."] if res else
              [f"Status: {snap.get('status', 'unknown')}; snapshot taken {snap.get('snapshot_taken_utc')}."]) + ["",
              f"Replayed modules (rc): {', '.join(f'{k}={v}' for k, v in sorted(rp['replayed'].items()))}", "",
              f"Built (build_rc) without a replay line yet: {', '.join(f'{k}={v}' for k, v in sorted(rp['built'].items()) if k not in rp['replayed'])}", "",
              "| paper | formal_cert modules copied | replayed (rc 0) | built, replay pending |", "|---|---|---|---|"]
        for s, v in rp["per_paper"].items():
            L.append(f"| {s} | {v['modules']} | {v['replayed_rc0']}/{len(v['replayed'])} {', '.join(v['replayed'])} | {', '.join(v['built_only']) or '-'} |")
    else:
        L.append("No snapshot present.")

    L += ["", "## 6. Secrets", ""]
    L += [f"- `{h['file']}` offset {h['offset']}: {h['kind']}" for h in s_hits] or ["No token pattern found."]
    L += ["", "## Not checked here", "",
          "- The compile transcripts and data that the evidence blobs point to live on the producing machine (paths redacted); "
          "only the blobs' own integrity is checked.",
          "- The Elenchus ledger gate itself, if `tool/ledger.py` is missing (then it is reported as SKIPPED).",
          "- No Lean is re-run by this script. Kernel checks are the producers', the auditors' and the replay snapshot's.",
          "- Statement adequacy (does the Lean statement mean what the prose says?) has been audited by AI agents only, never by a person.", ""]
    with open(args.report, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("\n".join(L[:14]))
    if not args.offline and unresolved == len(z_rows):
        return 2
    return 1 if (z_bad or l_bad or f_bad or s_bad or esc_review) else 0


if __name__ == "__main__":
    sys.exit(main())
