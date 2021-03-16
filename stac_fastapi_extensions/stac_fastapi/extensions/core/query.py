"""query extension."""
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

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
