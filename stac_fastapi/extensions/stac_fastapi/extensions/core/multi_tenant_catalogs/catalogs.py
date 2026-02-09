"""Catalogs extension."""

from typing import Any, Dict, List, Literal, Optional, Type, Union

import attr
from fastapi import APIRouter, FastAPI, Query, Request
from fastapi.responses import JSONResponse
from stac_pydantic.api.collections import Collections
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.item import Item
from stac_pydantic.item_collection import ItemCollection
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import str2bbox

from .client import AsyncBaseCatalogsClient
from .types import Catalogs, Children, ObjectUri

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

    client: AsyncBaseCatalogsClient = attr.ib(default=None)
    settings: dict = attr.ib(default=attr.Factory(dict))
    conformance_classes: List[str] = attr.ib(
        default=attr.Factory(lambda: CATALOGS_CONFORMANCE_CLASSES)
    )
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)

    async def get_catalog_collection_items(
        self,
        catalog_id: str,
        collection_id: str,
        request: Request,
        bbox: Optional[str] = Query(
            None,
            description="Bounding box to filter items.",
        ),
        datetime: Optional[str] = Query(None, description="Datetime to filter items"),
        limit: int = Query(10, ge=1, le=10000, description="Maximum number of items"),
        token: Optional[str] = Query(None, description="Pagination token"),
    ) -> ItemCollection:
        """Get items from a collection in a catalog with search support."""
        bbox_list = list(str2bbox(bbox)) if bbox else None

        return await self.client.get_catalog_collection_items(
            catalog_id=catalog_id,
            collection_id=collection_id,
            bbox=bbox_list,
            datetime=datetime,
            limit=limit,
            token=token,
            request=request,
        )

    # --- WRAPPERS ---

    async def _get_catalogs_wrapper(
        self,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        request: Request = None,
    ) -> Catalogs:
        return await self.client.get_catalogs(limit=limit, token=token, request=request)

    async def _create_catalog_wrapper(
        self, catalog: Catalog, request: Request = None
    ) -> Catalog:
        return await self.client.create_catalog(catalog=catalog, request=request)

    async def _get_catalog_wrapper(
        self, catalog_id: str, request: Request = None
    ) -> Catalog:
        return await self.client.get_catalog(catalog_id=catalog_id, request=request)

    async def _update_catalog_wrapper(
        self, catalog_id: str, catalog: Catalog, request: Request = None
    ) -> Catalog:
        return await self.client.update_catalog(
            catalog_id=catalog_id, catalog=catalog, request=request
        )

    async def _delete_catalog_wrapper(
        self, catalog_id: str, request: Request = None
    ) -> None:
        return await self.client.delete_catalog(catalog_id=catalog_id, request=request)

    async def _get_catalog_collections_wrapper(
        self, catalog_id: str, request: Request = None
    ) -> Collections:
        return await self.client.get_catalog_collections(
            catalog_id=catalog_id, request=request
        )

    async def _get_sub_catalogs_wrapper(
        self,
        catalog_id: str,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        request: Request = None,
    ) -> Catalogs:
        return await self.client.get_sub_catalogs(
            catalog_id=catalog_id,
            limit=limit,
            token=token,
            request=request,
        )

    async def _create_sub_catalog_wrapper(
        self,
        catalog_id: str,
        catalog: Union[Catalog, ObjectUri],
        request: Request = None,
    ) -> Catalog:
        return await self.client.create_sub_catalog(
            catalog_id=catalog_id, catalog=catalog, request=request
        )

    async def _create_catalog_collection_wrapper(
        self,
        catalog_id: str,
        collection: Union[Collection, ObjectUri],
        request: Request = None,
    ) -> Collection:
        return await self.client.create_catalog_collection(
            catalog_id=catalog_id,
            collection=collection,
            request=request,
        )

    async def _get_catalog_collection_wrapper(
        self,
        catalog_id: str,
        collection_id: str,
        request: Request = None,
    ) -> Collection:
        return await self.client.get_catalog_collection(
            catalog_id=catalog_id,
            collection_id=collection_id,
            request=request,
        )

    async def _unlink_catalog_collection_wrapper(
        self,
        catalog_id: str,
        collection_id: str,
        request: Request = None,
    ) -> None:
        return await self.client.unlink_catalog_collection(
            catalog_id=catalog_id,
            collection_id=collection_id,
            request=request,
        )

    async def _get_catalog_collection_item_wrapper(
        self,
        catalog_id: str,
        collection_id: str,
        item_id: str,
        request: Request = None,
    ) -> Item:
        return await self.client.get_catalog_collection_item(
            catalog_id=catalog_id,
            collection_id=collection_id,
            item_id=item_id,
            request=request,
        )

    async def _get_catalog_children_wrapper(
        self,
        catalog_id: str,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        type: Optional[Literal["Catalog", "Collection"]] = None,
        request: Request = None,
    ) -> Children:
        return await self.client.get_catalog_children(
            catalog_id=catalog_id,
            limit=limit,
            token=token,
            type=type,
            request=request,
        )

    async def _get_catalog_conformance_wrapper(
        self, catalog_id: str, request: Request = None
    ) -> dict:
        return await self.client.get_catalog_conformance(
            catalog_id=catalog_id, request=request
        )

    async def _get_catalog_queryables_wrapper(
        self, catalog_id: str, request: Request = None
    ) -> dict:
        return await self.client.get_catalog_queryables(
            catalog_id=catalog_id, request=request
        )

    async def _unlink_sub_catalog_wrapper(
        self,
        catalog_id: str,
        sub_catalog_id: str,
        request: Request = None,
    ) -> None:
        return await self.client.unlink_sub_catalog(
            catalog_id=catalog_id,
            sub_catalog_id=sub_catalog_id,
            request=request,
        )

    def register(self, app: FastAPI, settings: Optional[Dict[str, Any]] = None) -> None:
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
            endpoint=self._get_catalogs_wrapper,
            methods=["GET"],
            response_model=Catalogs,
            response_class=self.response_class,
            summary="Get All Catalogs",
            description="Returns a list of all catalogs in the database.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs",
            endpoint=self._create_catalog_wrapper,
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
            endpoint=self._get_catalog_wrapper,
            methods=["GET"],
            response_model=Catalog,
            response_class=self.response_class,
            summary="Get Catalog",
            description="Get a specific STAC catalog by ID.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}",
            endpoint=self._update_catalog_wrapper,
            methods=["PUT"],
            response_model=Catalog,
            response_class=self.response_class,
            summary="Update Catalog",
            description="Update an existing STAC catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}",
            endpoint=self._delete_catalog_wrapper,
            methods=["DELETE"],
            response_class=self.response_class,
            status_code=HTTP_204_NO_CONTENT,
            summary="Delete Catalog",
            description="Delete a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections",
            endpoint=self._get_catalog_collections_wrapper,
            methods=["GET"],
            response_model=Collections,
            response_class=self.response_class,
            summary="Get Catalog Collections",
            description="Get collections linked from a specific catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections",
            endpoint=self._create_catalog_collection_wrapper,
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
            endpoint=self._get_catalog_collection_wrapper,
            methods=["GET"],
            response_model=Collection,
            response_class=self.response_class,
            summary="Get Catalog Collection",
            description="Get a specific collection from a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections/{collection_id}",
            endpoint=self._unlink_catalog_collection_wrapper,
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
            endpoint=self.get_catalog_collection_items,
            methods=["GET"],
            response_model=ItemCollection,
            response_class=self.response_class,
            summary="Get Catalog Collection Items",
            description="Get items from a collection in a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/collections/{collection_id}/items/{item_id}",
            endpoint=self._get_catalog_collection_item_wrapper,
            methods=["GET"],
            response_model=Item,
            response_class=self.response_class,
            summary="Get Catalog Collection Item",
            description="Get a specific item from a collection in a catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/catalogs",
            endpoint=self._get_sub_catalogs_wrapper,
            methods=["GET"],
            response_model=Catalogs,
            response_class=self.response_class,
            summary="Get Catalog Sub-Catalogs",
            description="Get sub-catalogs linked from a specific catalog.",
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/catalogs",
            endpoint=self._create_sub_catalog_wrapper,
            methods=["POST"],
            response_model=Catalog,
            response_class=self.response_class,
            status_code=HTTP_201_CREATED,
            summary="Create Catalog Sub-Catalog",
            description=(
                "Create a new catalog or link an existing catalog as a sub-catalog "
                "of a specific catalog."
            ),
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/children",
            endpoint=self._get_catalog_children_wrapper,
            methods=["GET"],
            response_model=Children,
            response_class=self.response_class,
            summary="Get Catalog Children",
            description=(
                "Retrieve all children (Catalogs and Collections) of this catalog."
            ),
            tags=["Catalogs"],
        )

        self.router.add_api_route(
            path="/catalogs/{catalog_id}/conformance",
            endpoint=self._get_catalog_conformance_wrapper,
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
            endpoint=self._get_catalog_queryables_wrapper,
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
            endpoint=self._unlink_sub_catalog_wrapper,
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
