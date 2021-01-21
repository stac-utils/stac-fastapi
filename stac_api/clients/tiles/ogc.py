"""ogc tiles client"""

from typing import Union

import attr
from stac_pydantic.collection import SpatialExtent
from stac_pydantic.shared import MimeTypes
from starlette.responses import RedirectResponse

from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.models.links import TileLinks
from stac_api.models.ogc import TileSetResource


# TODO: Decouple from postgres by inherting from base class (stac_api.clients.base)
@attr.s
class TilesClient(CoreCrudClient):
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
                base_url=str(kwargs["request"].base_url),
            ).create_links(),
        )

        if "text/html" in kwargs["request"].headers["accept"]:
            viewer_url = [
                link.href for link in resource.links if link.type == MimeTypes.html
            ][0]
            return RedirectResponse(viewer_url)

        return resource
