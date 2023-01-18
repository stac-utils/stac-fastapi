"""Base clients."""
import abc
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import attr
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from stac_pydantic.version import STAC_VERSION
from starlette.responses import Response

from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.conformance import BASE_CONFORMANCE_CLASSES
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import BaseSearchPostRequest
from stac_fastapi.types.stac import Conformance

NumType = Union[float, int]
StacType = Dict[str, Any]


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC API Transaction Extension."""

    @abc.abstractmethod
    def create_item(
        self, collection_id: str, item: stac_types.Item
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: the item
            collection_id: the id of the collection from the resource path

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    def update_item(
        self, collection_id: str, item_id: str, item: stac_types.Item
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            item: the item (must be complete)
            collection_id: the id of the collection from the resource path

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    def delete_item(
        self, item_id: str, collection_id: str
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collection_id}/items/{item_id}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    def create_collection(
        self, collection: stac_types.Collection
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            collection: the collection

        Returns:
            The collection that was created.
        """
        ...

    @abc.abstractmethod
    def update_collection(
        self, collection: stac_types.Collection
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this item already exists.  The update should do a diff
        against the saved collection and perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection: the collection (must be complete)
            collection_id: the id of the collection from the resource path

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    def delete_collection(
        self, collection_id: str
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...


@attr.s  # type:ignore
class AsyncBaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC transaction extension."""

    @abc.abstractmethod
    async def create_item(
        self, collection_id: str, item: stac_types.Item
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    async def update_item(
        self, collection_id: str, item_id: str, item: stac_types.Item
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            item: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    async def delete_item(
        self, item_id: str, collection_id: str
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collection_id}/items/{item_id}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    async def create_collection(
        self, collection: stac_types.Collection
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            collection: the collection

        Returns:
            The collection that was created.
        """
        ...

    @abc.abstractmethod
    async def update_collection(
        self, collection: stac_types.Collection
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this item already exists.  The update should do a diff
        against the saved collection and perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection: the collection (must be complete)

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    async def delete_collection(
        self, collection_id: str
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...


@attr.s
class LandingPageMixin(abc.ABC):
    """Create a STAC landing page (GET /)."""

    stac_version: str = attr.ib(default=STAC_VERSION)
    landing_page_id: str = attr.ib(default="stac-fastapi")
    title: str = attr.ib(default="stac-fastapi")
    description: str = attr.ib(default="stac-fastapi")

    def _landing_page(
        self,
        conformance_classes: List[str],
        extension_schemas: List[str],
    ) -> stac_types.LandingPage:
        landing_page = stac_types.LandingPage(
            type="Catalog",
            id=self.landing_page_id,
            title=self.title,
            description=self.description,
            stac_version=self.stac_version,
            conformsTo=conformance_classes,
            links=[
                {
                    "rel": Relations.self.value,
                    "type": MimeTypes.json,
                    "href": "/",
                },
                {
                    "rel": Relations.root.value,
                    "type": MimeTypes.json,
                    "href": "/",
                },
                {
                    "rel": "data",
                    "type": MimeTypes.json,
                    "href": "/collections",
                },
                {
                    "rel": Relations.conformance.value,
                    "type": MimeTypes.json,
                    "title": "STAC/WFS3 conformance classes implemented by this server",
                    "href": "/conformance",
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson,
                    "title": "STAC search",
                    "href": "/search",
                    "method": "GET",
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson,
                    "title": "STAC search",
                    "href": "/search",
                    "method": "POST",
                },
            ],
            stac_extensions=extension_schemas,
        )
        return landing_page


@attr.s  # type:ignore
class BaseCoreClient(LandingPageMixin, abc.ABC):
    """Defines a pattern for implementing STAC api core endpoints.

    Attributes:
        extensions: list of registered api extensions.
    """

    base_conformance_classes: List[str] = attr.ib(
        factory=lambda: BASE_CONFORMANCE_CLASSES
    )
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    post_request_model = attr.ib(default=BaseSearchPostRequest)

    def conformance_classes(self) -> List[str]:
        """Generate conformance classes by adding extension conformance to base conformance classes."""
        base_conformance_classes = self.base_conformance_classes.copy()

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            base_conformance_classes.extend(extension_classes)

        return list(set(base_conformance_classes))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if an api extension is enabled."""
        return any([type(ext).__name__ == extension for ext in self.extensions])

    def list_conformance_classes(self):
        """Return a list of conformance classes, including implemented extensions."""
        base_conformance = BASE_CONFORMANCE_CLASSES

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            base_conformance.extend(extension_classes)

        return base_conformance

    def landing_page(self) -> stac_types.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        landing_page = self._landing_page(
            conformance_classes=self.conformance_classes(),
            extension_schemas=[],
        )

        # Add Collections links
        collections = self.all_collections()
        for collection in collections["collections"]:
            landing_page["links"].append(
                {
                    "rel": Relations.child.value,
                    "type": MimeTypes.json.value,
                    "title": collection.get("title") or collection.get("id"),
                    "href": f"/collections/{collection['id']}",
                }
            )

        return landing_page

    def conformance(self) -> stac_types.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        return Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    def post_search(
        self, search_request: BaseSearchPostRequest
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
    def get_search(
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
    ) -> stac_types.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_item(self, item_id: str, collection_id: str) -> stac_types.Item:
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
    def all_collections(self) -> stac_types.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    def get_collection(self, collection_id: str) -> stac_types.Collection:
        """Get collection by id.

        Called with `GET /collections/{collection_id}`.

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    @abc.abstractmethod
    def item_collection(
        self,
        collection_id: str,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: int = 10,
        token: str = None,
        **kwargs,
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

    def conformance_classes(self) -> List[str]:
        """Generate conformance classes by adding extension conformance to base conformance classes."""
        conformance_classes = self.base_conformance_classes.copy()

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            conformance_classes.extend(extension_classes)

        return list(set(conformance_classes))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if an api extension is enabled."""
        return any([type(ext).__name__ == extension for ext in self.extensions])

    async def landing_page(self) -> stac_types.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        landing_page = self._landing_page(
            conformance_classes=self.conformance_classes(),
            extension_schemas=[],
        )
        collections = await self.all_collections()
        for collection in collections["collections"]:
            landing_page["links"].append(
                {
                    "rel": Relations.child.value,
                    "type": MimeTypes.json.value,
                    "title": collection.get("title") or collection.get("id"),
                    "href": f"collections/{collection['id']}",
                }
            )
        return landing_page

    async def conformance(self) -> stac_types.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        return Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    async def post_search(
        self, search_request: BaseSearchPostRequest
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
    ) -> stac_types.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    async def get_item(self, item_id: str, collection_id: str) -> stac_types.Item:
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
    async def all_collections(self) -> stac_types.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    async def get_collection(self, collection_id: str) -> stac_types.Collection:
        """Get collection by id.

        Called with `GET /collections/{collection_id}`.

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    @abc.abstractmethod
    async def item_collection(
        self,
        collection_id: str,
        bbox: Optional[List[NumType]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: int = 10,
        token: str = None,
        **kwargs,
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
        self, collection_id: Optional[str] = None
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

    def get_queryables(self, collection_id: Optional[str] = None) -> Dict[str, Any]:
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
