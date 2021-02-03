# arturo-stac-api ![arturo-stac-api](https://github.com/arturo-ai/arturo-stac-api/workflows/arturo-stac-api/badge.svg)
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