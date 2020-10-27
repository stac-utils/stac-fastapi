"""tiles extension"""
from dataclasses import dataclass

import pkg_resources
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from stac_api.api.extensions import ApiExtension


@dataclass
class TilesExtension(ApiExtension):
    """titiler extension"""
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

        app.include_router(titiler_router)
