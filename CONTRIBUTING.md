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

# If needed, you can run pre-commit script manually 
uv run pre-commit run --all-files 
```

### Docs

```bash
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
# Build docs
uvx --with-requirements requirements/requirements-docs.txt mkdocs build -f docs/mkdocs.yml
```

Hot-reloading docs:

```bash
uvx --with-requirements requirements/requirements-docs.txt mkdocs serve -f docs/mkdocs.yml --livereload
```

To manually deploy docs (note you should never need to do this because GitHub
Actions deploys automatically for new commits.):

```bash
# deploy
uvx --with-requirements requirements/requirements-docs.txt mkdocs gh-deploy -f docs/mkdocs.yml
```
