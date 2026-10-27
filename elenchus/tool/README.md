# The Elenchus ledger gate (`ledger.py`)

`ledger.py` reads a claim ledger (`ledger.json`) and refuses to say "all is well" while something is missing or inconsistent. It is a single Python 3 file that uses only the standard library.

**Provenance.** This file is byte-for-byte the copy used to check every ledger in [`../discoveries/`](../discoveries/). It comes from the author's private Elenchus repository, `tools/ledger.py` at commit `c9ae8cd4af776c3b0d69a3a4b4d868d03d1bf497`, sha256 `5284cdf102973d516c20097a4c4bf67cfcdb3d236dc0a5bbf59e71b446f97f86`. Nothing else from that repository is published here.

## What it checks

Each claim in a ledger has an identifier, a level (tier), a kind of evidence, the claims it depends on, and the sha256 digest of an evidence file. The gate checks the bookkeeping:
- the records are well formed;
- no identifier is used twice;
- the level written inside an identifier matches the claim's level;
- every dependency exists, and no claim rests on itself;
- no claim is filed above what its kind of evidence allows (a numerical result can never be above X, a citation never above L, an argument never above C; only a Lean proof with an axiom check can reach A);
- no claim is filed above the weakest thing it rests on;
- with `--evidence-dir`, every digest names an evidence file whose bytes really hash to that digest.

It also raises a flag, `LEDGER_UNAUDITED_TIER_A`, for every level-A claim that no person has audited. Such an audit asks whether the formal statement really says what its plain-language description says.

## What it does not do

- **It proves nothing.** A clean run means the bookkeeping holds. It says nothing about whether any claim is true. In the tool's own words: "Bookkeeping only: this licenses nothing."
- **It does not run Lean**, and it does not re-run any calculation. It trusts the evidence files to describe what was run, and it checks only that they have not changed.
- **Unaudited level-A rows keep exit code 1.** No human has audited any statement in this repository, so every ledger with level-A rows exits 1 with only `LEDGER_UNAUDITED_TIER_A` flags. That is the honest state of the work, not a malfunction.

| Exit code | Meaning |
|---|---|
| 0 | No findings (bookkeeping only) |
| 1 | Findings: either blocking problems or, here, only the "unaudited level A" flags |
| 2 | The check could not run, or looked at nothing (an empty ledger is never a pass) |

## How to run it on the examples

From the repository root, with Python 3:

```bash
# A ledger with no level-A rows: expected "no findings", exit 0
python3 elenchus/tool/ledger.py elenchus/discoveries/p2_3d_feasibility/ledger/ledger.json \
    --evidence-dir elenchus/discoveries/p2_3d_feasibility/ledger/evidence

# A ledger with level-A rows: expected exit 1, with only LEDGER_UNAUDITED_TIER_A flags
python3 elenchus/tool/ledger.py elenchus/discoveries/ar_yukawa_crystal/ledger/ledger.json \
    --evidence-dir elenchus/discoveries/ar_yukawa_crystal/ledger/evidence

# All 17 ledgers, together with the other checks (Zenodo, Lean hashes, kernel-escape scan)
python3 elenchus/tools/check_consistency.py --offline
```

Results when this release was prepared (2026-10-27): the first command gave "30 claims checked, no findings", exit 0. Over all 17 ledgers: 0 blocking findings and 154 `LEDGER_UNAUDITED_TIER_A` flags, the same totals as when the papers were published. Changing one byte in one evidence file of `ar_yukawa_crystal` turned that ledger into a blocking `LEDGER_EVIDENCE_MISMATCH`, and the consistency check exited 1. That is the negative control: the gate can say no.

## Licence

This file is distributed as part of this repository under the GNU Affero General Public License, version 3 or later, with the additional attribution terms in [`../../LICENSING.md`](../../LICENSING.md) and [`../../NOTICE`](../../NOTICE). Copyright (c) 2026 Xavier Callens (SocrateAI Lab).
