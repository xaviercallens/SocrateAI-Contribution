# Licensing

> **Status.** These terms were chosen by the author on 27 October 2026 to carry out his wish that credit is kept and that improvements stay open source. The licences below are the way that wish is implemented. Legal advice is still recommended before relying on any of them being enforced.

Three licences apply, each to a different part of the repository.

| Path | Licence | Text |
|---|---|---|
| **Code outside `books/`**: every `*.py` and `*.lean` file, including the Elenchus ledger gate `elenchus/tool/ledger.py`, `elenchus/tools/check_consistency.py`, the `build_ledger.py` scripts and the Lean files under `elenchus/discoveries/*/lean/`, and `figures/make_loop_figure.py` | **GNU Affero General Public License v3.0 or later** (AGPL-3.0-or-later), with the additional attribution terms in [`NOTICE`](NOTICE) (section 7(b) of the licence). Copyright (c) 2026 Xavier Callens (SocrateAI Lab). | [`LICENSE`](LICENSE) |
| **Texts and figures new in this repository**: `README.md`, `README.fr.md`, everything in `docs/`, `figures/*.png` and `figures/*.svg`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSING.md`, `NOTICE`, `books/README.md`, `elenchus/tool/README.md`, `elenchus/REDACTION.md`, `CITATION.cff`, `.github/` | **Creative Commons Attribution-ShareAlike 4.0 International** (CC BY-SA 4.0) | [`LICENSE-CONTENT-SA.txt`](LICENSE-CONTENT-SA.txt) |
| **Already-published works and their records**: everything in `books/` (the two PDF books and their LaTeX sources, including the figure scripts in `books/source-*/code/`), and all non-code files in `elenchus/` not listed above (ledgers, evidence files, audits, revisions, metadata, registry, preregistrations, replay record, reports) | **Creative Commons Attribution 4.0 International** (CC BY 4.0), as on their Zenodo records. That licence is irrevocable for what was already published, so it stays. | [`LICENSE-CONTENT.txt`](LICENSE-CONTENT.txt) |

## What the terms mean in plain words

- **Code (AGPL).** You may use, study, change and share the code. If you share a changed version, or let people use it over a network, you must publish your changes under the same licence. Improvements therefore stay open source.
- **Attribution notices (AGPL section 7(b)).** Every copy or derivative of the code must keep the `NOTICE` file, the copyright notices, the `LICENSE` file and the author attribution "Xavier Callens (SocrateAI Lab)".
- **New texts and figures (CC BY-SA).** You may reuse and adapt them if you credit the author and share your adaptations under the same licence.
- **Published books (CC BY).** You may reuse and adapt them if you credit the author.

## What a licence cannot do

A licence can require that attribution notices are kept. **It cannot force anyone to cite this work in an academic paper.** Citation is requested, not required. [`CITATION.cff`](CITATION.cff) and the "How to cite" section of [`NOTICE`](NOTICE) say how to cite it.

## Things the author should know before publishing

- **The remote repository's first commit has an MIT `LICENSE`.** The commits prepared here replace it with the AGPL text. Copies anyone took while the MIT file was in place stay under MIT.
- **The ledger gate.** Earlier private copies of `elenchus/tool/ledger.py` carried an MIT notice in the name "Socrate AI Lab". This copy is offered under AGPL-3.0-or-later, by the same author. Anyone who received an MIT copy earlier keeps those MIT rights for that copy.
- **The books' source folders** (`books/source-fr/`, `books/source-en/`) are published on Zenodo under CC BY 4.0, scripts included. They therefore stay under CC BY 4.0 here and are not under the AGPL.

## What these licences do not cover

- **Short quotations from other people's papers.** Some evidence files in `elenchus/discoveries/*/ledger/` quote a few lines of published papers, to show exactly what a citation says. Those quotations belong to their authors. They are included as short scholarly quotations and are not relicensed. No full text of anyone else's paper is in this repository.
- **Fonts embedded in the PDF books.** They keep their own licences.
- **Upstream work named here** (OpenAI's `openai/math` and `openai/NavierStokesAndEuler`, Lean, Mathlib, SUNDIALS). None of it is copied here, and each keeps its own licence.
