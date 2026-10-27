# Elenchus discoveries, October 2026

This folder holds 24 Zenodo publications (23 papers and one textbook) from one AI-executed research programme in mathematics and mathematical physics, together with the claim ledgers, audits, Lean sources and the consistency check behind them. It follows the programme's two standing rules, **Verification Primacy** and **the Primacy of the Kernel**. A language model is not a mathematical reviewer. A claim reaches the top tier only when the Lean 4 kernel has checked it. Floating-point output never supports a claim, which is the Elenchus form of the *Zéro Simulation Flottante* rule.

> **About this public copy (2026-10-27).** This folder is a curated copy of the programme's record, prepared for a public showcase. Compared with the record the author keeps:
> - **The 24 PDFs are not copied.** Each paper is on Zenodo, at the DOI in the registry. The published PDFs mention machine paths and private repository names, and a published record cannot be edited, so they stay on Zenodo only.
> - **The Elenchus ledger gate (`ledger.py`) is included**, unmodified, in [`tool/`](tool/), with its own README. `tools/check_consistency.py` runs it on every ledger with `--evidence-dir`. On this copy it gives the same totals as at publication: 0 blocking findings and 154 `LEDGER_UNAUDITED_TIER_A` flags. Each ledger's committed gate output (`ledger/gate_output.*`) is kept too.
> - **Machine paths and private repository names were redacted** by one deterministic script. Because the evidence blobs are content-addressed, every changed blob was renamed to the sha256 of its new content and its ledger digest updated. [`REDACTION.md`](REDACTION.md) lists the rules and every old→new digest.
> - **Not redistributed:** third-party source texts (`ledger/sources/`), two Lean files withheld for the same path reason (listed in `REDACTION.md`).
> - **Kernel replay:** [`kernel_replay_2026-10-26/`](kernel_replay_2026-10-26/) holds the final record of that day's replay (93 modules rc 0, 778 skipped, no failure), not the partial snapshot described in earlier copies.

**The method comes first in this document because it is the contribution.** The individual results are mostly modest: corollaries, formalisations of known theorems, audits and negative results. What should carry over to other work is the procedure that sorted them into tiers and the record of the errors it caught. `METHODOLOGY.md` gives the long form with a worked case for each rule.

> **Read this first.** All of this was produced by AI agents (Claude) under the direction of the author, Xavier Callens (SocrateAI Lab). Every audit cited here was done by another AI agent instance. **No person has reviewed any statement, proof or paper in this folder.** Where a result rests on an upstream formalisation (openai/math, openai/NavierStokesAndEuler), it is conditional on that upstream work, which is itself AI-generated and not peer reviewed.

---

## 1. The Elenchus method

*Elenchus* is the Socratic cross-examination: a claim survives only if the attempts to refute it fail. In this programme every claim is filed with a tier, and every tier names the instrument that can attack it.

### 1.1 The four tiers

| tier | name | what establishes it | what it licenses |
|---|---|---|---|
| **A** | kernel-checked | A Lean 4 proof that compiles under a pinned toolchain and passes the Tier-A gate (§1.5). | The Lean statement holds, relative to Lean, Mathlib and any named upstream theorem. Nothing about whether the statement means what the prose says. That is *statement adequacy*, a separate audit that no person has yet done here. |
| **L** | literature | A cited source, quoted verbatim, with the source text hashed into the evidence blob. | That the source says it. It does not certify that the source is right. |
| **C** | human-style argument | A written proof or derivation that no machine has checked. Here it was written and audited by AI agents. | A plausible argument. A Tier C row is a target for formalisation, never a theorem. |
| **X** | exploration | Floating-point numerics, solver output, figures read off plots, LLM output. | Nothing on its own. Tier X can **refute** (a counterexample found numerically is reported as one), and it can motivate. It never **supports** a claim. |

The Elenchus gate also knows a tier **B** (exact-arithmetic harness, capped below A). No paper here files B rows.

A claim cannot be filed above the tier of what it rests on. The gate computes each claim's *effective* tier as the minimum over its dependency closure. A claim filed above that is blocked (`LEDGER_TIER_INVERSION`). Each kind of evidence also caps the tier (`LEDGER_KIND_OVERCLAIM`): `numeric` and `llm_output` are capped at X, `citation` at L, `argument` at C. Only `lean_axioms` can reach A.

