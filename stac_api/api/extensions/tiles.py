"""tiles extension"""
from dataclasses import dataclass

import pkg_resources
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from stac_api.api.extensions.extension import ApiExtension
from stac_api.api.models import ItemUri
from stac_api.api.routes import create_endpoint_with_depends
from stac_api.clients.tiles.ogc import TilesClient
from stac_api.models.ogc import TileSetResource


@dataclass
class TilesExtension(ApiExtension):
    """titiler extension"""

    client: TilesClient = TilesClient()

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        from titiler.endpoints.stac import STACTiler

        template_dir = pkg_resources.resource_filename("titiler", "templates")
        templates = Jinja2Templates(directory=template_dir)

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
