# Changelog

## [Unreleased]

## [2.4.5] - 2023-04-04

### Changed

* Default branch to **main** ([#544](https://github.com/stac-utils/stac-fastapi/pull/544))

### Fixed

* Use `V()` instead of f-strings for pgstac queries ([#554](https://github.com/stac-utils/stac-fastapi/pull/554))

## [2.4.4] - 2023-03-09

### Added

* Nginx service as second docker-compose stack to demonstrate proxy ([#503](https://github.com/stac-utils/stac-fastapi/pull/503))
* Validation checks in CI using [stac-api-validator](github.com/stac-utils/stac-api-validator) ([#508](https://github.com/stac-utils/stac-fastapi/pull/508))
* Required links to the sqlalchemy ItemCollection endpoint ([#508](https://github.com/stac-utils/stac-fastapi/pull/508))
* Publication of docker images to GHCR ([#525](https://github.com/stac-utils/stac-fastapi/pull/525))

### Changed

* Updated CI to test against [pgstac v0.6.12](https://github.com/stac-utils/pgstac/releases/tag/v0.6.12) ([#511](https://github.com/stac-utils/stac-fastapi/pull/511))
* Reworked `update_openapi` and added a test for it ([#523](https://github.com/stac-utils/stac-fastapi/pull/523))
* Limit values above 10,000 are now replaced with 10,000 instead of returning a 400 error ([#526](https://github.com/stac-utils/stac-fastapi/pull/526))
* Updated pgstac to v0.7.1 ([#535](https://github.com/stac-utils/stac-fastapi/pull/535))

### Removed

* Incorrect context STAC extension url from the landing page ([#508](https://github.com/stac-utils/stac-fastapi/pull/508))

### Fixed

* Allow url encoded values for `query` in GET requests ([#504](https://github.com/stac-utils/stac-fastapi/pull/504))
* Fix path in `register_update_item` docstring ([#507](https://github.com/stac-utils/stac-fastapi/pull/507))
* `self` link rel for `/collections/{c_id}/items` ([#508](https://github.com/stac-utils/stac-fastapi/pull/508))
* Media type of the item collection endpoint ([#508](https://github.com/stac-utils/stac-fastapi/pull/508))
* Manually exclude non-truthy optional values from sqlalchemy serialization of Collections ([#508](https://github.com/stac-utils/stac-fastapi/pull/508))
* Support `intersects` in GET requests ([#521](https://github.com/stac-utils/stac-fastapi/pull/521))
* Deleting items that had repeated ids in other collections ([#520](https://github.com/stac-utils/stac-fastapi/pull/520))
* 404 for missing collection on /items for sqlalchemy ([#528](https://github.com/stac-utils/stac-fastapi/pull/528))
* Conformance URIs for the filter extension ([#540](https://github.com/stac-utils/stac-fastapi/pull/540))

### Deprecated

* Deprecated `VndOaiResponse` and `config_openapi`, will be removed in v3.0 ([#523](https://github.com/stac-utils/stac-fastapi/pull/523))

## [2.4.3] - 2022-11-25

### Added

* Add the `ENABLED_EXTENSIONS` environment variable determining which extensions are enabled in the pgstac application, all extensions are enabled by default ([#495](https://github.com/stac-utils/stac-fastapi/pull/495))

### Changed

### Removed

### Fixed

## [2.4.2] - 2022-11-25

### Added

* Add support in pgstac backend for /queryables and /collections/{collection_id}/queryables endpoints with functions exposed in pgstac 0.6.8 ([#474](https://github.com/stac-utils/stac-fastapi/pull/474))
* Add `bbox` and `datetime` query parameters to `/collections/{collection_id}/items`. ([#476](https://github.com/stac-utils/stac-fastapi/issues/476), [#380](https://github.com/stac-utils/stac-fastapi/issues/380))
* Update pgstac requirement to 0.6.10
* Add `servers` and `description` to OpenAPI ([#459](https://github.com/stac-utils/stac-fastapi/pull/459))

### Changed

### Removed

* Removed `stac_fastapi.api.routes.create_sync_endpoint` function to reduce code duplication ([#471](https://github.com/stac-utils/stac-fastapi/pull/471))

### Fixed

* Quote password in pgsql strings to accomodate special characters. ([#455](https://github.com/stac-utils/stac-fastapi/issues/455))
* Fix pgstac backend for /queryables endpoint to return 404 for non-existent collections ([#482](https://github.com/stac-utils/stac-fastapi/pull/482))
* `/collection/{collection_id}/items` endpoints now return geojson media type ([#488](https://github.com/stac-utils/stac-fastapi/pull/488))

## [2.4.1] - 2022-08-05

### Added

### Changed

### Removed

### Fixed

* `ciso8601` fails to build in some environments, instead use `pyiso8601` to parse datetimes.

## [2.4.0] - 2022-08-04

### Added

* Add hook to allow adding dependencies to routes. ([#295](https://github.com/stac-utils/stac-fastapi/pull/295))
* Ability to POST an ItemCollection to the collections/{collectionId}/items route. ([#367](https://github.com/stac-utils/stac-fastapi/pull/367))
* Add STAC API - Collections conformance class. ([383](https://github.com/stac-utils/stac-fastapi/pull/383))
* Bulk item inserts for pgstac implementation. ([411](https://github.com/stac-utils/stac-fastapi/pull/411))
* Add APIRouter prefix support for pgstac implementation. ([429](https://github.com/stac-utils/stac-fastapi/pull/429))
* Respect `Forwarded` or `X-Forwarded-*` request headers when building links to better accommodate load balancers and proxies.

### Changed

* Update FastAPI requirement to allow version >=0.73 ([#337](https://github.com/stac-utils/stac-fastapi/pull/337))
* Bump version of PGStac to 0.4.5  ([#346](https://github.com/stac-utils/stac-fastapi/pull/346))
* Add support for PGStac Backend to use PyGeofilter to convert Get Request with cql2-text into cql2-json to send to PGStac backend ([#346](https://github.com/stac-utils/stac-fastapi/pull/346))
* Updated all conformance classes to 1.0.0-rc.1. ([383](https://github.com/stac-utils/stac-fastapi/pull/383))
* Bulk Transactions object Items iterator now returns the Item objects rather than the string IDs of the Item objects
  ([#355](https://github.com/stac-utils/stac-fastapi/issues/355))
* docker-compose now runs uvicorn with hot-reloading enabled
* Bump version of PGStac to 0.6.2 that includes support for hydrating results in the API backed ([#397](https://github.com/stac-utils/stac-fastapi/pull/397))
* Make item geometry and bbox nullable in sqlalchemy backend. ([#398](https://github.com/stac-utils/stac-fastapi/pull/398))
* Transactions Extension update Item endpoint Item is now `/collections/{collection_id}/items/{item_id}` instead of
  `/collections/{collection_id}/items` to align with [STAC API
  spec](https://github.com/radiantearth/stac-api-spec/tree/main/ogcapi-features/extensions/transaction#methods) ([#425](https://github.com/stac-utils/stac-fastapi/pull/425))

### Removed

* Remove the unused `router_middleware` function ([#439](https://github.com/stac-utils/stac-fastapi/pull/439))

### Fixed

* Bumped uvicorn version to 0.17 (from >=0.12, <=0.14) to resolve security vulnerability related to websockets dependency version ([#343](https://github.com/stac-utils/stac-fastapi/pull/343))
* `AttributeError` and/or missing properties when requesting the complete `properties`-field in searches. Added test. ([#339](https://github.com/stac-utils/stac-fastapi/pull/339))
* Fixes issues (and adds tests) for issues caused by regression in pgstac ([#345](https://github.com/stac-utils/stac-fastapi/issues/345)
* Update error response payloads to match the API spec. ([#361](https://github.com/stac-utils/stac-fastapi/pull/361))
* Fixed stray `/` before the `#` in several extension conformance class strings ([383](https://github.com/stac-utils/stac-fastapi/pull/383))
* SQLAlchemy backend bulk item insert now works ([#356](https://github.com/stac-utils/stac-fastapi/issues/356))
* PGStac Backend has stricter implementation of Fields Extension syntax ([#397](https://github.com/stac-utils/stac-fastapi/pull/397))
* `/queryables` endpoint now has type `application/schema+json` instead of `application/json` ([#421](https://github.com/stac-utils/stac-fastapi/pull/421))
* Transactions Extension update Item endpoint validates that the `{collection_id}` path parameter matches the Item `"collection"` property
  from the request body, if present, and falls back to using the path parameter if no `"collection"` property is found in the body
  ([#425](https://github.com/stac-utils/stac-fastapi/pull/425))
* PGStac Backend Transactions endpoints return added Item/Collection instead of Item/Collection from request ([#424](https://github.com/stac-utils/stac-fastapi/pull/424))
* Application no longer breaks on startup when pagination extension is not included ([#444](https://github.com/stac-utils/stac-fastapi/pull/444))

## [2.3.0] - 2022-01-18

### Added

* Add link with rel-type of 'service-doc', pointing to HTML API documentation ([#298](https://github.com/stac-utils/stac-fastapi/pull/298))

### Changed

* Refactor to remove hardcoded search request models. Request models are now dynamically created based on the enabled extensions.
  ([#213](https://github.com/stac-utils/stac-fastapi/pull/213))
* Change example data to use correct `type` for the example Joplin collection ([#314](https://github.com/stac-utils/stac-fastapi/pull/314))
* Changed the geometry type in the Item model from Polygon to Geometry.
* Upgrade pgstac backend to use version 0.4.2 ([#321](https://github.com/stac-utils/stac-fastapi/pull/321))
* STAC 1.0.0-beta.4 conformance classes updated ([#298](https://github.com/stac-utils/stac-fastapi/pull/298))
* Upgrade pgstac backend to use version 0.4.3 ([#326](https://github.com/stac-utils/stac-fastapi/pull/326))

### Removed

* The tiles extension and all tiles links, added for demonstration purposes, have been removed. ([#309](https://github.com/stac-utils/stac-fastapi/pull/309))

### Fixed

* Import error using `importlib.util` ([#325](https://github.com/stac-utils/stac-fastapi/pull/325))
* Add environment variables required by upgraded pgstac container ([#313](https://github.com/stac-utils/stac-fastapi/pull/313))
* Enabled `ContextExtension` by default ([#207](https://github.com/stac-utils/stac-fastapi/issues/207))
* Content-type response headers for the /search endpoint now reflect the geojson response expected in the STAC api spec ([#220](https://github.com/stac-utils/stac-fastapi/issues/220))
* The minimum `limit` value for searches is now 1 ([#296](https://github.com/stac-utils/stac-fastapi/pull/296))
* Links stored with Collections and Items (e.g. license links) are now returned with those STAC objects ([#282](https://github.com/stac-utils/stac-fastapi/pull/282))
* Content-type response headers for the /api endpoint now reflect those expected in the STAC api spec ([#287](https://github.com/stac-utils/stac-fastapi/pull/287))
* Changed type options for datetime in BaseSearchGetRequest ([#318](https://github.com/stac-utils/stac-fastapi/pull/318))
* Expanded on tests to ensure properly testing get and post searches ([#318](https://github.com/stac-utils/stac-fastapi/pull/318))
* Ensure invalid datetimes result in 400s ([#323](https://github.com/stac-utils/stac-fastapi/pull/323))

## [2.2.0] - 2021-10-19

### Added

* Add CQL2 support ([#308](https://github.com/stac-utils/stac-fastapi/pull/308))
* Add ability to override ItemCollectionUri and SearchGetRequest models ([#271](https://github.com/stac-utils/stac-fastapi/pull/271))
* Added `collections` attribute to list of default fields to include, so that we satisfy the STAC API spec, which requires a `collections` attribute to be output when an item is part of a collection ([#276](https://github.com/stac-utils/stac-fastapi/pull/276))

### Changed

* Update pgstac to 0.4.0 ([#308](https://github.com/stac-utils/stac-fastapi/pull/308))
* Update get_item in sqlalchemy backend to allow for querying for items with same ids but in different collections. ([#275](https://github.com/stac-utils/stac-fastapi/pull/275))

## [2.1.1] - 2021-09-23

### Added

* Add `middlewares` option in `stac_fastapi.api.StacApi` to allow custom middleware configuration ([#267](https://github.com/stac-utils/stac-fastapi/pull/267))
* Support non-interval datetime queries on sqlalchemy backend ([#262](https://github.com/stac-utils/stac-fastapi/pull/262))
* Restrict `limit` parameter in sqlalchemy backend to between 1 and 10,000. ([#251](https://github.com/stac-utils/stac-fastapi/pull/251))
* Fix OAS conformance URL ([#263](https://github.com/stac-utils/stac-fastapi/pull/263))
* Links to children collections from the landing pagge always have a title ([#260](https://github.com/stac-utils/stac-fastapi/pull/260))
* Fix collection links in the `all_collections` method in `pgstac` ([#269](https://github.com/stac-utils/stac-fastapi/pull/269))

### Fixed

* Pin FastAPI to 0.67 to avoid issues with rendering OpenAPI documentation ([#246](https://github.com/stac-utils/stac-fastapi/pull/246))
* Add `stac_version` to default search attributes ([#268](https://github.com/stac-utils/stac-fastapi/pull/268))
* pgstac backend specifies collection_id when fetching a single item ([#279](https://github.com/stac-utils/stac-fastapi/pull/270))

## [2.1.0] - 2021-08-26

### Added

* Added filter extension. ([#165](https://github.com/stac-utils/stac-fastapi/pull/165))
* Add Support for CQL JSON to PGStac Backend ([#209](https://github.com/stac-utils/stac-fastapi/pull/209))
* Added item_serializer and item_table to BulkTransactionsClient in sqlalchemy backend ([#210](https://github.com/stac-utils/stac-fastapi/pull/210))
* Enable conformance class configuration ([#214](https://github.com/stac-utils/stac-fastapi/pull/214))
* Add/fix landing page links ([#229](https://github.com/stac-utils/stac-fastapi/pull/229))
* Correct response codes for bad/unusable bboxes ([#235](https://github.com/stac-utils/stac-fastapi/pull/235))
* Add a "method" field for search links ([#236](https://github.com/stac-utils/stac-fastapi/pull/236))
* Add extension schemas to landing ([#237](https://github.com/stac-utils/stac-fastapi/pull/237))

### Removed

* Remove shapely from stac_fastapi.pgstac requirements ([#225](https://github.com/stac-utils/stac-fastapi/pull/225))

### Changed

* Update to STAC API 1.0.0-beta.3 ([#239](https://github.com/stac-utils/stac-fastapi/pull/239))

### Fixed

* Make collection title optional in landing page links ([#198](https://github.com/stac-utils/stac-fastapi/pull/198))
* Preserve relative paths on link generation ([#199](https://github.com/stac-utils/stac-fastapi/pull/199))
* Fix collection endpoint return value to match spec (fixes regression) ([#232](https://github.com/stac-utils/stac-fastapi/pull/232))
* Return empty item collection instead of error when searching ([#233](https://github.com/stac-utils/stac-fastapi/pull/233))
* Correct response codes for bad/unusable bboxes ([#235](https://github.com/stac-utils/stac-fastapi/pull/235))
* Update pgstac to return 400 on invalid date parameter ([#240](https://github.com/stac-utils/stac-fastapi/pull/240))

## [2.0.0] - 2021-07-26

* Refactor stac-fastapi into submodules ([#106](https://github.com/)stac-utils/stac-fastapi/pull/106)
* Add pgstac backend ([#126](https://github.com/stac-utils/stac-fastapi/pull/126))
* Upgrade to stac-pydantic 2.0.0 and stac-spec 1.0.0 ([#181](https://github.com/stac-utils/stac-fastapi/pull/181))

## [1.1.0] - 2021-01-28

* Improve how the library declares API extensions ([#54](https://github.com/stac-utils/arturo-stac-api/pull/54))
* Add postgres bulk transactions client ([#59](https://github.com/stac-utils/arturo-stac-api/pull/59))
* Update TiTiler version ([#61](https://github.com/stac-utils/arturo-stac-api/pull/61))
* Use attrs instead of dataclasses ([#73](https://github.com/stac-utils/arturo-stac-api/pull/73))
* Remove postgres database connection from API layer ([#74](https://github.com/stac-utils/arturo-stac-api/pull/74))
* Fix `pre-commit` config ([#75](https://github.com/stac-utils/arturo-stac-api/pull/75))

## [1.0.0] - 2020-09-28

* First PyPi release!

[Unreleased]: <https://github.com/stac-utils/stac-fastapi/compare/2.4.5..main>
[2.4.5]: <https://github.com/stac-utils/stac-fastapi/compare/2.4.4..2.4.5>
[2.4.4]: <https://github.com/stac-utils/stac-fastapi/compare/2.4.3..2.4.4>
[2.4.3]: <https://github.com/stac-utils/stac-fastapi/compare/2.4.2..2.4.3>
[2.4.2]: <https://github.com/stac-utils/stac-fastapi/compare/2.4.1..2.4.2>
[2.4.1]: <https://github.com/stac-utils/stac-fastapi/compare/2.4.0..2.4.1>
[2.4.0]: <https://github.com/stac-utils/stac-fastapi/compare/2.3.0..2.4.0>
[2.3.0]: <https://github.com/stac-utils/stac-fastapi/compare/2.2.0..2.3.0>
[2.2.0]: <https://github.com/stac-utils/stac-fastapi/compare/2.1.1..2.2.0>
[2.1.1]: <https://github.com/stac-utils/stac-fastapi/compare/2.1.0..2.1.1>
[2.1.0]: <https://github.com/stac-utils/stac-fastapi/compare/2.1.0..main>
[2.0.0]: <https://github.com/stac-utils/stac-fastapi/compare/1.1.0..2.0.0>
[1.1.0]: <https://github.com/stac-utils/stac-fastapi/compare/1.0.0..1.1.0>
[1.0.0]: <https://github.com/stac-utils/stac-fastapi/tree/1.0.0>
