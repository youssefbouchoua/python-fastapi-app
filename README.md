# FastAPI Starter

A minimal, production‑leaning FastAPI template with testing (coverage), linting/formatting, Docker, and CI. Ships with a root endpoint and a health check.

## Features
- FastAPI + Uvicorn
- Pydantic Settings for configuration management
- Custom logging with TRACE level support
- Testing with pytest + pytest-cov (HTML/XML coverage, 85% threshold)
- Ruff for linting and formatting; optional mypy typing
- Dockerfile and GitHub Actions CI (Python 3.13)

## Endpoints
- `GET /` → `{ "message": "the server is now active" }`
- `GET /health` → `{ "ok": true }`

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env  # Optional: customize your environment variables
uvicorn app.main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000) and [http://localhost:8000/health](http://localhost:8000/health)

## Testing with Coverage

```bash
pytest
# Outputs: htmlcov/ (HTML), coverage.xml (XML), threshold enforced via pyproject.toml
```

## Linting and Formatting

```bash
ruff check .
ruff format .
# Optional typing
mypy app
```

## Docker

```bash
docker build -t fastapi-starter .
docker run -p 8000:8000 fastapi-starter
```

## CI

GitHub Actions workflow runs linting and tests with coverage on Python 3.13. See `.github/workflows/ci.yml`.

## License

MIT. See [LICENSE](./LICENSE).


## TP5 – GitHub Actions CI : Questions et réponses

### Q0. Préparation du dépôt
**Réponse :** Le dépôt a été forké et cloné, puis la branche `feature/tp-ci` a été créée. Le code se trouve dans `app/`, les tests dans `tests/` et les dépendances de développement dans `requirements-dev.txt`. Le projet a été vérifié avec Ruff et Pytest.

### Q1. Configuration des filtres
**Réponse :** Le workflow se déclenche sur les push vers `main` ou `feature/**`, uniquement si des fichiers de `app/**` ou `tests/**` sont modifiés. Pour les Pull Requests, les événements sont `opened` et `synchronize`.

### Q2. Test des filtres
**Réponse :** Une modification de `README.md` seule ne déclenche pas le workflow filtré sur les push, car ce fichier n'est pas inclus dans `paths`. Une modification dans `app/` déclenche le workflow sur une branche autorisée.

### Q3. Logique des filtres
**Réponse :** Entre `branches` et `paths`, la logique est ET. Entre les types d'activité, la logique est OU.

### Q4. Déclenchement par tags
**Réponse :** Le workflow `tag.yml` utilise `tags: ['v*']`. Il se déclenche lorsqu'un tag commençant par `v`, comme `v1.0.0`, est poussé vers GitHub.

### Q5. Configuration des jobs
**Réponse :** Trois jobs ont été configurés : `lint` avec Ruff, `build` pour vérifier l'application et `test` avec Pytest. `lint` et `build` s'exécutent en parallèle, puis `test` démarre après leur réussite.

### Q6. Utilisation de needs
**Réponse :** Sans `needs`, les trois jobs peuvent s'exécuter en parallèle, ce qui peut réduire la durée totale. Avec `needs: [lint, build]`, le job `test` attend leur réussite. Lorsqu'une erreur Ruff a été introduite, `test` a été ignoré.

### Q7. Isolation des jobs
**Réponse :** Chaque job s'exécute sur un runner indépendant. Il faut donc refaire `actions/checkout` pour récupérer le code et `actions/setup-python` pour configurer Python dans le job `test`.

### Q8. Utilisation des contextes
**Réponse :** Le nom de l'application utilise `env.APP_NAME`, l'acteur `github.actor`, l'événement `github.event_name`, la branche `github.ref_name`, le SHA `github.sha` et le système du runner `runner.os`.

### Q9. Contextes d'une Pull Request
**Réponse :** Lors d'un push, `github.event_name` vaut `push`, tandis que `github.head_ref` et `github.base_ref` sont vides. Lors d'une Pull Request, `github.event_name` vaut `pull_request`, `github.head_ref` indique `feature/tp-ci` et `github.base_ref` indique `main`.

### Q10. Affichage du contexte GitHub en JSON
**Réponse :** L'expression `toJson(github)` permet d'afficher le contexte GitHub au format JSON. Pour un événement push, le message du commit se trouve dans `github.event.head_commit.message`.

### Lien d'exécution du pipeline CI

Lien du run complet avec succès : [https://github.com/youssefbouchoua/python-fastapi-app/actions/runs/42307087869]



