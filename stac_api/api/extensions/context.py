"""context extension"""
from dataclasses import dataclass

from fastapi import FastAPI

from stac_api.api.extensions import ApiExtension


@dataclass
class ContextExtension(ApiExtension):
    """
    stac-api context extension
    (https://github.com/radiantearth/stac-api-spec/tree/master/extensions/context)
    """

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        pass
