
<p align="center">
  <p align="center">Arturo's STAC compliant API implementation.</p>
</p>

<p align="center">
  <a href="https://github.com/arturo-ai/arturo-stac-api/actions?query=workflow%3Acicd" target="_blank">
      <img src="https://github.com/arturo-ai/arturo-stac-api/workflows/arturo-stac-api/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/arturo-ai/arturo-stac-api" target="_blank">
      <img src="https://codecov.io/gh/arturo-ai/arturo-stac-api/branch/master/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/arturo-stac-api" target="_blank">
      <img src="https://img.shields.io/pypi/v/arturo-stac-api?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/arturo-ai/arturo-stac-api/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/arturo-ai/arturo-stac-api.svg" alt="Downloads">
  </a>
</p>

---


---

**Documentation**: coming soon...

**Source Code**: [https://github.com/arturo-ai/arturo-stac-api](https://github.com/arturo-ai/arturo-stac-api)

---

Python library for building a STAC compliant FastAPI application.  It provides:
- An API layer which enforces the [stac-api spec](https://github.com/radiantearth/stac-api-spec) and allows users
to customize how the API interacts with their data through dependency injection.
- A PostGIS implementation using [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)/[geoalchemy2](https://geoalchemy-2.readthedocs.io/en/latest/).

```
pip install arturo-stac-api
```

## Usage
```python
from stac_api.api.app import StacApi
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.session import Session
from stac_api.config import ApiSettings

settings = ApiSettings()
session = Session(settings.reader_connection_string, settings.writer_connection_string)
api = StacApi(
    settings=settings,
    client=CoreCrudClient(
        session=Session(settings.reader_connection_string, settings.writer_connection_string)
    ),
)

# FastAPI application
app = api.app
```

## Project Structure
```
.
├── alembic             # Database migrations
│   └── versions        # Migration versions
├── scripts             # Scripts for local development
├── stac_api
│   ├── api             # API layer
│   ├── clients
│   │   ├── postgres    # Postgres CRUD client
│   │   └── tiles       # OGC Tiles API client
│   ├── models          # Pydantic and ORM models
│   └── utils           # Helper functions
└── tests
    ├── api             # Test api creation
    ├── clients         # Test application logic
    └── resources       # Test api endpoints
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
