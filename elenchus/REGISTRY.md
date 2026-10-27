# Registry of Zenodo publications, Elenchus programme 2026-10

Every DOI below was resolved against the public Zenodo API (`https://zenodo.org/api/records/<id>`) when this registry was built, and its title compared with the title in the local `publication_meta.json`. `tools/check_consistency.py` repeats that check from this repository alone. Machine-readable: `REGISTRY.json`.

**Read every row with its caveat.** Tier counts are claims filed in the paper's claim ledger (A kernel-checked, L cited, C human argument, X floating point). The audit is an AI audit (a separate agent instance), never a human review. `gate` = exit code of the Elenchus ledger gate run with `--evidence-dir`: 1 with only `LEDGER_UNAUDITED_TIER_A` flags means 0 blocking findings and no human statement audit yet.

| id | date | title (short) | DOI | kind | result | tiers | gate (blocks/flags) | AI audit | Zenodo title match |
|---|---|---|---|---|---|---|---|---|---|
| ED-01 | 2026-10-08 | [The sharp constant of the absolute dyadic triangular Hilbert sum is at least 3](discoveries/dyadic_triangular_hilbert/)  | [10.5281/zenodo.23232389](https://doi.org/10.5281/zenodo.23232389) | paper | positive (lower bound) | no ledger | - | independent pre-publication review (run notes); no AUDIT.md file | exact |
| ED-02 | 2026-10-08 | [A null result for the matrix-valued sharp one-dimensional Lieb-Thirring inequality, and a ...](discoveries/lt_matrix_audit/)  | [10.5281/zenodo.23245266](https://doi.org/10.5281/zenodo.23245266) | paper | negative (null result) + audit | no ledger | - | independent pre-publication review (run notes); no AUDIT.md file | exact |
| ED-03 | 2026-10-08 | [Kernel-checked enclosures of DESI DR2 BAO distances in Lean 4: certifying solver output wi...](discoveries/certified_bao/)  | [10.5281/zenodo.23247730](https://doi.org/10.5281/zenodo.23247730) | paper | positive | no ledger | - | CONFIRMED_WITH_CORRECTIONS | exact |
| ED-04 | 2026-10-10 | [Kernel-checked constraints from DESI DR2 BAO in Lean 4: certified exclusions of Omega_m ba...](discoveries/certified_desi_h0/)  | [10.5281/zenodo.23284020](https://doi.org/10.5281/zenodo.23284020) | paper | partial (P2) + positive (P3) | no ledger | - | CONFIRMED_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS | exact |
| ED-05 | 2026-10-10 | [Riesz-energy, finiteness and every-density corollaries of the openai/math planar universal...](discoveries/triangular_riesz/)  | [10.5281/zenodo.23285631](https://doi.org/10.5281/zenodo.23285631) | paper | positive (corollaries) | no ledger | - | CONFIRMED_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS | exact |
| ED-06 | 2026-10-11 | [Planar universal optimality, tiered: kernel-checked consequences, a non-uniqueness theorem...](discoveries/universal_optimality_tiered/)  | [10.5281/zenodo.23293112](https://doi.org/10.5281/zenodo.23293112) | paper | positive (Tier A) + partial numerics | A 6 / L 7 / C 3 / X 6 | 1 (0/6) | ACCEPT_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS | exact |
| ED-07 | 2026-10-11 | [Planar universal optimality, tiered: kernel-checked consequences, a non-uniqueness theorem...](discoveries/universal_optimality_tiered/) v2 | [10.5281/zenodo.23293429](https://doi.org/10.5281/zenodo.23293429) | paper | positive (Tier A) + partial numerics | A 6 / L 7 / C 3 / X 6 | 1 (0/6) | ACCEPT_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS | exact |
| ED-08 | 2026-10-11 | [The Triangular Lattice and Universal Optimality: human proofs, Lean 4 verification, numeri...](discoveries/textbook_universal_optimality/)  | [10.5281/zenodo.23295142](https://doi.org/10.5281/zenodo.23295142) | textbook | exposition | no ledger | - | ACCEPT_WITH_CORRECTIONS | exact |
| ED-09 | 2026-10-25 | [The bilayer dipolar-exciton interaction is completely monotone in r^2: kernel-checked tria...](discoveries/ar_dipolar_exciton/)  | [10.5281/zenodo.23646103](https://doi.org/10.5281/zenodo.23646103) | paper | positive | A 14 / L 4 / C 7 / X 8 | 1 (0/14) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-10 | 2026-10-25 | [The triangular lattice minimises the planar Yukawa energy at every density and for every f...](discoveries/ar_yukawa_crystal/)  | [10.5281/zenodo.23646105](https://doi.org/10.5281/zenodo.23646105) | paper | positive + erratum fix | A 11 / L 5 / C 3 / X 6 | 1 (0/11) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-11 | 2026-10-25 | [The Rytova-Keldysh interaction is a positive Gaussian mixture: kernel-checked admissibilit...](discoveries/ar_keldysh_tmd/)  | [10.5281/zenodo.23646107](https://doi.org/10.5281/zenodo.23646107) | paper | positive | A 9 / L 5 / C 6 / X 10 | 1 (0/9) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-12 | 2026-10-25 | [A cutoff-independent enstrophy bound for the sigma = 3 dispersive dyadic shell model: kern...](discoveries/ar_sigma3_enstrophy/)  | [10.5281/zenodo.23646111](https://doi.org/10.5281/zenodo.23646111) | paper | positive | A 7 / L 2 / C 4 / X 5 | 1 (0/7) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-13 | 2026-10-25 | [The Bogoliubov structure factor under the dual-scale envelope sqrt(k/2k_s): kernel-checked...](discoveries/ar_bogoliubov_sk/)  | [10.5281/zenodo.23646117](https://doi.org/10.5281/zenodo.23646117) | paper | positive (shape) + one-sided test | A 8 / L 4 / C 4 / X 8 | 1 (0/8) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-14 | 2026-10-26 | [The Sandier-Serfaty triangular-lattice conjecture: an independent reproduction of a claime...](discoveries/prog_sandier_serfaty_audit/)  | [10.5281/zenodo.23653827](https://doi.org/10.5281/zenodo.23653827) | paper | audit / reproduction | A 7 / L 5 / C 5 / X 8 | 1 (0/7) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-15 | 2026-10-26 | [Does the triangular lattice minimise the harmonic zero-point energy? A numerical counterex...](discoveries/prog_zero_point_optimality/)  | [10.5281/zenodo.23653833](https://doi.org/10.5281/zenodo.23653833) | paper | negative (QU-1 refuted numerically) | A 8 / L 3 / C 13 / X 13 | 1 (0/8) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-16 | 2026-10-26 | [Completely monotone and Bernstein functions in Lean 4: a kernel-checked library with a gen...](discoveries/prog_cm_bernstein_library/)  | [10.5281/zenodo.23653842](https://doi.org/10.5281/zenodo.23653842) | paper | positive (library) | A 20 / L 5 / C 6 / X 4 | 1 (0/20) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-17 | 2026-10-26 | [The Feynman-Bijl single-mode bound in Lean, and a diffraction test of the Bogoliubov envel...](discoveries/prog_superfluid_structure_factor/)  | [10.5281/zenodo.23653846](https://doi.org/10.5281/zenodo.23653846) | paper | positive (Lean) + negative (envelope refuted) | A 11 / L 5 / C 7 / X 8 | 1 (0/11) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-18 | 2026-10-26 | [Fixation probabilities as absorption limits of matrix powers, kernel-checked: neutral Wrig...](discoveries/prog_population_genetics_fixation/)  | [10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850) | paper | positive | A 14 / L 5 / C 8 / X 9 | 1 (0/14) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-19 | 2026-10-26 | [Can the planar Sandier-Serfaty proof architecture reach three-dimensional bcc jellium? A f...](discoveries/p2_3d_feasibility/)  | [10.5281/zenodo.23655002](https://doi.org/10.5281/zenodo.23655002) | paper | negative | A 0 / L 4 / C 18 / X 8 | 0 (0/0) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-20 | 2026-10-26 | [The triangular lattice is not a local minimum of the harmonic zero-point energy for exp(-p...](discoveries/p2_certified_zero_point/)  | [10.5281/zenodo.23655392](https://doi.org/10.5281/zenodo.23655392) | paper | positive (certified counterexample) | A 8 / L 0 / C 13 / X 2 | 1 (0/8) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-21 | 2026-10-26 | [The harmonic triangular-to-oblique instability of the quantum Gaussian-core crystal: first...](discoveries/p2_quantum_transition/)  | [10.5281/zenodo.23655625](https://doi.org/10.5281/zenodo.23655625) | paper | negative (within SCHA) | A 0 / L 0 / C 26 / X 13 | 0 (0/0) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-22 | 2026-10-26 | [Toward a machine-checked proof of the claimed Sandier-Serfaty certificate: 4 of 12 stages ...](discoveries/p2_sandier_serfaty_lean/)  | [10.5281/zenodo.23656804](https://doi.org/10.5281/zenodo.23656804) | paper | partial (4/12 stages) | A 16 / L 1 / C 8 / X 10 | 1 (0/16) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-23 | 2026-10-26 | [The isothermal theorem of evolutionary graph theory for birth-death updating, kernel-check...](discoveries/p3_isothermal_theorem/)  | [10.5281/zenodo.23660071](https://doi.org/10.5281/zenodo.23660071) | paper | positive (+ preregistration error caught) | A 11 / L 4 / C 9 / X 2 | 1 (0/11) | ACCEPT_WITH_CORRECTIONS | exact |
| ED-24 | 2026-10-26 | [An independent rebuild, kernel replay and statement audit of the openai/NavierStokesAndEul...](discoveries/p2_navier_stokes_audit/) v1.1 | [10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381) | paper | audit | A 4 / L 4 / C 8 / X 10 | 1 (0/4) | ACCEPT_WITH_CORRECTIONS | exact |

## Code, Lean and caveats

### ED-01 — dyadic_triangular_hilbert v1

- **Title:** The sharp constant of the absolute dyadic triangular Hilbert sum is at least 3
- **DOI:** 10.5281/zenodo.23232389 (https://zenodo.org/records/23232389); concept DOI 10.5281/zenodo.23232388
- **Domain:** harmonic analysis; **result:** positive (lower bound)
- **Lean files:** 0 copied, 0 upstream listed ([LEAN.md](discoveries/dyadic_triangular_hilbert/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** - (independent pre-publication review (run notes); no AUDIT.md file); human audit: none
- **Caveat:** C* >= 3 holds for the ABSOLUTE dyadic sum only; nothing transfers to upstream's signed form; nothing in it is machine-checked.

### ED-02 — lt_matrix_audit v1

- **Title:** A null result for the matrix-valued sharp one-dimensional Lieb-Thirring inequality, and a Comparator check of the scalar Lean formalisation
- **DOI:** 10.5281/zenodo.23245266 (https://zenodo.org/records/23245266); concept DOI 10.5281/zenodo.23245265
- **Domain:** mathematical physics (Lieb-Thirring); **result:** negative (null result) + audit
- **Lean files:** 0 copied, 0 upstream listed ([LEAN.md](discoveries/lt_matrix_audit/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** - (independent pre-publication review (run notes); no AUDIT.md file); human audit: none
- **Caveat:** No violation found at ~1e-6 instrument resolution: a null result, not a proof; fidelity of the scalar Lean statement to the conjecture is not audited.

### ED-03 — certified_bao v1

- **Title:** Kernel-checked enclosures of DESI DR2 BAO distances in Lean 4: certifying solver output with integer certificates
- **DOI:** 10.5281/zenodo.23247730 (https://zenodo.org/records/23247730); concept DOI 10.5281/zenodo.23247729
- **Domain:** cosmology (certified numerics); **result:** positive
- **Lean files:** 6 copied, 0 upstream listed ([LEAN.md](discoveries/certified_bao/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** CONFIRMED_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Kernel-checked enclosures of integrals at one parameter point (Om = 0.29743, the rusty-SUNDIALS fit, not DESI's value); not a new measurement.

### ED-04 — certified_desi_h0 v1

- **Title:** Kernel-checked constraints from DESI DR2 BAO in Lean 4: certified exclusions of Omega_m bands and of H0 >= 73 km/s/Mpc with a BBN prior
- **DOI:** 10.5281/zenodo.23284020 (https://zenodo.org/records/23284020); concept DOI 10.5281/zenodo.23284019
- **Domain:** cosmology (certified numerics); **result:** partial (P2) + positive (P3)
- **Lean files:** 206 copied, 0 upstream listed ([LEAN.md](discoveries/certified_desi_h0/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** CONFIRMED_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Certified version of a known tension (radiation off, Aubourg fitting formula, Gaussian likelihoods); preregistered slab layout H8 failed and was amended.

### ED-05 — triangular_riesz v1

- **Title:** Riesz-energy, finiteness and every-density corollaries of the openai/math planar universal-optimality theorem, kernel-checked in Lean 4
- **DOI:** 10.5281/zenodo.23285631 (https://zenodo.org/records/23285631); concept DOI 10.5281/zenodo.23285630
- **Domain:** discrete geometry / energy minimisation; **result:** positive (corollaries)
- **Lean files:** 4 copied, 0 upstream listed ([LEAN.md](discoveries/triangular_riesz/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** CONFIRMED_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Conditional on upstream openai/math universal_energy_minimum (AI-generated, Comparator-accepted, statement not human-audited); informative only for Riesz s > 2.

### ED-06 — universal_optimality_tiered v1

- **Title:** Planar universal optimality, tiered: kernel-checked consequences, a non-uniqueness theorem, and a CVODE N-body consistency check for the Yukawa interaction
- **DOI:** 10.5281/zenodo.23293112 (https://zenodo.org/records/23293112); concept DOI 10.5281/zenodo.23293111
- **Domain:** discrete geometry + N-body numerics; **result:** positive (Tier A) + partial numerics
- **Lean files:** 5 copied, 3 upstream listed ([LEAN.md](discoveries/universal_optimality_tiered/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/72 (open, empty diff: its content reached main via #73, merged); https://github.com/xaviercallens/SocrateAI-Scientific-MechanicaFluidorum/pull/1 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS (separate instance of the same AI model (named in the audit file)); human audit: none
- **Caveat:** v1. Shifted-force truncation at r_c = 8 shifts energies by more than the tri/square gap (erratum; exact-potential fix in ED-09); annealing fails at kappa = 1; 6 Tier A rows unaudited by a human; published by owner decision with gate exit 1.

### ED-07 — universal_optimality_tiered v2

- **Title:** Planar universal optimality, tiered: kernel-checked consequences, a non-uniqueness theorem, and a CVODE N-body consistency check for the Yukawa interaction
- **DOI:** 10.5281/zenodo.23293429 (https://zenodo.org/records/23293429); concept DOI 10.5281/zenodo.23293111
- **Domain:** discrete geometry + N-body numerics; **result:** positive (Tier A) + partial numerics
- **Lean files:** 5 copied, 3 upstream listed ([LEAN.md](discoveries/universal_optimality_tiered/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/72 (open, empty diff: its content reached main via #73, merged); https://github.com/xaviercallens/SocrateAI-Scientific-MechanicaFluidorum/pull/1 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS / CONFIRMED_WITH_CORRECTIONS (separate instance of the same AI model (named in the audit file)); human audit: none
- **Caveat:** v2 of ED-06 (figures, jellium controls, lab protocols). Same truncation erratum (owed; fixed by ED-09). The local PDF is the current build, which may differ from the v2 upload.

### ED-08 — textbook_universal_optimality v1

- **Title:** The Triangular Lattice and Universal Optimality: human proofs, Lean 4 verification, numerical validation in Python and Rust, and physics from fluids to plasmas (a textbook for students)
- **DOI:** 10.5281/zenodo.23295142 (https://zenodo.org/records/23295142); concept DOI 10.5281/zenodo.23295141
- **Domain:** discrete geometry / physics (teaching); **result:** exposition
- **Lean files:** 7 copied, 0 upstream listed ([LEAN.md](discoveries/textbook_universal_optimality/LEAN.md))
- **Code:** rusty-SUNDIALS b7e4380 (jellium worktree)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Five chapters written by independent agents from one fact sheet; whole-book AI audit only; inherits the ED-06/07 truncation erratum; no ledger of its own.

### ED-09 — ar_dipolar_exciton v1

- **Title:** The bilayer dipolar-exciton interaction is completely monotone in r^2: kernel-checked triangular-lattice corollaries at every density and an exact-Ewald CVODE consistency study
- **DOI:** 10.5281/zenodo.23646103 (https://zenodo.org/records/23646103); concept DOI 10.5281/zenodo.23646102
- **Domain:** condensed matter (excitons); **result:** positive
- **Lean files:** 7 copied, 2 upstream listed ([LEAN.md](discoveries/ar_dipolar_exciton/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/74 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Corollaries conditional on upstream universal_energy_minimum; CVODE numerics are Tier X.

### ED-10 — ar_yukawa_crystal v1

- **Title:** The triangular lattice minimises the planar Yukawa energy at every density and for every finite mixture of screening lengths: kernel-checked corollaries of planar universal optimality, a human proof, and an exact-potential CVODE consistency study
- **DOI:** 10.5281/zenodo.23646105 (https://zenodo.org/records/23646105); concept DOI 10.5281/zenodo.23646104
- **Domain:** plasma / colloids (Yukawa); **result:** positive + erratum fix
- **Lean files:** 5 copied, 3 upstream listed ([LEAN.md](discoveries/ar_yukawa_crystal/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/75 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Exact (untruncated) potential fixes the shifted-force erratum of ED-06/07; corollaries conditional on upstream.

### ED-11 — ar_keldysh_tmd v1

- **Title:** The Rytova-Keldysh interaction is a positive Gaussian mixture: kernel-checked admissibility for planar universal optimality and Keldysh-jellium Madelung energies of TMD Wigner lattices
- **DOI:** 10.5281/zenodo.23646107 (https://zenodo.org/records/23646107); concept DOI 10.5281/zenodo.23646106
- **Domain:** 2D materials (TMD); **result:** positive
- **Lean files:** 3 copied, 2 upstream listed ([LEAN.md](discoveries/ar_keldysh_tmd/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/76 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** The Struve-form identification is Tier C (human argument, not machine-checked); finiteness of the regularised energy not proved; producer and verifier not separated at paper stage.

### ED-12 — ar_sigma3_enstrophy v1

- **Title:** A cutoff-independent enstrophy bound for the sigma = 3 dispersive dyadic shell model: kernel-checked conservation of the second invariant along solutions, CVODE controls, and an illustration on The Well data
- **DOI:** 10.5281/zenodo.23646111 (https://zenodo.org/records/23646111); concept DOI 10.5281/zenodo.23646110
- **Domain:** turbulence (shell models); **result:** positive
- **Lean files:** 6 copied, 0 upstream listed ([LEAN.md](discoveries/ar_sigma3_enstrophy/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/77 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Specialisation of an existing owner lemma (dispersive_norm_le); The Well data used as illustration only.

### ED-13 — ar_bogoliubov_sk v1

- **Title:** The Bogoliubov structure factor under the dual-scale envelope sqrt(k/2k_s): kernel-checked shape theorems, a one-sided diffraction test, and a Gross-Pitaevskii linear-response check in rusty-SUNDIALS
- **DOI:** 10.5281/zenodo.23646117 (https://zenodo.org/records/23646117); concept DOI 10.5281/zenodo.23646116
- **Domain:** superfluids (Bogoliubov); **result:** positive (shape) + one-sided test
- **Lean files:** 3 copied, 0 upstream listed ([LEAN.md](discoveries/ar_bogoliubov_sk/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/78 (merged); https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster/releases/tag/v3.49.0
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** No HuggingFace S(k) dataset exists (the paper says so); the diffraction test is one-sided.

### ED-14 — prog_sandier_serfaty_audit v1

- **Title:** The Sandier-Serfaty triangular-lattice conjecture: an independent reproduction of a claimed finite certificate, an adversarial audit of the claimed reduction, and a Lean statement (no proof of the conjecture is claimed)
- **DOI:** 10.5281/zenodo.23653827 (https://zenodo.org/records/23653827); concept DOI 10.5281/zenodo.23653826
- **Domain:** mathematical physics (Coulomb gases); **result:** audit / reproduction
- **Lean files:** 2 copied, 0 upstream listed ([LEAN.md](discoveries/prog_sandier_serfaty_audit/LEAN.md))
- **Code:** [private LeanFlow repository] (open): commits 542cea97 (generator), 2c168be2 (sentinel + #exit refusal), 84e0c289 (docs)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** No proof of the conjecture is claimed; the Lean file states the conjecture (not proved); the reduction is Tier C.

### ED-15 — prog_zero_point_optimality v1

- **Title:** Does the triangular lattice minimise the harmonic zero-point energy? A numerical counterexample for completely monotone potentials, with kernel-checked curvature identities
- **DOI:** 10.5281/zenodo.23653833 (https://zenodo.org/records/23653833); concept DOI 10.5281/zenodo.23653832
- **Domain:** lattice dynamics (zero-point energy); **result:** negative (QU-1 refuted numerically)
- **Lean files:** 2 copied, 0 upstream listed ([LEAN.md](discoveries/prog_zero_point_optimality/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/79 (open)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** The refutation is a floating-point result (Tier X), reproduced by an independent spectral implementation to 1e-14; certified in part by ED-20.

### ED-16 — prog_cm_bernstein_library v1

- **Title:** Completely monotone and Bernstein functions in Lean 4: a kernel-checked library with a general subordination theorem, applied to planar universal optimality
- **DOI:** 10.5281/zenodo.23653842 (https://zenodo.org/records/23653842); concept DOI 10.5281/zenodo.23653840
- **Domain:** analysis (completely monotone functions); **result:** positive (library)
- **Lean files:** 11 copied, 3 upstream listed ([LEAN.md](discoveries/prog_cm_bernstein_library/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent, Claude Opus-family (named in the audit file)); human audit: none
- **Caveat:** Mathlib PR not opened (needs owner OK and Mathlib AI-policy review).

### ED-17 — prog_superfluid_structure_factor v1

- **Title:** The Feynman-Bijl single-mode bound in Lean, and a diffraction test of the Bogoliubov envelope on published structure factors of superfluid 4He and trapped Bose gases
- **DOI:** 10.5281/zenodo.23653846 (https://zenodo.org/records/23653846); concept DOI 10.5281/zenodo.23653845
- **Domain:** superfluids (helium-4); **result:** positive (Lean) + negative (envelope refuted)
- **Lean files:** 4 copied, 0 upstream listed ([LEAN.md](discoveries/prog_superfluid_structure_factor/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** He-4 data from a published table (Tier L); BEC data figure-read (Tier X).

### ED-18 — prog_population_genetics_fixation v1

- **Title:** Fixation probabilities as absorption limits of matrix powers, kernel-checked: neutral Wright-Fisher, the Moran model with selection, the Price equation, and a fail-closed CVODE certificate
- **DOI:** 10.5281/zenodo.23653850 (https://zenodo.org/records/23653850); concept DOI 10.5281/zenodo.23653849
- **Domain:** population genetics; **result:** positive
- **Lean files:** 15 copied, 0 upstream listed ([LEAN.md](discoveries/prog_population_genetics_fixation/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/80 (open); https://github.com/xaviercallens/SocrateAI-Scientific-Genetic/pull/1 (open); https://github.com/xaviercallens/SocrateAI-Scientific-Genetic/pull/2 (open)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent, Claude Opus-family (named in the audit file)); human audit: none
- **Caveat:** Textbook results, newly kernel-checked; Genetic PRs overlap and are unmerged.

### ED-19 — p2_3d_feasibility v1

- **Title:** Can the planar Sandier-Serfaty proof architecture reach three-dimensional bcc jellium? A feasibility study with a negative outcome
- **DOI:** 10.5281/zenodo.23655002 (https://zenodo.org/records/23655002); concept DOI 10.5281/zenodo.23655001
- **Domain:** mathematical physics (3D jellium); **result:** negative
- **Lean files:** 0 copied, 0 upstream listed ([LEAN.md](discoveries/p2_3d_feasibility/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Negative feasibility result scoped by rotation invariance; floating-point numerics only.

### ED-20 — p2_certified_zero_point v1

- **Title:** The triangular lattice is not a local minimum of the harmonic zero-point energy for exp(-pi r^2): a certified linear-response majorant along a symmetric shear
- **DOI:** 10.5281/zenodo.23655392 (https://zenodo.org/records/23655392); concept DOI 10.5281/zenodo.23655391
- **Domain:** lattice dynamics (certified); **result:** positive (certified counterexample)
- **Lean files:** 9 copied, 0 upstream listed ([LEAN.md](discoveries/p2_certified_zero_point/LEAN.md))
- **Code:** LeanFlow lean.certify (unmodified)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent, Claude Opus-family (named in the audit file)); human audit: none
- **Caveat:** Lean holds the logic and rationals; the integrals are ball arithmetic (python-flint), outside the kernel.

### ED-21 — p2_quantum_transition v1

- **Title:** The harmonic triangular-to-oblique instability of the quantum Gaussian-core crystal: first order, near the Lindemann melting estimate, and absent in the self-consistent harmonic approximation (a preregistered negative result)
- **DOI:** 10.5281/zenodo.23655625 (https://zenodo.org/records/23655625); concept DOI 10.5281/zenodo.23655624
- **Domain:** quantum crystals; **result:** negative (within SCHA)
- **Lean files:** 0 copied, 0 upstream listed ([LEAN.md](discoveries/p2_quantum_transition/LEAN.md))
- **Code:** https://github.com/xaviercallens/rusty-SUNDIALS/pull/79 (open; SCHA module on the same branch)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Negative within the self-consistent harmonic approximation; Rydberg dressing is a soft shoulder, not a Gaussian.

### ED-22 — p2_sandier_serfaty_lean v1

- **Title:** Toward a machine-checked proof of the claimed Sandier-Serfaty certificate: 4 of 12 stages re-executed in the Lean kernel, one reduction lemma proved, and the measured cost of the rest (a partial formalization; the conjecture is not formally proved)
- **DOI:** 10.5281/zenodo.23656804 (https://zenodo.org/records/23656804); concept DOI 10.5281/zenodo.23656803
- **Domain:** mathematical physics (Coulomb gases); **result:** partial (4/12 stages)
- **Lean files:** 53 copied, 0 upstream listed ([LEAN.md](discoveries/p2_sandier_serfaty_lean/LEAN.md))
- **Code:** LeanFlow commit 06084ef5c40057c66c476feba18ea3da8fb150ba (decide_kernel tactic; local, in no remote branch at the time of writing; not part of PR #1)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Partial formalisation: 4 of 12 stages; the conjecture is not formally proved; 16 Tier A rows unaudited by a human.

### ED-23 — p3_isothermal_theorem v1

- **Title:** The isothermal theorem of evolutionary graph theory for birth-death updating, kernel-checked in Lean 4: Moran fixation on strongly connected isothermal graphs and its stationary-selection generalization
- **DOI:** 10.5281/zenodo.23660071 (https://zenodo.org/records/23660071); concept DOI 10.5281/zenodo.23660070
- **Domain:** evolutionary graph theory; **result:** positive (+ preregistration error caught)
- **Lean files:** 7 copied, 0 upstream listed ([LEAN.md](discoveries/p3_isothermal_theorem/LEAN.md))
- **Code:** https://github.com/xaviercallens/SocrateAI-Scientific-Genetic/pull/3 (open)
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Known theorem, newly kernel-checked; the preregistered 'count is a birth-death chain' clause was false (not strongly lumpable) and is reported.

### ED-24 — p2_navier_stokes_audit v1.1

- **Title:** An independent rebuild, kernel replay and statement audit of the openai/NavierStokesAndEuler breakdown theorems (independently rebuilt and audited; not a claim that a Clay problem is solved)
- **DOI:** 10.5281/zenodo.23661381 (https://zenodo.org/records/23661381); concept DOI 10.5281/zenodo.23661380
- **Domain:** fluid PDE (audit of openai/NavierStokesAndEuler); **result:** audit
- **Lean files:** 7 copied, 2 upstream listed ([LEAN.md](discoveries/p2_navier_stokes_audit/LEAN.md))
- **Code:** no code PR for this item
- **Audit:** ACCEPT_WITH_CORRECTIONS (AI agent instance (model not named in the audit file)); human audit: none
- **Caveat:** Independently rebuilt and audited; NOT a claim that a Clay problem is solved; credit for the corpus belongs to its authors (OpenAI).

## Excluded

- 10.5281/zenodo.23003926 (BAO cosmology reproductions, September 2026): a different run and worktree, before this programme.
- 10.5281/zenodo.23293111: the concept DOI of ED-06/ED-07, not a separate publication.
- `textbook_formalisation_2026` (French CPGE textbook draft): no DOI, unaudited draft.
