"""Base clients."""
import abc
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import attr
from stac_pydantic import Collection, Item, ItemCollection
from stac_pydantic.api import ConformanceClasses, LandingPage, Search
from stac_pydantic.shared import Link, MimeTypes, Relations
from stac_pydantic.version import STAC_VERSION

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.links import CollectionLinks

NumType = Union[float, int]


@attr.s  # type:ignore
class BaseTransactionsClient(abc.ABC):
    """Defines a pattern for implementing the STAC transaction extension."""

    @abc.abstractmethod
    def create_item(self, model: Item, **kwargs) -> Item:
        """Create a new item.

        Called with `POST /collections/{collectionId}/items`.

        Args:
            model: the item

        Returns:
            The item that was created.

        """
        ...

    @abc.abstractmethod
    def update_item(self, model: Item, **kwargs) -> Item:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collectionId}/items`. It is expected that this item already exists.  The update
        should do a diff against the saved item and perform any necessary updates.  Partial updates are not supported
        by the transactions extension.

        Args:
            model: the item (must be complete)

        Returns:
            The updated item.
        """
        ...

    @abc.abstractmethod
    def delete_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collectionId}/items/{itemId}`

        Args:
            id: id of the item.

        Returns:
            The deleted item.
        """
        ...

    @abc.abstractmethod
    def create_collection(self, model: Collection, **kwargs) -> Collection:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            model: the collection

        Returns:
            The collection that was created.
        """
        ...

    @abc.abstractmethod
    def update_collection(self, model: Collection, **kwargs) -> Collection:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this item already exists.  The update should do a diff
        against the saved collection and perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            model: the collection (must be complete)

        Returns:
            The updated collection.
        """
        ...

    @abc.abstractmethod
    def delete_collection(self, id: str, **kwargs) -> Collection:
        """Delete a collection.

        Called with `DELETE /collections/{collectionId}`

        Args:
            id: id of the collection.

        Returns:
            The deleted collection.
        """
        ...


@attr.s  # type:ignore
class BaseCoreClient(abc.ABC):
    """Defines a pattern for implementing STAC api core endpoints.

    Attributes:
        extensions: list of registered api extensions.
    """

    stac_version: str = attr.ib(default=STAC_VERSION)
    landing_page_id: str = attr.ib(default="stac-fastapi")
    title: str = attr.ib(default="stac-fastapi")
    description: str = attr.ib(default="stac-fastapi")
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if an api extension is enabled."""
        return any([type(ext).__name__ == extension for ext in self.extensions])

    def list_conformance_classes(self):
        """Return a list of conformance classes, including implemented extensions."""
        base_conformance = [
            "https://stacspec.org/STAC-api.html",
            "http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#ats_geojson",
        ]

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            base_conformance.extend(extension_classes)

        return base_conformance

    def landing_page(self, **kwargs) -> LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        base_url = str(kwargs["request"].base_url)
        landing_page = LandingPage(
            id=self.landing_page_id,
            title=self.title,
            description=self.description,
            conformsTo=self.list_conformance_classes(),
            stac_version=self.stac_version,
            links=[
                Link(
                    rel=Relations.self,
                    type=MimeTypes.json,
                    href=base_url,
                ),
                Link(
                    rel="data",
                    type=MimeTypes.json,
                    href=urljoin(base_url, "collections"),
                ),
                Link(
                    rel=Relations.docs,
                    type=MimeTypes.html,
                    title="OpenAPI docs",
                    href=urljoin(str(base_url), "docs"),
                ),
                Link(
                    rel=Relations.conformance,
                    type=MimeTypes.json,
                    title="STAC/WFS3 conformance classes implemented by this server",
                    href=urljoin(str(base_url), "conformance"),
                ),
                Link(
                    rel=Relations.search,
                    type=MimeTypes.geojson,
                    title="STAC search",
                    href=urljoin(str(base_url), "search"),
                ),
            ],
        )

        if self.extension_is_enabled("FilterExtension"):
            landing_page.links.append(
                Link(
                    rel="http://www.opengis.net/def/rel/ogc/1.0/queryables",
                    type=MimeTypes.geojson,
                    title="Filter Queryables",
                    href=urljoin(str(base_url), "queryables"),
                )
            )

        collections = self.all_collections(request=kwargs["request"])
        for coll in collections:
            coll_link = CollectionLinks(
                collection_id=coll.id, base_url=str(base_url)
            ).self()
            coll_link.rel = Relations.child
            coll_link.title = coll.title
            landing_page.links.append(coll_link)
        return landing_page

    @abc.abstractmethod
    def conformance(self, **kwargs) -> ConformanceClasses:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        ...

    @abc.abstractmethod
    def post_search(self, search_request: Search, **kwargs) -> Dict[str, Any]:
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
        **kwargs
    ) -> Dict[str, Any]:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_item(self, item_id: str, collection_id: str, **kwargs) -> Item:
        """Get item by id.

        Called with `GET /collections/{collectionId}/items/{itemId}`.

        Args:
            id: Id of the item.

        Returns:
            Item.
        """
        ...

    @abc.abstractmethod
    def all_collections(self, **kwargs) -> List[Collection]:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    def get_collection(self, id: str, **kwargs) -> Collection:
        """Get collection by id.

        Called with `GET /collections/{collectionId}`.

        Args:
            id: Id of the collection.

        Returns:
            Collection.
        """
        ...

    @abc.abstractmethod
    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collectionId}/items`

        Args:
            id: id of the collection.
            limit: number of items to return.
            token: pagination token.

        Returns:
            An ItemCollection.
        """
        ...


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
