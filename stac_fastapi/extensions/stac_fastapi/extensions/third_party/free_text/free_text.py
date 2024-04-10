"""Free-text extension."""

from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import FreeTextExtensionGetRequest, FreeTextExtensionPostRequest


@attr.s
class FreeTextExtension(ApiExtension):
    """Free-text Extension.

    The Free-text extension adds an additional `q` parameter to `/search` requests which
    allows the caller to perform free-text queries against STAC metadata.
    https://github.com/stac-api-extensions/freetext-search/README.md
    """

    GET = FreeTextExtensionGetRequest
    POST = FreeTextExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        factory=lambda: [
            "https://api.stacspec.org/v1.0.0-rc.1/item-search#free-text",
            "https://api.stacspec.org/v1.0.0-rc.1/item-search#advanced-free-text",
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text",
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#advanced-free-text",
            "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features#free-text",
            "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features#advanced-free-text",
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
