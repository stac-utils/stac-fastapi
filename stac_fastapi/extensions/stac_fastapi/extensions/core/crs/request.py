"""Request model for the Crs extension."""

from typing import Optional

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class CrsExtensionGetRequest(APIRequest):
    """Crs Extension GET request model."""

    crs: Optional[str] = attr.ib(default="http://www.opengis.net/def/crs/OGC/1.3/CRS84")


class CrsExtensionPostRequest(BaseModel):
    """Crs Extension POST request model."""

    crs: Optional[str] = attr.ib(default="http://www.opengis.net/def/crs/OGC/1.3/CRS84")
