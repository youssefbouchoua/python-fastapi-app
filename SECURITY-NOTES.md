
# TP 7 – Sécurité des actions tierces

## Q3. Pourquoi faut-il épingler une version (@v4) plutôt que @main ?

Il est préférable d'utiliser @v4 pour avoir une version plus stable et limiter les changements imprévus. La branche @main peut être modifiée à tout moment.

Pour plus de sécurité en production, on peut utiliser le SHA complet d'un commit.

## Q4. Le badge « créateur vérifié » garantit-il qu'une action est sûre ?

Non. Le badge confirme l'identité du créateur, mais ne garantit pas que son code est totalement sécurisé.

Il faut également vérifier le code source, les dépendances et les mises à jour de l'action.

## Q5. Citez deux vérifications à faire avant d'utiliser une action d'un fournisseur inconnu.

1. Vérifier le code source pour détecter les comportements suspects et les accès aux données sensibles.
2. Vérifier les mises à jour, les dépendances et les éventuelles failles de sécurité.
