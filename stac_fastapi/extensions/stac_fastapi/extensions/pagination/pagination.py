"""Pagination API extension."""

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest

from .request import GETPagination, POSTPagination


@attr.s
class PaginationExtension(ApiExtension):
    """Token Pagination.

    Though not strictly an extension, the chosen pagination will modify the form of the
    request object. By making pagination an extension class, we can use
    create_request_model to dynamically add the correct pagination parameter to the
    request model for OpenAPI generation.
    """

    GET: type[APIRequest] = GETPagination
    POST: type[BaseModel] = POSTPagination

    conformance_classes: list[str] = attr.ib(factory=list)
    schema_href: str | None = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
