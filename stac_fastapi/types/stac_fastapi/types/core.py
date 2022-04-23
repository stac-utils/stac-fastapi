"""Base clients."""
import abc
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import attr
from fastapi import Request
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
    """Defines an interface for implementing the STAC API transaction extension.

    The transaction extension adds support for creating, editing, and deletion
    of items and collections through several RESTful endpoints.  The interface
    requires implementing one method for each endpoint in the extension.
    """

    @abc.abstractmethod
    def create_item(
        self, item: stac_types.Item, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: The item.

        Returns:
            Item: The item that was created.

        """
        ...

    @abc.abstractmethod
    def update_item(
        self, item: stac_types.Item, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected that this
        item already exists.  The update should do a diff against the saved item and
        perform any necessary updates.  Partial updates are not supported by the transactions
        extension.

        Args:
            item: The item (must be complete).

        Returns:
            Item: The updated item.
        """
        ...

    @abc.abstractmethod
    def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collection_id}/items/{item_id}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            Item: The deleted item.
        """
        ...

    @abc.abstractmethod
    def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            collection: The collection.

        Returns:
            Collection: The collection that was created.
        """
        ...

    @abc.abstractmethod
    def update_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this collection already
        exists.  The update should do a diff against the existing collection and
        perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection: The collection (must be complete)

        Returns:
            Collection: The updated collection.
        """
        ...

    @abc.abstractmethod
    def delete_collection(
        self, collection_id: str, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection: The deleted collection.
        """
        ...


@attr.s  # type:ignore
class AsyncBaseTransactionsClient(abc.ABC):
    """Defines an interface for implementing the STAC API transaction extension.

    The transaction extension adds support for creating, editing, and deletion
    of items and collections through several RESTful endpoints.  The interface
    requires implementing one method for each endpoint in the extension.

    This is the same interface as :class:`stac_fastapi.types.core.BaseTransactionsClient`
    but implements async/await syntax.
    """

    @abc.abstractmethod
    async def create_item(
        self, item: stac_types.Item, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Create a new item.

        Called with `POST /collections/{collection_id}/items`.

        Args:
            item: The item.

        Returns:
            Item: The item that was created.

        """
        ...

    @abc.abstractmethod
    async def update_item(
        self, item: stac_types.Item, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Perform a complete update on an existing item.

        Called with `PUT /collections/{collection_id}/items`. It is expected that this
        item already exists.  The update should do a diff against the saved item and
        perform any necessary updates.  Partial updates are not supported by the transactions
        extension.

        Args:
            item: The item (must be complete).

        Returns:
            Item: The updated item.
        """
        ...

    @abc.abstractmethod
    async def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> Optional[Union[stac_types.Item, Response]]:
        """Delete an item from a collection.

        Called with `DELETE /collections/{collection_id}/items/{item_id}`

        Args:
            item_id: id of the item.
            collection_id: id of the collection.

        Returns:
            Item: The deleted item.
        """
        ...

    @abc.abstractmethod
    async def create_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Create a new collection.

        Called with `POST /collections`.

        Args:
            collection: The collection.

        Returns:
            Collection: The collection that was created.
        """
        ...

    @abc.abstractmethod
    async def update_collection(
        self, collection: stac_types.Collection, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Perform a complete update on an existing collection.

        Called with `PUT /collections`. It is expected that this collection already
        exists.  The update should do a diff against the existing collection and
        perform any necessary updates.  Partial updates are not supported by the
        transactions extension.

        Args:
            collection: The collection (must be complete)

        Returns:
            Collection: The updated collection.
        """
        ...

    @abc.abstractmethod
    async def delete_collection(
        self, collection_id: str, **kwargs
    ) -> Optional[Union[stac_types.Collection, Response]]:
        """Delete a collection.

        Called with `DELETE /collections/{collection_id}`

        Args:
            collection_id: id of the collection.

        Returns:
            Collection: The deleted collection.
        """
        ...


@attr.s
class LandingPageMixin(abc.ABC):
    """Create a STAC landing page (GET /).

    Attributes:
        stac_version: The STAC version implemented by the API, defaults
            to 1.0.0.
        landing_page_id: The id of the catalog.
        title: The title of the catalog.
        description: The description of the catalog.
    """

    stac_version: str = attr.ib(default=STAC_VERSION)
    landing_page_id: str = attr.ib(default="stac-fastapi")
    title: str = attr.ib(default="stac-fastapi")
    description: str = attr.ib(default="stac-fastapi")

    def _landing_page(
        self,
        base_url: str,
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
                    "href": base_url,
                },
                {
                    "rel": Relations.root.value,
                    "type": MimeTypes.json,
                    "href": base_url,
                },
                {
                    "rel": "data",
                    "type": MimeTypes.json,
                    "href": urljoin(base_url, "collections"),
                },
                {
                    "rel": Relations.conformance.value,
                    "type": MimeTypes.json,
                    "title": "STAC/WFS3 conformance classes implemented by this server",
                    "href": urljoin(base_url, "conformance"),
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson,
                    "title": "STAC search",
                    "href": urljoin(base_url, "search"),
                    "method": "GET",
                },
                {
                    "rel": Relations.search.value,
                    "type": MimeTypes.geojson,
                    "title": "STAC search",
                    "href": urljoin(base_url, "search"),
                    "method": "POST",
                },
            ],
            stac_extensions=extension_schemas,
        )
        return landing_page


