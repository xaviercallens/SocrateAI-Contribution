# Check it yourself

[Version française](check-it-yourself.fr.md)

You should not have to trust us. Here is how to check the work, from a five-minute check to a full re-run, and how to challenge a result.

## 1. Is this the published book? (two minutes)

Each PDF in [`books/`](../books/) should be exactly the file published on Zenodo. Compute its fingerprint:

```bash
md5sum books/discovery-journal-2026-fr.pdf books/discovery-journal-2026-en.pdf
```

Then compare it with the checksum shown on the Zenodo record ([French](https://doi.org/10.5281/zenodo.23669395), [English](https://doi.org/10.5281/zenodo.23669463)), in the record's file list. When this repository was prepared they were `04d2e91cc117c16fecdb255366200164` (French) and `a2b0758673d537056a8e77f4a5bfc89d` (English).

## 2. Download a paper's full bundle (ten minutes)

Each of the 24 papers listed in [`elenchus/REGISTRY.md`](../elenchus/REGISTRY.md) has a Zenodo record. The record holds the PDF and, for most papers, the sources, data, scripts and a manifest of checksums. Download the record from its DOI and read its reproduction notes.

## 3. Run the checks in this repository (a few minutes; needs only Python 3)

```bash
# Everything except the online Zenodo check
python3 elenchus/tools/check_consistency.py --offline

# Including the Zenodo check (needs the internet)
python3 elenchus/tools/check_consistency.py
```

The script writes [`elenchus/CONSISTENCY_REPORT.md`](../elenchus/CONSISTENCY_REPORT.md). It:
- runs the Elenchus ledger gate on all 17 claim ledgers, re-hashing every evidence file;
- re-hashes the 360 copied Lean files against the hashes recorded when the claims were filed;
- scans the Lean files for the known ways of fooling the proof checker;
- lists which modules appear in the kernel-replay record;
- checks every DOI on Zenodo.

**What we got on 2026-10-27:** exit code 0 in the first runs, with 24 of 24 DOIs resolving and matching titles. In the last run, the one whose report is committed, Zenodo's server answered "504 Gateway Time-out" for 3 records, and the script exited 1. That is the script correctly reporting a check it could not complete. If it happens to you, run it again later. 17 ledgers had 0 blocking findings and 154 "unaudited level A" flags. Of the Lean files, 0 mismatch. The kernel-escape scan found nothing unexplained. 93 of 93 replayed modules have return code 0.

**A negative control you can try.** Change one character in any file under `elenchus/discoveries/*/ledger/evidence/` and run the check again. It should exit 1 and name the claim whose evidence no longer matches. (We did this with one file of `ar_yukawa_crystal`, and it did.) Restore the file afterwards, for example with `git checkout -- elenchus/`.

To run the ledger gate alone on one paper, see [`elenchus/tool/README.md`](../elenchus/tool/README.md).

**What these checks do not prove.** They check bookkeeping and integrity: that the files are the files, and that the ledgers are consistent. They do not re-run Lean, and they say nothing about whether a statement is true.

## 4. Re-run the proof checker (hours, and several gigabytes)

This is the real test, and it is heavy. The recipe used for the kernel replay of 26 October 2026 is in [`elenchus/kernel_replay_2026-10-26/REPLAY.md`](../elenchus/kernel_replay_2026-10-26/REPLAY.md). In outline:

1. Install the pinned Lean toolchain named there (Lean 4.34.1).
2. Fetch the upstream projects at the commits listed in each paper's `LEAN.md`: Mathlib, and OpenAI's `openai/math` for the results that build on it. They are not copied here.
3. Build the modules from `elenchus/discoveries/<paper>/lean/`.
4. For each claimed theorem, run `#print axioms`. The answer must contain only `propext`, `Classical.choice` and `Quot.sound`. Any `sorryAx`, or any other axiom, means the claim fails.
5. Run `leanchecker <Module>` to replay the stored declarations through the kernel. Return code 0 is a pass.
6. Search the sources for `sorry`, `axiom`, `debug.skipKernelTC`, `addDecl`, `native_decide`, `implemented_by` and `#exit`. A hit outside a file named as a planted control needs an explanation.

**Try the controls too.** Add `sorry` to a proof, or a line `axiom cheat : False`, and check that step 4 catches it. A check that cannot fail is worth nothing.

We did not re-run Lean for this repository. The numbers in step 3 come from the checks above, and the replay numbers from the record of 26 October.

## 5. Read the statements (the step nobody has done yet)

A level-A result means the proof checker accepted a proof of the *formal statement*. Whether the formal statement says what the plain-language description says has **not been audited by any person** for any result here. Each ledger flags this with `LEDGER_UNAUDITED_TIER_A`. If you read Lean, this is the most valuable check you can make: take a Tier A row from a `ledger.json`, find the theorem in the Lean files, and ask whether it really says what the row claims.

## 6. Challenge a result

Please [open an issue](../CONTRIBUTING.md). "Red-team" issues are welcome: they argue that something is wrong, overstated or mislabelled. A useful challenge says:
- which claim it is about (the DOI, and the ledger row id if there is one, such as `YK-A-0001`);
- what you think is wrong;
- how you checked: what you ran, what you read and what you got.

The intention is that a challenge that turns out to be right is acknowledged and its correction published, as earlier corrections were ([what we got wrong](what-we-got-wrong.md)).
