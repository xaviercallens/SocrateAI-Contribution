# The books

## The Discovery Journal (two editions)

A book for readers who are not scientists. It tells one year of work with AI agents, with twenty contributions chosen by a scoring grid that was fixed before anything was scored, the method used to check them, and the list of claims that were withdrawn. 153 pages in each language.

| File | Language | DOI (Zenodo record) |
|---|---|---|
| [`discovery-journal-2026-fr.pdf`](discovery-journal-2026-fr.pdf) | French: *Le journal des découvertes* | [10.5281/zenodo.23669395](https://doi.org/10.5281/zenodo.23669395) |
| [`discovery-journal-2026-en.pdf`](discovery-journal-2026-en.pdf) | English: *The Discovery Journal* | [10.5281/zenodo.23669463](https://doi.org/10.5281/zenodo.23669463) |

Both files are byte-for-byte the PDFs published on Zenodo. Their md5 checksums match the checksums Zenodo shows: `04d2e91cc117c16fecdb255366200164` (French) and `a2b0758673d537056a8e77f4a5bfc89d` (English).

The LaTeX sources are in [`source-fr/`](source-fr/) and [`source-en/`](source-en/): the chapters, the frame chapters (`cadre/`), the generated tables (`gen/`), the figure scripts (`code/`), the figures, and the audit and revision notes. Three kinds of files are left out:
- the `data/` folders, which hold copies of public Zenodo records and are included in each record's source archive (`*.tar.gz` on Zenodo);
- each folder's `main.pdf`, which is the same book as the PDF above;
- build by-products.

To rebuild, download the source archive from the Zenodo record. It contains `data/`.

## The textbooks (Zenodo only)

| Title | Language | DOI |
|---|---|---|
| *De la conjecture au noyau Lean : réseaux optimaux, énergies quantiques et génétique des populations* (175 pages) | French | [10.5281/zenodo.23665820](https://doi.org/10.5281/zenodo.23665820) |
| *From Conjecture to the Lean Kernel: optimal lattices, quantum energies and population genetics* (181 pages) | English | [10.5281/zenodo.23665873](https://doi.org/10.5281/zenodo.23665873) |

These are textbooks for students: each result is given as a human proof, as a Lean statement and as computer tests. **Their PDFs are not copied into this repository.** Their published text includes file paths from the machine that built them and the names of the author's private code repositories. A published record cannot be edited, so the textbooks stay on Zenodo, where they can be downloaded at the DOIs above.

## Status of everything here

The books were written by AI agents under the author's direction and audited by other AI agents. **No human scientist has reviewed them.** They say so themselves.

Licence: CC BY 4.0 (see [`../LICENSING.md`](../LICENSING.md)).
