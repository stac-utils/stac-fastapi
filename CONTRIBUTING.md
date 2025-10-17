# Contributing

Issues and pull requests are more than welcome.

**dev install**

```bash
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
uv sync --dev
```

**pre-commit**

This repo is set to use `pre-commit` to run *ruff*, *pydocstring* and mypy when committing new code.

```bash
uv run pre-commit install 
```

### Docs

```bash
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
uv pip instal -r requirements/requirements-docs.txt
```

Hot-reloading docs:

```bash
uv run mkdocs serve -f docs/mkdocs.yml
```

To manually deploy docs (note you should never need to do this because GitHub
Actions deploys automatically for new commits.):

```bash
# deploy
uv run mkdocs gh-deploy -f docs/mkdocs.yml
```
