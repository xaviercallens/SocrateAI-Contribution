# Deux ans, racontés honnêtement

[English version](two-years.md)

Voici l'histoire de deux années de travail avec des agents d'IA, d'octobre 2024 à octobre 2026. Elle est racontée par étapes, avec des dates, et sans retirer les erreurs. Chaque DOI ci-dessous a la forme `10.5281/zenodo.<numéro>` et s'ouvre à l'adresse `https://doi.org/10.5281/zenodo.<numéro>`. Les sources sont les notices publiques de Zenodo, le compte GitHub de l'auteur et les fichiers de sélection figés qui sous-tendent *Le journal des découvertes*.

## Année 1 (octobre 2024 à octobre 2025) : une année d'apprentissage

Rien de vérifié n'est sorti de cette première année : c'est le résumé honnête.

- **Lire le travail des autres.** Cette année-là, l'essentiel de l'activité sur GitHub consiste en copies (*forks*) de projets d'autres personnes, pour apprendre : IA de jeu (échecs, poker), modèles de protéines et de code, modèles de langage pour les mathématiques et l'écriture de preuves, cadres pour agents, apprentissage automatique pour la finance. C'est le travail d'autres personnes, et aucune paternité n'est revendiquée.
- **Premiers projets personnels, en septembre et octobre 2025 :** un cadre pour faire dialoguer des agents logiciels (AMCP, en Java) et un jeu éducatif pour enfants, né d'une idée de mon fils, avec des adversaires pilotés par l'ordinateur. Le journal d'entraînement du jeu donne un taux de victoire qui n'a jamais été recalculé de façon indépendante.
- **Pas de science.** Aucun dépôt de cette année ne touche aux mathématiques, à la physique ou à la preuve formelle.

## Novembre 2025 à avril 2026 : de petits projets

Le compte montre de petits projets logiciels et personnels. Le premier lié à la science, en février 2026, est un ensemble de documents de conception ouverts pour un photobioréacteur à algues. Les mathématiques, la physique et Lean ne commencent qu'en mai 2026.

## Mai à août 2026 : des agents qui promettent trop

- **Les instruments arrivent d'abord.** Le 11 mai 2026 démarre rusty-SUNDIALS, une traduction en Rust, assistée par IA, d'un solveur standard d'équations différentielles. Il deviendra le moteur de calcul de tout le programme.
- **Les affirmations devancent les preuves.** Les 25 et 26 mai, la même affirmation d'une phrase est déposée 13 fois (20380024 et 12 copies). Elle annonce une méthode d'apprentissage sur du matériel spécialisé, 40 % d'économie d'énergie et une « vérification formelle en Lean 4 ». La notice ne contient aucun fichier Lean.
- Les mêmes jours, la version 1 d'un projet appelé RunuX (20383038, 20383105, 20383112) annonce des résultats qui, la version 2 l'admettra, n'avaient jamais été obtenus.
- Deux autres notices, SymBrain (20397720) et CPUGym (20538871, 20539058), donnent des chiffres de performance qu'un lecteur ne peut pas vérifier.
- **Une cosmologie bâtie sur des coïncidences numériques.** Des articles de juin et juillet affirment que les surfaces K3 de la théorie des cordes expliquent des tensions dans les observations de galaxies du télescope JWST (20863378, 20863381, 21350629).
- **Les premiers retraits** ont lieu dans des dépôts de code en juillet : des nombres de réseaux sont retirés, et deux « théorèmes » se révèlent ne rien dire.
- **Premier contact avec la preuve formelle**, avec ses leçons :
  - un article sur les quotients êta (22160184) utilise un raccourci de Lean, `native_decide`, qui fait confiance à du code compilé au lieu du vérificateur ;
  - un autre article (22161523) qualifie sa vérification Lean de « zéro sorry, code de sortie 0 ». Mais une preuve à trou (`sorry`) se termine elle aussi avec le code 0.

**Leçon :** le compte rendu de succès d'un agent n'est pas une preuve.

## Septembre 2026 : se corriger en public

- **Vérifier les axiomes, pas les codes de sortie.** L'article sur l'involution de Fricke (22682139) fixe ses théorèmes avec des contrôles d'axiomes et un contrôle négatif. Il retire aussi sa propre prétention à être « la première formalisation » après qu'un audit a trouvé des travaux antérieurs.
- **Une interprétation retirée en trois jours.** Un article sur les preuves d'OpenAI concernant les équations des fluides (22723078) proposait une lecture physique. Trois jours plus tard, « Where the continuum ends » (22773907) reconnaît les constructions comme des mathématiques valides, retire l'interprétation et publie une table de corrections.
- **La méthode est mise par écrit.** « A laboratory method for AI-assisted science » (22829767, 18 septembre) décrit le registre d'affirmations qui deviendra Elenchus.
- **L'idée « double échelle » est retirée.** Le même jour, la révision 5 de l'article (22837842) indique que son nombre central échoue à un test dans les 25 classes où il a été essayé, ce qui en fait de la numérologie. Un test préenregistré contre les données (22837837) donne quatre verdicts négatifs. Les mathématiques Lean de ce programme sont conservées, séparément de la physique retirée.
- **Corrections en cascade :**
  - deux « découvertes » sur les fluides quantiques sont retirées après une vérification de la littérature (22853896) ;
  - un article sur la dualité T retire les affirmations de sa version 1 (22872083) ;
  - la version 2 de RunuX retire les résultats jamais obtenus : « retirés, pas renommés » (22879667).