### 1.2 Preregistration before any attempt

Each round fixes its hypotheses, priors, kill criteria, toolchain and compute budget in a `preregistration.json`. That file is committed to git **before** the first attempt and never edited afterwards. Copies and their first-commit hashes are in [`preregistrations/`](preregistrations/). A deviation from the preregistration is reported as a deviation in the paper. It is never folded silently into the result. One preregistered clause was later shown false by the kernel itself (N4, §1.9), and the paper says so.

### 1.3 Falsification gates with positive and negative controls

- **Numbers before Lean.** Where a cheap numerical check could refute a statement (complete-monotonicity signs, a finite search, a spectral computation), it runs first. A refutation found this way is a result and is published.
- **Every instrument shows that it can say no.** A Lean gate is trusted only after it has rejected things planted to be rejected:
  - a `sorry`;
  - a custom `axiom ... : False`;
  - a tampered data table;
  - a mutated constant;
  - a forged declaration.

  A numerical pipeline must also reproduce a known positive case (a Coulomb Madelung constant, a closed-form EdS distance) and must fail on a planted negative.
- **Controls go in separate files.** Planted controls live in separate `*Controls.lean` files and are never imported by a claimed module. This rule was learned the hard way (§1.9).

### 1.4 Karpathy-style keep/discard, with the kernel as the judge

This adapts Karpathy's *autoresearch* loop. One artifact (a Lean file) changes. A fixed-budget attempt runs (45 min wall clock on 2 cores, at most 2 attempts). One binary metric is read, and the change is **kept** only if all of the following hold:

- the file compiles under the preregistered toolchain (rc 0);
- every claimed theorem's axioms are inside the whitelist;
- the planted controls are still caught;
- the grep in §1.5 finds nothing.

Otherwise it is **discarded** and the error class is logged. A stuck attempt is discarded, not extended. A KEEP is still not Tier A: it becomes Tier A only after the producer ≠ verifier step. ([program text](preregistrations/autoresearch_2026-10-25_program.md))

### 1.5 The Tier-A gate

A Lean theorem is filed at Tier A only when **all three** of these hold:

1. **`#print axioms` is inside `{propext, Classical.choice, Quot.sound}`** for every claimed declaration. `sorryAx`, or any user axiom, rejects the claim.
2. **A kernel replay.** `#print axioms` only walks the constants a proof term references. It does not re-run the kernel. The A2 audit ([ED-24](discoveries/p2_navier_stokes_audit/)) demonstrated the consequence, which is a known limitation that it does not present as new. Under `set_option debug.skipKernelTC true`, `addDecl` stores a "theorem" `forged_false : False` whose value is `True.intro`, and `#print axioms` then reports *"does not depend on any axioms"*, exactly as it would for an honest proof. Only a replay of the stored declarations (`leanchecker`, or `Lean.Replay` / `Kernel.Environment.replay`) rejects it, with a type mismatch.
   - `leanchecker` without `--fresh` is **per-module**. In the A2 auditor's control, a module that only imports a forged module passes it with rc 0.
   - Coverage of the whole import closure therefore comes from the replay, not from `leanchecker` on the roots.
3. **A source grep** for `sorry`, user `axiom`, `debug.skipKernelTC`, `addDecl`, `native_decide`, `implemented_by` and `#exit`. Any hit outside a planted-control file blocks the claim until it is explained. `#exit` is on this list because of the LeanFlow forgery found in P1 ([ED-14](discoveries/prog_sandier_serfaty_audit/), §1.9).

Certificates that delegate arithmetic to the kernel use `decide +kernel` or a fail-closed equivalent, never `native_decide`, which trusts compiled code. The final record of the kernel replay of 2026-10-26 is in [`kernel_replay_2026-10-26/`](kernel_replay_2026-10-26/): 93 modules replayed with rc 0, 778 skipped (776 of them a Lean tree still being generated), no failure. See its `REPLAY.md`.

### 1.6 Producer ≠ verifier

Every published paper here was audited before publication by an AI agent instance separate from the one that produced the work and the one that wrote the paper. That auditor recompiled the Lean itself, planted its own `sorry` and axiom, re-ran the numerics and returned a verdict: ACCEPT, ACCEPT_WITH_CORRECTIONS or REJECT. The rule is that the auditor sits on a model tier **no cheaper than the producer's**.

