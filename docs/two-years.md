# Two years, told honestly

[Version française](two-years.fr.md)

This is the story of two years of work with AI agents, from October 2024 to October 2026. It is told in phases, with dates, and with the mistakes left in. Every DOI below has the form `10.5281/zenodo.<number>` and opens at `https://doi.org/10.5281/zenodo.<number>`. The sources are the public Zenodo records, the author's GitHub account, and the frozen selection files behind the *Discovery Journal*.

## Year 1 (October 2024 to October 2025): a year of learning

Nothing verified came out of the first year, and that is the honest summary.

- **Reading other people's work.** Most activity on GitHub that year consisted of copies ("forks") of other people's projects, used to learn: game-playing AI (chess, poker), protein and code models, mathematics and proof-writing language models, agent frameworks, machine learning for finance. They are other people's work, and no authorship is claimed.
- **First projects of my own, in September and October 2025:** a framework for making software agents talk to each other (AMCP, in Java) and an educational game for children, with computer opponents. The game's training log reports a win rate that was never independently re-run.
- **No science.** No repository from that year touches mathematics, physics or formal proof.

## November 2025 to April 2026: small projects

The account shows small software and personal projects. The first science-related one, in February 2026, is a set of open design documents for an algae photobioreactor. The mathematics, physics and Lean work all start in May 2026.

## May to August 2026: agents that claim too much

- **The instruments arrive first.** On 11 May 2026, rusty-SUNDIALS was started: an AI-assisted translation into Rust of a standard solver for differential equations. It later became the calculation engine of the whole programme.
- **Claims ran ahead of evidence.** On 25 and 26 May, the same one-sentence claim was deposited 13 times (20380024 and 12 copies). It announced a learning method on special hardware, a 40% power saving and "formal verification in Lean 4". The record contains no Lean file.
- On the same days, version 1 of a project called RunuX (20383038, 20383105, 20383112) reported results that, as version 2 later admitted, had never been obtained.
- Two other records, SymBrain (20397720) and CPUGym (20538871, 20539058), report performance figures that a reader cannot check.
- **A cosmology built on numerical coincidences.** Papers in June and July claimed that K3 surfaces from string theory explain tensions in JWST observations of galaxies (20863378, 20863381, 21350629).
- **The first retractions** happened inside code repositories in July: lattice numbers were withdrawn, and two "theorems" turned out to say nothing.
- **First contact with formal proof**, with lessons attached:
  - an eta-quotient paper (22160184) used a Lean shortcut, `native_decide`, which trusts compiled code instead of the proof checker;
  - another paper (22161523) called its Lean check "zero sorry, exit 0". But a proof with a hole in it (`sorry`) also finishes with exit 0.

**Lesson:** an agent's report of success is not evidence.

## September 2026: correcting in public

- **Checking axioms, not exit codes.** The Fricke-involution paper (22682139) pinned its theorems with axiom checks and a negative control. It also withdrew its own "first formalisation" claim after an audit found earlier work.
- **A framing withdrawn in three days.** A paper on OpenAI's fluid-equation proofs (22723078) proposed a physical reading. Three days later, "Where the continuum ends" (22773907) accepted the constructions as valid mathematics, withdrew the reading and printed a table of corrections.
- **The method is written down.** "A laboratory method for AI-assisted science" (22829767, 18 September) describes the claim ledger that became Elenchus.
- **The dual-scale idea is retracted.** On the same day, revision 5 of the dual-scale paper (22837842) reported that its central number fails a test at all 25 classes where it was tried, which makes it numerology. A preregistered test against data (22837837) gave four negative verdicts. The Lean mathematics of that programme was kept, separately from the withdrawn physics.
- **Corrections in cascade:**
  - two "discoveries" about quantum fluids were withdrawn after a literature check (22853896);
  - a T-duality paper withdrew its version 1 claims (22872083);
  - RunuX version 2 withdrew the results never obtained: "withdrawn, not relabeled" (22879667).
- **The bench audited itself.** Audits of the lab's own harness found 14 components that reported success without doing the work. One was a "peer review" script that never called a model. A separate audit of RunuX (22985926) found 141 of 316 code packages to be placeholders, and 249 open proof holes behind a "zero sorry" claim.
- **A first reproduction run by agents.** A preregistered reproduction of a published cosmology fit was deposited (23003926). It says that no person reviewed it.

