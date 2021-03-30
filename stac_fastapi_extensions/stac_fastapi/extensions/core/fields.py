"""fields extension."""
from typing import Set

import attr
from fastapi import FastAPI

from stac_fastapi.types.extension import ApiExtension


@attr.s
class FieldsExtension(ApiExtension):
    """Fields Extension.

    The Fields extension adds functionality to the `/search` endpoint which allows the caller to include or exclude
    specific from the API response.  Registering this extension with the application has the added effect of removing
    the `ItemCollection` response model from the `/search` endpoint, as the Fields extension allows the API to return
    potentially invalid responses by excluding fields which are required by the STAC spec, such as geometry.

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#fields

    Attributes:
        default_includes (set): defines the default set of included fields.

    """

    default_includes: Set[str] = attr.ib(
        default=attr.Factory(
            lambda: {
                "id",
                "type",
                "geometry",
                "bbox",
                "links",
                "assets",
                "properties.datetime",
            }
        )
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app (fastapi.FastAPI): target FastAPI application.

        Returns:
            None
        """
        pass
