"""sort extension"""
from dataclasses import dataclass

from fastapi import FastAPI

from stac_api.api.extensions import ApiExtension


@dataclass
class SortExtension(ApiExtension):
    """
    stac-api query extension
    (https://github.com/radiantearth/stac-api-spec/tree/master/extensions/sort)
    """

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        pass
