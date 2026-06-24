"""Free-text extension."""

from enum import StrEnum

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


class FreeTextConformanceClasses(StrEnum):
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

    GET: type[APIRequest] = FreeTextExtensionGetRequest
    POST: type[BaseModel] = FreeTextExtensionPostRequest

    conformance_classes: list[str] = attr.ib(
        default=[
            FreeTextConformanceClasses.SEARCH,
        ]
    )
    schema_href: str | None = attr.ib(default=None)

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

    GET: type[APIRequest] = FreeTextAdvancedExtensionGetRequest
    POST: type[BaseModel] = FreeTextAdvancedExtensionPostRequest

    conformance_classes: list[str] = attr.ib(
        default=[
            FreeTextConformanceClasses.SEARCH_ADVANCED,
        ]
    )
    schema_href: str | None = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
