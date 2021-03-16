"""context extension."""
import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension


@attr.s
class ContextExtension(ApiExtension):
    """Context Extension.

    The Context extension adds a JSON object to ItemCollection responses (`/search`, `/collections/{collectionId}/items`)
    which includes the number of items matched, returned, and the limit requested.

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#context
    """

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
