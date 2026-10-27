# Nos erreurs

[English version](what-we-got-wrong.md)

Voici, par ordre de date, les affirmations retirées, réfutées ou corrigées en public, puis nos propres idées, testées, qui ont perdu. Chaque entrée donne la date, la notice, ce qui était faux et la façon dont l'erreur a été repérée. Quand les sources utilisées ici ne disent pas comment l'erreur a été remarquée, l'entrée le dit au lieu de deviner. Les DOI ont la forme `10.5281/zenodo.<numéro>`.

Ces erreurs ne sont pas cachées dans une note de bas de page : elles font partie de l'histoire, et souvent de sa partie la plus utile.

## Retraits et corrections

| Date (2026) | Notice | Ce qui était faux | Comment on l'a vu |
|---|---|---|---|
| juillet | (dépôts de code, sans DOI) | Des nombres de réseaux dans un dépôt de cosmologie sont retirés. Dans un dépôt de propositions Lean, deux théorèmes d'« intégralité » se révèlent ne rien dire. | Réexamen dans ces dépôts, avec des retraits écrits sur place. |
| 9 sept. | [22682139](https://doi.org/10.5281/zenodo.22682139) | L'article se présentait comme la première formalisation de l'involution de Fricke. | Un audit a trouvé des travaux antérieurs. |
| 15 sept. | [22723078](https://doi.org/10.5281/zenodo.22723078) → [22773907](https://doi.org/10.5281/zenodo.22773907) | Une lecture physique (« censure topologique de l'explosion ») des preuves d'OpenAI sur les équations des fluides. Les constructions étaient des mathématiques valides ; la lecture est retirée, avec une table de corrections. | Non précisé dans les sources utilisées ici. Le retrait est venu trois jours après la publication. |
| 18 sept. | [22837842](https://doi.org/10.5281/zenodo.22837842), [22837837](https://doi.org/10.5281/zenodo.22837837) | La théorie « double échelle ». Son nombre central (27720) échoue à un test de torsion (*twining*) dans les 25 classes non triviales du groupe M24, ce qui en fait de la numérologie, et sa conjecture testable ne survit pas aux données. Cette ligne comprenait les articles de juin et juillet qui reliaient la théorie des cordes aux tensions des galaxies observées par JWST (20863378, 20863381, 21350629). | Un test contre les données, préenregistré : quatre verdicts négatifs. |
| 20 sept. | [22853896](https://doi.org/10.5281/zenodo.22853896) | Deux « découvertes » d'une bibliothèque sur les fluides quantiques. | Une vérification de la littérature. |
| 21 sept. | [22872083](https://doi.org/10.5281/zenodo.22872083) | Les affirmations de la version 1 d'un article sur la dualité T. | Non précisé dans les sources utilisées ici. |
| 21 sept. | [22879667](https://doi.org/10.5281/zenodo.22879667) | La version 1 de RunuX (20383038, 20383105, 20383112) annonçait, sur du matériel spécialisé, avec un modèle de 70 milliards de paramètres et des certificats Lean, des résultats jamais obtenus. La version 2 dit : « retirés, pas renommés ». | Autocorrection. Un audit ultérieur « affirmations contre preuves » ([22985926](https://doi.org/10.5281/zenodo.22985926)) a trouvé 141 paquets de code sur 316 qui n'étaient que des coquilles vides, et 249 trous de preuve ouverts derrière une annonce de « zéro sorry ». |
| 25–26 sept. | (le banc d'essai du laboratoire) | 14 composants annonçaient un succès sans avoir fait le travail, dont un script de « relecture par les pairs » qui n'appelait jamais aucun modèle, un évaluateur Lean trompé par ce qu'il affichait, et un résultat d’entraînement étiqueté « SUCCESS » dont la perte (*loss*) avait augmenté. | Des audits de remise en état du banc lui-même. |
| 3 oct. | [23119953](https://doi.org/10.5281/zenodo.23119953) | Les chiffres de performance des versions 1 et 2 de la porte GWAYA. | Retirés dans la version 3. Les sources utilisées ici ne détaillent pas comment le problème a été trouvé. |
| 9 oct. | [23262132](https://doi.org/10.5281/zenodo.23262132), [23262143](https://doi.org/10.5281/zenodo.23262143) | On lisait la friction des tourbillons comme suivant la « densité normale » ; elle suit la température. L'article sur le transport est corrigé (version 2.2). | L'article de correction. |
| 11 oct. | [23293429](https://doi.org/10.5281/zenodo.23293429) → [23646105](https://doi.org/10.5281/zenodo.23646105) | La simulation coupait la force à une distance fixe, ce qui déplaçait les énergies de plus que l'écart mesuré. | L'erratum est publié, et le calcul refait avec la force exacte dans 23646105. Un erratum en version 3 de 23293429 lui-même reste dû. |
| 19 oct. | [23468458](https://doi.org/10.5281/zenodo.23468458) | Un « rapport de relecture » produit par un script, avec des relecteurs inventés. | Retiré par cette notice. |
| 19–21 oct. | [23525655](https://doi.org/10.5281/zenodo.23525655) | L'étiquette « 5-Round Opus Peer-Reviewed » sur un lot d'articles. Le fichier de relecture « a été produit par un script qui n'appelle aucun relecteur ». Aucun humain n'a relu aucun de ces articles. | En vérifiant si un relecteur avait vraiment été appelé. Retrait deux jours plus tard. |
| 21 oct. | [23526783](https://doi.org/10.5281/zenodo.23526783) | Le mécanisme de correction moléculaire « POLE P286R » proposé par l'article lui-même. | Réfuté dans l'édition 3, qui ajoute un théorème d'impossibilité. |
| 21 oct. | [23532458](https://doi.org/10.5281/zenodo.23532458) | La prémisse de l'article sur le stellarator, selon laquelle une méthode de simulation standard (RK4) « chauffe » lentement les particules jusqu'à les faire s'échapper. Aux pas de calcul utilisés, RK4 les refroidit. Ses chiffres de confiance et un théorème sont retirés. | Un test sur 2 000 orbites par bande d'énergie, une règle de réfutation fixée à l'avance, et des contrôles capables d'échouer. |
| 21 oct. | [23532595](https://doi.org/10.5281/zenodo.23532595) | Le théorème 2.5 d'un article sur un modèle de turbulence (sous-maille), et son affirmation d'explosion. | Réfuté et retiré par cette notice. |
| 21 oct. | [23532601](https://doi.org/10.5281/zenodo.23532601) | Un « vérificateur SQIsign vérifié » (cryptographie post-quantique). Il accepte le nombre 256, qu'il devrait refuser. Trois affirmations principales sont retirées. | Un test avec une entrée qui doit être refusée. |

## Erreurs repérées par la méthode avant publication

- **Un faux rapport d'axiomes** (derrière [23653827](https://doi.org/10.5281/zenodo.23653827)). L'auditeur a montré qu'on pouvait faire dire `verified: true` à l'outil de certificat du projet pour un fichier contenant un axiome faux, grâce à une commande (`#exit`) qui arrête Lean avant le contrôle. *Repéré par* l'attaque volontaire de l'auditeur. L'outil a été réparé.
- **Une page jamais passée devant le juge** (derrière [23661381](https://doi.org/10.5281/zenodo.23661381)). Une déclaration enregistrée sans contrôle du noyau passe la liste habituelle des axiomes. *Repéré par* une contrefaçon fabriquée exprès par l'auditeur. Depuis, les règles exigent une relecture par le noyau et la recherche de ce genre d'options.
- **Un axiome faux dans un fichier revendiqué** (travail derrière [23653850](https://doi.org/10.5281/zenodo.23653850)). Un axiome de test planté se trouvait dans un fichier que d'autres auraient importé, et ils en auraient hérité. *Repéré par* le vérificateur. Les tests plantés vivent désormais dans des fichiers séparés.
- **Un préenregistrement faux** ([23660071](https://doi.org/10.5281/zenodo.23660071)). Une sous-hypothèse préenregistrée était fausse. *Repéré par* le noyau de Lean lui-même, pendant la formalisation. L'article le signale.

## Nos propres idées, testées et réfutées

Ce ne sont pas des retraits. Ce sont des idées du projet, testées comme prévu, qui ont perdu, et qui ont été publiées comme des résultats.

- L'inégalité de Lieb–Thirring sous forme matricielle : un résultat nul ([23245266](https://doi.org/10.5281/zenodo.23245266)).
- Des prédictions réfutées, conservées dans la série sur la conductance (23228685, 23241463, 23244556, 23248393).
- La série sur les fluides d'excitons : la plupart des tests préenregistrés échouent, et les articles le disent.
- L'idée QU-1 sur l'énergie de point zéro : réfutée par le calcul pour 8 forces sur 12 ([23653833](https://doi.org/10.5281/zenodo.23653833)), puis par certificat pour une force ([23655392](https://doi.org/10.5281/zenodo.23655392)) et pour des forces écrantées ([23663551](https://doi.org/10.5281/zenodo.23663551)). Dans le premier article, le meilleur concurrent annoncé d'abord s'est révélé à peine stable, et a été corrigé.
- La formule d'« enveloppe » du projet pour l'hélium : réfutée par les données de neutrons, aux 21 points de la région des rotons ([23653846](https://doi.org/10.5281/zenodo.23653846)).
- En biologie et en recherche automatisée : un certificat dont le transfert aux données de séquences échoue (23604793) ; des seuils « dus au hasard » sous-estimés, puis corrigés (23610116, 23610123) ; un transfert à la programmation génétique, réfuté (23611425) ; « la recombinaison n'aide pas » (23626924).
- L'extension de l'approche de Sandier–Serfaty à trois dimensions : un résultat négatif de faisabilité ([23655002](https://doi.org/10.5281/zenodo.23655002)). Une transition quantique attendue : un résultat négatif ([23655625](https://doi.org/10.5281/zenodo.23655625)).

## Affirmations restées sans retrait

Quelques notices du printemps contiennent des affirmations qu'on ne peut pas vérifier à partir des notices elles-mêmes, et aucun retrait n'a été publié pour elles. Nous les signalons pour que personne ne les prenne pour des résultats :
- le même texte déposé treize fois les 25 et 26 mai (dont 20380024), qui annonce une méthode d'apprentissage, 40 % d'économie d'énergie et une « vérification formelle en Lean 4 », dans une notice qui ne contient aucun fichier Lean ;
- les notices SymBrain (20397720) et CPUGym (20538871, 20539058), dont un lecteur ne peut pas vérifier les chiffres de performance.

Sources : le chapitre « Ce que nous avons retiré » du *Journal des découvertes*, et [`elenchus/METHODOLOGY.md`](../elenchus/METHODOLOGY.md) (en anglais). Si vous trouvez une erreur qui ne figure pas sur cette page, [ouvrez un ticket](../CONTRIBUTING.md), s'il vous plaît.