@attr.s  # type:ignore
class BaseCoreClient(LandingPageMixin, abc.ABC):
    """Defines an interface for implementing the STAC API - Core Conformance class.

    The Core Conformance class defines a set of endpoint that must be implemented
    by an API to be considered compliant.  The core spec has been split apart
    since the time this interface was written.  It also implements the OAF Features
    and ItemSearch conformance classes in addition to Core.

    The interface requires implementing one method for each method in these conformance
    classes.

    Attributes:
        base_conformance_classes: The set of conformance classes implemented by
            the API not including extensions.
        extensions: The list of API extensions implemented by the API.
        post_request_model: The pydantic model used to serialize and validate
            request bodies required by ItemSearch.
    """

    base_conformance_classes: List[str] = attr.ib(
        factory=lambda: BASE_CONFORMANCE_CLASSES
    )
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    post_request_model = attr.ib(default=BaseSearchPostRequest)

    def conformance_classes(self) -> List[str]:
        """Generates a list of conformance classes used by the API.

        The final list of classes is generated by combining the `base_conformance_classes`
        with any conformance classes from extensions implemented by the API.

        Returns:
            List[str]: A list of conformance classes (http(s) references).
        """
        base_conformance_classes = self.base_conformance_classes.copy()

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            base_conformance_classes.extend(extension_classes)

        return list(set(base_conformance_classes))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if the given extension is enabled.

        Allows the API to determine if an extension is enabled within an
        active request.

        Args:
            extension: The extension to check.

        Returns:
            bool: True if enabled, otherwise False.
        """
        return any([type(ext).__name__ == extension for ext in self.extensions])

    def landing_page(self, **kwargs) -> stac_types.LandingPage:
        """Landing page.

        The landing page is a STAC Catalog which serves as an entrypoint into
        the API.  It allows the caller to browse through the API by following
        links, perform spatio-temporal searches into the STAC through search
        requests, and links to important metadata describing the specific
        API implementation such as conformance classes, STAC version, and
        available extensions.

        Called with `GET /`.

        Returns:
            LandingPage: An API landing page, serving as the entrypoint to the API.
        """
        extension_schemas = [
            schema.schema_href for schema in self.extensions if schema.schema_href
        ]

        # Create the initial landing page
        request: Request = kwargs["request"]
        base_url = str(request.base_url)
        landing_page = self._landing_page(
            base_url=base_url,
            conformance_classes=self.conformance_classes(),
            extension_schemas=extension_schemas,
        )

        # Add Collections links
        collections = self.all_collections(request=kwargs["request"])
        for collection in collections["collections"]:
            landing_page["links"].append(
                {
                    "rel": Relations.child.value,
                    "type": MimeTypes.json.value,
                    "title": collection.get("title") or collection.get("id"),
                    "href": urljoin(base_url, f"collections/{collection['id']}"),
                }
            )

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

    def conformance(self, **kwargs) -> stac_types.Conformance:
        """Conformance classes.

        Called with `GET /conformance`.

        Returns:
            Conformance: Conformance classes implemented by the server.
        """
        return Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
    ) -> stac_types.ItemCollection:
        """Cross collection search (POST).

        Enables spatio-temporal queries into the STAC with support for additional
        behavior like sorting, pagination, and query-by-attribute through several
        STAC API extensions.  Please refer to the STAC API spec for expected behavior
        and search semantics.

        Called with `POST /search`.

        Args:
            search_request: Search request parameters.

        Returns:
            ItemCollection: A set of items matching the search criteria.
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

        Enables spatio-temporal queries into the STAC with support for additional
        behavior like sorting, pagination, and query-by-attribute through several
        STAC API extensions.  Please refer to the STAC API spec for expected behavior
        and search semantics.

        Called with `GET /search`.

        Args:
            collections: The list of collections to search across.
            ids: The list of item ids to search across.
            bbox: Bounding box used as spatial filter.
            datetime: Single datetime or daterange defining temporal window.
            limit: The number of items returned by the search request.
            query: Comparison operators used by the search (see STAC API - Item Search - Query Extension).
            token: A pagination token (see OGC API - Common - Part 2).
            fields: Determines what fields are included/excluded from the search
                response (see STAC API - Item Search - Fields Extension).
            sortby: Applies a sort to the returned items (see STAC API - Item Search - Sort Extension).

        Returns:
            ItemCollection: A set of items matching the search criteria.
        """
        ...

    @abc.abstractmethod
    def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac_types.Item:
        """Get item by id.

        Called with `GET /collections/{collection_id}/items/{item_id}`.

        Args:
            item_id: Id of the item.
            collection_id: Id of the collection.

        Returns:
            Item: The matching item.
        """
        ...

    @abc.abstractmethod
    def all_collections(self, **kwargs) -> stac_types.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            Collections: A list of collections.
        """
        ...

    @abc.abstractmethod
    def get_collection(self, collection_id: str, **kwargs) -> stac_types.Collection:
        """Get collection by id.

        Called with `GET /collections/{collection_id}`.

        Args:
            collection_id: Id of the collection.

        Returns:
            Collection: The matching collection.
        """
        ...

    @abc.abstractmethod
    def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None, **kwargs
    ) -> stac_types.ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collection_id}/items`

        Args:
            collection_id: Id of the collection.
            limit: Number of items to return.
            token: A pagination token (see OGC API - Common - Part 2).

        Returns:
            ItemCollection: A set of items belonging to the collection.
        """
        ...


@attr.s  # type:ignore
class AsyncBaseCoreClient(LandingPageMixin, abc.ABC):
    """Defines an interface for implementing the STAC API - Core Conformance class.

    The Core Conformance class defines a set of endpoint that must be implemented
    by an API to be considered compliant.  The core spec has been split apart
    since the time this interface was written.  It also implements the OAF Features
    and ItemSearch conformance classes in addition to Core.

    The interface requires implementing one method for each method in these conformance
    classes, and is the same as :class:`stac_fastapi.types.core.BaseCoreClient` but
    implements async/await syntax.

    Attributes:
        base_conformance_classes: The set of conformance classes implemented by
            the API not including extensions.
        extensions: The list of API extensions implemented by the API.
        post_request_model: The pydantic model used to serialize and validate
            request bodies required by ItemSearch.
    """

    base_conformance_classes: List[str] = attr.ib(
        factory=lambda: BASE_CONFORMANCE_CLASSES
    )
    extensions: List[ApiExtension] = attr.ib(default=attr.Factory(list))
    post_request_model = attr.ib(default=BaseSearchPostRequest)

    def conformance_classes(self) -> List[str]:
        """Generates a list of conformance classes used by the API.

        The final list of classes is generated by combining the `base_conformance_classes`
        with any conformance classes from extensions implemented by the API.

        Returns:
            List[str]: A list of conformance classes (http(s) references).
        """
        conformance_classes = self.base_conformance_classes.copy()

        for extension in self.extensions:
            extension_classes = getattr(extension, "conformance_classes", [])
            conformance_classes.extend(extension_classes)

        return list(set(conformance_classes))

    def extension_is_enabled(self, extension: str) -> bool:
        """Check if the given extension is enabled.

        Allows the API to determine if an extension is enabled within an
        active request.

        Args:
            extension: The extension to check.

        Returns:
            bool: True if enabled, otherwise False.
        """
        return any([type(ext).__name__ == extension for ext in self.extensions])

    async def landing_page(self, **kwargs) -> stac_types.LandingPage:
        """Landing page.

        The landing page is a STAC Catalog which serves as an entrypoint into
        the API.  It allows the caller to browse through the API by following
        links, perform spatio-temporal searches into the STAC through search
        requests, and links to important metadata describing the specific
        API implementation such as conformance classes, STAC version, and
        available extensions.

        Called with `GET /`.

        Returns:
            LandingPage: An API landing page, serving as the entrypoint to the API.
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
            Conformance: Conformance classes implemented by the server.
        """
        return Conformance(conformsTo=self.conformance_classes())

    @abc.abstractmethod
    async def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
    ) -> stac_types.ItemCollection:
        """Cross collection search (POST).

        Enables spatio-temporal queries into the STAC with support for additional
        behavior like sorting, pagination, and query-by-attribute through several
        STAC API extensions.  Please refer to the STAC API spec for expected behavior
        and search semantics.

        Called with `POST /search`.

        Args:
            search_request: Search request parameters.

        Returns:
            ItemCollection: A set of items matching the search criteria.
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

        Enables spatio-temporal queries into the STAC with support for additional
        behavior like sorting, pagination, and query-by-attribute through several
        STAC API extensions.  Please refer to the STAC API spec for expected behavior
        and search semantics.

        Called with `GET /search`.

        Args:
            collections: The list of collections to search across.
            ids: The list of item ids to search across.
            bbox: Bounding box used as spatial filter.
            datetime: Single datetime or daterange defining temporal window.
            limit: The number of items returned by the search request.
            query: Comparison operators used by the search (see STAC API - Item Search - Query Extension).
            token: A pagination token (see OGC API - Common - Part 2).
            fields: Determines what fields are included/excluded from the search
                response (see STAC API - Item Search - Fields Extension).
            sortby: Applies a sort to the returned items (see STAC API - Item Search - Sort Extension).

        Returns:
            ItemCollection: A set of items matching the search criteria.
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
            Item: The matching item.
        """
        ...

    @abc.abstractmethod
    async def all_collections(self, **kwargs) -> stac_types.Collections:
        """Get all available collections.

        Called with `GET /collections`.

        Returns:
            Collections: A list of collections.
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
            Collection: The matching collection.
        """
        ...

    @abc.abstractmethod
    async def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None, **kwargs
    ) -> stac_types.ItemCollection:
        """Get all items from a specific collection.

        Called with `GET /collections/{collection_id}/items`

        Args:
            collection_id: Id of the collection.
            limit: Number of items to return.
            token: A pagination token (see OGC API - Common - Part 2).

        Returns:
            ItemCollection: A set of items belonging to the collection.
        """
        ...


@attr.s
class AsyncBaseFiltersClient(abc.ABC):
    """Defines a pattern for implementing the STAC filter extension.

    The filter extension provides a more robust query language than what is
    provided by the STAC API - Item Search - Query extension using the CQL2
    standard.  This is the same as :class:`stac_fastapi.types.core.BaseFiltersClient`
    but implements async/await syntax.
    """

    async def get_queryables(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """Get the queryables available for the given collection.

        This base implementation returns a black queryable schema.  This is not allowed
        under OGC CQL but it is permitted by the STAC API Filter Extension.

        Args:
            collection_id: Id of the collection.

        Returns:
            Dict[str, Any]: Queryables available for the collection.
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
    """Defines a pattern for implementing the STAC filter extension.

    The filter extension provides a more robust query language than what is
    provided by the STAC API - Item Search - Query extension using the CQL2
    standard.
    """

    def get_queryables(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """Get the queryables available for the given collection.

        This base implementation returns a black queryable schema.  This is not allowed
        under OGC CQL but it is permitted by the STAC API Filter Extension.

        Args:
            collection_id: Id of the collection.

        Returns:
            Dict[str, Any]: Queryables available for the collection.
        """
        return {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "https://example.org/queryables",
            "type": "object",
            "title": "Queryables for Example STAC API",
            "description": "Queryable names for the example STAC API Item Search filter.",
            "properties": {},
        }
