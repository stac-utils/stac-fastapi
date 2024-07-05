"""Request model for the Crs extension."""

from typing import Optional

import attr
#from pydantic import BaseModel
from pydantic import BaseModel, Field

from stac_fastapi.types.search import APIRequest


@attr.s
class CrsExtensionGetRequest(APIRequest):
    """Crs Extension GET request model."""

    crs: Optional[str] = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    bbox_crs: Optional[str]  = Field(default="http://www.opengis.net/def/crs/OGC/1.3/CRS84", alias="bbox-crs")


class CrsExtensionPostRequest(BaseModel):
    """Crs Extension POST request model."""

    crs: Optional[str] = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    bbox_crs: Optional[str]  = Field(default="http://www.opengis.net/def/crs/OGC/1.3/CRS84", alias="bbox-crs")
