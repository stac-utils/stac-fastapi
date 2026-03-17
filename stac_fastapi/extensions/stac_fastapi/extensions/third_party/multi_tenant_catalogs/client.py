"""Catalogs extension clients.

Link Strategy for v1.0.0-beta.4
================================

The v1.0.0-beta.4 specification introduces a refined link strategy to support
poly-hierarchy (multi-parenting) while maintaining clear contextual navigation
for UI clients like STAC Browser.

Key Principles:
--------------
1. **Single Parent Link**: Every resource MUST have exactly ONE rel="parent" link
   that represents the contextual navigation path the user took to reach it.

2. **Poly-Hierarchy via Related Links**: When a resource has multiple parents,
   the API MAY include rel="related" links to expose alternative parents.
   Implementations should filter these based on user permissions (RBAC).

3. **Canonical Links**: Scoped endpoints SHOULD include rel="canonical" links
   pointing to the global endpoint for the same resource.

4. **Duplicate Links**: Scoped endpoints MAY include rel="duplicate" links
   pointing to other scoped paths where the same resource exists.

Scoped vs. Global Routes:
------------------------
- **Scoped Routes** (/catalogs/{id}/collections/{col_id}):
  - rel="parent" points to the specific catalog in the path
  - Maintains breadcrumb trail for UI navigation
  - rel="canonical" points to global endpoint
  - rel="related" exposes other parents

- **Global Routes** (/collections/{col_id}):
  - rel="parent" points to the Global Root (/)
  - rel="related" MAY include all catalogs that claim this collection

Dynamic Link Generation:
-----------------------
Implementations SHOULD NOT persist static rel="parent" or rel="child" links
in the database. Instead, links should be dynamically generated at runtime
based on the requested endpoint to properly support poly-hierarchy and
maintain contextual navigation.
"""

import abc
from datetime import datetime
from typing import Literal

import attr
from fastapi import Request
from stac_pydantic.api.collections import Collections
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.item import Item
from stac_pydantic.item_collection import ItemCollection
from starlette.responses import Response

from .types import Catalogs, Children, ObjectUri


@attr.s
class AsyncBaseCatalogsClient(abc.ABC):
    """Defines an async pattern for implementing the STAC catalogs extension."""

    @abc.abstractmethod
    async def get_catalogs(
        self,
        limit: int | None = None,
        token: str | None = None,
        request: Request | None = None,
        **kwargs,
    ) -> Catalogs | Response:
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
        self, catalog: Catalog, request: Request | None = None, **kwargs
    ) -> Catalog | Response:
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
        self, catalog_id: str, request: Request | None = None, **kwargs
    ) -> Catalog | Response:
        """Get a specific catalog by ID.

        Link Strategy (v1.0.0-beta.4):
        - rel="parent": MUST point to exactly ONE immediate parent catalog.
          If top-level, points to the Global Root (/).
        - rel="related": If the catalog has multiple parents (poly-hierarchy),
          MAY include links to other parent catalogs (filtered by user permissions).
        - rel="child": MUST point to all immediate sub-catalogs and collections.
        - rel="root": MUST point to the Global Root (/).

        Implementations SHOULD dynamically generate these links at runtime based
        on the requested endpoint to support poly-hierarchy. Static linking is
        highly discouraged.

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
        request: Request | None = None,
        **kwargs,
    ) -> Catalog | Response:
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
        request: Request | None = None,
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
        request: Request | None = None,
        **kwargs,
    ) -> Collections | Response:
        """Get collections linked from a specific catalog.

        Link Strategy (v1.0.0-beta.4 - Scoped Route):
        To preserve contextual breadcrumb navigation in UI clients (e.g., STAC Browser):
        - rel="parent": MUST point exclusively to the specific catalog_id.
        - rel="related": MAY include links to other parent catalogs (poly-hierarchy).
        - rel="canonical": SHOULD point to the global /collections/{id} endpoint.
        - rel="duplicate": MAY point to other scoped paths for this collection.

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
        limit: int | None = None,
        token: str | None = None,
        request: Request | None = None,
        **kwargs,
    ) -> Catalogs | Response:
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
        catalog: Catalog | ObjectUri,
        request: Request | None = None,
        **kwargs,
    ) -> Catalog | Response:
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
        collection: Collection | ObjectUri,
        request: Request | None = None,
        **kwargs,
    ) -> Collection | Response:
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
        request: Request | None = None,
        **kwargs,
    ) -> Collection | Response:
        """Get a specific collection from a catalog (Scoped Route).

        Link Strategy (v1.0.0-beta.4 - Scoped Route):
        This endpoint provides contextual navigation within a specific catalog:
        - rel="self": MUST point to /catalogs/{catalog_id}/collections/{collection_id}.
        - rel="parent": MUST point exclusively to /catalogs/{catalog_id}.
        - rel="related": MAY include links to other parent catalogs (poly-hierarchy).
        - rel="canonical": SHOULD point to /collections/{collection_id} (global endpoint).
        - rel="duplicate": MAY point to other scoped paths where this collection exists.
        - rel="root": MUST point to the Global Root (/).

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
        request: Request | None = None,
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
        bbox: list[float] | None = None,
        datetime: str | datetime | None = None,
        limit: int | None = 10,
        token: str | None = None,
        request: Request | None = None,
        **kwargs,
    ) -> ItemCollection | Response:
        """Get items from a collection in a catalog with search support.

        Multiple filters are combined using AND logic. If both bbox and datetime
        are provided, only items matching both criteria are returned.

        Link Strategy (v1.0.0-beta.4 - Scoped Route):
        Links in the ItemCollection should maintain the scoped context:
        - rel="collection": MUST point to
          /catalogs/{catalog_id}/collections/{collection_id}.
        - rel="parent": MUST point to
          /catalogs/{catalog_id}/collections/{collection_id}.
        - rel="root": MUST point to the Global Root (/).

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
        request: Request | None = None,
        **kwargs,
    ) -> Item | Response:
        """Get a specific item from a collection in a catalog.

        Link Strategy (v1.0.0-beta.4 - Scoped Route):
        Links in the Item should maintain the scoped context:
        - rel="self": MUST point to
          /catalogs/{catalog_id}/collections/{collection_id}/items/{item_id}.
        - rel="collection": MUST point to
          /catalogs/{catalog_id}/collections/{collection_id}.
        - rel="parent": MUST point to
          /catalogs/{catalog_id}/collections/{collection_id}.
        - rel="root": MUST point to the Global Root (/).

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
        limit: int | None = None,
        token: str | None = None,
        type: Literal["Catalog", "Collection"] | None = None,
        request: Request | None = None,
        **kwargs,
    ) -> Children | Response:
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
        self, catalog_id: str, request: Request | None = None, **kwargs
    ) -> dict | Response:
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
        self, catalog_id: str, request: Request | None = None, **kwargs
    ) -> dict | Response:
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
        request: Request | None = None,
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
    """Defines a synchronous pattern for implementing the STAC catalogs extension.

    This is the base class for synchronous catalog client implementations.
    For async implementations, use AsyncBaseCatalogsClient instead.
    """

    pass
