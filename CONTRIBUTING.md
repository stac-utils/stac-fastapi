# Contributing

Issues and pull requests are more than welcome.

**dev install**

```bash
$ git clone https://github.com/stac-utils/stac-fastapi.git
$ cd stac-fastapi
$ pip install -e stac_fastapi/api[dev]
```

**Python3.8 only**

This repo is set to use `pre-commit` to run *isort*, *flake8*, *pydocstring*, *black* ("uncompromising Python code formatter") and mypy when committing new code.

```bash
$ pre-commit install
```

### Docs

```bash
$ git clone https://github.com/stac-utils/stac-fastapi.git
$ cd stac-fastapi
$ pip install -e stac_fastapi/api["docs"]
```

Hot-reloading docs:

```bash
$ mkdocs serve
```

To manually deploy docs (note you should never need to do this because GitHub
Actions deploys automatically for new commits.):

```bash
Create API documentations
$ pdocs as_markdown \
  --output_dir docs/api/ \
  --exclude_source \
  --overwrite \
  stac_fastapi

# deploy
$ mkdocs gh-deploy
```
