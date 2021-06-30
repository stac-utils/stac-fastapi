"""query extension."""
from typing import List

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension


@attr.s
class QueryExtension(ApiExtension):
    """Query Extension.

    The Query extension adds an additional `query` parameter to `/search` requests which allows the caller to perform
    queries against item metadata (ex. find all images with cloud cover less than 15%).

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#query
    """

    conformance_classes: List[str] = attr.ib(
        default=["https://api.stacspec.org/v1.0.0-beta.2/item-search#query"]
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
