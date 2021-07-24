"""Base clients."""
import abc
from datetime import datetime
from typing import Any, Dict, List, Optional, Type, Union
from urllib.parse import urljoin

import attr
from stac_pydantic.api import Search
from stac_pydantic.links import Relations
from stac_pydantic.shared import MimeTypes
from stac_pydantic.version import STAC_VERSION

from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.extension import ApiExtension

NumType = Union[float, int]
StacType = Dict[str, Any]


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC transaction extension."""

    @abc.abstractmethod
    def create_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Create a new item.

        Called with `POST /collections/{collectionId}/items`.

        Args:
            item: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    def update_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collectionId}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            item: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collectionId}/items/{itemId}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
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
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
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
    def delete_collection(self, collection_id: str, **kwargs) -> stac_types.Collection:
        """Delete a collection.

        Called with `DELETE /collections/{collectionId}`

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
    async def create_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Create a new item.

        Called with `POST /collections/{collectionId}/items`.

        Args:
            item: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    async def update_item(self, item: stac_types.Item, **kwargs) -> stac_types.Item:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collectionId}/items`. It is expected that this item already exists.  The update
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
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collectionId}/items/{itemId}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    async def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
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
        self, collection: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
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
        self, collection_id: str, **kwargs
    ) -> stac_types.Collection:
        """Delete a collection.

        Called with `DELETE /collections/{collectionId}`

        Args:
            collection_id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...


@attr.s
class LandingPageMixin:
    """Create a STAC landing page (GET /)."""

    stac_version: str = attr.ib(default=STAC_VERSION)
    landing_page_id: str = attr.ib(default="stac-fastapi")
    title: str = attr.ib(default="stac-fastapi")
    description: str = attr.ib(default="stac-fastapi")

    def _landing_page(self, base_url: str) -> stac_types.LandingPage:
        landing_page = stac_types.LandingPage(
            type="Catalog",
            id=self.landing_page_id,
            title=self.title,
            description=self.description,
            stac_version=self.stac_version,
            conformsTo=[
                "https://stacspec.org/STAC-api.html",
                "http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#ats_geojson",
            ],
            links=[
                {
                    "rel": Relations.self.value,
                    "type": MimeTypes.json,
                    "href": base_url,
                },
                {
                    "rel": "data",
                    "type": MimeTypes.json,
                    "href": urljoin(base_url, "collections"),
                },
                {
                    "rel": Relations.docs.value,
                    "type": MimeTypes.json,
                    "title": "OpenAPI docs",
                    "href": urljoin(base_url, "docs"),
                },
                {
                    "rel": Relations.conformance.value,
                    "type": MimeTypes.json,
                    "title": "STAC/WFS3 conformance classes implemented by this server",
                    "href": base_url,
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.json,
                    "title": "STAC search",
                    "href": urljoin(base_url, "search"),
                },
            ],
            stac_extensions=[],
        )
        return landing_page


@attr.s  # type:ignore
class BaseCoreClient(LandingPageMixin, abc.ABC):
    """Defines a pattern for implementing STAC api core endpoints.

    Attributes:
        extensions: list of registered api extensions.
    """

    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))

    def extension_is_enabled(self, extension: Type[ApiExtension]) -> bool:
        """Check if an api extension is enabled."""
        return any([isinstance(ext, extension) for ext in self.extensions])

    def landing_page(self, **kwargs) -> stac_types.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        base_url = str(kwargs["request"].base_url)
        landing_page = self._landing_page(base_url=base_url)
        collections = self.all_collections(request=kwargs["request"])
        for collection in collections:
            landing_page["links"].append(
                {
                    "rel": Relations.child.value,
                    "type": MimeTypes.json.value,
                    "title": collection["title"],
                    "href": urljoin(base_url, f"collections/{collection['id']}"),
                }
            )
        return landing_page

    @abc.abstractmethod
    def conformance(self, **kwargs) -> stac_types.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        ...

    @abc.abstractmethod
    def post_search(
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
        **kwargs,
    ) -> stac_types.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac_types.Item:
        """Get item by id.

        Called with `GET /collections/{collectionId}/items/{itemId}`.

        Args:
            item_id: Id of the item.
            collection_id: Id of the collection.

        Returns:
            Item.
        """
        ...

    @abc.abstractmethod
    def all_collections(self, **kwargs) -> List[stac_types.Collection]:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    def get_collection(self, collection_id: str, **kwargs) -> stac_types.Collection:
        """Get collection by id.

        Called with `GET /collections/{collectionId}`.

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    @abc.abstractmethod
    def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None, **kwargs
    ) -> stac_types.ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collectionId}/items`

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

    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))

    def extension_is_enabled(self, extension: Type[ApiExtension]) -> bool:
        """Check if an api extension is enabled."""
        return any([isinstance(ext, extension) for ext in self.extensions])

    async def landing_page(self, **kwargs) -> stac_types.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        base_url = str(kwargs["request"].base_url)
        landing_page = self._landing_page(base_url=base_url)
        collections = await self.all_collections(request=kwargs["request"])
        for collection in collections:
            landing_page["links"].append(
                {
                    "rel": Relations.child.value,
                    "type": MimeTypes.json.value,
                    "title": collection["title"],
                    "href": urljoin(base_url, f"collections/{collection['id']}"),
                }
            )
        return landing_page

    @abc.abstractmethod
    async def conformance(self, **kwargs) -> stac_types.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        ...

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

        Called with `GET /collections/{collectionId}/items/{itemId}`.

        Args:
            item_id: Id of the item.
            collection_id: Id of the collection.

        Returns:
            Item.
        """
        ...

    @abc.abstractmethod
    async def all_collections(self, **kwargs) -> List[stac_types.Collection]:
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

        Called with `GET /collections/{collectionId}`.

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    @abc.abstractmethod
    async def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None, **kwargs
    ) -> stac_types.ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collectionId}/items`

        Args:
            collection_id: id of the collection.
            limit: number of items to return.
            token: pagination token.

        Returns:
            An ItemCollection.
        """
        ...