- **Le banc s'audite lui-même.** Des audits du banc d'essai du laboratoire trouvent 14 composants qui annonçaient un succès sans avoir fait le travail. L'un était un script de « relecture par les pairs » qui n'appelait jamais aucun modèle. Un audit distinct de RunuX (22985926) trouve que 141 paquets de code sur 316 sont des coquilles vides, et 249 trous de preuve ouverts derrière une annonce de « zéro sorry ».
- **Une première reproduction menée par des agents.** Une reproduction préenregistrée d'un ajustement cosmologique publié est déposée (23003926). Elle indique qu'aucune personne ne l'a relue.

**Leçon :** la correction devient un acte publié, et non une retouche discrète.

## Du 1er au 11 octobre 2026 : la méthode à l'œuvre

- **Des portes capables de dire non.** La porte GWAYA (23119953) retire ses chiffres de performance antérieurs. Elle montre qu'une « preuve » Lean de 1 = 2, obtenue grâce à un axiome caché, compile sans erreur et n'est démasquée que par le contrôle des axiomes.
- **Les nombres passent devant le vérificateur.** Le 8 octobre, le noyau de Lean contrôle pour la première fois le certificat en nombres entiers d'un solveur, et encadre les distances de galaxies de DESI (23247730). Le 10 octobre, un calcul certifié exclut un taux d'expansion de 73 ou plus, dans le modèle standard et ses simplifications déclarées (23284020).
- **Des résultats négatifs publiés comme des résultats :**
  - un résultat nul sur une inégalité matricielle (23245266) ;
  - des prédictions réfutées, conservées dans une série sur la conductance (23228685, 23241463, 23244556, 23248393) ;
  - la friction des tourbillons suit la température, et un article sur le transport est corrigé (23262132, 23262143).
- **L'IA propose, Lean vérifie les conséquences.** La preuve, produite par une IA d'OpenAI, que le rangement en triangles est le plus économe en énergie devient le théorème amont. Des conséquences vérifiées par le noyau suivent (23285631, puis 23293112 et 23293429), ainsi qu'un manuel pour étudiants (23295142).

**Leçon :** la boucle fonctionne quand chaque étape a le droit de dire non.

## Du 17 au 21 octobre 2026 : la rechute

Le 19 octobre, un lot d'articles paraît sous l'étiquette « 5-Round Opus Peer-Reviewed » (« relu par les pairs en cinq tours »). Tous annoncent « zéro sorryAx, zéro axiome ajouté ». Il y a parmi eux sept copies d'un article sur un stellarator (une machine à fusion) et sept dépôts de cryptographie post-quantique. Des articles de génétique suivent le 20 octobre. **Aucun humain n'en avait relu aucun, et le fichier de relecture avait été produit par un script qui n'appelle aucun relecteur.** Cela se produit un mois après la mise par écrit de la méthode.

Les retraits arrivent deux jours plus tard, tous le 21 octobre :
- 23525655 : l'étiquette « relu par les pairs » est retirée ;
- 23526783 : le mécanisme de correction moléculaire proposé par l'article est réfuté ;
- 23532458 : la prémisse de l'article sur le stellarator est réfutée ;
- 23532595 : un théorème sur un modèle de turbulence est réfuté ;
- 23532601 : on montre que le « vérificateur SQIsign vérifié » accepte une valeur qu'il devrait refuser, et trois affirmations principales sont retirées.

Dès le 19 octobre, 23468458 avait retiré un « rapport de relecture » produit par un script, avec des relecteurs inventés.

**Leçon :** une méthode sur le papier n'empêche pas d'exagérer. Il faut l'appliquer. « Relu par des agents d'IA » n'est pas une relecture par des pairs humains.

## Du 23 au 26 octobre 2026 : la boucle complète

- **D'autres résultats négatifs**, en biologie et en recherche automatisée (23604793, 23610116, 23610123, 23611425, 23626924).
- **Cinq applications** du théorème du triangle à des systèmes physiques (23646103, 23646105, 23646107, 23646111, 23646117). Chacune a été auditée par un agent distinct, et chaque révision a été consignée.
- **Programmes du 26 octobre :**
  - le certificat de Sandier–Serfaty reproduit et audité, sans prétendre à une preuve (23653827) ;
  - l'idée sur l'énergie de point zéro réfutée par le calcul (23653833), puis par un certificat (23655392) ;
  - des résultats de génétique des populations vérifiés à la machine (23653850) ;
  - 4 étapes sur 12 du certificat refaites dans le noyau (23656804) ;
  - le théorème isotherme, avec sa propre erreur de préenregistrement signalée (23660071) ;
  - une reconstruction indépendante des preuves d'OpenAI sur les équations des fluides (23661381), qui n'affirme explicitement pas qu'un problème à prix de l'Institut Clay est résolu.
- **Une relecture par le noyau** des modules du programme, le 26 octobre : 93 modules relus, sans aucun échec.
- **Les livres.** Les deux manuels (23665820, 23665873) et les deux éditions du *Journal des découvertes* (23669395, 23669463) sont publiés le 26 octobre.

Ce qui manque encore est écrit dans chaque registre : aucune personne n'a encore vérifié que les énoncés contrôlés à la machine veulent dire ce que disent leurs descriptions en langage courant.

## Ce que deux ans ont appris

1. Les agents d'IA savent très bien dire qu'un travail est terminé. Ce n'est pas une preuve.
2. Il faut montrer que chaque contrôle est capable d'échouer.
3. Celui qui produit un résultat ne doit pas être celui qui le vérifie.
4. Une affirmation fausse se retire en public, avec sa raison.
5. Une méthode écrite ne protège de rien tant qu'on ne l'applique pas, à chaque fois.
6. La dernière étape, une lecture humaine des énoncés, n'a pas encore été faite.

Pour aller plus loin : [nos erreurs](what-we-got-wrong.fr.md), et *Le journal des découvertes* ([français](../books/discovery-journal-2026-fr.pdf), [anglais](../books/discovery-journal-2026-en.pdf)).
