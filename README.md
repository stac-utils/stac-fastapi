# arturo-stac-api ![arturo-stac-api](https://github.com/arturo-ai/arturo-stac-api/workflows/arturo-stac-api/badge.svg)
FastAPI/postgres implementation of the [STAC API specification](https://github.com/radiantearth/stac-api-spec).

## Project Structure
```
.
├── alembic             # Database migrations
│   └── versions        # Migration versions
├── stac_api            
│   ├── clients         # Database CRUD
│   ├── models          # Database and API data models
│   ├── resources       # API endpoints
│   └── utils           # FastAPI dependencies
└── tests
    ├── clients         # CRUD test cases
    ├── data            # Test data
    └── resources       # API test cases
```

## Local Development
Use docker-compose to deploy the application, migrate the database, and ingest an example collection:
```
docker-compose build
docker-compose up
```

Run tests (the `docker-compose` stack must be running):
```
make test
```