<!-- markdownlint-disable MD033 MD041 -->

<p align="center">
  <img src="https://github.com/radiantearth/stac-site/raw/master/images/logo/stac-030-long.png" width=400 alt="SpatioTemporal Asset Catalog (STAC) logo">
  <p align="center">FastAPI implemention of the STAC API spec.</p>
</p>
<p align="center">
  <a href="https://github.com/stac-utils/stac-fastapi/actions?query=workflow%3Acicd" target="_blank">
      <img src="https://github.com/stac-utils/stac-fastapi/workflows/stac-fastapi/badge.svg" alt="Test">
  </a>
  <a href="https://github.com/stac-utils/stac-fastapi/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/stac-fastapi.svg" alt="License">
  </a>
</p>

---

**Documentation**: [https://stac-utils.github.io/stac-fastapi/](https://stac-utils.github.io/stac-fastapi/)

**Source Code**: [https://github.com/stac-utils/stac-fastapi](https://github.com/stac-utils/stac-fastapi)

---

Python library for building a STAC-compliant FastAPI application.

> STAC stands for **SpatioTemporal Asset Catalogs**. The [STAC specification](https://stacspec.org/en/) is a common language to describe geospatial information, so it can more easily be worked with, indexed, and discovered.
> 
> [FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

This projects aims to make it easier to create a STAC-compatible API, with many tools embed. _No need to re-invent the wheel! :wheel:_

`stac-fastapi` was initially developed by [arturo-ai](https://github.com/arturo-ai).

## Features

<div class="grid cards" markdown>

- :material-web: STAC‑compliant FastAPI framework
- :material-package-variant-plus: Modular packages and extensions
- :material-database-cog: Multiple backend integrations
- :material-check-all: Model validation and types

</div>

## Library packages

### Namespaces

| Package |  Description | Version |
| ------- |------------- | ------- |
| [**stac_fastapi.api**](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/api) | An API layer which enforces the [stac-api-spec](https://github.com/radiantearth/stac-api-spec). | [![stac-fastapi.api](https://img.shields.io/pypi/v/stac-fastapi.api?color=%2334D058&label=pypi)](https://pypi.org/project/stac-fastapi.api) |
| [**stac_fastapi.extensions**](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions) | Abstract base classes for [STAC API extensions](https://github.com/radiantearth/stac-api-spec/blob/master/extensions.md) and third-party extensions. | [![stac-fastapi.extensions](https://img.shields.io/pypi/v/stac-fastapi.extensions?color=%2334D058&label=pypi)](https://pypi.org/project/stac-fastapi.extensions) |
| [**stac_fastapi.types**](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/types) | Shared types and abstract base classes used by the library. | [![stac-fastapi.types](https://img.shields.io/pypi/v/stac-fastapi.types?color=%2334D058&label=pypi)](https://pypi.org/project/stac-fastapi.types) |


### Backends

In addition to the packages in this repository, a server implemention will also require the selection of a backend to
connect with a database for STAC metadata storage. There are several different backend options, and each has their own
repository.

| Backend                                                                                                                                                                 | Code                                                                                                         | Remarks                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| :simple-postgresql: [PostgreSQL](https://github.com/postgres/postgres) + [PostGIS](https://github.com/postgis/postgis) + [PgSTAC](https://github.com/stac-utils/pgstac) | [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac)                                     |                                                                                                |
| :simple-elastic: [Elasticsearch](https://github.com/elastic/elasticsearch) or [OpenSearch](https://github.com/opensearch-project/OpenSearch)                            | [stac-fastapi-elasticsearch-opensearch](https://github.com/stac-utils/stac-fastapi-elasticsearch-opensearch) |                                                                                                |
| :simple-mongodb: [MongoDB](https://github.com/mongodb/mongo)                                                                                                            | [stac-fastapi-mongo](https://github.com/Healy-Hyperspatial/stac-fastapi-mongo)                               |                                                                                                |
| :material-grid-large: [GeoParquet](https://geoparquet.org) via [stacrs](https://github.com/stac-utils/stacrs)                                                           | [stac-fastapi-geoparquet](https://github.com/stac-utils/stac-fastapi-geoparquet)                             | Experimental                                                                                   |
| :simple-duckdb: [DuckDB](https://github.com/duckdb/duckdb)                                                                                                              | [stac-fastapi-duckdb](https://github.com/Healy-Hyperspatial/stac-fastapi-duckdb)                             | Experimental                                                                                   |
| :simple-sqlalchemy: [PostgreSQL](https://github.com/postgres/postgres) + [PostGIS](https://github.com/postgis/postgis) + [SQLAlchemy](https://www.sqlalchemy.org/)      | [stac-fastapi-sqlalchemy](https://github.com/stac-utils/stac-fastapi-sqlalchemy)                             | Abandoned in favor of [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac) |

### Extensions

The STAC API specification offers [an extension system](https://stac-api-extensions.github.io/), some of them are offered here to be ready-to-use in complement of your STAC FastAPI:

| Name                                                                                                                                                             | Description                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [Aggregation](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/aggregation)                                  | Aggregation Extension to provide aggregated data over a search, rather than individual Item results                            |
| [Bulk Transactions](https://github.com/stac-utils/stac-fastapi/blob/main/stac_fastapi/extensions/stac_fastapi/extensions/bulk_transactions/bulk_transactions.py) | Bulk Transaction extension allows efficient bulk insertion of items. |
| [Collection Search](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/collection_search)                      | Collection Search for STAC APIs                                                                                                |
| [Fields](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/fields)                                            | The Fields Extensions describes a mechanism to include or exclude certain fields from a response.                              |
| [Filter](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/filter)                                            | The Filter extension provides an expressive mechanism for searching based on Item attributes.                                  |
| [Free text](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/free_text)                                      | This defines a new parameter, q that allows the user to perform free-text queries against the item properties.                 |
| [Multi-tenant Catalogs](https://github.com/StacLabs/stac-fastapi-catalogs-extension)                                                                             | STAC API Extension to support Multi-Catalog hierarchies via a dedicated /catalogs endpoint. (Recursive Tree architecture).     |
| [Pagination](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/pagination)                                    | Though not strictly an extension, the chosen pagination will modify the form of the request object.  |
| [Query](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/query)                                              | The Query Extension adds a query parameter that allows additional filtering based on the properties of Item objects.           |
| [Sort](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/sort)                                                | The Sort Extension adds the `sortby` parameter and exposes `/sortables`, `/collections/{id}/sortables`, and `/collections-sortables` endpoints for discovering sortable fields. |
| [Transaction](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions/stac_fastapi/extensions/transaction)                                  | The Transaction Extension supports the creation, editing, and deleting of items through POST, PUT, PATCH, and DELETE requests. |

!!! note
    You can also create your own extensions! To do so, [check out the Development & Contributing guide](./contributing.md).


## Get started

```bash
# Install core software from PyPI
python -m pip install stac-fastapi.types stac-fastapi.api stac-fastapi.extensions uvicorn

# Install a backend of your choice, here's PgSTAC
python -m pip install stac-fastapi.pgstac

# Launch the API
uvicorn stac_fastapi.pgstac.app:app --host 0.0.0.0 --port 8080
```

Your API is running on [localhost:8080](http://localhost:8080).

For more details, please see our [get started guide](./get-started.md).

## Development & Contributing

See [our Development & Contributing guide](./contributing.md).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/stac-utils/stac-fastapi/blob/main/LICENSE) file for details.
