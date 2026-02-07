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

from stac_fastapi.types.extension import ApiExtension

from .client import AsyncBaseCatalogsClient
from .types import Catalogs, Children

CATALOGS_CONFORMANCE_CLASSES = [
    "https://api.stacspec.org/v1.0.0/core",
    "https://api.stacspec.org/v1.0.0-beta.1/multi-tenant-catalogs",
    "https://api.stacspec.org/v1.0.0-rc.2/children",
    "https://api.stacspec.org/v1.0.0-rc.2/children#type-filter",
]


@attr.s
class CatalogsExtension(ApiExtension):
    """Catalogs Extension.

    The Catalogs extension adds a /catalogs endpoint that returns a list of all catalogs
    in the database, similar to how /collections returns a list of collections.

    Attributes:
        client: A client implementing the catalogs extension pattern.
        settings: Extension settings.
        conformance_classes: List of conformance classes for this extension.
        router: FastAPI router for the extension endpoints.
        response_class: Response class for the extension.
    """

    client: AsyncBaseCatalogsClient = attr.ib()
    settings: dict = attr.ib(default=attr.Factory(dict))
    conformance_classes: List[str] = attr.ib(
        default=attr.Factory(lambda: CATALOGS_CONFORMANCE_CLASSES)
    )
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)

    def register(self, app: FastAPI, settings=None) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.
            settings: extension settings.
        """
        if self.client is None:
            raise ValueError("CatalogsExtension requires a client to be set")
        self.settings = settings or {}
        self.router = APIRouter()

        self.router.add_api_route(
            path="/catalogs",
            endpoint=self.client.get_catalogs,
            methods=["GET"],
            response_model=Catalogs,
            response_class=self.response_class,
            summary="Get All Catalogs",
            description="Returns a list of all catalogs in the database.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs",
            endpoint=self.client.create_catalog,
            methods=["POST"],
            response_model=Catalog,
            response_class=self.response_class,
            status_code=HTTP_201_CREATED,
            summary="Create Catalog",
            description="Create a new STAC catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}",
            endpoint=self.client.get_catalog,
            methods=["GET"],
            response_model=Catalog,
            response_class=self.response_class,
            summary="Get Catalog",
            description="Get a specific STAC catalog by ID.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}",
            endpoint=self.client.update_catalog,
            methods=["PUT"],
            response_model=Catalog,
            response_class=self.response_class,
            summary="Update Catalog",
            description="Update an existing STAC catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}",
            endpoint=self.client.delete_catalog,
            methods=["DELETE"],
            response_class=self.response_class,
            status_code=HTTP_204_NO_CONTENT,
            summary="Delete Catalog",
            description="Delete a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections",
            endpoint=self.client.get_catalog_collections,
            methods=["GET"],
            response_model=Collections,
            response_class=self.response_class,
            summary="Get Catalog Collections",
            description="Get collections linked from a specific catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections",
            endpoint=self.client.create_catalog_collection,
            methods=["POST"],
            response_model=Collection,
            response_class=self.response_class,
            status_code=HTTP_201_CREATED,
            summary="Create Catalog Collection",
            description="Create a new collection and link it to a specific catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections/{collection_id}",
            endpoint=self.client.get_catalog_collection,
            methods=["GET"],
            response_model=Collection,
            response_class=self.response_class,
            summary="Get Catalog Collection",
            description="Get a specific collection from a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections/{collection_id}",
            endpoint=self.client.unlink_catalog_collection,
            methods=["DELETE"],
            response_class=self.response_class,
            status_code=HTTP_204_NO_CONTENT,
            summary="Unlink Collection from Catalog",
            description=(
                "Removes the link between the catalog and collection. "
                "The Collection data is NOT deleted."
            ),
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections/{collection_id}/items",
            endpoint=self.client.get_catalog_collection_items,
            methods=["GET"],
            response_model=ItemCollection,
            response_class=self.response_class,
            summary="Get Catalog Collection Items",
            description="Get items from a collection in a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections/{collection_id}/items/{item_id}",
            endpoint=self.client.get_catalog_collection_item,
            methods=["GET"],
            response_model=Item,
            response_class=self.response_class,
            summary="Get Catalog Collection Item",
            description="Get a specific item from a collection in a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/catalogs",
            endpoint=self.client.get_sub_catalogs,
            methods=["GET"],
            response_model=Catalogs,
            response_class=self.response_class,
            summary="Get Catalog Sub-Catalogs",
            description="Get sub-catalogs linked from a specific catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/catalogs",
            endpoint=self.client.create_sub_catalog,
            methods=["POST"],
            response_model=Catalog,
            response_class=self.response_class,
            status_code=HTTP_201_CREATED,
            summary="Create Catalog Sub-Catalog",
            description=(
                "Create a new catalog and link it as a sub-catalog "
                "of a specific catalog."
            ),
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/children",
            endpoint=self.client.get_catalog_children,
            methods=["GET"],
            response_model=Children,
            response_class=self.response_class,
            summary="Get Catalog Children",
            description=(
                "Retrieve all children (Catalogs and Collections) " "of this catalog."
            ),
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/conformance",
            endpoint=self.client.get_catalog_conformance,
            methods=["GET"],
            response_class=self.response_class,
            summary="Get Catalog Conformance",
            description="Get conformance classes specific to this sub-catalog.",
            tags=["Catalogs"],
            responses={
                HTTP_200_OK: {"description": "Conformance classes for the catalog"}
            },
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/queryables",
            endpoint=self.client.get_catalog_queryables,
            methods=["GET"],
            response_class=self.response_class,
            summary="Get Catalog Queryables",
            description=(
                "Get queryable fields available for filtering in this "
                "sub-catalog (Filter Extension)."
            ),
            tags=["Catalogs"],
            responses={HTTP_200_OK: {"description": "Queryable fields for the catalog"}},
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/catalogs/{sub_catalog_id}",
            endpoint=self.client.unlink_sub_catalog,
            methods=["DELETE"],
            response_class=self.response_class,
            status_code=HTTP_204_NO_CONTENT,
            summary="Unlink Sub-Catalog",
            description=(
                "Unlink a sub-catalog from its parent. "
                "Does not delete the sub-catalog."
            ),
            tags=["Catalogs"],
        )

        app.include_router(self.router, tags=["Catalogs"])
