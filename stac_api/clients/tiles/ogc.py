"""ogc tiles client"""

from dataclasses import dataclass

from stac_api.clients.postgres.item import ItemCrudClient
from stac_api.models.links import TileLinks
from stac_api.models.ogc import TileSetResource
from stac_pydantic.collection import SpatialExtent


# TODO: Decouple from postgres by inherting from base class (stac_api.clients.base)
@dataclass
class TilesClient(ItemCrudClient):
    """OGC Tiles specific operations"""

    def get_item_tiles(self, id: str, **kwargs) -> TileSetResource:
        """Get OGC TileSet resource for a stac item"""
        item = self.get_item(id, **kwargs)
        return TileSetResource(
            extent=SpatialExtent(bbox=[list(item.bbox)]),
            title=f"Tiled layer of {item.collection}/{item.id}",
            links=TileLinks(
                item_id=item.id, collection_id=item.collection
            ).create_links(),
        )
