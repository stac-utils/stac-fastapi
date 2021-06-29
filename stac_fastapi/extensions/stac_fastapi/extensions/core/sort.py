"""sort extension."""
import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension

from typing import List

@attr.s
class SortExtension(ApiExtension):
    """Sort Extension.

    The Sort extension adds the `sortby` parameter to the `/search` endpoint, allowing the caller to specify the sort
    order of the returned items.

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#sort
    """

    conformance_classes: List[str] = attr.ib(default=["https://api.stacspec.org/v1.0.0-beta.2/item-search#sort"])

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
