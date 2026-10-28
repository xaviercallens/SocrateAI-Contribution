# SocrateAI-Contribution

*Two years of learning to work with AI on science, and to check what it says.*

[Version française](README.fr.md)

## What this is

- My name is Xavier Callens (SocrateAI Lab). For two years I have worked with AI agents: programs that can be handed a whole task, such as searching, calculating, writing or checking, and that carry it out step by step.
- The agents write fast and they write well. They also write false things, just as confidently. In my first months I believed them too easily, and I had to withdraw claims in public.
- What came out of that is a habit borrowed from Socrates: question every claim before believing it. I call it **Elenchus**, after the Greek word for his kind of questioning.
- This repository is a showcase of what that habit produced. It holds two books, written for readers who are not scientists, twenty contributions checked as carefully as I could manage, the claims I got wrong, and everything you need to check the work yourself.
- Most of the results are modest. The method, and the honest record of the mistakes, may be the most useful part.
- **No human mathematician or scientist has reviewed any of this work.** It was produced by AI agents under my direction and checked by other AI agents. I say this at the top because it is the most important limit of everything below.

## The habit: question first, believe later

Socrates did not try to prove that he was right. He asked questions until he found where a claim contradicted itself. A claim that survived the questioning deserved to be believed, at least for a while.

Here the questions are asked by rules and by programs. Every result goes round the same loop:

![The Elenchus loop: AI proposes, calculation explores, Lean judges, humans decide what it means](figures/elenchus-loop-en.png)

1. **AI proposes.** An agent suggests an idea, a proof or a program.
2. **Calculation explores.** Before anyone tries to prove the idea, computer calculations test it. Many ideas fail here, and the failures are published.
3. **The proof checker judges.** A small, strict program called the Lean kernel checks every step of a proof. It cannot be flattered and it does not care who wrote the proof.
4. **Humans decide what it means**, and whether it is worth publishing.

Every claim also carries a label that says who checked it:

| Level | In everyday words | What it means |
|---|---|---|
| **A** | "the judge looked" | The Lean proof checker checked every step. The proof uses only the three standard basic rules, a second program read the whole proof again (the "replay"), and a search found no trick for getting around the checker. When the replay is missing, the books write "As". |
| **L** | "it is in a serious book" | The result is published in the scientific literature, and we cite it precisely. |
| **C** | "someone reasoned, nobody machine-checked" | A written argument. Here it was almost always written by one AI agent and read by another. |
| **X** | "a pencil sketch" | A calculation with rounded decimal numbers, such as a simulation. It can point the way, or show that an idea is wrong. It never proves anything. |

A claim is only as strong as its weakest link. A few more rules complete the habit:
- the claim is written down before the test;
- every test has one case that must pass and one that must fail, to show that the test can say no;
- the agent that makes a result is not the agent that checks it;
- negative results are published like the others.

The method explained without jargon: [docs/elenchus-in-10-minutes.md](docs/elenchus-in-10-minutes.md).

**What's new (28 October 2026):** a census, a correction of our own earlier statement, a replication, two models and a note, all small, all AI-checked and not human-checked. Plain-language page: [docs/whats-new-2026-10-28.md](docs/whats-new-2026-10-28.md).

## Start here

