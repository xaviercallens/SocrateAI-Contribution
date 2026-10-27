# SocrateAI-Contribution

*Deux ans à apprendre à faire de la science avec l'IA, et à vérifier ce qu'elle dit.*

[English version](README.md)

## Ce que c'est

- Je m'appelle Xavier Callens (SocrateAI Lab). Depuis deux ans, je travaille avec des agents d'IA : des programmes à qui l'on confie une tâche entière (chercher, calculer, écrire, vérifier) et qui la mènent pas à pas.
- Les agents écrivent vite et bien. Ils écrivent aussi des choses fausses, avec la même assurance. Les premiers mois, je les ai crus trop facilement, et j'ai dû retirer publiquement des affirmations.
- J'en ai tiré une habitude empruntée à Socrate : interroger chaque affirmation avant de la croire. Je l'appelle **Elenchus**, du mot grec qui désigne sa manière de questionner.
- Ce dépôt est une vitrine de ce que cette habitude a produit. Il contient deux livres écrits pour des lecteurs qui ne sont pas scientifiques, vingt contributions vérifiées aussi soigneusement que j'ai pu, les affirmations sur lesquelles je me suis trompé, et tout ce qu'il faut pour vérifier le travail vous-même.
- La plupart des résultats sont modestes. La méthode, et le relevé honnête des erreurs, en sont peut-être la partie la plus utile.
- **Aucun mathématicien ni scientifique humain n'a relu ce travail.** Il a été produit par des agents d'IA sous ma direction, puis vérifié par d'autres agents d'IA. Je le dis en tête parce que c'est la limite la plus importante de tout ce qui suit.

## L'habitude : interroger d'abord, croire ensuite

Socrate ne cherchait pas à prouver qu'il avait raison. Il posait des questions jusqu'à trouver l'endroit où une affirmation se contredisait. Ce qui résistait à l'examen méritait d'être cru, au moins pour un temps.

Ici, ce sont des règles et des programmes qui posent les questions. Chaque résultat fait le même tour :

![La boucle Elenchus : l'IA propose, le calcul explore, Lean juge, l'humain décide du sens](figures/elenchus-loop-fr.png)

1. **L'IA propose.** Un agent suggère une idée, une preuve ou un programme.
2. **Le calcul explore.** Avant toute tentative de preuve, des calculs sur ordinateur mettent l'idée à l'épreuve. Beaucoup d'idées échouent à ce stade, et ces échecs sont publiés.
3. **Le vérificateur de preuves juge.** Un petit programme strict, le noyau de Lean, contrôle chaque pas d'une preuve. On ne peut pas le flatter, et il lui est égal de savoir qui a écrit la preuve.
4. **L'humain décide du sens**, et de ce qui mérite d'être publié.

Chaque affirmation porte aussi une étiquette qui dit qui l'a vérifiée :

| Niveau | En mots de tous les jours | Ce que cela veut dire |
|---|---|---|
| **A** | « le juge a regardé » | Le vérificateur de preuves Lean a contrôlé chaque pas. La preuve n'utilise que les trois règles de base habituelles, un second programme a relu toute la preuve (la « relecture », *replay*), et une recherche n'a trouvé aucune astuce pour contourner le juge. Quand la relecture manque, les livres écrivent « As ». |
| **L** | « c'est écrit dans un livre sérieux » | Le résultat est publié dans la littérature scientifique, et nous le citons précisément. |
| **C** | « quelqu'un a raisonné, personne n'a vérifié à la machine » | Un raisonnement écrit. Ici, il a presque toujours été écrit par un agent d'IA et relu par un autre. |
| **X** | « une esquisse au crayon » | Un calcul avec des nombres décimaux arrondis, comme une simulation. Il peut montrer la voie, ou montrer qu'une idée est fausse. Il ne prouve jamais rien. |

Une affirmation ne vaut que ce que vaut son maillon le plus faible. Quelques règles de plus complètent l'habitude :
- l'affirmation est écrite avant le test ;
- chaque test comporte un cas qui doit réussir et un cas qui doit échouer, pour montrer que le test sait dire non ;
- l'agent qui produit un résultat n'est pas celui qui le vérifie ;
- les résultats négatifs sont publiés comme les autres.

