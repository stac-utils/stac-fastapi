"""Offset Pagination API extension."""

from typing import List, Optional

import attrs
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from .request import GETOffsetPagination, POSTOffsetPagination


@attrs.define
class OffsetPaginationExtension(ApiExtension):
    """Offset Pagination.

    Though not strictly an extension, the chosen pagination will modify the form of the
    request object. By making pagination an extension class, we can use
    create_request_model to dynamically add the correct pagination parameter to the
    request model for OpenAPI generation.
    """

    GET = GETOffsetPagination
    POST = POSTOffsetPagination

    conformance_classes: List[str] = attrs.field(factory=list)
    schema_href: Optional[str] = attrs.field(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