- **If you are curious and not a scientist:** read the *Discovery Journal* ([English PDF](books/discovery-journal-2026-en.pdf), [French PDF](books/discovery-journal-2026-fr.pdf)). It starts with the method, explained with a trial, a smoke detector and a recipe tasted by someone else. Then read [the two-year story](docs/two-years.md) and [what we got wrong](docs/what-we-got-wrong.md).
- **If you saw a headline about an AI "proof":** read [how to read an AI-generated proof: five questions](docs/how-to-read-an-ai-generated-proof.md).
- **If you are a student:** read the textbook *From Conjecture to the Lean Kernel* ([doi:10.5281/zenodo.23665873](https://doi.org/10.5281/zenodo.23665873); French edition [doi:10.5281/zenodo.23665820](https://doi.org/10.5281/zenodo.23665820)). It gives each result three ways: as a human proof, as a Lean statement and as computer tests. Then try [check it yourself](docs/check-it-yourself.md).
- **If you are a specialist and want to check:** start with [`elenchus/README.md`](elenchus/README.md), [`elenchus/REGISTRY.md`](elenchus/REGISTRY.md) (24 Zenodo publications with their claim ledgers) and [`elenchus/CONSISTENCY_REPORT.md`](elenchus/CONSISTENCY_REPORT.md) and the ledger checker in [`elenchus/tool/`](elenchus/tool/). Then please try to break something: [CONTRIBUTING.md](CONTRIBUTING.md).

## The twenty contributions, in plain words

The *Discovery Journal* tells twenty contributions. They were chosen from about 112 published works and 57 science-related code projects with a scoring grid that was written down and frozen before anything was scored. The grid had to include at least three lessons (failures or self-corrections). The list below follows the book's ranking.

Several results build on proofs that an AI from OpenAI published in 2026 and that a computer checked. Those proofs are AI-generated and have not been peer reviewed. Rows marked **(conditional)** are only as sound as that upstream work.

| # | Contribution | In one plain line | Level | Record | Caveat |
|---|---|---|---|---|---|
| 1 | Cosmic distances with a machine-checked error margin | The distances to far galaxies measured by the DESI survey, computed together with a margin of error that the proof checker confirmed | As | [10.5281/zenodo.23247730](https://doi.org/10.5281/zenodo.23247730) | It checks a calculation, not a new measurement, and was done for one value of the matter density (the project's own fit, not DESI's). |
| 2 | A famous tension in cosmology, as a checked inequality | Inside the standard model of the universe and its stated simplifications, an expansion rate of 73 or more fits the DESI data and early-universe chemistry far worse than the best fit | As | [10.5281/zenodo.23284020](https://doi.org/10.5281/zenodo.23284020) | It certifies a tension already known from ordinary statistics. One planned way of slicing the calculation failed, was replaced, and the paper says so. |
| 3 | The triangle, the cheapest arrangement: consequences and a simulation | Consequences of the theorem that triangles are the lowest-energy way to arrange repelling points, checked by machine, plus a simulation | A (simulation X) | [10.5281/zenodo.23293429](https://doi.org/10.5281/zenodo.23293429) | **(conditional)**. The simulation cut the force off too early, an error repaired in row 4. |
| 4 | Screened repulsion joins the theorem, and an error is repaired | Charged dust and colloids repel with a "screened" force; the checker confirms that this force is covered by the triangle theorem | A | [10.5281/zenodo.23646105](https://doi.org/10.5281/zenodo.23646105) | **(conditional)**. It also fixes the earlier simulation error. |
| 5 | Redoing someone else's calculation, without declaring it right | OpenAI's large computer certificate for a famous conjecture (Sandier–Serfaty) was re-run and audited | X and C (Lean statement A) | [10.5281/zenodo.23653827](https://doi.org/10.5281/zenodo.23653827) | **The conjecture is not proved, verified or refuted here.** It was reproduced and audited, which is different. |
| 6 | A ruler proved straight shows our own sketch was wrong | A classic bound for superfluid helium checked by machine; real neutron data then refute a formula this project had proposed | A (data L) | [10.5281/zenodo.23653846](https://doi.org/10.5281/zenodo.23653846) | One positive formal result and one negative result about our own idea. |
| 7 | What chance does a mutation have of taking over? | Classic textbook answers from population genetics, checked step by step by the proof checker | A | [10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850) | Known results. What is new is the machine check. |
| 8 | When the seating plan changes nothing about selection | A classic theorem of evolution on networks, checked by machine | A | [10.5281/zenodo.23660071](https://doi.org/10.5281/zenodo.23660071) | One of our own pre-registered sub-claims was false, and the paper reports it. The converse is not proved. |
| 9 | A textbook that follows a theorem to the laboratory | A 105-page student textbook: each result as a human proof, a Lean statement and computer tests | A (new Lean parts) | [10.5281/zenodo.23295142](https://doi.org/10.5281/zenodo.23295142) | **(conditional)**. It inherits the simulation error of row 3. |
| 10 | Electron–hole pairs that line up in triangles, on paper | A force inside stacked thin materials is shown to be covered by the triangle theorem | A (simulation X) | [10.5281/zenodo.23646103](https://doi.org/10.5281/zenodo.23646103) | **(conditional)**. The simulation is a consistency check, not a proof. |
| 11 | The force in an ultra-thin semiconductor, as a pile of sand | The force between charges in atom-thin layers is a sum of bell-shaped pieces, so the triangle theorem covers it | A (one step C) | [10.5281/zenodo.23646107](https://doi.org/10.5281/zenodo.23646107) | **(conditional)**. One link is a human-style argument only. The producer and the checker were not fully separated at the paper stage. |
| 12 | Testing before proving: a natural idea that fails | The guess that triangles also minimise the quantum "trembling" energy fails in calculations for 8 of 12 forces | X (some lemmas A) | [10.5281/zenodo.23653833](https://doi.org/10.5281/zenodo.23653833) | A lesson. These are decimal calculations, not a proof that the guess is false. |
| 13 | Perfect at rest, not when it trembles | For one force, a certificate shows that a tiny shear of the triangle lattice lowers the trembling energy | C as a whole (logic and arithmetic A) | [10.5281/zenodo.23655392](https://doi.org/10.5281/zenodo.23655392) | A lesson. The integrals were enclosed by a program outside the proof checker. |
| 14 | Four floors out of twelve, and the price of the rest | Four of the twelve stages of the certificate from row 5 were redone inside the proof checker | A (4 stages) | [10.5281/zenodo.23656804](https://doi.org/10.5281/zenodo.23656804) | **The conjecture is not formally proved**, as the title says. |
| 15 | Rebuilding someone else's machine in your own workshop | OpenAI's machine-checked proofs about fluid equations were rebuilt independently, and 88,400 declarations were re-read by the checker | A (replay facts); statement comparison C | [10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381) | **Not a claim that any Clay prize problem is solved.** The credit belongs to the authors of those proofs. |
| 16 | One general guarantee, three precise certificates | Three short consequences of the triangle theorem, named and checked by machine | A | [10.5281/zenodo.23285631](https://doi.org/10.5281/zenodo.23285631) | **(conditional)**. They follow quickly from the theorem; later work built on them. |
| 17 | The calculation engine, and its inspection report | An AI-assisted translation of a standard solver for differential equations, used by many of the papers | X | [code repository](https://github.com/xaviercallens/rusty-SUNDIALS) (no Zenodo record) | Its numbers are never treated as proofs. An audit of its fusion material led to retractions. |
| 18 | A door that stays closed when in doubt | A gate that accepts AI-written code only if real compilers and the proof checker agree | As (one demonstration); rest self-checked | [10.5281/zenodo.23119953](https://doi.org/10.5281/zenodo.23119953) | Earlier performance figures were withdrawn. It still let some wrong code through. |
| 19 | The test bench that inspected itself | The lab bench that runs the agents; its own audit found 14 parts that reported success without doing the work | C (self-audit) | [code repository](https://github.com/xaviercallens/AutoevolveAI) (no Zenodo record) | Self-checked only. |
| 20 | The thermostat was accused of overheating | A claim from our own October batch, that a standard method slowly "heats" particles in a fusion device, tested and found false | X (with controls) | [10.5281/zenodo.23532458](https://doi.org/10.5281/zenodo.23532458) | A lesson: a withdrawal of our own claim. No one but the author has reviewed it. |

More detail on each contribution, in the same plain style, is in the *Discovery Journal*. Technical detail is in [`elenchus/`](elenchus/) and on each Zenodo record.

## What is NOT claimed

> - **No famous conjecture is proved here.** In particular, the Sandier–Serfaty conjecture is not proved: rows 5 and 14 reproduce, audit and partly re-check a certificate published by others.
> - **No Clay prize problem is solved.** Row 15 is an independent rebuild and re-check of proofs written by others, nothing more.
> - **Results that build on the OpenAI theorems are conditional.** Those upstream proofs were generated by AI and accepted by a computer, but they have not been peer reviewed.
> - **Everything here was produced by AI agents under my direction and audited by other AI agents.** An audit by an AI is not peer review. **No human has audited this work**, not even the question of whether each machine-checked statement says what its plain-language description says.
> - A level-A label means the proof checker accepted a proof of the formal statement. It does not mean that the statement captures the real-world question.

## The books

| Book | French | English |
|---|---|---|
| *The Discovery Journal* (153 pages, for everyone) | [PDF](books/discovery-journal-2026-fr.pdf) · [doi:10.5281/zenodo.23669395](https://doi.org/10.5281/zenodo.23669395) | [PDF](books/discovery-journal-2026-en.pdf) · [doi:10.5281/zenodo.23669463](https://doi.org/10.5281/zenodo.23669463) |
| *From Conjecture to the Lean Kernel* (textbook for students) | [doi:10.5281/zenodo.23665820](https://doi.org/10.5281/zenodo.23665820) | [doi:10.5281/zenodo.23665873](https://doi.org/10.5281/zenodo.23665873) |

The textbooks are on Zenodo only. [`books/README.md`](books/README.md) explains why.

## In this repository

- [`docs/`](docs/): [the two-year story](docs/two-years.md), [Elenchus in ten minutes](docs/elenchus-in-10-minutes.md), [what we got wrong](docs/what-we-got-wrong.md), [check it yourself](docs/check-it-yourself.md), [what we want to try next](docs/roadmap.md). Each page also exists in French (`.fr.md`), except the roadmap, which is in English only.
- [`books/`](books/): the two journal PDFs and their LaTeX sources.
- [`elenchus/`](elenchus/): the full record of 24 Zenodo publications, with claim ledgers, audits and Lean files, the Elenchus ledger checker ([`elenchus/tool/`](elenchus/tool/)) and a consistency check you can run.
- [`figures/`](figures/): the loop figure and the script that draws it.

## Questions, corrections, challenges

Please use the issue tracker. Challenges ("red-team" issues) are especially welcome: if you think a claim is wrong, overstated or badly labelled, say so. See [CONTRIBUTING.md](CONTRIBUTING.md). There is no e-mail contact: open an issue.

## Use it, cite it, give back

- **Use it.** You are welcome to read, reuse, adapt and share everything here, including the Elenchus ledger checker in [`elenchus/tool/`](elenchus/tool/).
- **Keep the names.** Any copy or adaptation must keep the author credit, "Xavier Callens (SocrateAI Lab)", the copyright notices and the [`NOTICE`](NOTICE) file.
- **Give back.** The code is under the GNU Affero GPL (version 3 or later). If you share an improved version, or run one for others over a network, you share its source under the same licence. The new texts and figures are under CC BY-SA 4.0, which asks the same of adaptations. The books already published on Zenodo stay under CC BY 4.0.
- **Cite it.** A licence cannot force a citation, so this is a request: if this work helps you, please cite the books. [`CITATION.cff`](CITATION.cff) gives the details.

Which licence covers which file: [`LICENSING.md`](LICENSING.md). These terms were chosen on 27 October 2026 to carry out the author's wish that credit is kept and that improvements stay open source. Legal advice is still recommended before relying on any of them being enforced.
