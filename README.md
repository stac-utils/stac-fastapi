<p align="center">
  <img src="https://github.com/radiantearth/stac-site/raw/master/images/logo/stac-030-long.png" width=400>
  <p align="center">FastAPI implemention of the STAC API spec.</p>
</p>
<p align="center">
  <a href="https://github.com/stac-utils/stac-fastapi/actions?query=workflow%3Acicd" target="_blank">
      <img src="https://github.com/stac-utils/stac-fastapi/workflows/stac-fastapi/badge.svg" alt="Test">
  </a>
  <a href="https://pypi.org/project/stac-fastapi" target="_blank">
      <img src="https://img.shields.io/pypi/v/stac-fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/stac-utils/stac-fastapi/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/stac-fastapi.svg" alt="Downloads">
  </a>
</p>

---

**Documentation**: [https://stac-utils.github.io/stac-fastapi/](https://stac-utils.github.io/stac-fastapi/)

**Source Code**: [https://github.com/stac-utils/stac-fastapi](https://github.com/stac-utils/stac-fastapi)

---

Python library for building a STAC compliant FastAPI application.  The project is split up into several namespace
packages:

- **stac_fastapi.api**: An API layer which enforces the [stac-api-spec](https://github.com/radiantearth/stac-api-spec).
- **stac_fastapi.extensions**: Abstract base classes for [STAC API extensions](https://github.com/radiantearth/stac-api-spec/blob/master/extensions.md) and third-party extensions.
- **stac_fastapi.types**: Shared types and abstract base classes used by the library.

#### Backends
- **stac_fastapi.sqlalchemy**: Postgres backend implementation with sqlalchemy.
- **stac_fastapi.pgstac**: Postgres backend implementation with [PGStac](https://github.com/stac-utils/pgstac).

`stac-fastapi` was initially developed by [arturo-ai](https://github.com/arturo-ai).

## Installation

```bash
pip install stac-fastapi

# or from sources

git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
pip install -e \
    stac_fastapi/api \
    stac_fastapi/types \
    stac_fastapi/extensions

# Install a backend
pip install -e stac_fastapi/sqlalchemy
# or
pip install -e stac_fastapi/pgstac
```

## Local Development
Use docker-compose to deploy the application, migrate the database, and ingest some example data:
```bash
docker-compose build
docker-compose up

# You can also launch application with specific backend (PGSTac or sqlalchemy)
docker-compose up app-sqlalchemy
# or
docker-compose up app-pgstac
```

For local development it is often more convenient to run the application outside of docker-compose:
```bash
make docker-run
```

### Testing
The database container provided by the docker-compose stack must be running.  Run all tests:
```bash
make test
```

Run individual tests by running pytest within the docker container:
```bash
make docker-shell
$ pytest -v
```
