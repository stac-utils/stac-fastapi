<p align="center">
  <img src="https://github.com/radiantearth/stac-site/raw/master/images/logo/stac-030-long.png" width=400>
  <p align="center">FastAPI implemention of the STAC API spec using <a href="https://github.com/stac-utils/pgstac">PGStac</a></p>
</p>
<p align="center">
  <a href="https://github.com/stac-utils/stac-fastapi/actions?query=workflow%3Acicd" target="_blank">
      <img src="https://github.com/stac-utils/stac-fastapi/workflows/stac-fastapi/badge.svg" alt="Test">
  </a>
  <a href="https://pypi.org/project/stac-fastapi" target="_blank">
      <img src="https://img.shields.io/pypi/v/stac-fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://github.com/stac-utils/stac-fastapi/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/stac-utils/stac-fastapi.svg" alt="Downloads">
  </a>
</p>

---

**Documentation**: [https://stac-utils.github.io/stac-fastapi/](https://stac-utils.github.io/stac-fastapi/)

**Source Code**: [https://github.com/stac-utils/stac-fastapi](https://github.com/stac-utils/stac-fastapi)

---

Stac FastAPI using the [PGStac](https://github.com/stac-utils/pgstac) backend.

[PGStac](https://github.com/stac-utils/pgstac) is a separately managed PostgreSQL database that is designed for enhanced performance to be able to scale Stac FastAPI to be able to efficiently handle hundreds of millions of records. [PGStac](https://github.com/stac-utils/pgstac) automatically includes indexes on Item id, Collection id, Item Geometry, Item Datetime, and an Index for equality checks on any key in Item Properties. Additional indexes may be added to Item Properties to speed up the use of order, <, <=, >, and >= queries.

Stac FastAPI acts as the HTTP interface validating any requests and data that is sent to the [PGStac](https://github.com/stac-utils/pgstac) backend and adds in Link items on data return relative to the service host. All other processing and search is provided directly using PGStac procedural sql / plpgsql functions on the database.

PGStac stores all collection and item records as jsonb fields exactly as they come in allowing for any custom fields to be stored and retrieved transparently.

While the Stac Sort Extension is fully supported, [PGStac](https://github.com/stac-utils/pgstac) is particularly enhanced to be able to sort by datetime (either ascending or descending). Sorting by anything other than datetime (the default if no sort is specified) on very large Stac repositories without very specific query limits (ie selecting a single day date range) will not have the same performance. For more than millions of records it is recommended to either set a low connection timeout on PostgreSQL or to disable use of the Sort Extension.

`stac-fastapi pgstac` was initially added to `stac-fastapi` by [developmentseed](https://github.com/developmentseed).

## Installation

```shell
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi
pip install -e \
    stac_fastapi/api[dev] \
    stac_fastapi/types[dev] \
    stac_fastapi/extensions[dev] \
    stac_fastapi/pgstac[dev,server]
```

### Settings

To configure PGStac stac-fastapi to [hydrate search result items in the API](https://github.com/stac-utils/pgstac#runtime-configurations), set the `USE_API_HYDRATE` environment variable to `true` or explicitly set the option in the PGStac Settings object.

### Migrations

PGStac is an external project and the may be used by multiple front ends.
For Stac FastAPI development, a docker image (which is pulled as part of the docker-compose) is available at
bitner/pgstac:[version] that has the full database already set up for PGStac.

There is also a python utility as part of PGStac (pypgstac) that includes a migration utility. The pgstac
version required by stac-fastapi/pgstac is pinned by using the pinned version of pypgstac in the [setup](setup.py) file.

In order to migrate database versions you can use the migration utility:

```shell
pypgstac migrate
```
