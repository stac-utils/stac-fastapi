# Contributing

Issues and pull requests are more than welcome.

**dev install**

```bash
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
python -m pip install -e stac_fastapi/api[dev]
```

**pre-commit**

This repo is set to use `pre-commit` to run *ruff*, *pydocstring* and mypy when committing new code.

```bash
pre-commit install
```

### Docs

```bash
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
python pip install -e stac_fastapi/api["docs"]
```

Hot-reloading docs:

```bash
$ mkdocs serve -f docs/mkdocs.yml
```

To manually deploy docs (note you should never need to do this because GitHub
Actions deploys automatically for new commits.):

```bash
Create API documentations
$ pdocs as_markdown \
  --output_dir docs/src/api/ \
  --exclude_source \
  --overwrite \
  stac_fastapi

# deploy
$ mkdocs gh-deploy -f docs/mkdocs.yml
```
