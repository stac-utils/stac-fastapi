"""Transaction extension."""

from typing import List, Optional, Type, Union

import attr
from fastapi import APIRouter, Body, FastAPI
from stac_pydantic import Catalog, Collection, Item
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.models import CatalogUri, CollectionUri, ItemUri
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import AsyncBaseTransactionsClient, BaseTransactionsClient
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest


@attr.s
class PostItem(CollectionUri):
    """Create Item."""

    item: Union[stac_types.Item, stac_types.ItemCollection] = attr.ib(
        default=Body(None)
    )
    workspace: str = attr.ib(default=None)


@attr.s
class PostCatalog(CatalogUri):
    """Create Catalog."""

    catalog: Union[stac_types.Catalog] = attr.ib(default=Body(None))
    workspace: str = attr.ib(default=None)
    is_public: bool = attr.ib(default=False)

@attr.s
class PutCatalogStripped(CatalogUri):
    """Create Catalog."""

    workspace: str = attr.ib(default=None)
    is_public: bool = attr.ib(default=False)
    access_list: List[str] = attr.ib(default=[])


@attr.s
class PostBaseCatalog(APIRequest):
    """Create Catalog."""
    workspace: str = attr.ib(default=None)
    catalog: Union[stac_types.Catalog] = attr.ib(default=Body(None))
    is_public: bool = attr.ib(default=False)


@attr.s
class PutCollectionStripped(CollectionUri):
    """Update Collection."""

    workspace: str = attr.ib(default=None)
    is_public: bool = attr.ib(default=False)
    access_list: List[str] = attr.ib(default=[])


@attr.s
class PutCollection(PutCollectionStripped):
    """Update Collection."""

    collection: Union[stac_types.Collection] = attr.ib(default=Body(None))


@attr.s
class PostCollection(CatalogUri):
    """Create Collection."""

    collection: Union[stac_types.Collection] = attr.ib(default=Body(None))
    workspace: str = attr.ib(default=None)
    is_public: bool = attr.ib(default=False)

@attr.s
class PutItem(ItemUri):
    """Update Item."""

    item: stac_types.Item = attr.ib(default=Body(None))
    workspace: str = attr.ib(default=None)


@attr.s  # type:ignore
class DeleteItemUri(ItemUri):
    """Delete item."""

    workspace: str = attr.ib(default=None)


@attr.s  # type:ignore
class DeleteCollectionUri(CollectionUri):
    """Delete collection."""

    workspace: str = attr.ib(default=None)


@attr.s  # type:ignore
class DeleteCatalogUri(CatalogUri):
    """Delete catalog."""

    workspace: str = attr.ib(default=None)


