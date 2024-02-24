"""Query extension."""

from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import QueryExtensionGetRequest, QueryExtensionPostRequest


@attr.s
class QueryExtension(ApiExtension):
    """Query Extension.

    The Query extension adds an additional `query` parameter to `/search` requests which
    allows the caller to perform queries against item metadata (ex. find all images with
    cloud cover less than 15%).
    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#query
    """

    GET = QueryExtensionGetRequest
    POST = QueryExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        factory=lambda: ["https://api.stacspec.org/v1.0.0/item-search#query"]
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
