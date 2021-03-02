# Contributing

Issues and pull requests are more than welcome.

**dev install**

```bash
$ git clone https://github.com/stac-utils/arturo-stac-api.git
$ cd arturo-stac-api
$ pip install -e .[dev]
```

**Python3.8 only**

This repo is set to use `pre-commit` to run *isort*, *flake8*, *pydocstring*, *black* ("uncompromising Python code formatter") and mypy when committing new code.

```bash
$ pre-commit install
```

### Docs

```bash
$ git clone https://github.com/stac-utils/arturo-stac-api.git
$ cd arturo-stac-api
$ pip install -e .["docs"]
```

Hot-reloading docs:

```bash
$ mkdocs serve
```

To manually deploy docs (note you should never need to do this because Github
Actions deploys automatically for new commits.):

```bash
Create API documentations
$ pdocs as_markdown \
  --output_dir docs/api/ \
  --exclude_source \
  --overwrite \
  stac_api.errors \
  stac_api.config \
  stac_api.models.database \
  stac_api.models.decompose \
  stac_api.models.links \
  stac_api.models.ogc \
  stac_api.models.schemas \
  stac_api.api.routes \
  stac_api.api.models \
  stac_api.api.app

# deploy
$ mkdocs gh-deploy
```
