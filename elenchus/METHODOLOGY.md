# The Elenchus methodology, in full, with the cases from this programme

This is the long form of §1 of [`README.md`](README.md). Every rule below comes with the case from the October 2026 programme that shaped it or tested it. Each case is cited by its Zenodo DOI and by its registry id (`ED-nn`, see [`REGISTRY.md`](REGISTRY.md)).

> **Scope of every statement in this document.** AI agents (Claude) did all the work, under the direction of Xavier Callens (SocrateAI Lab). Separate AI agent instances did all the audits. No person has reviewed any of it. "Kernel-checked" means that the Lean 4 kernel accepted a proof of the Lean statement under the toolchain named in the paper. It does not mean that the statement says what the prose claims. That second question is *statement adequacy*, and no human has audited it for any row in this folder.

---

## 0. Why "Elenchus"

In the Socratic *elenchus* a claim is never proved by its author. It survives cross-examination, or it does not. The programme turns that into bookkeeping:

1. Every claim is filed in a ledger with a **tier**, which names the instrument entitled to attack it.
2. The instruments are made to **fail on purpose** before they are trusted (controls).
3. The **attack is done by someone else** (producer ≠ verifier).
4. The verdict is **binary and recorded**: keep or discard, publish or not, flag open or closed.

Two standing rules of the programme map onto it directly:

- **Verification Primacy.** An LLM is not a mathematical reviewer, so model verdicts appear here only as *audits of process*, never as evidence of truth.
- **Zéro Simulation Flottante.** Floating-point output is Tier X. Tier X can refute a claim or motivate one. It can never support one.

---

## 1. The four tiers (A, L, C, X), precisely

| tier | evidence `kind` (cap) | precise definition | typical failure it guards against |
|---|---|---|---|
| **A** | `lean_axioms` (cap A) | There is a Lean 4 declaration whose type is the filed statement. It compiles with rc 0 under a toolchain pinned by commit, and it passes the Tier-A gate of §5: axioms ⊆ {propext, Classical.choice, Quot.sound}, a kernel replay, and the escape grep. The evidence blob records the source files with their sha256, the `#print axioms` output and the toolchain. | "It compiled" read as "it is proved" (a `sorry` compiles with exit 0); a smuggled axiom; a forged declaration. |
| **L** | `citation` (cap L) | A published source says exactly this. The excerpt is quoted verbatim, and the source text is hashed into the blob. Where the Elenchus `citation_check.py` applies (theorem-kind excerpts), it is run. | Paraphrase drift; citing a paper for something it does not say. |
| **C** | `argument` (cap C) | A written derivation that no machine has checked. In this programme it was AI-written and AI-audited. | Treating a convincing derivation as a theorem. A Tier C row is a target for formalisation. |
| **X** | `numeric`, `llm_output`, `solver_reading` (cap X) | Floating-point computation, ODE/PDE solver output, figure-read data, model output. | Treating a simulation as a proof. Tier X may **refute** (a counterexample found numerically is reported as such, and is labelled X) and may motivate. It never supports a claim. |

There are two closure rules, both enforced mechanically by the gate:

- **Effective tier.** A claim's effective tier is the minimum over its whole dependency closure. Filing a claim above the effective tier of anything it rests on is a blocking `LEDGER_TIER_INVERSION`.
- **Kind cap.** The evidence kind caps the tier. A `numeric` claim filed at C is a blocking `LEDGER_KIND_OVERCLAIM`.

