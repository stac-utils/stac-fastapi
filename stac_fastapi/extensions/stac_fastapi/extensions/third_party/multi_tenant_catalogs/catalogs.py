"""Catalogs extension."""

from typing import List, Type

import attr
from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from stac_pydantic.api.collections import Collections
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.item import Item
from stac_pydantic.item_collection import ItemCollection
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.extension import ApiExtension

from .client import AsyncBaseCatalogsClient
from .types import (
    CatalogChildrenRequest,
    CatalogCollectionItemsRequest,
    CatalogCollectionItemUri,
    CatalogCollectionUri,
    Catalogs,
    CatalogsGetRequest,
    CatalogsUri,
    Children,
    CreateCatalogCollectionRequest,
    CreateSubCatalogRequest,
    SubCatalogsRequest,
    UnlinkSubCatalogRequest,
    UpdateCatalogRequest,
)

CATALOGS_CONFORMANCE_CLASSES = [
    "https://api.stacspec.org/v1.0.0/core",
    "https://api.stacspec.org/v1.0.0-beta.1/multi-tenant-catalogs",
    "https://api.stacspec.org/v1.0.0-rc.2/children",
    "https://api.stacspec.org/v1.0.0-rc.2/children#type-filter",
]

CATALOGS_TRANSACTION_CONFORMANCE_CLASS = (
    "https://api.stacspec.org/v1.0.0-beta.1/multi-tenant-catalogs/transaction"
)


