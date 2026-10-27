# Vérifier par vous-même

[English version](check-it-yourself.md)

Vous ne devriez pas avoir à nous croire sur parole. Voici comment vérifier le travail, de la vérification en cinq minutes à la reprise complète, et comment contester un résultat.

## 1. Est-ce bien le livre publié ? (deux minutes)

Chaque PDF de [`books/`](../books/) doit être exactement le fichier publié sur Zenodo. Calculez son empreinte :

```bash
md5sum books/discovery-journal-2026-fr.pdf books/discovery-journal-2026-en.pdf
```

Comparez-la ensuite à la somme de contrôle affichée dans la liste des fichiers de la notice Zenodo ([français](https://doi.org/10.5281/zenodo.23669395), [anglais](https://doi.org/10.5281/zenodo.23669463)). À la préparation de ce dépôt, on obtenait `04d2e91cc117c16fecdb255366200164` (français) et `a2b0758673d537056a8e77f4a5bfc89d` (anglais).

## 2. Télécharger le dossier complet d'un article (dix minutes)

Chacun des 24 articles de [`elenchus/REGISTRY.md`](../elenchus/REGISTRY.md) a une notice Zenodo. Elle contient le PDF et, pour la plupart des articles, les sources, les données, les scripts et un manifeste des sommes de contrôle. Téléchargez la notice depuis son DOI et lisez ses instructions de reproduction.

## 3. Lancer les contrôles de ce dépôt (quelques minutes ; Python 3 suffit)

```bash
# Tout sauf le contrôle en ligne sur Zenodo
python3 elenchus/tools/check_consistency.py --offline

# Avec le contrôle Zenodo (il faut Internet)
python3 elenchus/tools/check_consistency.py
```

Le script écrit [`elenchus/CONSISTENCY_REPORT.md`](../elenchus/CONSISTENCY_REPORT.md). Il :
- passe les 17 registres d'affirmations au vérificateur de registres Elenchus, en recalculant l'empreinte de chaque fichier de preuve ;
- recalcule l'empreinte des 360 fichiers Lean copiés et la compare à celle notée au moment où les affirmations ont été déposées ;
- cherche dans les fichiers Lean les moyens connus de tromper le vérificateur ;
- liste les modules qui figurent dans le relevé de relecture par le noyau ;
- contrôle chaque DOI sur Zenodo.

**Ce que nous avons obtenu le 27 octobre 2026 :** code de sortie 0 lors des premiers passages, avec 24 DOI sur 24 qui répondent et des titres concordants. Au dernier passage, celui dont le rapport est enregistré ici, le serveur de Zenodo a répondu « 504 Gateway Time-out » pour 3 notices, et le script s’est terminé avec le code 1 : il signale correctement un contrôle qu’il n’a pas pu mener à bout. Si cela vous arrive, relancez-le plus tard. Les 17 registres ont 0 problème bloquant et 154 signaux « niveau A non audité ». Aucun fichier Lean ne diffère. La recherche de contournements ne trouve rien d'inexpliqué. Les 93 modules relus ont tous le code de retour 0.

**Un contrôle négatif à essayer.** Changez un caractère dans n'importe quel fichier de `elenchus/discoveries/*/ledger/evidence/` et relancez le contrôle. Il doit se terminer avec le code 1 et nommer l'affirmation dont la preuve ne correspond plus. (Nous l'avons fait avec un fichier de `ar_yukawa_crystal`, et c'est ce qui s'est passé.) Restaurez ensuite le fichier, par exemple avec `git checkout -- elenchus/`.

Pour lancer le vérificateur de registres seul sur un article, voir [`elenchus/tool/README.md`](../elenchus/tool/README.md) (en anglais).

**Ce que ces contrôles ne prouvent pas.** Ils vérifient la tenue des comptes et l'intégrité : que les fichiers sont bien les fichiers, et que les registres sont cohérents. Ils ne relancent pas Lean, et ils ne disent rien de la vérité d'un énoncé.

## 4. Relancer le vérificateur de preuves (des heures, et plusieurs gigaoctets)

C'est le vrai test, et il est lourd. La recette utilisée pour la relecture par le noyau du 26 octobre 2026 est dans [`elenchus/kernel_replay_2026-10-26/REPLAY.md`](../elenchus/kernel_replay_2026-10-26/REPLAY.md). En résumé :

1. Installer la version de Lean indiquée (Lean 4.34.1).
2. Récupérer les projets amont aux versions listées dans le `LEAN.md` de chaque article : Mathlib, et `openai/math` d'OpenAI pour les résultats qui s'appuient dessus. Ils ne sont pas copiés ici.
3. Compiler les modules de `elenchus/discoveries/<article>/lean/`.
4. Pour chaque théorème revendiqué, lancer `#print axioms`. La réponse ne doit contenir que `propext`, `Classical.choice` et `Quot.sound`. Un `sorryAx`, ou tout autre axiome, fait échouer l'affirmation.
5. Lancer `leanchecker <Module>` pour faire relire par le noyau les déclarations enregistrées. Le code de retour 0 signifie que le test est passé.
6. Chercher dans les sources `sorry`, `axiom`, `debug.skipKernelTC`, `addDecl`, `native_decide`, `implemented_by` et `#exit`. Une occurrence hors d'un fichier de contrôle planté doit être expliquée.

**Essayez aussi les contrôles.** Ajoutez `sorry` dans une preuve, ou une ligne `axiom cheat : False`, et vérifiez que l'étape 4 les attrape. Un contrôle qui ne peut pas échouer ne vaut rien.

Nous n'avons pas relancé Lean pour ce dépôt. Les chiffres de la section 3 viennent des contrôles ci-dessus, et ceux de la relecture viennent du relevé du 26 octobre.

## 5. Lire les énoncés (l'étape que personne n'a encore faite)

Un résultat de niveau A signifie que le vérificateur a accepté une preuve de l'*énoncé formel*. Pour aucun résultat présenté ici, **une personne n'a vérifié** que l'énoncé formel dit ce que dit sa description en langage courant. Chaque registre le signale avec `LEDGER_UNAUDITED_TIER_A`. Si vous lisez le Lean, c'est le contrôle le plus utile que vous puissiez faire : prenez une ligne de niveau A d'un `ledger.json`, trouvez le théorème dans les fichiers Lean, et demandez-vous s'il dit vraiment ce que la ligne affirme.

## 6. Contester un résultat

[Ouvrez un ticket](../CONTRIBUTING.md), s'il vous plaît. Les tickets « red team » sont les bienvenus : ils soutiennent que quelque chose est faux, exagéré ou mal étiqueté. Une contestation utile indique :
- l'affirmation visée (le DOI, et l'identifiant de la ligne du registre s'il existe, par exemple `YK-A-0001`) ;
- ce qui vous paraît faux ;
- comment vous avez vérifié : ce que vous avez lancé, ce que vous avez lu et ce que vous avez obtenu.

L'intention est qu'une contestation fondée soit reconnue et que sa correction soit publiée, comme les corrections précédentes ([nos erreurs](what-we-got-wrong.fr.md)).
