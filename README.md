# arturo-stac-api ![arturo-stac-api](https://github.com/arturo-ai/arturo-stac-api/workflows/arturo-stac-api/badge.svg)
---

**Documentation**: coming soon...

**Source Code**: [https://github.com/arturo-ai/arturo-stac-api](https://github.com/arturo-ai/arturo-stac-api)

---

Python library for building and customizing a STAC compliant API:


```
pip install arturo-stac-api
```


## Usage
```python
# my_app.py
from stac_api.config import ApiSettings
from stac_api.api import create_app

settings = ApiSettings()
app = create_app(settings)
```

```bash
$ uvicorn my_app:app --reload
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
