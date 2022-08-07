<p align="center">
  <img src="https://github.com/radiantearth/stac-site/raw/master/images/logo/stac-030-long.png" width=400>
  <p align="center">FastAPI implemention of the STAC API spec.</p>
</p>
<p align="center">
  <a href="https://github.com/stac-utils/stac-fastapi/actions?query=workflow%3Acicd" target="_blank">
      <img src="https://github.com/stac-utils/stac-fastapi/workflows/stac-fastapi/badge.svg" alt="Test">
  </a>
  <a href="https://pypi.org/project/stac-fastapi" target="_blank">
      <img src="https://img.shields.io/pypi/v/stac-fastapi.api?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/stac-utils/stac-fastapi/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/stac-fastapi.svg" alt="License">
  </a>
</p>

---

**Documentation**: [https://stac-utils.github.io/stac-fastapi/](https://stac-utils.github.io/stac-fastapi/)

**Source Code**: [https://github.com/stac-utils/stac-fastapi](https://github.com/stac-utils/stac-fastapi)

---

Python library for building a STAC compliant FastAPI application. This package provides the generic API layer and tools for an API compliant with the STAC API spec, but developers will need to install a database backend package as well in order to deploy a working API. This package includes the following modules:

- **stac_fastapi.api**: An API layer which enforces the [stac-api-spec](https://github.com/radiantearth/stac-api-spec).
- **stac_fastapi.extensions**: Abstract base classes for [STAC API extensions](https://github.com/radiantearth/stac-api-spec/blob/master/extensions.md) and third-party extensions.
- **stac_fastapi.types**: Shared types and abstract base classes used by the library.

Some `stac-fastapi` backends managed within the `stac-utils` organization include:

- [**stac-fastapi.pgstac**](https://github.com/stac-utils/stac-fastapi-pgstac): A PostgreSQL/PostGIS backend implemented
  using [PgSTAC](https://github.com/stac-utils/pgstac).
- [**stac-fastapi.sqlalchemy**](https://github.com/stac-utils/stac-fastapi-sqlalchemy): A PostgreSQL/PostGIS backend implemented using [SQLAlchemy](https://www.sqlalchemy.org/).
- [**stac-fastapi.elasticsearch](https://github.com/stac-utils/stac-fastapi-elasticsearch): An [Elasticsearch](https://www.elastic.co/) backend. *Note that this backend does not have any production deployments as of 2022-08-07.*

`stac-fastapi` was initially developed by [arturo-ai](https://github.com/arturo-ai).

## Installation

**Install from PyPi**

```bash
# Install from pypi.org
pip install stac-fastapi
```

**Install from Source**

```bash
#/////////////////////
# Install from sources

git clone https://github.com/stac-utils/stac-fastapi.git && cd stac-fastapi
pip install -e .
```

**Pre-v2.5.0**

Prior to v2.5.0 the `stac-fastapi.api`, `stac-fastapi.types`, and `stac-fastapi.extensions` modules were distributed
as separate packages in subdirectories of this repo. To install a version earlier that v2.5.0 you will need to install
each package separately:

```bash
# For v2.4.1...
pip install stac-fastapi.api==2.4.1
pip install stac-fastapi.types==2.4.1
pip install stac-fastapi.extensions==2.4.1
```

## Local Development

Developing the API locally requires that you install a backend package (e.g. `stac-fastapi.pgstac`) in addition to
this package. You can, however, run tests and linters and generate the docs without installing an additional
backend package.

### Install Development Environment

```bash
git clone https://github.com/stac-utils/stac-fastapi.git && cd stac-fastapi
pip install -e ".[dev]"
```

### Testing

To run tests for both the pgstac and sqlalchemy backends, execute:

```shell
make test
```

### Linting and Code Checking

This project uses the following libraries for code checking:

- [black](https://github.com/psf/black) for Python code formatting
- [isort](https://github.com/PyCQA/isort) for consistent sorting of import statements
- [flake8](https://github.com/pycqa/flake8) for Python style checks
- [pydocstyle](https://github.com/PyCQA/pydocstyle) for checking compliance with Python docstring conventions

Run the linters using `pre-commit`:

```bash
pre-commit run --all
```
