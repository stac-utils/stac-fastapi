"""Context extension."""

import warnings
from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension


@attr.s
class ContextExtension(ApiExtension):
    """Context Extension.

    The Context extension adds a JSON object to ItemCollection responses (`/search`,
    `/collections/{collection_id}/items`) which includes the number of items matched,
    returned, and the limit requested.
    https://github.com/stac-api-extensions/context
    """

    conformance_classes: List[str] = attr.ib(
        factory=lambda: ["https://api.stacspec.org/v1.0.0-rc.2/item-search#context"]
    )
    schema_href: Optional[str] = attr.ib(
        default="https://raw.githubusercontent.com/stac-api-extensions/context/v1.0.0-rc.2/json-schema/schema.json"
    )

    def __attrs_post_init__(self):
        """init."""
        warnings.warn(
            "The ContextExtension is deprecated and will be removed in 3.0.",
            DeprecationWarning,
            stacklevel=1,
        )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
