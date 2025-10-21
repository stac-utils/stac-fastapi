# Contributing

Issues and pull requests are more than welcome.

We recommand using [`uv`](https://docs.astral.sh/uv) as project manager for development.

See https://docs.astral.sh/uv/getting-started/installation/ for installation 

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
uv run --group docs mkdocs build -f docs/mkdocs.yml
```

Hot-reloading docs:

```bash
uv run --group docs mkdocs serve -f docs/mkdocs.yml --livereload
```

To manually deploy docs (note you should never need to do this because GitHub
Actions deploys automatically for new commits.):

```bash
# deploy
uv run --group docs mkdocs gh-deploy -f docs/mkdocs.yml
```
