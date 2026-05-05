"""Free-text extension."""

from enum import Enum
from typing import List, Optional, Type

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest

from .request import (
    FreeTextAdvancedExtensionGetRequest,
    FreeTextAdvancedExtensionPostRequest,
    FreeTextExtensionGetRequest,
    FreeTextExtensionPostRequest,
)


class FreeTextConformanceClasses(str, Enum):
    """Conformance classes for the Free-Text extension.

    See https://github.com/stac-api-extensions/freetext-search

    """

    # https://github.com/stac-api-extensions/freetext-search?tab=readme-ov-file#basic
    SEARCH = "https://api.stacspec.org/v1.0.0-rc.1/item-search#free-text"
    ITEMS = "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features#free-text"
    COLLECTIONS = "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text"

    # https://github.com/stac-api-extensions/freetext-search?tab=readme-ov-file#advanced
    SEARCH_ADVANCED = (
        "https://api.stacspec.org/v1.0.0-rc.1/item-search#advanced-free-text"
    )
    ITEMS_ADVANCED = (
        "https://api.stacspec.org/v1.0.0-rc.1/ogcapi-features#advanced-free-text"
    )
    COLLECTIONS_ADVANCED = (
        "https://api.stacspec.org/v1.0.0-rc.1/collection-search#advanced-free-text"
    )


@attr.s
class FreeTextExtension(ApiExtension):
    """Free-text Extension.

    The Free-text extension adds an additional `q` parameter to `/search` requests which
    allows the caller to perform free-text queries against STAC metadata.

    https://github.com/stac-api-extensions/freetext-search?tab=readme-ov-file#basic

    """

    GET: Type[APIRequest] = FreeTextExtensionGetRequest
    POST: Type[BaseModel] = FreeTextExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        default=[
            FreeTextConformanceClasses.SEARCH,
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


@attr.s
class FreeTextAdvancedExtension(ApiExtension):
    """Free-text Extension.

    The Free-text extension adds an additional `q` parameter to `/search` requests which
    allows the caller to perform free-text queries against STAC metadata.

    https://github.com/stac-api-extensions/freetext-search?tab=readme-ov-file#advanced

    """

    GET: Type[APIRequest] = FreeTextAdvancedExtensionGetRequest
    POST: Type[BaseModel] = FreeTextAdvancedExtensionPostRequest

    conformance_classes: List[str] = attr.ib(
        default=[
            FreeTextConformanceClasses.SEARCH_ADVANCED,
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
