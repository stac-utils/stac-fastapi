"""Query extension."""

from enum import Enum
from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import QueryExtensionGetRequest, QueryExtensionPostRequest


class QueryConformanceClasses(str, Enum):
    """Conformance classes for the Query extension.

    See https://github.com/stac-api-extensions/query
    """

    SEARCH = "https://api.stacspec.org/v1.0.0/item-search#query"
    ITEMS = "https://api.stacspec.org/v1.0.0/ogcapi-features#query"
    COLLECTIONS = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#query"


@attr.s
class QueryExtension(ApiExtension):
    """Query Extension.

    The Query extension adds an additional `query` parameter to `/search` requests which
    allows the caller to perform queries against item metadata (ex. find all images with
    cloud cover less than 15%).
    https://github.com/stac-api-extensions/query
    """

    GET = QueryExtensionGetRequest
    POST = QueryExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        factory=lambda: [
            QueryConformanceClasses.SEARCH,
        ]
    )
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
