# Contributing

Issues and pull requests are more than welcome.

**dev install**

```bash
$ git clone https://github.com/arturo-ai/arturo-stac-api.git
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
$ git clone https://github.com/arturo-ai/arturo-stac-api.git
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
$ mkdocs gh-deploy
```
