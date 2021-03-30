"""sort extension."""
import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension


@attr.s
class SortExtension(ApiExtension):
    """Sort Extension.

    The Sort extension adds the `sortby` parameter to the `/search` endpoint, allowing the caller to specify the sort
    order of the returned items.

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#sort
    """

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
