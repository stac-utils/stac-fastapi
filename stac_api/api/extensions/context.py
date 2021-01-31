"""context extension"""
import attr
from fastapi import FastAPI

from stac_api.api.extensions.extension import ApiExtension


@attr.s
class ContextExtension(ApiExtension):
    """Context Extension (https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#context)

    The Context extension adds a JSON object to ItemCollection responses (`/search`, `/collections/{collectionId}/items`)
    which includes the number of items matched, returned, and the limit requested
    """

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app (fastapi.FastAPI): target FastAPI application.

        Returns:
            None
        """
        pass