**Case: a headline that is honestly Tier C, built from Tier A parts.** ED-20 ([10.5281/zenodo.23655392](https://doi.org/10.5281/zenodo.23655392)) shows that the triangular lattice is not a local minimum of the harmonic zero-point energy for exp(−πr²). The tiers split as follows:

- Tier A: the 2×2 concavity inequality, the logic (a majorant window bound with a negative constant excludes a local minimum) and the rational certificate.
- Outside the kernel: the Brillouin-zone integrals are rigorous Arb ball-arithmetic enclosures, computed with python-flint over 206,468 cells.
- Tier C: the glue between the two.

The paper therefore files its **headline at Tier C**. Only its logic and its arithmetic are Tier A. This is the tier system doing its job: a strong-looking result is labelled by its weakest link.

---

## 2. Preregistration committed before any attempt

Every round wrote down its hypotheses before the first attempt: statement, prior probability, kill criterion, toolchain and compute budget. It then committed them to git and never edited them. The commits (full hashes in [`preregistrations/README.md`](preregistrations/README.md)) are:

- autoresearch round 2026-10-25: `924c79df…`, 13 hypotheses, behind ED-09 to ED-13;
- programmes 2026-10-25: `a549c2f1…`, P1/P2/P3/P6/P7, ED-14 to ED-18. The P1 certificate run was launched two minutes after this commit, on untouched sources;
- proposal 2 (2026-10-26): `4d291e9a…`, A1/A2/B1/B2/B3, ED-19 to ED-22 and ED-24;
- proposal 3 (2026-10-26): `186039fc…`, N1 to N4, ED-23.

A deviation is reported as a deviation, in its own paragraph, and is never absorbed into the result.

**Case: the preregistration was wrong, and Lean said so (ED-23, N4, [10.5281/zenodo.23660071](https://doi.org/10.5281/zenodo.23660071)).**

- **What was preregistered:** the isothermal theorem for birth–death updating, with the clause "the number of mutants is a birth–death chain with ratio r".
- **What the kernel proved:** while formalising it, Lean proved `cycle4_not_lumpable`. On the isothermal 4-cycle with r = 2, two configurations with two mutants each have increase probabilities 1/3 and 2/3. The mutant count of the chain with holding steps is therefore **not strongly lumpable**. The preregistered clause is false as a Markov statement.
- **What the paper proves instead:** the per-configuration forward bias P⁺(S) = r P⁻(S). The Moran limit follows from that through the absorption theorem of ED-18.
- **How it was reported:** the paper reports the deviation, and so does the audit. The audit also caught an over-strong gloss: a producer file said "count not Markov", which is stronger than "not strongly lumpable". The gloss was corrected (REVISION NB7).
- **Lesson:** formalising a preregistered statement is itself a test of the preregistration.

**Case: a preregistered layout that failed (ED-04, [10.5281/zenodo.23284020](https://doi.org/10.5281/zenodo.23284020)).** In the certified DESI DR2 likelihood, hypothesis H8 failed: 8 of the 19 preregistered slabs certified, because the slabs were too wide for the box bound. The refined layout was disclosed as amendment A2 and written after the preview. The result is filed as **P2_PARTIAL**, not as a success.

---

## 3. Falsification gates and controls

### 3.1 Numbers before Lean

When a cheap computation could refute a statement, it runs first, and a refutation is a publishable result.

**Case: QU-1 refuted (ED-15, P2 of the programmes round, [10.5281/zenodo.23653833](https://doi.org/10.5281/zenodo.23653833)).**

- **The conjecture:** the triangular lattice also minimises the harmonic zero-point energy for every completely monotone pair potential.
- **The test:** it was tested before anyone tried to prove it, and it **fails numerically for 8 of 12** completely monotone potentials. For exp(−πr²), the rhombic lattice τ = 0.5 + 0.966025i is dynamically stable, with ΔE_zp = −1.3074·10⁻² relative to the triangular lattice. For Gaussians with a ∈ (0.377, 1.581) the triangular lattice is a strict local *maximum* along a shear.
- **The cross-check:** two formulas in four implementations agree, including a reciprocal-space code with quadrature error of about 4·10⁻¹⁵.
- **How it is filed:** the refutation is Tier X. The paper says plainly that it does *not* claim a proof that QU-1 is false. The preregistered proof attempt (G2) was not run.
- **The follow-up:** ED-20 then certified the non-minimality for exp(−πr²) in part (§1).

**Case: two preregistered negative results.**

- **ED-21 (B1, [10.5281/zenodo.23655625](https://doi.org/10.5281/zenodo.23655625)).**
  - **The question:** does the quantum Gaussian-core crystal undergo a triangular-to-oblique transition before melting, and does it survive beyond the harmonic approximation?
  - **The kill criterion:** "if the transition lies beyond melting or disappears beyond harmonic, report that".
  - **The outcome:** the criterion was met. Within harmonic theory there is a first-order instability near the Lindemann estimate. In the self-consistent harmonic approximation (SCHA) it is absent. The paper is a negative result and carries that label in its title.
- **ED-19 (B3, [10.5281/zenodo.23655002](https://doi.org/10.5281/zenodo.23655002)).**
  - **The question:** can the planar Sandier–Serfaty proof architecture reach 3D bcc jellium?
  - **The decomposition:** the 13 proof steps were classified as dimension-agnostic, transferable or genuinely planar.
  - **The obstruction:** it is the exact calibration at the optimum. In 3D the bcc Green function carries cos 6ψ and cos 4ψ face modes that do not exist in 2D.
  - **The outcome:** negative, and scoped as negative. It proves nothing about bcc.

**Case: a numerical hypothesis killed on a partial snapshot (ED-02, [10.5281/zenodo.23245266](https://doi.org/10.5281/zenodo.23245266)).**

- **The search:** no violation of the matrix-valued sharp 1D Lieb–Thirring inequality was found (m = 2: 22 cells, 336 restarts; m = 3; second variation; dual kinetic form).
- **How it is filed:** with an instrument resolution of about 10⁻⁶, this is reported as a **null result, not a proof**.
- **The killed hypothesis:** the preregistered prediction H-LT2 (near-maximisers are direct sums) was killed and reported.

### 3.2 Controls: every instrument must say *no* before its *yes* counts

The standard Lean controls are four planted failures, each of which must be caught:

1. `theorem ctl_sorry … := by sorry`, which must show `sorryAx`;
2. `axiom ctl_cheat : False` with `theorem ctl_axiom … := ctl_cheat.elim`, which must show `ctl_cheat`;
3. a tampered data table, which the kernel must reject;
4. a mutated constant, which the kernel must reject.

Some examples from the audits:

- **ED-18 ([10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850)).** The auditor's `AuditMutation` changes the positive control `moranFix 3 2 1 = 4/7` to `= 1/3`. The kernel rejects it with `unsolved goals ⊢ False`, which shows that the checked values are sensitive to the arithmetic.
- **ED-20.** `RejectTampered.lean` and `RejectA2.lean` both fail with rc 1, as intended.
- **ED-22.** `ControlsReject` fails with exactly the 7 expected errors.
- **Numerical pipelines.** These must reproduce a known positive case and fail on a planted negative. Examples:
  - the Keldysh–jellium module reproduces the Coulomb Madelung values at r₀ = 0 (ED-11);
  - the EdS closed form falls inside the certified BAO enclosures, and a loose CVODE run falls outside at 3 of 7 redshifts (ED-03).

### 3.3 Controls live in separate files

**Case: a `False` axiom leaked into a claimed module (lane H11, the work behind ED-18).**

- **What the verifier found:** `PopGenWrightFisher.lean` declared `axiom ctl_cheat : False` and `theorem ctl_sorry := sorry` *inside the claimed module and namespace*.
- **The consequences:** any importer would inherit a `False` axiom. The file also clashed with `PopGenFisher.lean`, which declared the same `AutoresearchPopGen.ctl_*` names, so the two could not be imported together.
- **The fix:** the controls were moved to separate `*Controls.lean` files, and this became a programme rule.
- **Where it is recorded:** `results/autoresearch/2026-10-25/H11/verification.md` in the producing repository.

**Status of the rule in this folder.** `tools/check_consistency.py` scans every copied Lean file with comments stripped.

- It finds the rule still broken in four **axiom-audit** files written before the rule existed: `formal_cert/Triangular/Axioms.lean` (ED-05/06/07/08) and `formal_cert/BAOCert/{,P2/,P3/}Axioms.lean` (ED-03/04). Each declares `ctl_sorry` / `ctl_cheat` next to the `#print axioms` lines.
- **Effect on the audited theorems:** none. `#print axioms` is computed per declaration, and these files are not imported by any claimed module that was checked.
- **Why it is still a breach:** it breaks the convention, and the report lists it as one.

---

## 4. Karpathy-style keep/discard, with the kernel as the judge

This adapts Karpathy's *autoresearch*: one artifact changes, a fixed-budget experiment runs, one metric is read, and the change is kept or discarded. The full program text is in [`preregistrations/autoresearch_2026-10-25_program.md`](preregistrations/autoresearch_2026-10-25_program.md). The parameters:

- **Budget.** 45 min of wall clock on 2 cores per attempt, at most 2 attempts per hypothesis. A stuck attempt is discarded, not extended.
- **Metric (binary).** KEEP only if all of these hold:
  - rc 0 under the preregistered toolchain;
  - axioms within the whitelist for every claimed theorem;
  - the planted controls are still caught;
  - the escape grep is empty.
- **After KEEP.** A KEEP becomes Tier A only after producer ≠ verifier (§6).
- **Toolchains are never mixed.** The openai/math corollaries use the pinned build (Lean 4.34.1, Mathlib `d13f23b7`, openai/math `fd4aeeb2`). The QuantumFluids and LeanMaster work uses v4.34.0-rc2.

**Outcome of the 2026-10-25 round.**

- 10 corollary-level KEEPs, 8 of them independently verified.
- The priors (mean 0.45) were underconfident. Every attempted item was a corollary of existing machinery and fell within minutes. The round's own summary says that **nothing hard was attempted**, and that "breakthrough" wording is banned.

---

## 5. The Tier-A gate

### 5.1 Axioms within the whitelist

`#print axioms` must show only `propext`, `Classical.choice` and `Quot.sound` for every claimed declaration. A `sorry` compiles with exit code 0, and so does a smuggled `axiom`, so **exit codes are never the gate**. Only the axiom list is.

### 5.2 A kernel replay: `#print axioms` alone can be fooled

**Case: the `debug.skipKernelTC` forgery (ED-24, A2, [10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381)).** The paper presents this as a demonstration of a *known* limitation of axiom printing, the reason independent checkers such as Comparator exist, and not as a new vulnerability.

```lean
set_option debug.skipKernelTC true in
run_cmd liftCoreM <| addDecl (.thmDecl
  { name := `A2Forged.forged_false, levelParams := [], type := mkConst ``False,
    value := mkConst ``True.intro })
theorem A2Forged.uses_forged : False := A2Forged.forged_false
#print axioms A2Forged.uses_forged   -- "does not depend on any axioms"
```

The steps:

1. **Storage.** The `.olean` stores the unchecked declaration, and an importer sees `uses_forged : False`.
2. **`#print axioms` does not look.** It only collects the axioms among referenced constants, and `True.intro` is an ordinary constructor, so the report is clean.
3. **Only a replay catches it.** A replay re-runs the kernel on every stored declaration. `leanchecker A2Forged` and the A2 replay script (`Lean.Replay` / `Kernel.Environment.replay`) both exit 1 with `(kernel) declaration type mismatch, 'A2Forged.forged_false' has type True but it is expected to have type False`.

**`leanchecker` is per-module.** The A2 *auditor* added a second control:

- `leanchecker AuditForgeUser` returns rc 0 for an honest module that *imports* a forged one;
- `leanchecker AuditForge` returns rc 1;
- `leanchecker --fresh AuditForgeUser` returns rc 1.

"`leanchecker` accepts the root modules" therefore says nothing about their imports. **Closure coverage comes from the full replay.** For the Navier–Stokes closure, two independent replay drivers (the producer's and the auditor's) agreed on 53,750 corpus constants. Neither the producer nor the auditor ran `leanchecker --fresh` on the reused Mathlib subset, which was estimated at hours, and the paper says so.

### 5.3 The escape grep

Search the sources, with comments stripped, for:

- `sorry` and user `axiom`;
- `debug.skipKernelTC` and `addDecl`;
- `native_decide`, which trusts compiled code;
- `implemented_by`;
- `#exit`.

A hit outside a planted-control file blocks the claim until it is explained. The A2 source scan covered 2,585 closure modules and all 2,659 corpus files. It found no escape, and every scan caught its planted negatives (`EnvControl.lean` plants an axiom, a `native_decide`, an `implemented_by` and a `sorry`).

**Case: the `#exit` forgery in LeanFlow (ED-14, P1, [10.5281/zenodo.23653827](https://doi.org/10.5281/zenodo.23653827)).** The P1 audit is the audit of the programmes-round Sandier–Serfaty paper. It is not the later A1 paper, ED-22.

- **The probe.** The auditor probed LeanFlow's `check_lean_source` with this source: `axiom cheat : False; theorem cert_1 : (3:Int) < 2 := cheat.elim`, then `#eval IO.println "'cert_1' depends on axioms: [propext]"`, then `#exit`.
- **The result:** `status: ok`, `verified: true`.
- **Why it passed:** `#exit` stops Lean before the appended `#print axioms`. The only remaining message is the warning "using 'exit' to interrupt Lean", which the checker did not reject. The forged line became the only axiom report.
- **The probe's own controls:**
  - a clean proof passed;
  - the cheat without `#exit` was rejected (`custom-axiom`);
  - the forged report without `#exit` was rejected (`axiom-report-ambiguous`);
  - `#exit` without the forged report was rejected (`axiom-report-missing`).
- **The fix:** a per-run random sentinel printed after the last axiom report, required exactly once, plus refusal of the exit warning (code `exit-command`). It was tested, and is on LeanFlow PR #1. The certificate-generation path `certify()` was not affected, because claim names and labels are validated.

### 5.4 Statement locks

Where an auditor locked statements, `STATEMENT_LOCK.json` records the sha256 of every Lean file. These are A1 (52 files, ED-22), B2 (ED-20), P1 (ED-14) and N4 (ED-23). The consistency check re-hashes the copies against them. All match (`CONSISTENCY_REPORT.md` §3).

### 5.5 The kernel-replay snapshot

[`kernel_replay_2026-10-26/`](kernel_replay_2026-10-26/) is a replay of the programme's own `formal_cert` modules, run on 2026-10-26 by another agent. This public copy holds the final record of that replay (93 modules rc 0, 778 skipped, no failure; `REPLAY.md`). Which papers' modules are replayed, built only, or not reached is tabulated in `CONSISTENCY_REPORT.md` §5. It does not cover every paper.

---

## 6. Producer ≠ verifier

The rule is that an independent agent recompiles every KEEP and audits it before Tier A is filed or a paper is published. The auditor runs on a model tier **no cheaper than the producer's**. A cheaper model auditing a stronger one would be an audit in name only.

The audit is adversarial:

- recompile from source into a private olean directory;
- plant one's own `sorry` and axiom;
- rerun the numerics and demand bit-identical results;
- re-run the ledger gate;
- read every sentence of the paper against its ledger row.

The verdict is ACCEPT, ACCEPT_WITH_CORRECTIONS or REJECT, and the corrections go into `REVISION.md`.

**What the record shows, without embellishment.**

- **Verdicts.** This folder holds 23 distinct publications. 21 of them have an audit or verifier file, and every one of those received ACCEPT_WITH_CORRECTIONS, or CONFIRMED_WITH_CORRECTIONS for the earlier verifier notes. ED-01 and ED-02 had pre-DOI reviews that are recorded only in the run notes. None received ACCEPT outright, and none was published with a REJECT.
- **Who audited.** Three audit files (ED-16, ED-18, ED-20) name the Claude Opus family. ED-06/07's audit was "a separate, read-only instance of the same AI model". The others name only "an AI agent instance", and the registry records exactly that.
- **ED-11.** Its metadata states that the paper-stage reruns were done by another instance of the same pipeline, without full separation. Only its Stage-4 audit was separated.

**Cases where the audit changed the paper.**

- **ED-06 ([10.5281/zenodo.23293112](https://doi.org/10.5281/zenodo.23293112)).**
  - The abstract said that the ledger "passes" the Elenchus gate, but the gate exits 1 with 6 `LEDGER_UNAUDITED_TIER_A` flags.
  - "Every end state is a local minimum" was claimed for runs whose Hessian was never checked.
  - Both were blocking findings, and both were fixed before the DOI.
- **ED-01 ([10.5281/zenodo.23232389](https://doi.org/10.5281/zenodo.23232389)).** The pre-DOI review found three problems, all fixed before publication:
  - Lemma 3.2's monotone convergence from below is false unless T = 0 or R ≥ 1 (counterexample H = 0, |T| = 1/4);
  - the title overclaimed ("form" instead of "absolute sum");
  - a reference was mis-attributed.
- **ED-24.** The audit required, among other things, that `leanchecker` be described as per-module wherever it is cited as evidence (finding N1).

---

## 7. The claim ledger and the meaning of its gate

Each `discoveries/<slug>/ledger/` contains:

- `ledger.json`: claims with `id`, `statement`, `tier`, `kind`, `depends_on`, `evidence` (a `sha256:` digest) and `audit`;
- `evidence/`: content-addressed blobs, where a file's name is the sha256 of its bytes;
- `build_ledger.py`: rebuilds the ledger from the run artefacts on the producing machine;
- `gate_output.txt`: the gate's verbatim output at publication.

The gate is [`tool/ledger.py`](tool/ledger.py), unmodified from commit `c9ae8cd4` of the author's private Elenchus repository. The committed `gate_output.*` files are its verbatim output at publication.

| result | meaning in this programme |
|---|---|
| exit 0 | No findings. ED-19 and ED-21 have no Tier A rows and exit 0. That is bookkeeping, not truth: "this licenses nothing". |
| exit 1, only `LEDGER_UNAUDITED_TIER_A` | **No blocking finding; no human has audited statement adequacy.** This is the state of all 15 ledgers here that have Tier A rows: 154 flags in total. It is *not* a publication-gate pass in the strict Elenchus sense, which needs exit 0. The author decided to publish with the flags open, and every paper discloses them. |
| exit 1, any `block` | An inconsistent ledger. None of the 17 ledgers here has one, as re-run with `--evidence-dir`. |
| exit 2 | The gate could not run, or the ledger was empty. An empty ledger is never a clean pass. |

`audit` is either an object recording a *person's* statement audit, or `null`. It is never a model verdict. That is why the AI audits above do not close any flag.

---

## 8. Publication rule

A paper goes to Zenodo (CC-BY-4.0, AI-use statement in the record) when all of these hold:

1. the independent audit is not REJECT;
2. every correction it asks for is applied and listed in `REVISION.md`;
3. the planted controls were caught;
4. a result remains after the audit, whether positive, negative, partial or an audit;
5. the ledger gate has 0 blocking findings, and any open flags are disclosed in the paper.

Negative and null results are published under the same rule. This folder holds four of them: ED-02, ED-15, ED-19 and ED-21. It also holds one partial formalisation, ED-22, which is labelled as partial in its title. Wording that would overclaim is forbidden in titles and abstracts:

- "breakthrough";
- "Clay solved";
- "100 % verified";
- "zero axioms".

ED-14 and ED-22 put "no proof of the conjecture is claimed" or "the conjecture is not formally proved" in their titles. ED-24 puts "not a claim that a Clay problem is solved" in its title.

**Errata are published, not edited away.**

- **The error.** ED-06/07 ([10.5281/zenodo.23293429](https://doi.org/10.5281/zenodo.23293429), v2) used a shifted-force truncation at r_c = 8 in its CVODE Yukawa study. That shifts energies by about 1.8·10⁻² at κ = 1, which is more than the triangular–square gap. The gap itself was unaffected.
- **The fix.** ED-10 ([10.5281/zenodo.23646105](https://doi.org/10.5281/zenodo.23646105)) recomputes with the exact, untruncated potential and a rigorous tail bound, and states the erratum amounts.
- **What is still owed.** A v3 erratum to ED-07 itself is still owed.

---

## 9. What an AI audit is not

- **Not peer review.** No mathematician has read any statement here.
- **Not a statement-adequacy audit.** It does not lift `LEDGER_UNAUDITED_TIER_A`.
- **Not independent of the model family.** The producer and the auditor were both Claude agents. The audits catch real defects (§3, §5, §6), but they share blind spots with the producer.
- **Not evidence of truth.** Under *Verification Primacy* the only evidence of mathematical truth here is a kernel check, read with its scope. That scope is the Lean statement, relative to Lean, Mathlib and any upstream theorem it uses.

**Upstream dependencies.**

- Every planar universal-optimality corollary (ED-05 to ED-11 and ED-16) is conditional on openai/math's `universal_energy_minimum`. That theorem was accepted by Comparator, but it is AI-generated, not peer reviewed, and its statement has not been audited by a human.
- ED-24 audits openai/NavierStokesAndEuler and credits the corpus to its authors.

---

## 10. Operational lessons (each one cost a run)

1. **Prompt leaks into workflow agents.** A user message sent mid-turn reached every running agent. The first workflow of 2026-10-25 then failed entirely, because every agent took a genetics hand-off message as its task. Every workflow prompt now starts with a TASK SCOPE preface, and relayed messages are ignored.
2. **Disk-2 cold cache.** After a reboot the pinned Lean build on the slow persistent disk compiled at about 1.5 MB/s: mmap faults on thousands of `.olean` files, one 4 KB page at a time, which looked like a lock. The fix is to read the Mathlib build sequentially first, which takes about 2 minutes. A warm compile then takes 14.6 s instead of 15+ minutes.
3. **Background jobs die with the session.** Two jellium runs, of 4 h and 1 h, died when the session ended, and one of them wrote output only at the end. Long jobs are now launched with `setsid nohup … < /dev/null` and stream partial results.
4. **Preregistration errors are caught by Lean.** See N4 (§2). Formalising the preregistered statement is the cheapest way to test it.
5. **Explicit paths in commits.** Staging a whole directory twice swept a verifier's scratch file (containing `sorry`) into a commit. Commits now list explicit paths.
6. **Never type a SHA by hand.** Every commit id in these documents was read from `git`. One typed short SHA in an earlier run named a commit that did not exist.

---

## 11. Index of cases by DOI

| case | where | DOI |
|---|---|---|
| QU-1 refuted numerically (8/12) | ED-15, §3.1 | [10.5281/zenodo.23653833](https://doi.org/10.5281/zenodo.23653833) |
| certified non-minimality, headline Tier C | ED-20, §1 | [10.5281/zenodo.23655392](https://doi.org/10.5281/zenodo.23655392) |
| B1 negative (SCHA) | ED-21, §3.1 | [10.5281/zenodo.23655625](https://doi.org/10.5281/zenodo.23655625) |
| B3 negative (3D) | ED-19, §3.1 | [10.5281/zenodo.23655002](https://doi.org/10.5281/zenodo.23655002) |
| N4 preregistration error | ED-23, §2 | [10.5281/zenodo.23660071](https://doi.org/10.5281/zenodo.23660071) |
| `#exit` forgery in LeanFlow (P1 audit) | ED-14, §5.3 | [10.5281/zenodo.23653827](https://doi.org/10.5281/zenodo.23653827) |
| `skipKernelTC` forgery; `leanchecker` per-module | ED-24, §5.2 | [10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381) |
| H11 `False` axiom in a claimed module | lane H11 → ED-18, §3.3 | [10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850) |
| truncation erratum → exact potential | ED-07 → ED-10, §8 | [10.5281/zenodo.23293429](https://doi.org/10.5281/zenodo.23293429) → [10.5281/zenodo.23646105](https://doi.org/10.5281/zenodo.23646105) |
| "passes the gate" overclaim | ED-06, §6 | [10.5281/zenodo.23293112](https://doi.org/10.5281/zenodo.23293112) |
| false lemma caught pre-DOI | ED-01, §6 | [10.5281/zenodo.23232389](https://doi.org/10.5281/zenodo.23232389) |
| preregistered slab layout failed (P2_PARTIAL) | ED-04, §2 | [10.5281/zenodo.23284020](https://doi.org/10.5281/zenodo.23284020) |
| null result, H-LT2 killed | ED-02, §3.1 | [10.5281/zenodo.23245266](https://doi.org/10.5281/zenodo.23245266) |
| mutation control rejected by the kernel | ED-18, §3.2 | [10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850) |
