"""Catalogs extension types."""

from typing import Literal

import attr
from fastapi import Body, Path, Query
from pydantic import BaseModel
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.links import Links
from stac_pydantic.shared import BBox, StacBaseModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest, _bbox_converter


class ObjectUri(BaseModel):
    """Simple model for linking existing resources by ID.

    Used for Mode B (Linking) operations where only the ID is provided
    to reference an existing catalog or collection.
    """

    id: str


# --- Uri Request Models for create_async_endpoint factory ---


@attr.s
class CatalogsUri(APIRequest):
    """Base for catalog-specific endpoints."""

    catalog_id: Annotated[str, Path(description="Catalog ID")] = attr.ib()


@attr.s
class CatalogsGetRequest(APIRequest):
    """Parameters for the root /catalogs endpoint."""

    limit: Annotated[
        int | None,
        Query(ge=1, le=1000, description="Maximum number of catalogs to return"),
    ] = attr.ib(default=10)
    token: Annotated[str | None, Query(description="Pagination token")] = attr.ib(
        default=None
    )


@attr.s
class CatalogCollectionUri(CatalogsUri):
    """Combines catalog_id and collection_id."""

    collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()


@attr.s
class CatalogCollectionItemUri(CatalogCollectionUri):
    """Combines catalog_id, collection_id, and item_id."""

    item_id: Annotated[str, Path(description="Item ID")] = attr.ib()


@attr.s
class CatalogCollectionItemsRequest(CatalogCollectionUri):
    """Parameters for /catalogs/{catalog_id}/collections/{collection_id}/items."""

    bbox: Annotated[
        BBox | None,
        Query(description="Bounding box to filter items [minx, miny, maxx, maxy]"),
    ] = attr.ib(
        default=None,
        converter=lambda x: _bbox_converter(x) if x is not None else None,
    )
    datetime: Annotated[
        str | None, Query(description="Datetime to filter items")
    ] = attr.ib(default=None)
    limit: Annotated[
        int | None,
        Query(ge=1, le=10000, description="Maximum number of items to return"),
    ] = attr.ib(default=10)
    token: Annotated[str | None, Query(description="Pagination token")] = attr.ib(
        default=None
    )


@attr.s
class SubCatalogsRequest(CatalogsUri):
    """Parameters for /catalogs/{catalog_id}/catalogs."""

    limit: Annotated[
        int | None,
        Query(ge=1, le=1000, description="Maximum number of sub-catalogs to return"),
    ] = attr.ib(default=10)
    token: Annotated[str | None, Query(description="Pagination token")] = attr.ib(
        default=None
    )


@attr.s
class CatalogChildrenRequest(CatalogsUri):
    """Parameters for /catalogs/{catalog_id}/children."""

    limit: Annotated[
        int | None,
        Query(ge=1, le=1000, description="Maximum number of children to return"),
    ] = attr.ib(default=10)
    token: Annotated[str | None, Query(description="Pagination token")] = attr.ib(
        default=None
    )
    type: Annotated[
        Literal["Catalog", "Collection"] | None,
        Query(description="Filter by resource type"),
    ] = attr.ib(default=None)


# --- Request Models with Body for Transaction Endpoints ---


@attr.s
class CreateCatalogRequest(APIRequest):
    """Create catalog with body."""

    catalog: Annotated[Catalog, Body()] = attr.ib(default=None)


@attr.s
class UpdateCatalogRequest(CatalogsUri):
    """Update catalog with body."""

    catalog: Annotated[Catalog, Body()] = attr.ib(default=None)


@attr.s
class CreateCatalogCollectionRequest(CatalogsUri):
    """Create catalog collection with body."""

    collection: Annotated[Collection | ObjectUri, Body()] = attr.ib(default=None)


@attr.s
class CreateSubCatalogRequest(CatalogsUri):
    """Create sub-catalog with body."""

    catalog: Annotated[Catalog | ObjectUri, Body()] = attr.ib(default=None)


@attr.s
class UnlinkSubCatalogRequest(CatalogsUri):
    """Unlink sub-catalog request."""

    sub_catalog_id: Annotated[str, Path(description="Sub-Catalog ID")] = attr.ib()


class Catalogs(StacBaseModel):
    """Catalogs endpoint response."""

    catalogs: list[Catalog]
    links: Links
    numberMatched: int | None = None
    numberReturned: int | None = None


class Children(StacBaseModel):
    """Children endpoint response.

    Returns a mixed list of Catalogs and Collections as children.
    """

    children: list[Catalog | Collection]
    links: Links
    numberMatched: int | None = None
    numberReturned: int | None = None
