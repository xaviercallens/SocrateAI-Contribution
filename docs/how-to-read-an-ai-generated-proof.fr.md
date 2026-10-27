# Comment lire une preuve écrite par une IA : cinq questions

[English version](how-to-read-an-ai-generated-proof.md)

*Pour les lecteurs curieux et les étudiants. Sans formules.*

Les journaux disent parfois qu'un système d'IA a « démontré » quelque chose et qu'un ordinateur l'a « vérifié ». Cette page propose cinq questions à poser. Elles ne disent pas si une affirmation est vraie. Elles disent ce qui a été vérifié, par qui, et ce qui reste en attente.

## Une histoire vraie à garder en tête

Fin octobre 2026, OpenAI a annoncé trois résultats, en mathématiques, en informatique et en physique. Sa page *Building scientific understanding with academic communities* les décrit : l'un en analyse harmonique (les mathématiques des ondes), l'un sur l'existence de certaines théories de la physique des particules, et l'un sur une célèbre conjecture d'informatique, l'**hypothèse du temps exponentiel**, ou **ETH** (de l'anglais *Exponential Time Hypothesis*). La presse a suivi les 26 et 27 octobre (Gizmodo, DEV Community, MLQ.ai) ; ce sont des sources secondaires, que nous n'avons vues qu'en résumé et sur lesquelles nous n'appuyons aucune affirmation de cette page.

**Ce que dit l'ETH, en deux phrases.** Imaginez un casse-tête fait de nombreux interrupteurs et d'une liste de règles comme « interrupteur 3 allumé, ou interrupteur 7 éteint, ou interrupteur 9 allumé » : existe-t-il une position des interrupteurs qui respecte toutes les règles ? L'ETH, une conjecture qui tient depuis environ vingt-cinq ans, dit que, si astucieuse que soit la méthode, le temps nécessaire pour répondre dans le pire des cas croît de façon exponentielle avec le nombre d'interrupteurs : chaque interrupteur de plus multiplie le travail par un facteur fixe. (Des méthodes astucieuses font mieux qu'essayer toutes les positions ; l'ETH dit seulement qu'aucune n'échappe à ce genre de croissance.)

**Ce que dit OpenAI.** Sur sa page, dans la version française qui nous a été transmise, OpenAI écrit :

> « notre système a récemment démontré que l'ETH est fausse, un résultat qui a ensuite été vérifié en Lean »
> (OpenAI)

et, sur la suite :

> « Ces travaux seront vérifiés et encadrés par un groupe dirigé par Russell Impagliazzo (UC San Diego), Ramamohan Paturi (UC San Diego) et Ryan Williams (MIT) »
> (OpenAI)

**Ce que nous avons fait, et pas fait.** Nous n'avons pas lu la page en entier : seule une partie de son texte nous était accessible. Nous n'avons pas vérifié la preuve d'OpenAI, et nous n'avons pas fait tourner l'outil de vérification sur elle. **Nous n'affirmons rien sur la vérité ou la fausseté du résultat.** Nous prenons ce cas seulement parce qu'il est récent, public et clairement décrit.

## Question 1 : qui l'a vérifié, et comment ?

« Vérifié en Lean » veut dire quelque chose de précis. **Lean** est un langage dans lequel un énoncé mathématique et sa preuve sont écrits avec tant de détails qu'un programme peut contrôler chaque pas. En son centre se trouve un petit programme, le *noyau*, dont le seul travail est d'accepter ou de refuser chaque pas.

*L'image de tous les jours :* un correcteur d'orthographe et de grammaire pour la logique, très strict et jamais fatigué. Il lit chaque ligne et une écriture assurée ne l'impressionne pas.

*Où l'image s'arrête :* un correcteur de grammaire ne sait pas ce que vous vouliez dire. Lean, c'est pareil : il vérifie que la preuve démontre **l'énoncé qui a été écrit**. Il ne comprend pas l'idée qui est derrière.

Demandez donc : **qui a lancé le vérificateur, sur quels fichiers, et où sa réponse est-elle consignée ?**

## Question 2 : l'énoncé vérifié est-il le même que l'affirmation annoncée ?

Avant toute vérification, quelqu'un doit traduire l'affirmation du langage mathématique ordinaire vers Lean. Cette traduction s'appelle l'*énoncé formel*.

*L'image de tous les jours :* un tribunal statue sur le contrat signé, pas sur ce que les parties voulaient dire. Si la traduction d'un contrat dans une autre langue a changé un mot, le juge statue sur le texte traduit.

*Où l'image s'arrête :* lire un énoncé formel demande souvent un expert du sujet **et** un expert de Lean.

Voici trois façons dont un énoncé formel peut, sans bruit, s'écarter de l'idée qu'il doit exprimer. Ce sont des types d'écart que les lecteurs attentifs recherchent en général ; nous ne disons pas que l'un d'eux se trouve dans le travail d'OpenAI.

1. **Une définition secrètement plus faible, ou vide.** Si un mot du théorème est défini de façon à ne presque rien vouloir dire (par exemple une « mesure de taille » qui se révèle nulle partout), le théorème peut devenir vrai pour une raison triviale.
2. **Un modèle de calcul inhabituel.** Un énoncé sur « la vitesse à laquelle on peut résoudre un problème » dépend de ce qu'on appelle un ordinateur et un pas de calcul. Un modèle inhabituel peut changer le sens de l'énoncé.
3. **Une convention qui rend une chose vraie pour une mauvaise raison.** La bibliothèque mathématique de Lean fixe certaines valeurs par commodité : par exemple, la dérivée (le taux de variation) d'une fonction qui n'a pas de dérivée en un point y est définie comme valant 0. Un énoncé peut alors être vrai à cause de ce 0, et non grâce aux mathématiques.

La leçon pour le lecteur : regardez les **définitions**, pas seulement le théorème. Ce sont des experts qui font cette lecture, difficile et lente ; une machine ne peut pas la faire à leur place.

## Question 3 : à quoi le vérificateur doit-il faire confiance ?

Même un noyau parfait repose sur quelques éléments qu'il ne vérifie pas.

- **Les axiomes autorisés.** Un *axiome* est une règle admise sans preuve. Un axiome faux permet de tout prouver, même 1 = 2. Les projets soigneux n'autorisent que trois axiomes habituels et demandent à Lean la liste de ce sur quoi repose chaque théorème. Pour l'énoncé sur l'ETH, le fichier de configuration du dépôt autorise exactement ces trois-là.
- **Le noyau lui-même**, le petit programme qui contrôle chaque pas. Sa propre correction est supposée : dans une vérification ordinaire, rien ne la revérifie.
- **Les bibliothèques importées**, comme la grande bibliothèque mathématique partagée de Lean, sur laquelle la preuve s'appuie.

**Une leçon que nous avons apprise nous-mêmes.** La liste des axiomes ne suffit pas. Dans notre propre audit publié d'une autre collection Lean d'OpenAI (`openai/NavierStokesAndEuler`), nous avons planté exprès une déclaration contrefaite : un énoncé faux enregistré sans être passé par le noyau. La liste habituelle des axiomes l'a présentée exactement comme une preuve honnête. Seule la **relecture** (*replay*), où un programme renvoie chaque pas enregistré devant le noyau, l'a rejetée. La contrefaçon était la nôtre, plantée exprès comme test ; la collection elle-même a passé la relecture que nous avons faite (un petit nombre de déclarations auxiliaires ont été écartées à dessein : voir l'audit). (Notre audit : [doi:10.5281/zenodo.23661381](https://doi.org/10.5281/zenodo.23661381). Le mérite des preuves de cette collection revient à ses auteurs.)

*L'image de tous les jours :* le ralenti vidéo au sport. Au lieu de se fier à la feuille de match, on revoit chaque action.

*Où l'image s'arrête :* la relecture renvoie chaque pas devant le même noyau. C'est un second regard du même arbitre, pas un second arbitre indépendant.

Demandez donc : **quels axiomes, quelles bibliothèques, et l'ensemble a-t-il été relu ?**

## Question 4 : un expert humain l'a-t-il examiné, et qu'est-ce qui reste en attente ?

« Vérifié par une machine » et « compris et accepté par des experts » sont deux choses différentes. La machine répond à la question 1. Seules des personnes peuvent répondre à la question 2.

*L'image de tous les jours :* un bâtiment peut réussir un contrôle automatique de chaque soudure et avoir encore besoin d'un ingénieur pour dire s'il a été construit selon les bons plans.

*Où l'image s'arrête :* la lecture par des experts n'est pas un contrôle unique avec une note de passage. Ce sont des personnes qui lisent, discutent et parfois ne sont pas d'accord.

Sur la page d'OpenAI, l'étape des experts est écrite **au futur** (la deuxième citation plus haut) : le groupe qui y est nommé doit vérifier et encadrer les travaux. L'annonce est très récente. Pour l'instant, l'examen par les experts est en attente.

## Question 5 : qu'est-ce que cela changerait en pratique, et pour qui ?

Un résultat peut être important en principe sans rien changer à la prochaine application de votre téléphone. OpenAI dit elle-même que des gains pratiques de vitesse demanderaient encore beaucoup de recherche.

Voici une illustration grossière. **C'est notre propre calcul, pas celui des auteurs, et ce n'est qu'une esquisse.** L'énoncé formel autorise un temps de calcul dont la croissance contient des constantes qui ne sont pas données. Si on fixe ces constantes à 1, la borne de l'énoncé formel ne bat l'exponentielle simple (essayer toutes les positions des interrupteurs, l'une après l'autre) que lorsque le casse-tête compte plus d'environ **10^2390 interrupteurs** : un nombre qui s'écrit avec 2 391 chiffres, bien au-delà de tout casse-tête qui pourrait exister physiquement. Les vraies constantes ne sont pas données, et les constantes comptent : elles pourraient déplacer ce seuil de beaucoup. Le manuscrit annonce une borne plus fine que celle de l'énoncé formel.

*L'image de tous les jours :* un raccourci qui ne fait gagner du temps que sur des trajets plus longs que toute route possible.

*Où l'image s'arrête :* personne n'a donné les vraies constantes, donc la longueur de ce trajet n'est pas connue ; et contrairement à un raccourci inutile, le résultat compterait quand même pour la théorie.

Si le résultat tient, son importance serait théorique : beaucoup de résultats publiés sont énoncés « en supposant l'ETH », et ils perdraient cette hypothèse. Mais « une conjecture célèbre est fausse » ne veut pas dire « ce problème est désormais facile pour les ordinateurs ».

## Ce que dit le dépôt

OpenAI a publié les documents dans un dépôt public, `github.com/openai/math`. Son README les décrit comme des « raw research data » (des « données de recherche brutes ») et dit : « We defer to the math community completely on matters of credit, precedence, and concurrent work. » (« Nous nous en remettons entièrement à la communauté mathématique pour les questions de mérite, d'antériorité et de travaux concurrents. » OpenAI, `openai/math`, README, notre traduction.)

Dans le catalogue des formalisations Lean du dépôt, quand nous avons regardé, le 27 octobre 2026, le champ *review* (examen) de cette formalisation indiquait `unchecked` (« non vérifié »). Nous n'avons vu dans le dépôt aucun verdict consigné de l'outil de vérification. Cela ne veut pas dire qu'aucune vérification n'a été faite, seulement que nous n'en avons trouvé aucune consignée là.

## Nos propres niveaux, appliqués à ce cas

Le projet derrière ce dépôt donne un niveau à chaque affirmation (voir [Elenchus en dix minutes](elenchus-in-10-minutes.fr.md)) : **A**, « le juge a regardé » ; **L**, « c'est écrit dans un livre sérieux » ; **C**, « quelqu'un a raisonné, personne n'a vérifié à la machine » ; **X**, « une esquisse au crayon ». Le tableau est une **illustration, pas une note attribuée au travail d'OpenAI** : il dit seulement ce que *nous* pouvons voir.

| Étage | Où il en est, autant que nous puissions le voir |
|---|---|
| L'énoncé formel, vérifié par une machine | OpenAI dit qu'il a été vérifié en Lean. Nous n'avons pas vu de verdict consigné, et nous n'en avons pas produit. **Inconnu pour nous** ; nous ne pouvons pas écrire « A ». |
| L'énoncé formel dit-il ce que dit l'article ? | Une question humaine (question 2). **En attente.** |
| Examen par des experts humains | Annoncé, au futur (question 4). **En attente.** |
| Effet pratique | Notre calcul grossier (question 5) : **aucun pour les logiciels d'aujourd'hui**. Ce chiffre est le nôtre et n'est que de niveau **X**. |

## La liste du lecteur

1. Qu'est-ce qui est affirmé exactement, dans les mots des auteurs ?
2. Qui l'a vérifié : une machine, une personne, ou les deux ?
3. Quel vérificateur, lancé par qui, et où sa réponse est-elle consignée ?
4. Ai-je vu l'énoncé formel, ou seulement un titre à son sujet ?
5. Les définitions veulent-elles dire ce que les mots suggèrent, ou l'une d'elles pourrait-elle être vide ou inhabituelle ?
6. Une convention (comme « non défini vaut 0 ») pourrait-elle la rendre vraie pour une mauvaise raison ?
7. Sur quels axiomes et quelles bibliothèques repose-t-elle, et a-t-elle été relue (*replay*) ?
8. Un expert l'a-t-il examinée, ou est-ce encore à venir ?
9. Qu'est-ce que cela changerait en pratique, pour qui, et à partir de quelle taille ?
10. Qu'est-ce qui reste en attente, et quand en saura-t-on plus ?

## Ce que cette page ne fait pas

- Elle ne dit pas si l'affirmation d'OpenAI est juste ou fausse.
- Elle ne dit pas si OpenAI a raison ou tort de publier de cette façon.
- Elle ne cite ni ne nomme aucun critique.
- Le mérite des résultats revient à leurs auteurs et aux groupes qui les examinent. Nous ne faisons pas la course avec ces groupes.

## Pourquoi cela nous importe

Les cinq mêmes questions s'appliquent à notre propre travail. Nos résultats ont eux aussi été produits par des agents d'IA et audités par des agents d'IA, et **aucun mathématicien humain ne les a examinés**. Vous trouverez les affirmations que nous avons retirées dans [nos erreurs](what-we-got-wrong.fr.md), et vous pouvez tester notre travail avec [vérifier par vous-même](check-it-yourself.fr.md). Posez-nous aussi ces cinq questions, s'il vous plaît.
