"""Base clients."""

import abc
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import attr
from fastapi import Request
from geojson_pydantic.geometries import Geometry
from stac_pydantic.links import Relations
from stac_pydantic.shared import BBox, MimeTypes
from stac_pydantic.version import STAC_VERSION

from . import stac
from .config import ApiSettings
from .conformance import BASE_CONFORMANCE_CLASSES
from .extension import ApiExtension
from .requests import get_base_url
from .search import BaseSearchPostRequest

__all__ = [
    "NumType",
    "StacType",
    "LandingPageMixin",
    "BaseCoreClient",
    "AsyncBaseCoreClient",
]

NumType = Union[float, int]
StacType = Dict[str, Any]

api_settings = ApiSettings()


@attr.s
class LandingPageMixin(abc.ABC):
    """Create a STAC landing page (GET /)."""

    stac_version: str = attr.ib(default=STAC_VERSION)
    landing_page_id: str = attr.ib(default=api_settings.stac_fastapi_landing_id)
    title: str = attr.ib(default=api_settings.stac_fastapi_title)
    description: str = attr.ib(default=api_settings.stac_fastapi_description)

    def _landing_page(
        self,
        base_url: str,
        conformance_classes: List[str],
        extension_schemas: List[str],
    ) -> stac.LandingPage:
        landing_page = stac.LandingPage(
            type="Catalog",
            id=self.landing_page_id,
            title=self.title,
            description=self.description,
            stac_version=self.stac_version,
            conformsTo=conformance_classes,
            links=[
                {
                    "rel": Relations.self.value,
                    "type": MimeTypes.json.value,
                    "title": "This document",
                    "href": base_url,
                },
                {
                    "rel": Relations.root.value,
                    "type": MimeTypes.json.value,
                    "title": "Root",
                    "href": base_url,
                },
                {
                    "rel": Relations.data.value,
                    "type": MimeTypes.json.value,
                    "title": "Collections available for this Catalog",
                    "href": urljoin(base_url, "collections"),
                },
                {
                    "rel": Relations.conformance.value,
                    "type": MimeTypes.json.value,
                    "title": "STAC/OGC conformance classes implemented by this server",
                    "href": urljoin(base_url, "conformance"),
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson.value,
                    "title": "STAC search [GET]",
                    "href": urljoin(base_url, "search"),
                    "method": "GET",
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson.value,
                    "title": "STAC search [POST]",
                    "href": urljoin(base_url, "search"),
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

    def conformance_classes(self) -> List[str]:
        """Generate conformance classes by adding extension conformance to base
        conformance classes."""
        base_conformance_classes = self.base_conformance_classes.copy()

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            base_conformance_classes.extend(extension_classes)

        return sorted(list(set(base_conformance_classes)))

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

    def landing_page(self, **kwargs) -> stac.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        request: Request = kwargs["request"]
        base_url = get_base_url(request)

        landing_page = self._landing_page(
            base_url=base_url,
            conformance_classes=self.conformance_classes(),
            extension_schemas=[],
        )

        # Add Queryables link
        if self.extension_is_enabled("FilterExtension") or self.extension_is_enabled(
            "SearchFilterExtension"
        ):
            landing_page["links"].append(
                {
                    "rel": Relations.queryables.value,
                    "type": MimeTypes.jsonschema.value,
                    "title": "Queryables available for this Catalog",
                    "href": urljoin(base_url, "queryables"),
                }
            )

        # Add Aggregation links
        if self.extension_is_enabled("AggregationExtension"):
            landing_page["links"].extend(
                [
                    {
                        "rel": "aggregate",
                        "type": "application/json",
                        "title": "Aggregate",
                        "href": urljoin(base_url, "aggregate"),
                    },
                    {
                        "rel": "aggregations",
                        "type": "application/json",
                        "title": "Aggregations",
                        "href": urljoin(base_url, "aggregations"),
                    },
                ]
            )

        # Add OpenAPI URL
        landing_page["links"].append(
            {
                "rel": Relations.service_desc.value,
                "type": MimeTypes.openapi.value,
                "title": "OpenAPI service description",
                "href": str(request.url_for("openapi")),
            }
        )

        # Add human readable service-doc
        landing_page["links"].append(
            {
                "rel": Relations.service_doc.value,
                "type": MimeTypes.html.value,
                "title": "OpenAPI service documentation",
                "href": str(request.url_for("swagger_ui_html")),
            }
        )

        return stac.LandingPage(**landing_page)

    def conformance(self, **kwargs) -> stac.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        return stac.Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
    ) -> stac.ItemCollection:
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
        bbox: Optional[BBox] = None,
        intersects: Optional[Geometry] = None,
        datetime: Optional[str] = None,
        limit: Optional[int] = 10,
        **kwargs,
    ) -> stac.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
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
    def all_collections(self, **kwargs) -> stac.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    def get_collection(self, collection_id: str, **kwargs) -> stac.Collection:
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
        bbox: Optional[BBox] = None,
        datetime: Optional[str] = None,
        limit: int = 10,
        token: Optional[str] = None,
        **kwargs,
    ) -> stac.ItemCollection:
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

    def conformance_classes(self) -> List[str]:
        """Generate conformance classes by adding extension conformance to base
        conformance classes."""
        conformance_classes = self.base_conformance_classes.copy()

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            conformance_classes.extend(extension_classes)

        return sorted(list(set(conformance_classes)))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if an api extension is enabled."""
        return any([type(ext).__name__ == extension for ext in self.extensions])

    async def landing_page(self, **kwargs) -> stac.LandingPage:
        """Landing page.

        Called with `GET /`.

        Returns:
            API landing page, serving as an entry point to the API.
        """
        request: Request = kwargs["request"]
        base_url = get_base_url(request)

        landing_page = self._landing_page(
            base_url=base_url,
            conformance_classes=self.conformance_classes(),
            extension_schemas=[],
        )

        # Add Queryables link
        if self.extension_is_enabled("FilterExtension") or self.extension_is_enabled(
            "SearchFilterExtension"
        ):
            landing_page["links"].append(
                {
                    "rel": Relations.queryables.value,
                    "type": MimeTypes.jsonschema.value,
                    "title": "Queryables available for this Catalog",
                    "href": urljoin(base_url, "queryables"),
                    "method": "GET",
                }
            )

        # Add Aggregation links
        if self.extension_is_enabled("AggregationExtension"):
            landing_page["links"].extend(
                [
                    {
                        "rel": "aggregate",
                        "type": "application/json",
                        "title": "Aggregate",
                        "href": urljoin(base_url, "aggregate"),
                    },
                    {
                        "rel": "aggregations",
                        "type": "application/json",
                        "title": "Aggregations",
                        "href": urljoin(base_url, "aggregations"),
                    },
                ]
            )

        # Add OpenAPI URL
        landing_page["links"].append(
            {
                "rel": Relations.service_desc.value,
                "type": MimeTypes.openapi.value,
                "title": "OpenAPI service description",
                "href": str(request.url_for("openapi")),
            }
        )

        # Add human readable service-doc
        landing_page["links"].append(
            {
                "rel": Relations.service_doc.value,
                "type": MimeTypes.html.value,
                "title": "OpenAPI service documentation",
                "href": str(request.url_for("swagger_ui_html")),
            }
        )

        return stac.LandingPage(**landing_page)

    async def conformance(self, **kwargs) -> stac.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance classes which the server conforms to.
        """
        return stac.Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    async def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
    ) -> stac.ItemCollection:
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
        bbox: Optional[BBox] = None,
        intersects: Optional[Geometry] = None,
        datetime: Optional[str] = None,
        limit: Optional[int] = 10,
        **kwargs,
    ) -> stac.ItemCollection:
        """Cross catalog search (GET).

        Called with `GET /search`.

        Returns:
            ItemCollection containing items which match the search criteria.
        """
        ...

    @abc.abstractmethod
    async def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
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
    async def all_collections(self, **kwargs) -> stac.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            A list of collections.
        """
        ...

    @abc.abstractmethod
    async def get_collection(self, collection_id: str, **kwargs) -> stac.Collection:
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
        bbox: Optional[BBox] = None,
        datetime: Optional[str] = None,
        limit: int = 10,
        token: Optional[str] = None,
        **kwargs,
    ) -> stac.ItemCollection:
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
