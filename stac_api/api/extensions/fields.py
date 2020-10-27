"""fields extension"""
from dataclasses import dataclass, field
from typing import Set

from fastapi import FastAPI

from stac_api.api.extensions import ApiExtension


@dataclass
class FieldsExtension(ApiExtension):
    """
    stac-api fields extension
    (https://github.com/radiantearth/stac-api-spec/tree/master/extensions/fields)
    """

    default_includes: Set[str] = field(
        default_factory=lambda: {
            "id",
            "type",
            "geometry",
            "bbox",
            "links",
            "assets",
            "properties.datetime",
        }
    )

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        pass
