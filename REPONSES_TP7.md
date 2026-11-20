
---

# TP 7 – Actions tierces et actions personnalisées

## Q1. Pourquoi actions/checkout n'a-t-il pas besoin de with alors que setup-node en a besoin ?

actions/checkout utilise ses paramètres par défaut pour récupérer le code du dépôt.

Pour setup-node, nous utilisons with afin de préciser la version de Node.js souhaitée (version 20).

## Q2. Pourquoi le job verify ne retrouve-t-il pas report.txt sans l'artefact ?

Les jobs build et verify s'exécutent dans des environnements séparés.

Le fichier report.txt créé dans build n'est pas automatiquement disponible dans verify. L'artefact permet de transférer ce fichier entre les deux jobs.

## Q6. Pourquoi actions/checkout doit-il s'exécuter avant l'appel d'une action locale ?

actions/checkout récupère les fichiers du dépôt sur la machine GitHub Actions.

L'action locale se trouve dans le dépôt. Il faut donc récupérer ces fichiers avant de pouvoir l'exécuter.

## Q7. Pourquoi shell: bash est-il obligatoire dans une action composite ?

Dans une action composite, les steps qui utilisent run doivent préciser le shell utilisé.

shell: bash indique que les commandes doivent être exécutées avec Bash.
