"""fields extension."""
from typing import List, Optional, Set

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
        conformance_classes (list): Defines the list of conformance classes for the extension

    """

    conformance_classes: List[str] = attr.ib(
        factory=lambda: ["https://api.stacspec.org/v1.0.0-beta.3/item-search/#fields"]
    )
    schema_href: Optional[str] = attr.ib(default=None)
    default_includes: Set[str] = attr.ib(
        factory=lambda: {
            "id",
            "type",
            "stac_version",
            "geometry",
            "bbox",
            "links",
            "assets",
            "properties.datetime",
        }
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app (fastapi.FastAPI): target FastAPI application.

        Returns:
            None
        """
        pass