@attr.s
class CatalogsExtension(ApiExtension):
    """Catalogs Extension.

    The Catalogs extension adds a /catalogs endpoint that returns a list of all catalogs
    in the database, similar to how /collections returns a list of collections.

    Attributes:
        client: A client implementing the catalogs extension pattern.
        settings: Extension settings.
        enable_transactions: Enable catalog transaction endpoints (POST, PUT, DELETE).
        conformance_classes: List of conformance classes for this extension.
        router: FastAPI router for the extension endpoints.
        response_class: Response class for the extension.
    """

    client: AsyncBaseCatalogsClient = attr.ib(kw_only=True)
    enable_transactions: bool = attr.ib(default=False, kw_only=True)
    settings: dict = attr.ib(default=attr.Factory(dict), kw_only=True)
    conformance_classes: List[str] = attr.ib(factory=list, kw_only=True)
    router: APIRouter = attr.ib(factory=APIRouter, kw_only=True)
    response_class: Type[Response] = attr.ib(default=JSONResponse, kw_only=True)

    def __attrs_post_init__(self):
        """Initialize conformance classes based on settings."""
        self.conformance_classes = CATALOGS_CONFORMANCE_CLASSES.copy()
        if self.enable_transactions:
            self.conformance_classes.append(CATALOGS_TRANSACTION_CONFORMANCE_CLASS)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.
        """
        self.router = APIRouter()
        self.register_read_endpoints()
        if self.enable_transactions:
            self.register_transaction_endpoints()
        app.include_router(self.router, tags=["Catalogs"])

    def register_read_endpoints(self) -> None:
        """Register all GET endpoints using the async factory."""
        # GET /catalogs
        self.router.add_api_route(
            name="Get All Catalogs",
            path="/catalogs",
            methods=["GET"],
            endpoint=create_async_endpoint(self.client.get_catalogs, CatalogsGetRequest),
            response_model=Catalogs
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get All Catalogs",
            description="Returns a list of all catalogs in the database.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}
        self.router.add_api_route(
            name="Get Catalog",
            path="/catalogs/{catalog_id}",
            methods=["GET"],
            endpoint=create_async_endpoint(self.client.get_catalog, CatalogsUri),
            response_model=Catalog
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog",
            description="Get a specific STAC catalog by ID.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/collections
        self.router.add_api_route(
            name="Get Catalog Collections",
            path="/catalogs/{catalog_id}/collections",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_catalog_collections, CatalogsUri
            ),
            response_model=Collections
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog Collections",
            description="Get collections linked from a specific catalog.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/collections/{collection_id}
        self.router.add_api_route(
            name="Get Catalog Collection",
            path="/catalogs/{catalog_id}/collections/{collection_id}",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_catalog_collection, CatalogCollectionUri
            ),
            response_model=Collection
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog Collection",
            description="Get a specific collection from a catalog.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/collections/{collection_id}/items
        self.router.add_api_route(
            name="Get Catalog Collection Items",
            path="/catalogs/{catalog_id}/collections/{collection_id}/items",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_catalog_collection_items, CatalogCollectionItemsRequest
            ),
            response_model=ItemCollection
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog Collection Items",
            description="Get items from a collection in a catalog.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/collections/{collection_id}/items/{item_id}
        self.router.add_api_route(
            name="Get Catalog Collection Item",
            path="/catalogs/{catalog_id}/collections/{collection_id}/items/{item_id}",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_catalog_collection_item, CatalogCollectionItemUri
            ),
            response_model=Item
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog Collection Item",
            description="Get a specific item from a collection in a catalog.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/catalogs
        self.router.add_api_route(
            name="Get Catalog Sub-Catalogs",
            path="/catalogs/{catalog_id}/catalogs",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_sub_catalogs, SubCatalogsRequest
            ),
            response_model=Catalogs
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog Sub-Catalogs",
            description="Get sub-catalogs linked from a specific catalog.",
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/children
        self.router.add_api_route(
            name="Get Catalog Children",
            path="/catalogs/{catalog_id}/children",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_catalog_children, CatalogChildrenRequest
            ),
            response_model=Children
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Get Catalog Children",
            description=(
                "Retrieve all children (Catalogs and Collections) of this catalog."
            ),
            tags=["Catalogs"],
        )

        # GET /catalogs/{catalog_id}/conformance
        self.router.add_api_route(
            name="Get Catalog Conformance",
            path="/catalogs/{catalog_id}/conformance",
            methods=["GET"],
            endpoint=create_async_endpoint(self._get_catalog_conformance, CatalogsUri),
            response_class=self.response_class,
            summary="Get Catalog Conformance",
            description="Get conformance classes specific to this sub-catalog.",
            tags=["Catalogs"],
            responses={
                HTTP_200_OK: {"description": "Conformance classes for the catalog"}
            },
        )

        # GET /catalogs/{catalog_id}/queryables
        self.router.add_api_route(
            name="Get Catalog Queryables",
            path="/catalogs/{catalog_id}/queryables",
            methods=["GET"],
            endpoint=create_async_endpoint(
                self.client.get_catalog_queryables, CatalogsUri
            ),
            response_class=self.response_class,
            summary="Get Catalog Queryables",
            description=(
                "Get queryable fields available for filtering in this "
                "sub-catalog (Filter Extension)."
            ),
            tags=["Catalogs"],
            responses={HTTP_200_OK: {"description": "Queryable fields for the catalog"}},
        )

    def register_transaction_endpoints(self) -> None:
        """Register POST/PUT/DELETE endpoints."""
        # POST /catalogs
        self.router.add_api_route(
            name="Create Catalog",
            path="/catalogs",
            methods=["POST"],
            status_code=HTTP_201_CREATED,
            endpoint=create_async_endpoint(self.client.create_catalog, Catalog),
            response_model=Catalog
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Create Catalog",
            description="Create a new STAC catalog.",
            tags=["Catalogs"],
        )

        # PUT /catalogs/{catalog_id}
        self.router.add_api_route(
            name="Update Catalog",
            path="/catalogs/{catalog_id}",
            methods=["PUT"],
            endpoint=create_async_endpoint(
                self.client.update_catalog, UpdateCatalogRequest
            ),
            response_model=Catalog
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Update Catalog",
            description="Update an existing STAC catalog.",
            tags=["Catalogs"],
        )

        # DELETE /catalogs/{catalog_id}
        self.router.add_api_route(
            name="Delete Catalog",
            path="/catalogs/{catalog_id}",
            methods=["DELETE"],
            status_code=HTTP_204_NO_CONTENT,
            endpoint=create_async_endpoint(self.client.delete_catalog, CatalogsUri),
            response_class=self.response_class,
            summary="Delete Catalog",
            description="Delete a catalog.",
            tags=["Catalogs"],
        )

        # POST /catalogs/{catalog_id}/collections
        self.router.add_api_route(
            name="Create Catalog Collection",
            path="/catalogs/{catalog_id}/collections",
            methods=["POST"],
            status_code=HTTP_201_CREATED,
            endpoint=create_async_endpoint(
                self.client.create_catalog_collection, CreateCatalogCollectionRequest
            ),
            response_model=Collection
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Create Catalog Collection",
            description="Create a new collection and link it to a specific catalog.",
            tags=["Catalogs"],
        )

        # DELETE /catalogs/{catalog_id}/collections/{collection_id}
        self.router.add_api_route(
            name="Unlink Collection from Catalog",
            path="/catalogs/{catalog_id}/collections/{collection_id}",
            methods=["DELETE"],
            status_code=HTTP_204_NO_CONTENT,
            endpoint=create_async_endpoint(
                self.client.unlink_catalog_collection, CatalogCollectionUri
            ),
            response_class=self.response_class,
            summary="Unlink Collection from Catalog",
            description=(
                "Removes the link between the catalog and collection. "
                "The Collection data is NOT deleted."
            ),
            tags=["Catalogs"],
        )

        # POST /catalogs/{catalog_id}/catalogs
        self.router.add_api_route(
            name="Create Catalog Sub-Catalog",
            path="/catalogs/{catalog_id}/catalogs",
            methods=["POST"],
            status_code=HTTP_201_CREATED,
            endpoint=create_async_endpoint(
                self.client.create_sub_catalog, CreateSubCatalogRequest
            ),
            response_model=Catalog
            if self.settings.get("enable_response_models", True)
            else None,
            response_class=self.response_class,
            summary="Create Catalog Sub-Catalog",
            description=(
                "Create a new catalog or link an existing catalog as a "
                "sub-catalog of a specific catalog."
            ),
            tags=["Catalogs"],
        )

        # DELETE /catalogs/{catalog_id}/catalogs/{sub_catalog_id}
        self.router.add_api_route(
            name="Unlink Sub-Catalog",
            path="/catalogs/{catalog_id}/catalogs/{sub_catalog_id}",
            methods=["DELETE"],
            status_code=HTTP_204_NO_CONTENT,
            endpoint=create_async_endpoint(
                self.client.unlink_sub_catalog, UnlinkSubCatalogRequest
            ),
            response_class=self.response_class,
            summary="Unlink Sub-Catalog",
            description=(
                "Unlink a sub-catalog from its parent. "
                "Does not delete the sub-catalog."
            ),
            tags=["Catalogs"],
        )

    async def _get_catalog_conformance(
        self, catalog_id: str, request=None, **kwargs
    ) -> dict:
        """Get conformance classes specific to this sub-catalog.

        Merges client response with extension conformance classes.
        """
        result = await self.client.get_catalog_conformance(
            catalog_id=catalog_id, request=request
        )
        # Merge extension conformance classes with client response
        if "conformsTo" in result:
            result["conformsTo"].extend(self.conformance_classes)
        else:
            result["conformsTo"] = self.conformance_classes
        return result