Where the audit file names its model, this folder records it: three AUDIT.md files name the Claude Opus family, and the ED-06/07 audit was "a separate instance of the same AI model". Where the audit file does not name a model, the registry says so rather than guessing. In ED-11 the paper-stage reruns were not separated from the producer. Only its Stage-4 audit was.

### 1.7 The claim ledger and what its gate means

Each paper's claims live in a machine-readable `ledger/ledger.json`. Every claim has an id `PREFIX-<tier>-NNNN`, a tier, a kind, dependencies, a `sha256:` digest of a content-addressed evidence blob, and an `audit` field. The gate is the Elenchus `ledger.py`, shipped unmodified in [`tool/`](tool/), run with `--evidence-dir` so that every digest is re-hashed. Its verbatim output at publication is kept in each `ledger/gate_output.*`. Like every gate here it can say *no* and cannot say *yes*.

| exit | meaning |
|---|---|
| 0 | No findings. This happens only for ledgers with no Tier A rows (ED-19, ED-21). It certifies the bookkeeping, not the truth. |
| **1, with only `LEDGER_UNAUDITED_TIER_A` flags** | **0 blocking findings, and no person has yet certified that each Tier A statement means what its gloss says.** This is the state of every paper here with Tier A rows. It is *not* the Elenchus publication-gate pass, which needs exit 0. The papers were published by the author's explicit decision with these flags open, and each paper says so. |
| 1, with any `block` finding | Inconsistent ledger: an orphan, a tier inversion, a kind overclaim, a missing or mismatched evidence blob, a cycle or a schema error. Never published. |
| 2 | The gate could not run, or looked at nothing. An empty ledger is INCOMPLETE, never clean. |

### 1.8 The publication rule

A paper is published (Zenodo, CC-BY-4.0, with an AI-use statement) only when all of these hold:

