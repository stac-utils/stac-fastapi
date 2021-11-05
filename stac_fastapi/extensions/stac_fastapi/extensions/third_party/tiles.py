"""tiles extension."""
import abc
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin

import attr
from fastapi import FastAPI
from pydantic import BaseModel
from stac_pydantic.collection import SpatialExtent
from stac_pydantic.links import Link, Relations
from stac_pydantic.shared import MimeTypes
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse

from stac_fastapi.api.models import ItemUri
from stac_fastapi.api.routes import create_sync_endpoint
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.extension import ApiExtension


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
class TileLinks:
    """Create inferred links specific to OGC Tiles API."""

    base_url: str = attr.ib()
    collection_id: str = attr.ib()
    item_id: str = attr.ib()
    route_prefix: str = attr.ib()

    def __attrs_post_init__(self):
        """Post init handler."""
        self.item_uri = urljoin(
            self.base_url,
            f"collections/{self.collection_id}/items/{self.item_id}",
        )

    def tiles(self) -> OGCTileLink:
        """Create tiles link."""
        return OGCTileLink(
            href=urljoin(
                self.base_url,
                f"{self.route_prefix}/tiles/{{z}}/{{x}}/{{y}}.png?url={self.item_uri}",
            ),
            rel=Relations.item,
            title="tiles",
            type=MimeTypes.png,
            templated=True,
        )

    def viewer(self) -> OGCTileLink:
        """Create viewer link."""
        return OGCTileLink(
            href=urljoin(
                self.base_url,
                f"{self.route_prefix}/viewer?url={self.item_uri}",
            ),
            rel=Relations.alternate,
            type=MimeTypes.html,
            title="viewer",
        )

    def tilejson(self) -> OGCTileLink:
        """Create tilejson link."""
        return OGCTileLink(
            href=urljoin(
                self.base_url,
                f"{self.route_prefix}/tilejson.json?url={self.item_uri}",
            ),
            rel=Relations.alternate,
            type=MimeTypes.json,
            title="tilejson",
        )

    def wmts(self) -> OGCTileLink:
        """Create wmts capabilities link."""
        return OGCTileLink(
            href=urljoin(
                self.base_url,
                f"{self.route_prefix}/WMTSCapabilities.xml?url={self.item_uri}",
            ),
            rel=Relations.alternate,
            type=MimeTypes.xml,
            title="WMTS Capabilities",
        )

    def create_links(self) -> List[OGCTileLink]:
        """Return all inferred links."""
        return [self.tiles(), self.tilejson(), self.wmts(), self.viewer()]


@attr.s
class BaseTilesClient(abc.ABC):
    """Defines a pattern for implementing the Tiles Extension."""

    @abc.abstractmethod
    def get_item_tiles(
        self, item_id: str, collection_id: str, **kwargs
    ) -> Union[RedirectResponse, TileSetResource]:
        """Get OGC TileSet resource for a stac item.

        Args:
            id: stac item id

        Returns:
            A TileSetResource, or a redirect to another endpoint
            which returns a TileSetResource.
        """
        ...


@attr.s
class TilesClient(BaseTilesClient):
    """Defines the default Tiles extension used by the application.

    This extension should work with any backend that implements
    the `BaseCoreClient.get_item` method.  If the accept
    header is `text/html`, the endpoint will redirect to titiler's web viewer.
    """

    client: BaseCoreClient = attr.ib()
    route_prefix: str = attr.ib(default="/titiler")

    def get_item_tiles(
        self, item_id: str, collection_id: str, **kwargs
    ) -> Union[RedirectResponse, Dict[str, Any]]:
        """Get OGC TileSet resource for a stac item."""
        item = self.client.get_item(item_id, collection_id, **kwargs)
        resource = TileSetResource(
            extent=SpatialExtent(bbox=[list(item["bbox"])]),
            title=f"Tiled layer of {item['collection']}/{item['id']}",
            links=TileLinks(
                item_id=item["id"],
                collection_id=item["collection"],
                base_url=str(kwargs["request"].base_url),
                route_prefix=self.route_prefix,
            ).create_links(),
        )

        if "text/html" in kwargs["request"].headers["accept"]:
            viewer_url = [
                link.href for link in resource.links if link.type == MimeTypes.html
            ][0]
            return RedirectResponse(viewer_url)

        return resource.dict(exclude_unset=True)


@attr.s
class TilesExtension(ApiExtension):
    """Tiles Extension.

    The TilesExtension mounts `titiler` onto the application.

    https://github.com/developmentseed/titiler
    """

    client: BaseTilesClient = attr.ib()
    route_prefix: str = attr.ib(default="/titiler")
    conformance_classes: List[str] = attr.ib(default=list())
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        from titiler.endpoints.stac import stac
        from titiler.templates import templates

        titiler_router = stac.router

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

        app.include_router(titiler_router, prefix=self.route_prefix, tags=["Titiler"])

        app.add_api_route(
            name="Get OGC Tiles Resource",
            path="/collections/{collectionId}/items/{itemId}/tiles",
            response_model=TileSetResource,
            response_model_exclude_none=True,
            response_model_exclude_unset=True,
            methods=["GET"],
            endpoint=create_sync_endpoint(self.client.get_item_tiles, ItemUri),
            tags=["OGC Tiles"],
        )
