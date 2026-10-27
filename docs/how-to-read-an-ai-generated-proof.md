# How to read an AI-generated proof: five questions

[Version française](how-to-read-an-ai-generated-proof.fr.md)

*For curious readers and students. No formulas.*

The news now sometimes says that an AI system "proved" something and that a computer "verified" it. This page offers five questions to ask. They do not tell you whether a claim is true. They tell you what has been checked, by whom, and what is still waiting.

## A true story to keep in mind

In late October 2026, OpenAI announced three results, in mathematics, computer science and physics. Its page *Building scientific understanding with academic communities* describes them: one in harmonic analysis (the mathematics of waves), one about the existence of certain theories of particle physics, and one about a famous conjecture in computer science, the **Exponential Time Hypothesis**, or **ETH**. Press coverage followed on 26 and 27 October (Gizmodo, DEV Community, MLQ.ai); these are secondary sources, which we saw only in summary and do not rely on for any claim here.

**What ETH says, in two sentences.** Imagine a puzzle made of many on/off switches and a list of rules such as "switch 3 on, or switch 7 off, or switch 9 on": is there a setting of the switches that obeys every rule? ETH, a conjecture that has stood for about twenty-five years, says that however clever the method, the time needed to answer this puzzle in the worst case grows exponentially with the number of switches: each extra switch multiplies the work by some fixed amount. (Clever methods do exist and beat trying every setting; ETH says only that none escapes this kind of growth.)

**What OpenAI says.** On its page, OpenAI writes, in the French version that was shared with us:

> « notre système a récemment démontré que l'ETH est fausse, un résultat qui a ensuite été vérifié en Lean »
> ("our system recently proved that ETH is false, a result that was then verified in Lean"; OpenAI, our translation)

and, about what comes next:

> « Ces travaux seront vérifiés et encadrés par un groupe dirigé par Russell Impagliazzo (UC San Diego), Ramamohan Paturi (UC San Diego) et Ryan Williams (MIT) »
> ("This work will be verified and supervised by a group led by Russell Impagliazzo (UC San Diego), Ramamohan Paturi (UC San Diego) and Ryan Williams (MIT)"; OpenAI, our translation)

**What we did and did not do.** We did not read the whole page: only part of its text was available to us. We did not check OpenAI's proof, and we did not run the checking tool on it. **We claim nothing about whether the result is true or false.** We use this case only because it is recent, public and clearly described.

## Question 1: Who checked it, and how?

"Verified in Lean" means something precise. **Lean** is a language in which a mathematical statement and its proof are written out in so much detail that a computer program can check every step. At its centre sits a small program, the *kernel*, whose only job is to accept or reject each step.

*The everyday picture:* a spell-and-grammar checker for logic, very strict and never tired. It reads every line and is not impressed by confident writing.

*Where the picture stops:* a grammar checker does not know what you meant to say. Lean is the same: it checks that the proof proves **the statement that was written down**. It does not understand the idea behind it.

So ask: **who ran the checker, on which files, and where is its answer recorded?**

## Question 2: Is the statement that was checked the same as the claim that was made?

Before a computer can check a proof, someone has to translate the claim from ordinary mathematical language into Lean. That translation is called the *formal statement*.

*The everyday picture:* a court rules on the contract that was signed, not on what the parties meant. If the translation of a contract into another language changed one word, the judge rules on the translated text.

*Where the picture stops:* reading a formal statement often needs an expert in the subject **and** an expert in Lean.

Here are three ways in which a formal statement can quietly differ from the idea it is meant to express. They are general kinds of gap that careful readers look for; we are not saying that any of them occurs in OpenAI's work.

1. **A definition that is secretly weaker, or empty.** If a word used in the theorem is defined so that it means almost nothing (for example, a "measure of size" that turns out to be zero everywhere), the theorem can become true for a trivial reason.
2. **A non-standard model of computation.** A statement about "how fast a problem can be answered" depends on what counts as a computer and as one step. A model that is unusual in some way can change what the statement means.
3. **A convention that makes something true for the wrong reason.** Lean's mathematics library sets some convenient values by convention: for instance, the derivative (rate of change) of a function that has no derivative at a point is defined to be 0. A statement can then come out true because of that 0, and not because of the mathematics.

The lesson for readers: look at the **definitions**, not only at the theorem. Experts do this reading, and it is hard, slow work. A machine cannot do it for them.

## Question 3: What does the checker have to trust?

Even a perfect kernel rests on a few things it does not check.

- **The axioms allowed.** An *axiom* is a rule accepted without proof. A false one lets you prove anything, even 1 = 2. Careful projects allow only three standard axioms and ask Lean to list what each theorem rests on. For the ETH statement, the repository's configuration file allows exactly those three.
- **The kernel itself**, the small program that checks each step. Its own correctness is assumed: in a normal check, nothing re-checks it.
- **The libraries imported**, such as Lean's large shared mathematics library, which the proof builds on.

