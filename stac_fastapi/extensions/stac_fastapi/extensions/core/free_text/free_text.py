"""Free-text extension."""

from enum import Enum
from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import FreeTextExtensionGetRequest, FreeTextExtensionPostRequest


class FreeTextConformanceClasses(str, Enum):
    """Conformance classes for the Free-Text extension.

    See https://github.com/stac-api-extensions/freetext-search

    """

    # https://github.com/stac-api-extensions/freetext-search?tab=readme-ov-file#basic
    SEARCH_BASIC = "https://api.stacspec.org/v1.0.0-rc.1/item-search#free-text"
    COLLECTIONS_BASIC = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text"
    ITEMS_BASIC = "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features#free-text"

    # https://github.com/stac-api-extensions/freetext-search?tab=readme-ov-file#advanced
    SEARCH_ADVANCED = (
        "https://api.stacspec.org/v1.0.0-rc.1/item-search#advanced-free-text"
    )
    COLLECTIONS_ADVANCED = (
        "https://api.stacspec.org/v1.0.0-rc.1/collection-search#advanced-free-text"
    )
    ITEMS_ADVANCED = (
        "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features#advanced-free-text"
    )


@attr.s
class FreeTextExtension(ApiExtension):
    """Free-text Extension.

    The Free-text extension adds an additional `q` parameter to `/search` requests which
    allows the caller to perform free-text queries against STAC metadata.

    https://github.com/stac-api-extensions/freetext-search/README.md

    """

    GET = FreeTextExtensionGetRequest
    POST = FreeTextExtensionPostRequest

    conformance_classes: List[str] = attr.ib()
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
