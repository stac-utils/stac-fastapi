"""Token pagination API extension."""

from typing import List, Optional, Type

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest

from .request import GETTokenPagination, POSTTokenPagination


@attr.s
class TokenPaginationExtension(ApiExtension):
    """Token Pagination.

    Though not strictly an extension, the chosen pagination will modify the form of the
    request object. By making pagination an extension class, we can use
    create_request_model to dynamically add the correct pagination parameter to the
    request model for OpenAPI generation.
    """

    GET: Type[APIRequest] = GETTokenPagination
    POST: Type[BaseModel] = POSTTokenPagination

    conformance_classes: List[str] = attr.ib(factory=list)
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