@attr.s
class TransactionExtension(ApiExtension):
    """Transaction Extension.

    The transaction extension adds several endpoints which allow the creation,
    deletion, and updating of items and collections:
        POST /collections
        PUT /collections/{collection_id}
        DELETE /collections/{collection_id}
        POST /collections/{collection_id}/items
        PUT /collections/{collection_id}/items
        DELETE /collections/{collection_id}/items

    https://github.com/radiantearth/stac-api-spec/blob/master/ogcapi-features/extensions/transaction/README.md

    Attributes:
        client: CRUD application logic
    """

    client: Union[AsyncBaseTransactionsClient, BaseTransactionsClient] = attr.ib()
    settings: ApiSettings = attr.ib()
    conformance_classes: List[str] = attr.ib(
        factory=lambda: [
            "https://api.stacspec.org/v1.0.0-rc.3/ogcapi-features/extensions/transaction",
        ]
    )
    schema_href: Optional[str] = attr.ib(default=None)
    router: APIRouter = attr.ib(factory=APIRouter)
    response_class: Type[Response] = attr.ib(default=JSONResponse)

    def register_create_item(self):
        """Register create item endpoint (POST /catalogs/{catalog_id}/collections/{collection_id}/items)."""
        self.router.add_api_route(
            name="Create Item",
            path="/catalogs/{catalog_path:path}/collections/{collection_id}/items",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.create_item, PostItem),
        )

    def register_update_item(self):
        """Register update item endpoint (PUT
        /catalogs/{catalog_id}/collections/{collection_id}/items/{item_id})."""
        self.router.add_api_route(
            name="Update Item",
            path="/catalogs/{catalog_path:path}/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(self.client.update_item, PutItem),
        )

    def register_delete_item(self):
        """Register delete item endpoint (DELETE
        /catalogs/{catalog_id}/collections/{collection_id}/items/{item_id})."""
        self.router.add_api_route(
            name="Delete Item",
            path="/catalogs/{catalog_path:path}/collections/{collection_id}/items/{item_id}",
            response_model=Item if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_async_endpoint(self.client.delete_item, DeleteItemUri),
        )

    def register_create_collection(self):
        """Register create collection endpoint (POST /catalogs/{catalog_id}/collections)."""
        self.router.add_api_route(
            name="Create Collection",
            path="/catalogs/{catalog_path:path}/collection",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(
                self.client.create_collection, PostCollection
            ),
        )

    def register_update_collection(self):
        """Register update collection endpoint (PUT /catalogs/{catalog_id}/collections/{collection_id})."""
        self.router.add_api_route(
            name="Update Collection",
            path="/catalogs/{catalog_path:path}/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(
                self.client.update_collection, PutCollection
            ),
        )

    def register_delete_collection(self):
        """Register delete collection endpoint (DELETE /catalogs/{catalog_id}/collections/{collection_id})."""
        self.router.add_api_route(
            name="Delete Collection",
            path="/catalogs/{catalog_path:path}/collections/{collection_id}",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_async_endpoint(
                self.client.delete_collection, DeleteCollectionUri
            ),
        )

    def register_create_catalog(self):
        """Register create catalog endpoint (POST /catalogs)."""
        self.router.add_api_route(
            name="Create Catalog",
            path="/catalogs/{catalog_path:path}",
            response_model=Catalog if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.create_catalog, PostCatalog),
        )

    def register_create_base_catalog(self):
        """Register create base catalog endpoint (POST /catalogs)."""
        self.router.add_api_route(
            name="Create Base Catalog (internal only)",
            path="/catalogs",
            response_model=Catalog if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_async_endpoint(self.client.create_catalog, PostBaseCatalog),
        )

    def register_update_catalog(self):
        """Register update catalog endpoint (PUT /catalogs/{catalog_id})."""
        self.router.add_api_route(
            name="Update Catalog",
            path="/catalogs/{catalog_path:path}",
            response_model=Catalog if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(self.client.update_catalog, PostCatalog),
        )

    def register_delete_catalog(self):
        """Register delete collection endpoint (DELETE /catalogs/{catalog_id})."""
        self.router.add_api_route(
            name="Delete Catalog",
            path="/catalogs/{catalog_path:path}",
            response_model=Catalog if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["DELETE"],
            endpoint=create_async_endpoint(
                self.client.delete_catalog, DeleteCatalogUri
            ),
        )

    def register_update_catalog_access(self):
        """Register update collection endpoint (PUT /catalogs/{catalog_path})."""
        self.router.add_api_route(
            name="Update Catalog Access Control",
            path="/catalogs/{catalog_path:path}/access",
            response_model=Catalog if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(self.client.update_catalog_access_control, PutCatalogStripped),
        )

    def register_update_collection_access(self):
        """Register update collection endpoint (PUT /catalogs/{catalog_path}/collections/{collection_id})."""
        self.router.add_api_route(
            name="Update Collection Access Control",
            path="/catalogs/{catalog_path:path}/collections/{collection_id}/access",
            response_model=Collection if self.settings.enable_response_models else None,
            response_class=self.response_class,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["PUT"],
            endpoint=create_async_endpoint(
                self.client.update_collection_access_control, PutCollectionStripped
            ),
        )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix
        self.register_create_item()
        self.register_update_item()
        self.register_delete_item()
        self.register_create_collection()
        self.register_create_catalog()
        self.register_create_base_catalog()
        
        self.register_delete_collection()
        self.register_delete_catalog()
        self.register_update_collection_access()
        self.register_update_catalog_access()
        self.register_update_collection()
        self.register_update_catalog()
        app.include_router(self.router, tags=["Transaction Extension"])
