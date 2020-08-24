"""ogc tiles client"""

from dataclasses import dataclass
from typing import Union
from urllib.parse import urljoin

from starlette.responses import RedirectResponse

from stac_api.clients.postgres.item import ItemCrudClient
from stac_api.models.links import TileLinks
from stac_api.models.ogc import TileSetResource
from stac_pydantic.collection import SpatialExtent


# TODO: Decouple from postgres by inherting from base class (stac_api.clients.base)
@dataclass
class TilesClient(ItemCrudClient):
    """OGC Tiles specific operations"""

    def get_item_tiles(
        self, id: str, **kwargs
    ) -> Union[RedirectResponse, TileSetResource]:
        """Get OGC TileSet resource for a stac item"""
        item = self.get_item(id, **kwargs)
        resource = TileSetResource(
            extent=SpatialExtent(bbox=[list(item.bbox)]),
            title=f"Tiled layer of {item.collection}/{item.id}",
            links=TileLinks(
                item_id=item.id,
                collection_id=item.collection,
                base_url=kwargs["request"].base_url,
            ).create_links(),
        )

        if "text/html" in kwargs["request"].headers["accept"]:
            item_uri = urljoin(
                kwargs["request"].base_url,
                f"collections/{item.collection}/items/{item.id}",
            )
            redirect_url = (
                f"{urljoin(kwargs['request'].base_url, '/stac/viewer')}?url={item_uri}"
            )
            return RedirectResponse(redirect_url)

        return resource
