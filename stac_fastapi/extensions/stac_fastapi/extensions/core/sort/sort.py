"""Sort extension."""

from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import SortExtensionGetRequest, SortExtensionPostRequest


@attr.s
class SortExtension(ApiExtension):
    """Sort Extension.

    The Sort extension adds the `sortby` parameter to the `/search` endpoint, allowing the
    caller to specify the sort order of the returned items.
    https://github.com/stac-api-extensions/sort
    """

    GET = SortExtensionGetRequest
    POST = SortExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        factory=lambda: ["https://api.stacspec.org/v1.0.0/item-search#sort"]
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
