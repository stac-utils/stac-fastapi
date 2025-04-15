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

`stac-fastapi` was initially developed by [arturo-ai](https://github.com/arturo-ai).

The project contains several namespace packages:

| Package |  Description | Version |
| ------- |------------- | ------- |
| [**stac_fastapi.api**](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/api) | An API layer which enforces the [stac-api-spec](https://github.com/radiantearth/stac-api-spec). | [![stac-fastapi.api](https://img.shields.io/pypi/v/stac-fastapi.api?color=%2334D058&label=pypi)](https://pypi.org/project/stac-fastapi.api) |
| [**stac_fastapi.extensions**](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/extensions) | Abstract base classes for [STAC API extensions](https://github.com/radiantearth/stac-api-spec/blob/master/extensions.md) and third-party extensions. | [![stac-fastapi.extensions](https://img.shields.io/pypi/v/stac-fastapi.extensions?color=%2334D058&label=pypi)](https://pypi.org/project/stac-fastapi.extensions) |
| [**stac_fastapi.types**](https://github.com/stac-utils/stac-fastapi/tree/main/stac_fastapi/types) | Shared types and abstract base classes used by the library. | [![stac-fastapi.types](https://img.shields.io/pypi/v/stac-fastapi.types?color=%2334D058&label=pypi)](https://pypi.org/project/stac-fastapi.types) |

#### Backends

In addition to the packages in this repository, a server implemention will also require the selection of a backend to
connect with a database for STAC metadata storage. There are several different backend options, and each has their own
repository.

The two most widely-used and supported backends are:

- [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac): [PostgreSQL](https://github.com/postgres/postgres) + [PostGIS](https://github.com/postgis/postgis) via [PgSTAC](https://github.com/stac-utils/pgstac).
- [stac-fastapi-elasticsearch-opensearch](https://github.com/stac-utils/stac-fastapi-elasticsearch-opensearch): [Elasticsearch](https://github.com/elastic/elasticsearch) or [OpenSearch](https://github.com/opensearch-project/OpenSearch)

Other implementations include:

- [stac-fastapi-mongo](https://github.com/Healy-Hyperspatial/stac-fastapi-mongo): [MongoDB](https://github.com/mongodb/mongo)
- [stac-fastapi-geoparquet)](https://github.com/stac-utils/stac-fastapi-geoparquet): [GeoParquet](https://geoparquet.org) via [stacrs](https://github.com/stac-utils/stacrs) (experimental)
- [stac-fastapi-duckdb](https://github.com/Healy-Hyperspatial/stac-fastapi-duckdb): [DuckDB](https://github.com/duckdb/duckdb) (experimental)
- [stac-fastapi-sqlalchemy](https://github.com/stac-utils/stac-fastapi-sqlalchemy): [PostgreSQL](https://github.com/postgres/postgres) + [PostGIS](https://github.com/postgis/postgis) via [SQLAlchemy](https://www.sqlalchemy.org/) (abandoned in favor of stac-fastapi-pgstac)

## Response Model Validation

A common question when using this package is how request and response types are validated?

This package uses [`stac-pydantic`](https://github.com/stac-utils/stac-pydantic) to validate and document STAC objects. However, by default, validation of response types is turned off and the API will simply forward responses without validating them against the Pydantic model first. This decision was made with the assumption that responses usually come from a (typed) database and can be considered safe. Extra validation would only increase latency, in particular for large payloads.

To turn on response validation, set `ENABLE_RESPONSE_MODELS` to `True`. Either as an environment variable or directly in the `ApiSettings`.

With the introduction of Pydantic 2, the extra [time it takes to validate models became negatable](https://github.com/stac-utils/stac-fastapi/pull/625#issuecomment-2045824578). While `ENABLE_RESPONSE_MODELS` still defaults to `False` there should be no penalty for users to turn on this feature but users discretion is advised.

## Installation

```bash
# Install from PyPI
python -m pip install stac-fastapi.types stac-fastapi.api stac-fastapi.extensions

# Install a backend of your choice
python -m pip install stac-fastapi.pgstac
```

Other backends may be available from other sources, search [PyPI](https://pypi.org/) for more.

## Development

Install the packages in editable mode:

```shell
python -m pip install -e \
  'stac_fastapi/types[dev]' \
  'stac_fastapi/api[dev]' \
  'stac_fastapi/extensions[dev]'
```

To run the tests:

```shell
python -m pytest
```

## Releasing

See [RELEASING.md](./RELEASING.md).
