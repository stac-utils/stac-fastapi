"""ogc tiles api models"""

from typing import List, Optional

from pydantic import BaseModel
from stac_pydantic.collection import SpatialExtent
from stac_pydantic.shared import Link


class OGCTileLink(Link):
    """OGC Tiles API - Link"""

    templated: Optional[bool] = False


class TileSetResource(BaseModel):
    """OGC Tiles API - TileSetResource"""

    extent: SpatialExtent
    links: List[OGCTileLink]
    title: Optional[str]
    description: Optional[str]
