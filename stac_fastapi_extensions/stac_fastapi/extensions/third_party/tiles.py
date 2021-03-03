"""tiles extension."""
import abc
from typing import List, Optional, Union

import attr
from fastapi import FastAPI
from pydantic import BaseModel
from stac_pydantic.collection import SpatialExtent
from stac_pydantic.shared import Link
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse

from stac_fastapi.api.models import ItemUri
from stac_fastapi.api.routes import create_endpoint_with_depends
from stac_fastapi.extensions.core.extension import ApiExtension


class OGCTileLink(Link):
    """OGC Tiles API - Link."""

    templated: Optional[bool] = False


class TileSetResource(BaseModel):
    """OGC Tiles API - TileSetResource."""

    extent: SpatialExtent
    links: List[OGCTileLink]
    title: Optional[str]
    description: Optional[str]


@attr.s
class BaseTilesClient(abc.ABC):
    """Defines a pattern for implementing the Tiles Extension."""

    @abc.abstractmethod
    def get_item_tiles(
        self, id: str, **kwargs
    ) -> Union[RedirectResponse, TileSetResource]:
        """Get OGC TileSet resource for a stac item.

        Args:
            id: stac item id

        Returns:
            A TileSetResource, or a redirect to another endpoint which returns a TileSetResource.
        """
        ...


@attr.s
class TilesExtension(ApiExtension):
    """Tiles Extension.

    The TilesExtension mounts `titiler` onto the application.

    https://github.com/developmentseed/titiler
    """

    client: BaseTilesClient = attr.ib()

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        from titiler.endpoints.stac import STACTiler
        from titiler.templates import templates

        titiler_router = STACTiler().router

        @titiler_router.get("/viewer", response_class=HTMLResponse)
        def stac_demo(request: Request):
            """STAC Viewer."""
            return templates.TemplateResponse(
                name="stac_index.html",
                context={
                    "request": request,
                    "tilejson": request.url_for("tilejson"),
                    "metadata": request.url_for("info"),
                },
                media_type="text/html",
            )

        app.include_router(titiler_router, prefix="/titiler", tags=["Titiler"])

        app.add_api_route(
            name="Get OGC Tiles Resource",
            path="/collections/{collectionId}/items/{itemId}/tiles",
            response_model=TileSetResource,
            response_model_exclude_none=True,
            response_model_exclude_unset=True,
            methods=["GET"],
            endpoint=create_endpoint_with_depends(self.client.get_item_tiles, ItemUri),
            tags=["OGC Tiles"],
        )
