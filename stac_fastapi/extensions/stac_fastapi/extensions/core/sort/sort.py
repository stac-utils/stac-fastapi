"""Sort extension."""

from enum import Enum
from typing import List, Optional, Type

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest

from .request import SortExtensionGetRequest, SortExtensionPostRequest


class SortConformanceClasses(str, Enum):
    """Conformance classes for the Sort extension.

    See https://github.com/stac-api-extensions/sort

    """

    SEARCH = "https://api.stacspec.org/v1.0.0/item-search#sort"
    ITEMS = "https://api.stacspec.org/v1.0.0/ogcapi-features#sort"
    COLLECTIONS = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#sort"


@attr.s
class SortExtension(ApiExtension):
    """Sort Extension.

    The Sort extension adds the `sortby` parameter to the `/search` endpoint, allowing the
    caller to specify the sort order of the returned items.
    https://github.com/stac-api-extensions/sort
    """

    GET: Type[APIRequest] = SortExtensionGetRequest
    POST: Type[BaseModel] = SortExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        factory=lambda: [
            SortConformanceClasses.SEARCH,
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
