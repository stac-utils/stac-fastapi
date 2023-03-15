<!-- markdownlint-disable MD033 MD041 -->

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
  <a href="https://github.com/stac-utils/stac-fastapi/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/stac-fastapi.svg" alt="License">
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
# Install from pypi.org
pip install stac-fastapi.api stac-fastapi.types stac-fastapi.extensions

# Install a backend of your choice
pip install stac-fastapi.sqlalchemy
# or
pip install stac-fastapi.pgstac

#/////////////////////
# Install from sources

git clone https://github.com/stac-utils/stac-fastapi.git && cd stac-fastapi
pip install \
  -e stac_fastapi/api \
  -e stac_fastapi/types \
  -e stac_fastapi/extensions

# Install a backend of your choice
pip install -e stac_fastapi/sqlalchemy
# or
pip install -e stac_fastapi/pgstac
```

### Pre-built Docker images

Pre-built images are available from the [Github Container Registry](https://github.com/stac-utils/stac-fastapi/pkgs/container/stac-fastapi).
The latest images are tagged with `main-pgstac` and `main-sqlalchemy`.
To pull the image to your local system:

```shell
docker pull ghcr.io/stac-utils/stac-fastapi:main-pgstac  # or main-sqlalchemy
```

This repository provides two example [Docker compose](https://docs.docker.com/compose/) files that demonstrate how you might link the pre-built images with a postgres/pgstac database:

- [docker-compose.pgstac.yml](./docker/docker-compose.pgstac.yml)
- [docker-compose.sqlalchemy.yml](./docker/docker-compose.sqlalchemy.yml)

## Local Development

Use docker-compose via make to start the application, migrate the database, and ingest some example data:

```bash
make image
make docker-run-all
```

- The SQLAlchemy backend app will be available on <http://localhost:8081>.
- The PGStac backend app will be available on <http://localhost:8082>.

You can also launch only one of the applications with either of these commands:

```shell
make docker-run-pgstac
make docker-run-sqlalchemy
```

The application will be started on <http://localhost:8080>.

By default, the apps are run with uvicorn hot-reloading enabled. This can be turned off by changing the value
of the `RELOAD` env var in docker-compose.yml to `false`.

### nginx proxy

This repo includes an example nginx proxy service.
To start:

```shell
make docker-run-nginx-proxy
```

The proxy will be started on <http://localhost>, with the pgstac app available at <http://localhost/api/v1/pgstac/> and the sqlalchemy app at <http://localhost/api/v1/sqlalchemy/>.
If you need to customize the proxy port, use the `STAC_FASTAPI_NGINX_PORT` environment variable:

```shell
STAC_FASTAPI_NGINX_PORT=7822 make docker-run-nginx-proxy
```

### Note to Docker for Windows users

You'll need to enable experimental features on Docker for Windows in order to run the docker-compose,
due to the "--platform" flag that is required to allow the project to run on some Apple architectures.
To do this, open Docker Desktop, go to settings, select "Docker Engine", and modify the configuration
JSON to have `"experimental": true`.

### Testing

Before running the tests, ensure the database and apps run with docker-compose are down:

```shell
docker-compose down
```

The database container provided by the docker-compose stack must be running. This can be started with:

```shell
make run-database
```

To run tests for both the pgstac and sqlalchemy backends, execute:

```shell
make test
```

To only run pgstac backend tests:

```shell
make test-pgstac
```

To only run sqlalchemy backend tests:

```shell
make test-sqlalchemy
```

Run individual tests by running pytest within a docker container:

```shell
make docker-shell-pgstac # or docker-shell-sqlalchemy
$ pip install -e stac_fastapi/pgstac[dev]
$ pytest -v stac_fastapi/pgstac/tests/api/test_api.py 
```
