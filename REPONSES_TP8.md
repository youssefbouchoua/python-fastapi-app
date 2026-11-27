# TP 8 – Stratégies GitHub Actions

## Q1. Combien de jobs sont générés ? Donnez la liste des combinaisons.
**6 jobs** sont générés ($2 \text{ OS} \times 3 \text{ versions de Python}$) :
- `(ubuntu-latest, 3.11)`
- `(ubuntu-latest, 3.12)`
- `(ubuntu-latest, 3.13)`
- `(windows-latest, 3.11)`
- `(windows-latest, 3.12)`
- `(windows-latest, 3.13)`

## Q2. Combien de jobs au total après `exclude` et `include` ?
Il y a toujours **6 jobs** au total :
- 6 combinaisons de base
- `- 1` combinaison supprimée par `exclude` : `(windows-latest, 3.11)`
- `+ 1` combinaison ajoutée par `include` : `(ubuntu-latest, 3.14, experimental: true)`

## Q3. Que se passerait-il si vous tentiez d'exclure la combinaison `3.14` ? Pourquoi ?
La combinaison `3.14` **ne serait pas exclue** et continuerait de s'exécuter. GitHub Actions évalue toujours `exclude` **avant** `include` : au moment où `exclude` est appliqué, la combinaison `(ubuntu-latest, 3.14)` n'existe pas encore dans la matrice de base ; elle est ajoutée ensuite par `include`.

## Q4. Quelle est la différence observée entre `fail-fast: true` et `fail-fast: false` ? Dans quel cas choisir l'un ou l'autre ?
- **Avec `fail-fast: true` (défaut) :** 4 jobs réussis (Ubuntu 3.11 à 3.14), 1 job échoué (`windows-latest, 3.12`) et **1 job annulé** (`windows-latest, 3.13`), interrompu dès le premier échec.
- **Avec `fail-fast: false` :** 4 jobs réussis (Ubuntu), **2 jobs échoués** (`windows-latest, 3.12` et `3.13`) et **0 job annulé** ; tous les jobs vont jusqu'au bout.
- **Quand choisir `true` :** sur les Pull Requests et le développement quotidien, pour obtenir un feedback rapide et économiser des minutes de runners dès qu'une erreur apparaît.
- **Quand choisir `false` :** lors des tests de compatibilité multi-plateformes ou avant une release, pour disposer d'un diagnostic complet et savoir exactement quelles combinaisons échouent.

## Q5. Donnez deux raisons d'utiliser `max-parallel` en entreprise.
1. **Préserver la capacité des runners partagés :** éviter qu'un seul workflow avec une grande matrice ne sature les runners auto-hébergés (*self-hosted*) ou le quota de jobs simultanés de l'organisation, ce qui bloquerait les pipelines des autres équipes.
2. **Protéger des ressources externes partagées :** limiter la charge simultanée sur une base de données de test, un environnement de staging ou une API tierce soumise à du *rate limiting*.