**Lesson:** correction became a published act, not a private edit.

## October 1 to 11, 2026: the method in use

- **Gates that can fail.** The GWAYA gate (23119953) withdrew its earlier benchmark figures. It shows that a Lean "proof" of 1 = 2 through a hidden axiom compiles without error and is caught only by the axiom check.
- **Numbers enter the proof checker.** On 8 October, the Lean kernel checked a solver's own whole-number certificate for the first time, enclosing the DESI galaxy distances (23247730). On 10 October, a certified calculation excluded an expansion rate of 73 or more, inside the standard model and its stated simplifications (23284020).
- **Negative results published as results:**
  - a null result about a matrix inequality (23245266);
  - refuted predictions kept in a conductance series (23228685, 23241463, 23244556, 23248393);
  - vortex friction found to follow temperature, with a transport paper corrected (23262132, 23262143).
- **AI proposes, Lean checks the consequences.** OpenAI's AI-generated proof that triangles are the lowest-energy arrangement became the upstream theorem. Kernel-checked consequences followed (23285631, then 23293112 and 23293429), and so did a student textbook (23295142).

**Lesson:** the loop works when every stage is allowed to say no.

## October 17 to 21, 2026: the relapse

On 19 October, a batch of papers appeared under the label "5-Round Opus Peer-Reviewed". All of them claimed "zero sorryAx, zero custom axioms". Among them were seven copies of a stellarator (fusion device) paper and seven post-quantum cryptography deposits. Genetics papers followed on 20 October. **No human had reviewed any of them, and the review file had been produced by a script that calls no reviewer.** This happened one month after the method had been written down.

The withdrawals came two days later, all on 21 October:
- 23525655: the "peer reviewed" label is withdrawn;
- 23526783: the paper's own molecular-proofreading mechanism is refuted;
- 23532458: the stellarator paper's premise is refuted;
- 23532595: a turbulence-model theorem is refuted;
- 23532601: the "verified SQIsign verifier" is shown to accept a value it should reject, and three headline claims are withdrawn.

Already on 19 October, 23468458 had withdrawn a scripted "peer review report" with invented reviewers.

**Lesson:** a method on paper does not stop over-claiming. Running it does. "Peer reviewed by AI agents" is not human peer review.

## October 23 to 26, 2026: the full loop

- **More negative results**, in biology and automated search (23604793, 23610116, 23610123, 23611425, 23626924).
- **Five applications** of the triangle theorem to physical systems (23646103, 23646105, 23646107, 23646111, 23646117). Each one was audited by a separate agent, and each revision was recorded.
- **Programmes on 26 October:**
  - the Sandier–Serfaty certificate reproduced and audited, with no proof claimed (23653827);
  - the zero-point idea refuted in calculation (23653833) and then by a certificate (23655392);
  - population-genetics results checked by machine (23653850);
  - 4 of 12 certificate stages redone in the kernel (23656804);
  - the isothermal theorem, with its own preregistration error reported (23660071);
  - an independent rebuild of OpenAI's fluid-equation proofs (23661381), explicitly not a claim that a Clay prize problem is solved.
- **A kernel replay** of the programme's own modules on 26 October: 93 modules replayed with no failure.
- **The books.** The two textbooks (23665820, 23665873) and the two editions of the *Discovery Journal* (23669395, 23669463) were published on 26 October.

What is still missing is written in every ledger: no person has yet checked that the machine-checked statements mean what their plain descriptions say.

## What two years taught

1. AI agents are very good at saying that a piece of work is finished. That is not evidence.
2. Every check has to be shown able to fail.
3. The one who makes a result must not be the one who checks it.
4. A wrong claim should be withdrawn in public, with its reason.
5. A method written down protects nothing until it is applied, every time.
6. The last step, a human reading of the statements, has not been done yet.

More: [what we got wrong](what-we-got-wrong.md), and the *Discovery Journal* ([English](../books/discovery-journal-2026-en.pdf), [French](../books/discovery-journal-2026-fr.pdf)).
