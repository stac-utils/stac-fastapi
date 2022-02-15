"""context extension."""
from typing import List, Optional

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension


@attr.s
class ContextExtension(ApiExtension):
    """Context Extension.

    The Context extension adds a JSON object to ItemCollection responses (`/search`, `/collections/{collection_id}/items`)
    which includes the number of items matched, returned, and the limit requested.

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#context
    """

    conformance_classes: List[str] = attr.ib(
        factory=lambda: ["https://api.stacspec.org/v1.0.0-beta.4/item-search/#context"]
    )
    schema_href: Optional[str] = attr.ib(
        default="https://raw.githubusercontent.com/radiantearth/stac-api-spec/v1.0.0-beta.4/fragments/context/json-schema/schema.json"
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
