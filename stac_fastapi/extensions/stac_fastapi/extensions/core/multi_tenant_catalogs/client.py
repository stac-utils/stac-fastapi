"""Catalogs extension clients."""

import abc
from datetime import datetime
from typing import List, Literal, Optional, Union

import attr
from fastapi import Request
from stac_pydantic.api.collections import Collections
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.item import Item
from stac_pydantic.item_collection import ItemCollection

from .types import Catalogs, Children, ObjectUri


@attr.s
class AsyncBaseCatalogsClient(abc.ABC):
    """Defines an async pattern for implementing the STAC catalogs extension."""

    @abc.abstractmethod
    async def get_catalogs(
        self,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalogs:
        """Get all catalogs with pagination support.

        Args:
            limit: The maximum number of catalogs to return.
            token: Pagination token for the next page of results.
            request: Optional FastAPI request object.

        Returns:
            Catalogs object containing catalogs and pagination links.
        """
        ...

    @abc.abstractmethod
    async def create_catalog(
        self, catalog: Catalog, request: Optional[Request] = None, **kwargs
    ) -> Catalog:
        """Create a new catalog.

        Args:
            catalog: The catalog to create.
            request: Optional FastAPI request object.

        Returns:
            The created catalog.
        """
        ...

    @abc.abstractmethod
    async def get_catalog(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> Catalog:
        """Get a specific catalog by ID.

        Args:
            catalog_id: The ID of the catalog to retrieve.
            request: Optional FastAPI request object.

        Returns:
            The requested catalog.
        """
        ...

    @abc.abstractmethod
    async def update_catalog(
        self,
        catalog_id: str,
        catalog: Catalog,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalog:
        """Update an existing catalog.

        Args:
            catalog_id: The ID of the catalog to update.
            catalog: The updated catalog data.
            request: Optional FastAPI request object.

        Returns:
            The updated catalog.
        """
        ...

    @abc.abstractmethod
    async def delete_catalog(
        self,
        catalog_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> None:
        """Delete a catalog.

        Args:
            catalog_id: The ID of the catalog to delete.
            request: Optional FastAPI request object.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_collections(
        self,
        catalog_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Collections:
        """Get collections linked from a specific catalog.

        Args:
            catalog_id: The ID of the catalog.
            request: Optional FastAPI request object.

        Returns:
            Collections object containing collections linked from the catalog.
        """
        ...

    @abc.abstractmethod
    async def get_sub_catalogs(
        self,
        catalog_id: str,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalogs:
        """Get all sub-catalogs of a specific catalog with pagination.

        Args:
            catalog_id: The ID of the parent catalog.
            limit: Maximum number of results to return.
            token: Pagination token for cursor-based pagination.
            request: Optional FastAPI request object.

        Returns:
            A Catalogs response containing sub-catalogs with pagination links.
        """
        ...

    @abc.abstractmethod
    async def create_sub_catalog(
        self,
        catalog_id: str,
        catalog: Union[Catalog, ObjectUri],
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalog:
        """Create a new catalog or link an existing catalog as a sub-catalog.

        Supports two modes:
        - Mode A (Creation): Full Catalog JSON body with id that doesn't exist
          → creates new catalog
        - Mode B (Linking): Minimal body with just id of existing catalog
          → links as sub-catalog

        Logic:
        1. Verifies the parent catalog exists.
        2. If the sub-catalog already exists: Appends the parent ID to its
           parent_ids (enabling poly-hierarchy - a catalog can have multiple
           parents).
        3. If the sub-catalog is new: Creates it with parent_ids initialized
           to [catalog_id].

        Args:
            catalog_id: The ID of the parent catalog.
            catalog: The catalog to create or link (full Catalog or ObjectUri with id).
            request: Optional FastAPI request object.

        Returns:
            The created or linked catalog.
        """
        ...

    @abc.abstractmethod
    async def create_catalog_collection(
        self,
        catalog_id: str,
        collection: Union[Collection, ObjectUri],
        request: Optional[Request] = None,
        **kwargs,
    ) -> Collection:
        """Create a new collection or link an existing collection to catalog.

        Supports two modes:
        - Mode A (Creation): Full Collection JSON body with id that doesn't
          exist → creates new collection
        - Mode B (Linking): Minimal body with just id of existing collection
          → links to catalog

        Args:
            catalog_id: The ID of the catalog to link the collection to.
            collection: Create or link (full Collection or ObjectUri with id).
            request: Optional FastAPI request object.

        Returns:
            The created or linked collection.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_collection(
        self,
        catalog_id: str,
        collection_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Collection:
        """Get a specific collection from a catalog.

        Args:
            catalog_id: The ID of the catalog.
            collection_id: The ID of the collection.
            request: Optional FastAPI request object.

        Returns:
            The requested collection.
        """
        ...

    @abc.abstractmethod
    async def unlink_catalog_collection(
        self,
        catalog_id: str,
        collection_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> None:
        """Unlink a collection from a catalog.

        Removes the link between the catalog and collection.
        The Collection data is NOT deleted.

        Args:
            catalog_id: The ID of the catalog.
            collection_id: The ID of the collection.
            request: Optional FastAPI request object.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_collection_items(
        self,
        catalog_id: str,
        collection_id: str,
        bbox: Optional[List[float]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        token: Optional[str] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> ItemCollection:
        """Get items from a collection in a catalog with search support.

        Multiple filters are combined using AND logic. If both bbox and datetime
        are provided, only items matching both criteria are returned.

        Args:
            catalog_id: The ID of the catalog.
            collection_id: The ID of the collection.
            bbox: Bounding box to filter items [minx, miny, maxx, maxy].
            datetime: Datetime or datetime range to filter items.
            limit: Maximum number of items to return (default 10).
            token: Pagination token for cursor-based pagination.
            request: Optional FastAPI request object.

        Returns:
            ItemCollection containing items from the collection.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_collection_item(
        self,
        catalog_id: str,
        collection_id: str,
        item_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Item:
        """Get a specific item from a collection in a catalog.

        Args:
            catalog_id: The ID of the catalog.
            collection_id: The ID of the collection.
            item_id: The ID of the item.
            request: Optional FastAPI request object.

        Returns:
            The requested item.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_children(
        self,
        catalog_id: str,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        type: Optional[Literal["Catalog", "Collection"]] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Children:
        """Get all children (Catalogs and Collections) of a specific catalog.

        Args:
            catalog_id: The ID of the catalog.
            limit: Maximum number of results to return.
            token: Pagination token.
            type: Filter by resource type (Catalog or Collection).
            request: Optional FastAPI request object.

        Returns:
            Children object containing children and pagination links.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_conformance(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> dict:
        """Get conformance classes specific to this sub-catalog.

        Args:
            catalog_id: The ID of the catalog.
            request: Optional FastAPI request object.

        Returns:
            Dictionary containing conformance classes.
        """
        ...

    @abc.abstractmethod
    async def get_catalog_queryables(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> dict:
        """Get queryable fields available for filtering in this sub-catalog.

        Args:
            catalog_id: The ID of the catalog.
            request: Optional FastAPI request object.

        Returns:
            Dictionary containing queryable fields (Filter Extension).
        """
        ...

    @abc.abstractmethod
    async def unlink_sub_catalog(
        self,
        catalog_id: str,
        sub_catalog_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> None:
        """Unlink a sub-catalog from its parent.

        Args:
            catalog_id: The ID of the parent catalog.
            sub_catalog_id: The ID of the sub-catalog to unlink.
            request: Optional FastAPI request object.
        """
        ...


@attr.s
class BaseCatalogsClient(abc.ABC):
    """Defines a synchronous pattern for implementing the STAC catalogs extension."""

    @abc.abstractmethod
    def get_catalogs(
        self,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalogs:
        """Get all catalogs with pagination support."""
        ...

    @abc.abstractmethod
    def create_catalog(
        self, catalog: Catalog, request: Optional[Request] = None, **kwargs
    ) -> Catalog:
        """Create a new catalog."""
        ...

    @abc.abstractmethod
    def get_catalog(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> Catalog:
        """Get a specific catalog by ID."""
        ...

    @abc.abstractmethod
    def update_catalog(
        self,
        catalog_id: str,
        catalog: Catalog,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalog:
        """Update an existing catalog."""
        ...

    @abc.abstractmethod
    def delete_catalog(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> None:
        """Delete a catalog."""
        ...

    @abc.abstractmethod
    def get_catalog_collections(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> Collections:
        """Get collections linked from a specific catalog."""
        ...

    @abc.abstractmethod
    def get_sub_catalogs(
        self,
        catalog_id: str,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalogs:
        """Get all sub-catalogs of a specific catalog with pagination."""
        ...

    @abc.abstractmethod
    def create_sub_catalog(
        self,
        catalog_id: str,
        catalog: Union[Catalog, ObjectUri],
        request: Optional[Request] = None,
        **kwargs,
    ) -> Catalog:
        """Create a new catalog or link an existing catalog as a sub-catalog."""
        ...

    @abc.abstractmethod
    def create_catalog_collection(
        self,
        catalog_id: str,
        collection: Union[Collection, ObjectUri],
        request: Optional[Request] = None,
        **kwargs,
    ) -> Collection:
        """Create a new collection or link an existing collection to catalog."""
        ...

    @abc.abstractmethod
    def get_catalog_collection(
        self,
        catalog_id: str,
        collection_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Collection:
        """Get a specific collection from a catalog."""
        ...

    @abc.abstractmethod
    def unlink_catalog_collection(
        self,
        catalog_id: str,
        collection_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> None:
        """Unlink a collection from a catalog."""
        ...

    @abc.abstractmethod
    def get_catalog_collection_items(
        self,
        catalog_id: str,
        collection_id: str,
        bbox: Optional[List[float]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        token: Optional[str] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> ItemCollection:
        """Get items from a collection in a catalog with search support."""
        ...

    @abc.abstractmethod
    def get_catalog_collection_item(
        self,
        catalog_id: str,
        collection_id: str,
        item_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Item:
        """Get a specific item from a collection in a catalog."""
        ...

    @abc.abstractmethod
    def get_catalog_children(
        self,
        catalog_id: str,
        limit: Optional[int] = None,
        token: Optional[str] = None,
        type: Optional[Literal["Catalog", "Collection"]] = None,
        request: Optional[Request] = None,
        **kwargs,
    ) -> Children:
        """Get all children (Catalogs and Collections) of a specific catalog."""
        ...

    @abc.abstractmethod
    def get_catalog_conformance(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> dict:
        """Get conformance classes specific to this sub-catalog."""
        ...

    @abc.abstractmethod
    def get_catalog_queryables(
        self, catalog_id: str, request: Optional[Request] = None, **kwargs
    ) -> dict:
        """Get queryable fields available for filtering in this sub-catalog."""
        ...

    @abc.abstractmethod
    def unlink_sub_catalog(
        self,
        catalog_id: str,
        sub_catalog_id: str,
        request: Optional[Request] = None,
        **kwargs,
    ) -> None:
        """Unlink a sub-catalog from its parent."""
        ...
