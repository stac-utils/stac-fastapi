"""fields extension"""
from typing import Set

import attr
from fastapi import FastAPI

from stac_api.api.extensions.extension import ApiExtension


@attr.s
class FieldsExtension(ApiExtension):
    """
    stac-api fields extension
    (https://github.com/radiantearth/stac-api-spec/tree/master/extensions/fields)
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
        """register extension with the application"""
        pass
