
# TP 6 – Variables d'environnement, Inputs et Outputs

## Q1. Pourquoi la variable n'est-elle disponible que dans les steps suivantes ?

GITHUB_ENV permet de partager des variables entre les steps d'un même job. La variable devient disponible dans les steps suivantes, mais pas dans la step qui l'a définie.

## Q2. Quelle est la portée de GITHUB_ENV ?

La variable APP_NAME définie dans le job build n'est pas disponible dans le job verify-env.

GITHUB_ENV fonctionne uniquement entre les steps d'un même job. Chaque job possède son propre environnement.

## Q3. Que se passe-t-il si on utilise > au lieu de >> dans GITHUB_OUTPUT ?

Le symbole > remplace le contenu du fichier, tandis que >> ajoute une nouvelle ligne.

Si deux outputs sont écrits avec >, le deuxième peut écraser le premier.

## Q4. Pourquoi GITHUB_ENV ne suffit-il pas entre deux jobs ?

GITHUB_ENV permet de partager des variables uniquement dans un même job.

Pour transmettre une valeur entre deux jobs, on utilise GITHUB_OUTPUT, les outputs du job et needs.

## Q5. Que se passe-t-il si on retire needs: build du job deploy ?

Le job deploy ne dépend plus du job build.

Il peut s'exécuter avant ou en même temps que build. De plus, il ne peut plus accéder à la version avec needs.build.outputs.full_version.