La méthode expliquée sans jargon : [docs/elenchus-in-10-minutes.fr.md](docs/elenchus-in-10-minutes.fr.md).

## Par où commencer

- **Si vous êtes curieux sans être scientifique :** lisez *Le journal des découvertes* ([PDF en français](books/discovery-journal-2026-fr.pdf), [PDF en anglais](books/discovery-journal-2026-en.pdf)). Il commence par la méthode, expliquée avec un procès, un détecteur de fumée et une recette goûtée par quelqu'un d'autre. Lisez ensuite [l'histoire des deux ans](docs/two-years.fr.md) et [nos erreurs](docs/what-we-got-wrong.fr.md).
- **Si vous avez vu un titre sur une « preuve » écrite par une IA :** lisez [comment lire une preuve écrite par une IA : cinq questions](docs/how-to-read-an-ai-generated-proof.fr.md).
- **Si vous êtes étudiant :** lisez le manuel *De la conjecture au noyau Lean* ([doi:10.5281/zenodo.23665820](https://doi.org/10.5281/zenodo.23665820) ; édition anglaise [doi:10.5281/zenodo.23665873](https://doi.org/10.5281/zenodo.23665873)). Chaque résultat y est donné de trois façons : une preuve humaine, un énoncé Lean et des tests sur ordinateur. Essayez ensuite [vérifier par vous-même](docs/check-it-yourself.fr.md).
- **Si vous êtes spécialiste et voulez vérifier :** commencez par [`elenchus/README.md`](elenchus/README.md), [`elenchus/REGISTRY.md`](elenchus/REGISTRY.md) (24 publications Zenodo avec leurs registres d'affirmations), [`elenchus/CONSISTENCY_REPORT.md`](elenchus/CONSISTENCY_REPORT.md) et le vérificateur de registres [`elenchus/tool/`](elenchus/tool/). Puis essayez, s'il vous plaît, de casser quelque chose : [CONTRIBUTING.md](CONTRIBUTING.md).

## Les vingt contributions, en mots simples

*Le journal des découvertes* raconte vingt contributions. Elles ont été choisies parmi environ 112 travaux publiés et 57 projets de code liés à la science, avec une grille de notation écrite et figée avant toute note. La grille imposait au moins trois leçons (échecs ou autocorrections). La liste suit le classement du livre.

Plusieurs résultats s'appuient sur des preuves qu'une IA d'OpenAI a publiées en 2026 et qu'un ordinateur a vérifiées. Ces preuves sont produites par une IA et n'ont pas été relues par des pairs. Les lignes marquées **(conditionnel)** ne valent que ce que vaut ce travail amont.

| # | Contribution | En une ligne simple | Niveau | Notice | Réserve |
|---|---|---|---|---|---|
| 1 | Des distances cosmiques avec une marge d'erreur vérifiée par une machine | Les distances des galaxies lointaines mesurées par le relevé DESI, calculées avec une marge d'erreur confirmée par le vérificateur de preuves | As | [10.5281/zenodo.23247730](https://doi.org/10.5281/zenodo.23247730) | On vérifie un calcul, pas une nouvelle mesure, et pour une seule valeur de la densité de matière (l'ajustement du projet, pas celui de DESI). |
| 2 | Une tension célèbre de la cosmologie, écrite comme une inégalité vérifiée | Dans le modèle standard de l'Univers et ses simplifications déclarées, un taux d'expansion de 73 ou plus s'accorde bien moins bien aux données DESI et à la chimie de l'Univers primitif que le meilleur ajustement | As | [10.5281/zenodo.23284020](https://doi.org/10.5281/zenodo.23284020) | On certifie une tension déjà connue par les statistiques ordinaires. Un découpage prévu du calcul a échoué, a été remplacé, et l'article le dit. |
| 3 | Le triangle, rangement le moins coûteux : des conséquences vérifiées et une simulation | Des conséquences du théorème selon lequel le rangement en triangles est le plus économe pour des points qui se repoussent, vérifiées à la machine, plus une simulation | A (simulation X) | [10.5281/zenodo.23293429](https://doi.org/10.5281/zenodo.23293429) | **(conditionnel)**. La simulation coupait la force trop tôt, erreur réparée à la ligne 4. |
| 4 | La répulsion écrantée entre dans la famille du théorème, et une erreur est réparée | Poussières chargées et colloïdes se repoussent par une force « écrantée » ; le vérificateur confirme que cette force est couverte par le théorème du triangle | A | [10.5281/zenodo.23646105](https://doi.org/10.5281/zenodo.23646105) | **(conditionnel)**. Corrige aussi l'erreur de simulation précédente. |
| 5 | Refaire le calcul d'un autre, sans le déclarer juste | Le grand certificat informatique d'OpenAI pour une conjecture célèbre (Sandier–Serfaty) a été relancé et audité | X et C (énoncé Lean A) | [10.5281/zenodo.23653827](https://doi.org/10.5281/zenodo.23653827) | **La conjecture n'est ici ni démontrée, ni vérifiée, ni réfutée.** Elle a été reproduite et auditée, ce qui est différent. |
| 6 | Une règle prouvée droite montre que notre propre esquisse était fausse | Une borne classique de l'hélium superfluide vérifiée à la machine ; de vraies données de neutrons réfutent ensuite une formule proposée par le projet | A (données L) | [10.5281/zenodo.23653846](https://doi.org/10.5281/zenodo.23653846) | Un résultat formel positif et un résultat négatif sur notre propre idée. |
| 7 | Quelle chance a une mutation d'envahir une population ? | Des réponses classiques de la génétique des populations, contrôlées pas à pas par le vérificateur | A | [10.5281/zenodo.23653850](https://doi.org/10.5281/zenodo.23653850) | Résultats connus. Ce qui est nouveau, c'est la vérification à la machine. |
| 8 | Quand le plan de table ne change rien à la sélection | Un théorème classique de l'évolution sur un réseau, vérifié à la machine | A | [10.5281/zenodo.23660071](https://doi.org/10.5281/zenodo.23660071) | Une de nos propres sous-hypothèses préenregistrées était fausse, et l'article le signale. La réciproque n'est pas démontrée. |
| 9 | Un manuel pour suivre un théorème jusqu'au laboratoire | Un manuel de 105 pages pour étudiants : chaque résultat en preuve humaine, en énoncé Lean et en tests sur ordinateur | A (parties Lean nouvelles) | [10.5281/zenodo.23295142](https://doi.org/10.5281/zenodo.23295142) | **(conditionnel)**. Hérite de l'erreur de simulation de la ligne 3. |
| 10 | Des paires électron–trou qui se rangent en triangles, sur le papier | Une force dans des matériaux minces empilés est couverte par le théorème du triangle | A (simulation X) | [10.5281/zenodo.23646103](https://doi.org/10.5281/zenodo.23646103) | **(conditionnel)**. La simulation est un contrôle de cohérence, pas une preuve. |
| 11 | La force dans un semi-conducteur atomiquement mince, en tas de sable | La force entre charges dans des couches d'un atome d'épaisseur est une somme de morceaux en cloche, donc couverte par le théorème | A (une étape C) | [10.5281/zenodo.23646107](https://doi.org/10.5281/zenodo.23646107) | **(conditionnel)**. Un lien n'est qu'un raisonnement. Producteur et vérificateur n'étaient pas entièrement séparés à l'étape de l'article. |
| 12 | Tester avant de prouver : une idée naturelle qui ne tient pas | L'idée que le triangle minimise aussi l'énergie quantique du « frisson » échoue dans les calculs pour 8 forces sur 12 | X (quelques lemmes A) | [10.5281/zenodo.23653833](https://doi.org/10.5281/zenodo.23653833) | Une leçon. Ce sont des calculs décimaux, pas une preuve que l'idée est fausse. |
| 13 | Parfait au repos, pas quand il frissonne | Pour une force, un certificat montre qu'un tout petit cisaillement du réseau triangulaire abaisse l'énergie du frisson | C dans l'ensemble (logique et arithmétique A) | [10.5281/zenodo.23655392](https://doi.org/10.5281/zenodo.23655392) | Une leçon. Les intégrales ont été encadrées par un programme extérieur au vérificateur. |
| 14 | Quatre étages sur douze, et le prix du reste | Quatre des douze étapes du certificat de la ligne 5 ont été refaites dans le vérificateur | A (4 étapes) | [10.5281/zenodo.23656804](https://doi.org/10.5281/zenodo.23656804) | **La conjecture n'est pas démontrée formellement**, comme le dit le titre. |
| 15 | Remonter la machine des autres dans son propre atelier | Les preuves d'OpenAI sur les équations des fluides, vérifiées par ordinateur, ont été reconstruites indépendamment, et 88 400 déclarations relues par le vérificateur | A (faits de relecture) ; comparaison des énoncés C | [10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381) | **Aucun problème à prix de l'Institut Clay n'est déclaré résolu.** Le mérite revient aux auteurs de ces preuves. |
| 16 | Une garantie générale, trois certificats précis | Trois conséquences courtes du théorème du triangle, nommées et vérifiées à la machine | A | [10.5281/zenodo.23285631](https://doi.org/10.5281/zenodo.23285631) | **(conditionnel)**. Elles découlent vite du théorème ; des travaux ultérieurs s'en sont servis. |
| 17 | Le moteur des calculs, et son rapport d'inspection | Une traduction, assistée par IA, d'un solveur standard d'équations différentielles, utilisée par beaucoup des articles | X | [dépôt de code](https://github.com/xaviercallens/rusty-SUNDIALS) (pas de notice Zenodo) | Ses nombres ne sont jamais pris pour des preuves. Un audit de sa partie fusion a conduit à des retraits. |
| 18 | Une porte qui reste fermée quand on ne sait pas | Une porte qui n'accepte le code écrit par une IA que si de vrais compilateurs et le vérificateur sont d'accord | As (une démonstration) ; le reste autovérifié | [10.5281/zenodo.23119953](https://doi.org/10.5281/zenodo.23119953) | Des chiffres de performance antérieurs ont été retirés. Elle a encore laissé passer du code faux. |
| 19 | Le banc d'essai qui s'est inspecté lui-même | Le banc qui fait tourner les agents ; son propre audit a trouvé 14 composants qui annonçaient un succès sans avoir fait le travail | C (autoaudit) | [dépôt de code](https://github.com/xaviercallens/AutoevolveAI) (pas de notice Zenodo) | Autovérifié seulement. |
| 20 | On accusait le thermostat de surchauffer | Une affirmation de notre propre lot d'octobre, selon laquelle une méthode standard « chauffe » lentement des particules dans une machine à fusion, testée et trouvée fausse | X (avec contrôles) | [10.5281/zenodo.23532458](https://doi.org/10.5281/zenodo.23532458) | Une leçon : le retrait d'une de nos affirmations. Personne d'autre que l'auteur ne l'a relue. |

Chaque contribution est racontée plus en détail, dans le même style simple, dans *Le journal des découvertes*. Les détails techniques sont dans [`elenchus/`](elenchus/) et sur chaque notice Zenodo.

## Ce qui n'est PAS affirmé

> - **Aucune conjecture célèbre n'est démontrée ici.** En particulier, la conjecture de Sandier–Serfaty ne l'est pas : les lignes 5 et 14 reproduisent, auditent et revérifient en partie un certificat publié par d'autres.
> - **Aucun problème à prix de l'Institut Clay n'est résolu.** La ligne 15 est une reconstruction et une relecture indépendantes de preuves écrites par d'autres, rien de plus.
> - **Les résultats qui s'appuient sur les théorèmes d'OpenAI sont conditionnels.** Ces preuves amont ont été produites par une IA et acceptées par un ordinateur, mais elles n'ont pas été relues par des pairs.
> - **Tout ici a été produit par des agents d'IA sous ma direction et audité par d'autres agents d'IA.** Un audit par une IA n'est pas une relecture par des pairs. **Aucun humain n'a audité ce travail**, pas même la question de savoir si chaque énoncé vérifié à la machine dit bien ce que dit sa description en langage courant.
> - Un niveau A signifie que le vérificateur a accepté une preuve de l'énoncé formel. Cela ne veut pas dire que l'énoncé capture la question du monde réel.

## Les livres

| Livre | Français | Anglais |
|---|---|---|
| *Le journal des découvertes* (153 pages, pour tous) | [PDF](books/discovery-journal-2026-fr.pdf) · [doi:10.5281/zenodo.23669395](https://doi.org/10.5281/zenodo.23669395) | [PDF](books/discovery-journal-2026-en.pdf) · [doi:10.5281/zenodo.23669463](https://doi.org/10.5281/zenodo.23669463) |
| *De la conjecture au noyau Lean* (manuel pour étudiants) | [doi:10.5281/zenodo.23665820](https://doi.org/10.5281/zenodo.23665820) | [doi:10.5281/zenodo.23665873](https://doi.org/10.5281/zenodo.23665873) |

Les manuels sont sur Zenodo seulement. [`books/README.md`](books/README.md) explique pourquoi.

## Dans ce dépôt

- [`docs/`](docs/) : [l'histoire des deux ans](docs/two-years.fr.md), [Elenchus en dix minutes](docs/elenchus-in-10-minutes.fr.md), [nos erreurs](docs/what-we-got-wrong.fr.md), [vérifier par vous-même](docs/check-it-yourself.fr.md), [ce que nous voulons essayer ensuite](docs/roadmap.md) (en anglais).
- [`books/`](books/) : les deux PDF du journal et leurs sources LaTeX.
- [`elenchus/`](elenchus/) : le dossier complet de 24 publications Zenodo, avec registres d'affirmations, audits et fichiers Lean, le vérificateur de registres Elenchus ([`elenchus/tool/`](elenchus/tool/)) et un contrôle de cohérence que vous pouvez lancer.
- [`figures/`](figures/) : la figure de la boucle et le programme qui la dessine.

## Questions, corrections, contestations

Utilisez le suivi des tickets (*issues*). Les contestations (tickets « red team ») sont particulièrement bienvenues : si vous pensez qu'une affirmation est fausse, exagérée ou mal étiquetée, dites-le. Voir [CONTRIBUTING.md](CONTRIBUTING.md). Il n'y a pas de contact par courriel : ouvrez un ticket.

## Utilisez-le, citez-le, rendez la pareille

- **Utilisez-le.** Vous pouvez lire, réutiliser, adapter et partager tout ce qui est ici, y compris le vérificateur de registres Elenchus de [`elenchus/tool/`](elenchus/tool/).
- **Gardez les noms.** Toute copie ou adaptation doit conserver le crédit de l'auteur, « Xavier Callens (SocrateAI Lab) », les mentions de droit d'auteur et le fichier [`NOTICE`](NOTICE).
- **Rendez la pareille.** Le code est sous licence GNU Affero GPL (version 3 ou ultérieure). Si vous partagez une version améliorée, ou la faites tourner pour d'autres par le réseau, vous en partagez le code source sous la même licence. Les nouveaux textes et figures sont sous CC BY-SA 4.0, qui demande la même chose pour les adaptations. Les livres déjà publiés sur Zenodo restent sous CC BY 4.0.
- **Citez-le.** Une licence ne peut pas imposer une citation ; c'est donc une demande : si ce travail vous aide, citez les livres, s'il vous plaît. [`CITATION.cff`](CITATION.cff) donne les détails.

Quelle licence couvre quel fichier : [`LICENSING.md`](LICENSING.md) (en anglais). Ces conditions ont été choisies le 27 octobre 2026 pour réaliser le souhait de l'auteur : que le crédit soit conservé et que les améliorations restent libres. Un avis juridique reste recommandé avant de compter sur leur application.