**A lesson we learned ourselves.** Listing the axioms is not enough. In our own published audit of a different OpenAI Lean collection (`openai/NavierStokesAndEuler`), we deliberately planted a forged declaration: a false statement stored without being sent to the kernel. Lean's usual axiom listing reported it exactly as it would an honest proof. Only a **replay**, in which a program sends every stored step back through the kernel, rejected it. The forgery was ours, planted on purpose as a test; the collection itself passed the replay we ran (a small number of auxiliary declarations were skipped by design: see the audit). (Our audit: [doi:10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381). The credit for the proofs in that collection belongs to its authors.)

*The everyday picture:* a video replay in sport. Instead of trusting the scoresheet, you look again at every play.

*Where the picture stops:* the replay sends every step back through the same kernel. It is a second look by the same referee, not a second, independent referee.

So ask: **which axioms, which libraries, and was the whole thing replayed?**

## Question 4: Has a human expert reviewed it, and what is still pending?

"Checked by a machine" and "understood and accepted by experts" are two different things. The machine answers question 1. Only people can answer question 2.

*The everyday picture:* a building can pass an automatic inspection of every weld and still need an engineer to say whether it was built to the right plans.

*Where the picture stops:* expert reading is not one inspection with a pass mark. It is people reading, discussing and sometimes disagreeing.

On OpenAI's page, the expert step is written in the **future tense** (the second quotation above): the group named there is to verify and supervise the work. The announcement is very recent. For now, the expert review is pending.

## Question 5: What would it change in practice, and for whom?

A result can be important in principle and make no difference to the next app on your phone. OpenAI itself says that practical speed-ups would need a lot more research.

Here is a rough illustration. **This is our own calculation, not the authors', and it is only a sketch.** The formal statement allows a running time whose growth includes some constants that are not stated. If we set those constants to 1, the bound in the formal statement beats the plain exponential (trying all on/off settings, one after another) only when the puzzle has more than about **10^2390 switches**: a number written with 2,391 digits, far beyond any puzzle that could exist physically. The true constants are not stated, and constants matter: they could move this threshold a long way. The manuscript claims a sharper bound than the one in the formal statement.

*The everyday picture:* a shortcut that saves time only on journeys longer than any road could ever be.

*Where the picture stops:* nobody has stated the real constants, so the length of that journey is not known; and unlike a useless shortcut, the result would still matter for theory.

If the result holds, its importance would be for theory: many published results are stated "assuming ETH", and they would lose that assumption. But "a famous conjecture is false" does not mean "this problem is now easy for computers".

## What the repository says

OpenAI published the materials in a public repository, `github.com/openai/math`. Its README describes them as "raw research data" and says: "We defer to the math community completely on matters of credit, precedence, and concurrent work." (OpenAI, `openai/math`, README.)

In the repository's catalogue of Lean formalisations, when we looked, on 27 October 2026, the review field for this formalisation read `unchecked`. We saw no recorded verdict of the checking tool in the repository. That does not mean no check was run, only that we found none recorded there.

## Our own levels, applied to this case

The project behind this repository gives every claim a level (see [Elenchus in ten minutes](elenchus-in-10-minutes.md)): **A**, "the judge looked"; **L**, "it is in a serious book"; **C**, "someone reasoned, nobody machine-checked"; **X**, "a pencil sketch". The table is an **illustration, not a rating of OpenAI's work**: it says only what *we* can see.

| Layer | Where it stands, as far as we can see |
|---|---|
| The formal statement, checked by a machine | OpenAI says it was verified in Lean. We have not seen a recorded verdict, and we did not run one. **Unknown to us**; we cannot write "A". |
| Whether the formal statement says what the paper says | A human question (question 2). **Pending.** |
| Review by human experts | Announced, in the future tense (question 4). **Pending.** |
| Practical effect | Our rough calculation (question 5): **none for today's software**. That figure is ours and is only level **X**. |

## A reader's checklist

1. What exactly is claimed, in the authors' own words?
2. Who checked it: a machine, a person, or both?
3. Which checker, run by whom, and where is its answer recorded?
4. Have I seen the formal statement, or only a headline about it?
5. Do the definitions mean what the words suggest, or could one be empty or unusual?
6. Could a convention (such as "undefined means 0") make it true for the wrong reason?
7. Which axioms and libraries does it rest on, and was it replayed?
8. Has an expert reviewed it, or is that still to come?
9. What would it change in practice, and for whom, and at what size?
10. What is still pending, and when will we know more?

## What this page does not do

- It does not say whether OpenAI's claim is right or wrong.
- It does not say whether OpenAI is right or wrong to publish in this way.
- It does not quote or name any critic.
- The credit for the results belongs to their authors and to the groups examining them. We do not race those groups.

## Why we care

The same five questions apply to our own work. Our results were also produced by AI agents and audited by AI agents, and **no human mathematician has reviewed them**. You can see the claims we withdrew in [what we got wrong](what-we-got-wrong.md), and you can test our work in [check it yourself](check-it-yourself.md). Please ask these five questions of us too.
