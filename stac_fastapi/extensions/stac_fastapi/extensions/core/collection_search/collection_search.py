"""Collection-Search extension."""

from enum import Enum
from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import CollectionSearchExtensionGetRequest


class ConformanceClasses(str, Enum):
    """Conformance classes for the Collection-Search extension.

    See
    https://github.com/stac-api-extensions/collection-search
    """

    COLLECTIONSEARCH = "https://api.stacspec.org/v1.0.0-rc.1/collection-search"
    BASIS = "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"
    FREETEXT = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text"
    FILTER = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#filter"
    QUERY = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#query"
    SORT = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#sort"
    FIELDS = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#fields"


@attr.s
class CollectionSearchExtension(ApiExtension):
    """Collection-Search Extension.

    The Collection-Search extension adds functionality to the `GET - /collections`
    endpoint which allows the caller to include or exclude specific from the API
    response.
    Registering this extension with the application has the added effect of
    removing the `ItemCollection` response model from the `/search` endpoint, as
    the Fields extension allows the API to return potentially invalid responses
    by excluding fields which are required by the STAC spec, such as geometry.

    https://github.com/stac-api-extensions/collection-search

    Attributes:
        conformance_classes (list): Defines the list of conformance classes for
            the extension
    """

    GET = CollectionSearchExtensionGetRequest
    POST = None

    conformance_classes: List[str] = attr.ib(
        default=[ConformanceClasses.COLLECTIONSEARCH, ConformanceClasses.BASIS]
    )
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app (fastapi.FastAPI): target FastAPI application.

        Returns:
            None
        """
        pass
