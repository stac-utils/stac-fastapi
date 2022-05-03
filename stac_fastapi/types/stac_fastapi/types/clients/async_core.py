"""Base clients."""
import abc
import asyncio
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import attr
from fastapi import HTTPException, Request
from stac_pydantic.api import Search
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes

from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.clients.landing import LandingPageMixin
from stac_fastapi.types.conformance import (
    BASE_CONFORMANCE_CLASSES,
    BROWSEABLE_CONFORMANCE_CLASS,
    CHILDREN_CONFORMANCE_CLASS,
)
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.hierarchy import (
    BrowseableNode,
    browseable_catalog_link,
    browseable_catalog_page,
    browseable_collection_link,
    browseable_item_link,
    find_catalog,
)
from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Conformance

NumType = Union[float, int]
StacType = Dict[str, Any]


@attr.s  # type:ignore
class AsyncBaseCoreClient(LandingPageMixin, abc.ABC):
    """Defines a pattern for implementing STAC api core endpoints.

    Attributes:
        extensions: list of registered api extensions.
    """

    base_conformance_classes: List[str] = attr.ib(
        factory=lambda: BASE_CONFORMANCE_CLASSES
    )
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    post_request_model = attr.ib(default=BaseSearchPostRequest)
    hierarchy_definition: Optional[BrowseableNode] = attr.ib(default=None)

    def conformance_classes(self) -> List[str]:
        """Generate conformance classes by adding extension conformance to base conformance classes."""
        conformance_classes = self.base_conformance_classes.copy()

        # TODO: replace hierarchy_definition with a flag
        if self.hierarchy_definition is not None:
            conformance_classes.append(BROWSEABLE_CONFORMANCE_CLASS)
            conformance_classes.append(CHILDREN_CONFORMANCE_CLASS)

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            conformance_classes.extend(extension_classes)

        return list(set(conformance_classes))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if an api extension is enabled."""
        return any([type(ext).__name__ == extension for ext in self.extensions])

    async def landing_page(self, **kwargs) -> stac_types.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        request: Request = kwargs["request"]
        base_url = str(request.base_url)
        extension_schemas = [
            schema.schema_href for schema in self.extensions if schema.schema_href
        ]
        landing_page = self._landing_page(
            base_url=base_url,
            conformance_classes=self.conformance_classes(),
            extension_schemas=extension_schemas,
        )

        # Add Collections links
        collections = await self.all_collections(request=kwargs["request"])
        for collection in collections["collections"]:
            landing_page["links"].append(
                {
                    "rel": Relations.child.value,
                    "type": MimeTypes.json.value,
                    "title": collection.get("title") or collection.get("id"),
                    "href": urljoin(base_url, f"collections/{collection['id']}"),
                }
            )

        # Add links for children and browseable conformance
        if self.hierarchy_definition is not None:
            # Children
            landing_page["links"].append(
                {
                    "rel": Relations.children,
                    "type": MimeTypes.json.value,
                    "title": "Child collections and catalogs",
                    "href": urljoin(base_url, "children"),
                }
            )

            for child in self.hierarchy_definition["children"]:
                if "collection_id" in child:
                    landing_page["links"].append(
                        browseable_collection_link(child, base_url)
                    )
                if "catalog_id" in child:
                    landing_page["links"].append(
                        browseable_catalog_link(child, base_url, child["catalog_id"])
                    )
            for item in self.hierarchy_definition["items"]:
                landing_page["links"].append(browseable_item_link(item, base_url))

        # Add OpenAPI URL
        landing_page["links"].append(
            {
                "rel": "service-desc",
                "type": "application/vnd.oai.openapi+json;version=3.0",
                "title": "OpenAPI service description",
                "href": urljoin(base_url, request.app.openapi_url.lstrip("/")),
            }
        )

        # Add human readable service-doc
        landing_page["links"].append(
            {
                "rel": "service-doc",
                "type": "text/html",
                "title": "OpenAPI service documentation",
                "href": urljoin(base_url, request.app.docs_url.lstrip("/")),
            }
        )

        return landing_page

    async def conformance(self, **kwargs) -> stac_types.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        return Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    async def post_search(
        self, search_request: Search, **kwargs
    ) -> stac_types.ItemCollection:
        """Cross catalog search (POST).

        Called with `POST /search`.

        Args:
            search_request: search request parameters.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    async def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> stac_types.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    async def get_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        """Get item by id.

        Called with `GET /collections/{collection_id}/items/{item_id}`.

        Args:
            item_id: Id of the item.
            collection_id: Id of the collection.

        Returns:
            Item.
        """
        ...

    @abc.abstractmethod
    async def all_collections(self, **kwargs) -> stac_types.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    async def get_collection(
        self, collection_id: str, **kwargs
    ) -> stac_types.Collection:
        """Get collection by id.

        Called with `GET /collections/{collection_id}`.

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    async def get_root_children(self, **kwargs) -> stac_types.Children:
        """Get  children at root.

        Called with `GET /children`.

        Returns:
            Children.
        """
        request: Request = kwargs["request"]
        base_url = str(request.base_url)
        extension_schemas = [
            schema.schema_href for schema in self.extensions if schema.schema_href
        ]
        if self.hierarchy_definition:
            catalog_children = [
                browseable_catalog_page(
                    child,
                    base_url,
                    child["catalog_id"],
                    self.stac_version,
                    self.conformance_classes(),
                    extension_schemas,
                )
                for child in self.hierarchy_definition["children"]
                if "catalog_id" in child
            ]
        else:
            catalog_children = []
        collection_children = await self.all_collections(**kwargs)
        links = [
            {
                "rel": Relations.root.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.parent.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.self.value,
                "type": MimeTypes.json,
                "href": urljoin(base_url, "children"),
            },
        ]
        return stac_types.Children(
            children=catalog_children + collection_children["collections"], links=links
        )

    async def get_catalog_children(
        self, catalog_path: str, **kwargs
    ) -> stac_types.Children:
        """Get children by catalog path.

        Called with `GET /catalogs/{catalog_path}/children`.

        Args:
            catalog_path: Path through hierarchy to catalog.

        Returns:
            Children.
        """
        hierarchy = self.hierarchy_definition.copy()
        split_path = catalog_path.split("/")
        selected_catalog = find_catalog(hierarchy, split_path)
        request: Request = kwargs["request"]
        base_url = str(request.base_url)

        extension_schemas = [
            schema.schema_href for schema in self.extensions if schema.schema_href
        ]
        catalog_children = [
            browseable_catalog_page(
                child,
                base_url,
                child["catalog_id"],
                self.stac_version,
                self.conformance_classes(),
                extension_schemas,
            )
            for child in selected_catalog["children"]
            if "catalog_id" in child
        ]
        child_collection_ids = [
            child["collection_id"]
            for child in selected_catalog["children"]
            if "collection_id" in child
        ]
        all_collections = await self.all_collections(**kwargs)
        collection_children = [
            coll
            for coll in all_collections["collections"]
            if coll["id"] in child_collection_ids
        ]

        links = [
            {
                "rel": Relations.root.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.parent.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.self.value,
                "type": MimeTypes.json,
                "href": urljoin(base_url, "children"),
            },
        ]
        return stac_types.Children(
            children=catalog_children + collection_children, links=links
        )

    async def post_catalog_search(
        self, search_request: Search, **kwargs
    ) -> stac_types.ItemCollection:
        """Catalog refined search (POST).

        Called with `POST /search`.

        Args:
            search_request: search request parameters.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        # Pydantic is fine for specifying body parameters but proves difficult to
        # use for Path parameters. Here, the starlette request is inspected instead
        request_path = kwargs["request"]["path"]
        split_path = request_path.split("/")[2:-1]
        remaining_hierarchy = self.hierarchy_definition.copy()
        selected_catalog = find_catalog(remaining_hierarchy, split_path)
        if not selected_catalog:
            raise HTTPException(
                status_code=404, detail=f"Catalog at {'/'.join(split_path)} not found"
            )
        child_collections = [
            node["collection_id"]
            for node in selected_catalog["children"]
            if "collection_id" in node
        ]
        search_request.collections = child_collections
        return await self.post_search(search_request, **kwargs)

    async def get_catalog_search(
        self,
        catalog_path: str,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        query: Optional[str] = None,
        token: Optional[str] = None,
        fields: Optional[List[str]] = None,
        sortby: Optional[str] = None,
        **kwargs,
    ) -> stac_types.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        hierarchy = self.hierarchy_definition.copy()
        split_path = catalog_path.split("/")
        selected_catalog = find_catalog(hierarchy, split_path)
        if not selected_catalog:
            raise HTTPException(
                status_code=404, detail=f"Catalog at {'/'.join(split_path)} not found"
            )
        # What should we do with the collections provided by the user?
        # Xor/toggle search collections as gathered via the hierarchy? I'm guessing people would
        # be surprised by just about any behavior we pick. Maybe just ignore provided collections?
        child_collections = [
            node["collection_id"]
            for node in selected_catalog["children"]
            if "collection_id" in node
        ]
        print("CHILD COLLECTION IN SEARCH", child_collections)
        return await self.get_search(
            child_collections,
            ids,
            bbox,
            datetime,
            limit,
            query,
            token,
            fields,
            sortby,
            **kwargs,
        )

    async def get_catalog_collections(
        self, catalog_path: str, **kwargs
    ) -> stac_types.Collections:
        """Get all subcollections of a catalog.

        Called with `GET /catalogs/{catalog_path}/collections`.

        Args:
            catalog_path: The full path of the catalog in the browseable hierarchy.

        Returns:
            Collections.
        """
        remaining_hierarchy = self.hierarchy_definition.copy()
        split_path = catalog_path.split("/")
        selected_catalog = find_catalog(remaining_hierarchy, split_path)
        if not selected_catalog:
            raise HTTPException(
                status_code=404, detail=f"Catalog at {'/'.join(split_path)} not found"
            )
        child_collections_io = [
            self.get_collection(node["collection_id"], **kwargs)
            for node in selected_catalog["children"]
            if "collection_id" in node
        ]
        child_collections = await asyncio.gather(*child_collections_io)

        base_url = str(kwargs["request"].base_url).strip("/")
        links = [
            {
                "rel": Relations.root.value,
                "type": MimeTypes.json,
                "href": base_url,
            },
            {
                "rel": Relations.parent.value,
                "type": MimeTypes.json,
                "href": "/".join([base_url, "catalogs", catalog_path]),
            },
            {
                "rel": Relations.self.value,
                "type": MimeTypes.json,
                "href": "/".join([base_url, "catalogs", catalog_path, "collections"]),
            },
        ]
        return stac_types.Collections(collections=child_collections or [], links=links)

    async def get_catalog(self, catalog_path: str, **kwargs) -> stac_types.Catalog:
        """Get collection by id.

        Called with `GET /catalogs/{catalog_path}`.

        Args:
            catalog_path: The full path of the catalog in the browseable hierarchy.

        Returns:
            Catalog.
        """
        request: Request = kwargs["request"]
        base_url = str(request.base_url)
        split_path = catalog_path.split("/")
        remaining_hierarchy = self.hierarchy_definition.copy()
        selected_catalog = find_catalog(remaining_hierarchy, split_path)
        if not selected_catalog:
            raise HTTPException(
                status_code=404, detail=f"Catalog at {'/'.join(split_path)} not found"
            )

        extension_schemas = [
            schema.schema_href for schema in self.extensions if schema.schema_href
        ]

        return browseable_catalog_page(
            selected_catalog,
            base_url,
            catalog_path,
            self.stac_version,
            self.conformance_classes(),
            extension_schemas,
        )

    @abc.abstractmethod
    async def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None, **kwargs
    ) -> stac_types.ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collection_id}/items`

        Args:
            collection_id: id of the collection.
            limit: number of items to return.
            token: pagination token.

        Returns:
            An ItemCollection.
        """
        ...


@attr.s
class AsyncBaseFiltersClient(abc.ABC):
    """Defines a pattern for implementing the STAC filter extension."""

    async def get_queryables(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """Get the queryables available for the given collection_id.

        If collection_id is None, returns the intersection of all
        queryables over all collections.

        This base implementation returns a blank queryable schema. This is not allowed
        under OGC CQL but it is allowed by the STAC API Filter Extension

        https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#queryables
        """
        return {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "https://example.org/queryables",
            "type": "object",
            "title": "Queryables for Example STAC API",
            "description": "Queryable names for the example STAC API Item Search filter.",
            "properties": {},
        }


@attr.s
class BaseFiltersClient(abc.ABC):
    """Defines a pattern for implementing the STAC filter extension."""

    def get_queryables(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """Get the queryables available for the given collection_id.

        If collection_id is None, returns the intersection of all
        queryables over all collections.

        This base implementation returns a blank queryable schema. This is not allowed
        under OGC CQL but it is allowed by the STAC API Filter Extension

        https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#queryables
        """
        return {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "https://example.org/queryables",
            "type": "object",
            "title": "Queryables for Example STAC API",
            "description": "Queryable names for the example STAC API Item Search filter.",
            "properties": {},
        }
