
<p align="center">
  <p align="center">sta.</p>
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


---

**Documentation**: [https://stac-utils.github.io/stac-fastapi/](https://stac-utils.github.io/stac-fastapi/)

**Source Code**: [https://github.com/stac-utils/stac-fastapi](https://github.com/stac-utils/stac-fastapi)

---

Python library for building a STAC compliant FastAPI application.  The project is split up into several namespace
packages:
- **stac_fastapi.api**: An API layer which enforces the [stac-api-spec](https://github.com/radiantearth/stac-api-spec).
- **stac_fastapi.extensions**: Abstract base classes for [STAC API extensions](https://github.com/radiantearth/stac-api-spec/blob/master/extensions.md) and third-party extensions.
- **stac_fastapi.server**: Standalone FastAPI server for the application.
- **stac_fastapi.sqlalchemy**: Postgres backend implementation with sqlalchemy.
- **stac_fastapi.types**: Shared types and abstract base classes used by the library.

Initially developed by [arturo-ai](https://github.com/arturo-ai).

```
pip install stac-fastapi
```

## Local Development
Use docker-compose to deploy the application, migrate the database, and ingest some example data:
```bash
docker-compose build
docker-compose up
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
