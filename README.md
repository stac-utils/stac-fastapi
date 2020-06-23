# arturo-stac-api
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
Deploy the database and application locally with docker compose:
```
docker-compose build
docker-compose up
```

Run tests (the `docker-compose` stack must be running):
```
make test
```