- the independent audit did not return REJECT;
- every correction it asked for was applied (each paper's `REVISION.md`);
- the controls were caught;
- a result remains after the audit.

**Negative results are published like positive ones.** In this folder, ED-15 (QU-1 refuted), ED-19 (3D feasibility, negative), ED-21 (quantum transition absent in SCHA) and ED-02 (a null result) went out as papers.

**What an AI audit is NOT.** It is not peer review. It is not a human statement-adequacy audit. It does not lift a `LEDGER_UNAUDITED_TIER_A` flag. It is a second agent attacking the first agent's work with the same kinds of tools. That catches real errors (§1.9), but it does not replace a mathematician reading the statements. Under this repository's *Verification Primacy* rule, no audit verdict here is evidence of mathematical correctness. Only the kernel checks, read with their scope, are.

### 1.9 Errors the method caught (details and DOIs in `METHODOLOGY.md`)

- **ED-15 / P2:** the zero-point optimality conjecture QU-1 is *refuted* numerically for 8 of 12 completely monotone potentials. It was published as a counterexample, and ED-20 then certified one case in part.
- **ED-21 / B1 and ED-19 / B3:** preregistered hypotheses failed and were published as negative results.
- **ED-23 / N4:** the preregistration itself was wrong. The kernel proved `cycle4_not_lumpable`, so the mutant count is *not* strongly lumpable with holding steps. The paper reports the false clause.
- **ED-14 / P1:** the audit forged a LeanFlow axiom report with `#exit`: the checker returned `verified: true` for `axiom cheat : False`. LeanFlow was fixed with a per-run sentinel.
- **ED-24 / A2:** a `debug.skipKernelTC` + `addDecl` forgery passes `#print axioms` and fails only a kernel replay. As a result, the Tier-A gate now requires a replay and a grep.
- **H11 (lane behind ED-18):** a planted `axiom ctl_cheat : False` sat inside a claimed module, where any importer would inherit it. It was moved out, and the separate-controls rule was adopted.
- **ED-06/07 → ED-10:** a shifted-force truncation at r_c = 8 moved Yukawa energies by more than the triangular–square gap. The erratum was owed against ED-07 and was fixed with the exact potential in ED-10.

### 1.10 Operational lessons

- **Prompts leak into workflow agents.** A user message sent mid-run reached every running agent, and the whole first workflow of 2026-10-25 executed the wrong task. Every workflow prompt now begins with a TASK SCOPE preface, and relayed messages are ignored.
- **Cold page cache on disk 2.** After a reboot the pinned Lean build compiles at about 1.5 MB/s (mmap faults, one 4 KB page at a time), which looks like a hang. Warm the cache with sequential reads before fanning out Lean jobs.
- **Background jobs die with the session.** Two multi-hour jellium runs were lost. Long jobs are now launched with `setsid nohup` and stream partial results.
- **Lean catches preregistration errors.** Formalising a preregistered claim is itself a test of the preregistration (N4).
- **Planted controls belong in separate files.** This folder's own consistency check found four axiom-audit files (`formal_cert/Triangular/Axioms.lean` and three `BAOCert/**/Axioms.lean`) written before the rule was adopted that still declare `ctl_sorry` / `ctl_cheat` inline. They are reported, not hidden (`CONSISTENCY_REPORT.md` §4).

---

## 2. Registry

The full metadata (Lean files, code PRs, auditor and caveats) is in [`REGISTRY.md`](REGISTRY.md) and [`REGISTRY.json`](REGISTRY.json). Each DOI was resolved against the public Zenodo API, and every title matched the local metadata exactly. The md5 of every copied PDF matched the checksum of the PDF that Zenodo serves. Tiers count the rows of each paper's own ledger. ED-06 and ED-07 share one ledger.

| id | date | publication | DOI | result | tiers A/L/C/X | AI audit |
|---|---|---|---|---|---|---|
| ED-01 | 2026-10-08 | [The sharp constant of the absolute dyadic triangular Hilbert sum is at least 3](discoveries/dyadic_triangular_hilbert/) | [10.5281/zenodo.23232389](https://doi.org/10.5281/zenodo.23232389) | positive (lower bound) | no ledger | review (no AUDIT.md) |
| ED-02 | 2026-10-08 | [A null result for the matrix-valued sharp one-dimensional Lieb-Thirring inequali...](discoveries/lt_matrix_audit/) | [10.5281/zenodo.23245266](https://doi.org/10.5281/zenodo.23245266) | negative (null result) + audit | no ledger | review (no AUDIT.md) |
| ED-03 | 2026-10-08 | [Kernel-checked enclosures of DESI DR2 BAO distances in Lean 4: certifying solver...](discoveries/certified_bao/) | [10.5281/zenodo.23247730](https://doi.org/10.5281/zenodo.23247730) | positive | no ledger | CONFIRMED_WITH_CORRECTIONS |
| ED-04 | 2026-10-10 | [Kernel-checked constraints from DESI DR2 BAO in Lean 4: certified exclusions of ...](discoveries/certified_desi_h0/) | [10.5281/zenodo.23284020](https://doi.org/10.5281/zenodo.23284020) | partial (P2) + positive (P3) | no ledger | CONFIRMED_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS |
| ED-05 | 2026-10-10 | [Riesz-energy, finiteness and every-density corollaries of the openai/math planar...](discoveries/triangular_riesz/) | [10.5281/zenodo.23285631](https://doi.org/10.5281/zenodo.23285631) | positive (corollaries) | no ledger | CONFIRMED_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS |
| ED-06 | 2026-10-11 | [Planar universal optimality, tiered: kernel-checked consequences, a non-uniquene...](discoveries/universal_optimality_tiered/) | [10.5281/zenodo.23293112](https://doi.org/10.5281/zenodo.23293112) | positive (Tier A) + partial numerics | 6/7/3/6 | ACCEPT_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS |
| ED-07 | 2026-10-11 | [Planar universal optimality, tiered: kernel-checked consequences, a non-uniquene...](discoveries/universal_optimality_tiered/) (v2) | [10.5281/zenodo.23293429](https://doi.org/10.5281/zenodo.23293429) | positive (Tier A) + partial numerics | 6/7/3/6 | ACCEPT_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS |
| ED-08 | 2026-10-11 | [The Triangular Lattice and Universal Optimality: human proofs, Lean 4 verificati...](discoveries/textbook_universal_optimality/) | [10.5281/zenodo.23295142](https://doi.org/10.5281/zenodo.23295142) | exposition | no ledger | ACCEPT_WITH_CORRECTIONS |
| ED-09 | 2026-10-25 | [The bilayer dipolar-exciton interaction is completely monotone in r^2: kernel-ch...](discoveries/ar_dipolar_exciton/) | [10.5281/zenodo.23646103](https://doi.org/10.5281/zenodo.23646103) | positive | 14/4/7/8 | ACCEPT_WITH_CORRECTIONS |
| ED-10 | 2026-10-25 | [The triangular lattice minimises the planar Yukawa energy at every density and f...](discoveries/ar_yukawa_crystal/) | [10.5281/zenodo.23646105](https://doi.org/10.5281/zenodo.23646105) | positive + erratum fix | 11/5/3/6 | ACCEPT_WITH_CORRECTIONS |
| ED-11 | 2026-10-25 | [The Rytova-Keldysh interaction is a positive Gaussian mixture: kernel-checked ad...](discoveries/ar_keldysh_tmd/) | [10.5281/zenodo.23646107](https://doi.org/10.5281/zenodo.23646107) | positive | 9/5/6/10 | ACCEPT_WITH_CORRECTIONS |
| ED-12 | 2026-10-25 | [A cutoff-independent enstrophy bound for the sigma = 3 dispersive dyadic shell m...](discoveries/ar_sigma3_enstrophy/) | [10.5281/zenodo.23646111](https://doi.org/10.5281/zenodo.23646111) | positive | 7/2/4/5 | ACCEPT_WITH_CORRECTIONS |
| ED-13 | 2026-10-25 | [The Bogoliubov structure factor under the dual-scale envelope sqrt(k/2k_s): kern...](discoveries/ar_bogoliubov_sk/) | [10.5281/zenodo.23646117](https://doi.org/10.5281/zenodo.23646117) | positive (shape) + one-sided test | 8/4/4/8 | ACCEPT_WITH_CORRECTIONS |
| ED-14 | 2026-10-26 | [The Sandier-Serfaty triangular-lattice conjecture: an independent reproduction o...](discoveries/prog_sandier_serfaty_audit/) | [10.5281/zenodo.23653827](https://doi.org/10.5281/zenodo.23653827) | audit / reproduction | 7/5/5/8 | ACCEPT_WITH_CORRECTIONS |
| ED-15 | 2026-10-26 | [Does the triangular lattice minimise the harmonic zero-point energy? A numerical...](discoveries/prog_zero_point_optimality/) | [10.5281/zenodo.23653833](https://doi.org/10.5281/zenodo.23653833) | negative (QU-1 refuted numerically) | 8/3/13/13 | ACCEPT_WITH_CORRECTIONS |
| ED-16 | 2026-10-26 | [Completely monotone and Bernstein functions in Lean 4: a kernel-checked library ...](discoveries/prog_cm_bernstein_library/) | [10.5281/zenodo.23653842](https://doi.org/10.5281/zenodo.23653842) | positive (library) | 20/5/6/4 | ACCEPT_WITH_CORRECTIONS |
| ED-17 | 2026-10-26 | [The Feynman-Bijl single-mode bound in Lean, and a diffraction test of the Bogoli...](discoveries/prog_superfluid_structure_factor/) | [10.5281/zenodo.23653846](https://doi.org/10.5281/zenodo.23653846) | positive (Lean) + negative (envelope refuted) | 11/5/7/8 | ACCEPT_WITH_CORRECTIONS |
| ED-18 | 2026-10-26 | [Fixation probabilities as absorption limits of matrix powers, kernel-checked: ne...](discoveries/prog_population_genetics_fixation/) | [10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850) | positive | 14/5/8/9 | ACCEPT_WITH_CORRECTIONS |
| ED-19 | 2026-10-26 | [Can the planar Sandier-Serfaty proof architecture reach three-dimensional bcc je...](discoveries/p2_3d_feasibility/) | [10.5281/zenodo.23655002](https://doi.org/10.5281/zenodo.23655002) | negative | 0/4/18/8 | ACCEPT_WITH_CORRECTIONS |
| ED-20 | 2026-10-26 | [The triangular lattice is not a local minimum of the harmonic zero-point energy ...](discoveries/p2_certified_zero_point/) | [10.5281/zenodo.23655392](https://doi.org/10.5281/zenodo.23655392) | positive (certified counterexample) | 8/0/13/2 | ACCEPT_WITH_CORRECTIONS |
| ED-21 | 2026-10-26 | [The harmonic triangular-to-oblique instability of the quantum Gaussian-core crys...](discoveries/p2_quantum_transition/) | [10.5281/zenodo.23655625](https://doi.org/10.5281/zenodo.23655625) | negative (within SCHA) | 0/0/26/13 | ACCEPT_WITH_CORRECTIONS |
| ED-22 | 2026-10-26 | [Toward a machine-checked proof of the claimed Sandier-Serfaty certificate: 4 of ...](discoveries/p2_sandier_serfaty_lean/) | [10.5281/zenodo.23656804](https://doi.org/10.5281/zenodo.23656804) | partial (4/12 stages) | 16/1/8/10 | ACCEPT_WITH_CORRECTIONS |
| ED-23 | 2026-10-26 | [The isothermal theorem of evolutionary graph theory for birth-death updating, ke...](discoveries/p3_isothermal_theorem/) | [10.5281/zenodo.23660071](https://doi.org/10.5281/zenodo.23660071) | positive (+ preregistration error caught) | 11/4/9/2 | ACCEPT_WITH_CORRECTIONS |
| ED-24 | 2026-10-26 | [An independent rebuild, kernel replay and statement audit of the openai/NavierSt...](discoveries/p2_navier_stokes_audit/) (v1.1) | [10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381) | audit | 4/4/8/10 | ACCEPT_WITH_CORRECTIONS |

## 3. Layout

```
elenchus/
  README.md                this file (method first, then the registry)
  METHODOLOGY.md           the long form, with the cases where the method caught errors
  REGISTRY.json / .md      every Zenodo publication of the programme
  CONSISTENCY_REPORT.md    output of tools/check_consistency.py (committed as run)
  preregistrations/        the preregistrations, with their first-commit hashes
  REDACTION.md             what was redacted for the public copy, and every re-hashed evidence digest
  kernel_replay_2026-10-26/  final record of the 2026-10-26 kernel replay (REPLAY.md, replay.jsonl, result.json)
  discoveries/<slug>/      publication_meta.json, zenodo_doi.txt, AUDIT.md, REVISION.md,
                           ledger/ (ledger.json, build scripts, evidence/, gate_output.txt),
                           STATEMENT_LOCK.json (where the auditor locked statements),
                           LEAN.md + lean_manifest.json + lean/ (the Lean files the ledger cites, at their module paths;
                           for ED-03..08, which recorded no hashes, the version last committed before publication)
  tools/check_consistency.py
  tool/ledger.py           the Elenchus ledger gate (unmodified) + README.md
```

**What was not copied:**

- Upstream Lean sources (openai/math, openai/NavierStokesAndEuler, Mathlib, Apache-2.0). They are listed by path and sha256 in each `LEAN.md`. Fetch them at the pinned commits.
- Large data and run directories, and the paper build trees (`data/`, `gen/`, LaTeX sources).
- Third-party full texts that the Tier L quote checks used (3 files). They are listed with their sha256 in `ledger/NOT_REDISTRIBUTED.md`. The quoted excerpts stay in the evidence blobs.
- The PDFs of the 24 publications (on Zenodo at each DOI).
- The 126 MB A1-continuation Lean tree (`formal_cert/Programmes/SandierSerfatyL1/`), which was still running.

The evidence blobs name compile transcripts by absolute paths on the producing machine. Those transcripts are not in this repository.

## 4. Re-checking from this repository

```bash
python3 elenchus/tools/check_consistency.py            # needs network for Zenodo
python3 elenchus/tools/check_consistency.py --offline  # ledgers, hashes, scans only
```

## 5. Credits and limits

- The A2 audit ([ED-24](discoveries/p2_navier_stokes_audit/)) is an independent rebuild and audit of **openai/NavierStokesAndEuler**. All credit for that formalisation belongs to its authors. ED-24 is not a claim that a Clay problem is solved.
- Every planar universal-optimality corollary depends on **openai/math**'s `universal_energy_minimum`. That theorem was accepted by Comparator, is AI-generated and is not peer reviewed.
- All producers and auditors were AI agents, and no human audit has taken place. The 154 `LEDGER_UNAUDITED_TIER_A` flags across the ledgers are the open work.
