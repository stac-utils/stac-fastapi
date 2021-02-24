"""transaction extension."""
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Type

import attr
from cogeo_mosaic.backends.base import BaseBackend
from cogeo_mosaic.backends.stac import default_stac_accessor
from cogeo_mosaic.errors import NoAssetFoundError
from cogeo_mosaic.mosaic import MosaicJSON
from fastapi import FastAPI, Query
from morecantile import TileMatrixSet
from rio_tiler.constants import WEB_MERCATOR_TMS
from rio_tiler.io import BaseReader, STACReader
from rio_tiler.models import ImageData
from rio_tiler.mosaic import mosaic_reader
from titiler.dependencies import DefaultDependency
from titiler.endpoints.factory import MosaicTilerFactory

from stac_api.api.extensions.extension import ApiExtension
from stac_api.clients.postgres.core import CoreCrudClient


@attr.s
class FakeRequest:
    """Mock necessary methods of the request object

    When the API is separated from the link creation, this likely won't be necessary.
    """
    base_url: str = "http://localhost:8081"
    query_params: Dict = {}


@attr.s
class DynamicStacBackend(BaseBackend):
    """Like a STAC backend but dynamic"""

    path: str = attr.ib()
    reader: Type[BaseReader] = attr.ib(default=STACReader)
    reader_options: Dict = attr.ib(factory=dict)
    backend_options: Dict = attr.ib(factory=dict)

    item_collection: Dict = attr.ib(factory=dict)

    # default values for bounds and zoom
    bounds: Tuple[float, float, float, float] = attr.ib(default=(-180, -90, 180, 90))
    minzoom: int = attr.ib(default=0)
    maxzoom: int = attr.ib(default=30)
    mosaic_quadkey_zoom: Optional[int] = attr.ib(default=None)

    # Because we are not using mosaicjson we are not limited to the WebMercator TMS
    tms: TileMatrixSet = attr.ib(default=WEB_MERCATOR_TMS)

    mosaic_def: MosaicJSON = attr.ib(init=False)

    _backend_name = "DynamicSTAC"

    def __attrs_post_init__(self):
        """Post Init."""
        # Construct a FAKE mosaicJSON
        self.mosaic_def = MosaicJSON(
            mosaicjson="0.0.2",
            name="it's fake but it's ok",
            minzoom=self.minzoom,
            maxzoom=self.maxzoom,
            quadkey_zoom=self.mosaic_quadkey_zoom,
            tiles=[],
        )

    def write(self, overwrite: bool = True):
        """Write mosaicjson document."""
        pass

    def update(self):
        pass

    def _read(self) -> MosaicJSON:
        pass

    def assets_for_tile(self, x: int, y: int, z: int, **kwargs) -> List[str]:
        """Retrieve assets for tile."""
        bounds = self.tms.bounds(x, y, z)
        return self.get_assets(list(bounds), **kwargs)

    def assets_for_point(self, lng: float, lat: float) -> List[str]:
        """Retrieve assets for point."""
        bounds = [lng, lat, lng, lat]
        return self.get_assets(bounds)

    def get_assets(self, bbox, **kwargs) -> List[Dict]:
        """Find assets."""
        print("get assets kwargs")
        print(kwargs)
        kwargs["bbox"] = bbox
        client = self.reader_options["client"]

        kwargs["request"] = FakeRequest()

        print("get_assets edited kwargs")
        print(kwargs)

        feature_collection = client.get_search(**kwargs)

        print("feature_collection")
        print(feature_collection)

        return feature_collection["features"]

    @property
    def _quadkeys(self) -> List[str]:
        return []

    def tile(  # type: ignore
        self,
        x: int,
        y: int,
        z: int,
        reverse: bool = False,
        **kwargs: Any,
    ) -> Tuple[ImageData, List[str]]:
        """Get Tile from multiple observation."""
        print("tile kwargs")
        print(kwargs)
        mosaic_assets = self.assets_for_tile(x, y, z, **kwargs)
        if not mosaic_assets:
            raise NoAssetFoundError(f"No assets found for tile {z}-{x}-{y}")

        if reverse:
            mosaic_assets = list(reversed(mosaic_assets))

        # Sanitize kwargs to remove stac api kwargs
        remove_kwargs = [
            "collections",
            "ids",
            "datetime",
            "limit",
            "query",
            "token",
            "fields",
            "sortby",
        ]
        kwargs = {k: v for k, v in kwargs.items() if k not in remove_kwargs}

        def _reader(asset: str, x: int, y: int, z: int, **kwargs: Any) -> ImageData:
            # Take out reader_options for now because that's how I'm passing the
            # postgres client to self.get_assets
            # with self.reader(None, item=asset, **self.reader_options) as src_dst:
            with self.reader(None, item=asset) as src_dst:
                return src_dst.tile(x, y, z, **kwargs)

        return mosaic_reader(mosaic_assets, _reader, x, y, z, **kwargs)


@dataclass
class AssetParams(DefaultDependency):
    """Band names and Expression parameters."""

    assets: Optional[str] = Query(
        None,
        title="Asset names",
        description="comma-delimited asset names.",
    )

    def __post_init__(self):
        """Post Init."""
        if self.assets is not None:
            self.kwargs["assets"] = self.assets.split(",")


@dataclass
class DatasetDependency(DefaultDependency):
    """Add STAC search params to query."""

    collections: Optional[str] = Query(
        None, title="Collections", description="Collections to search within"
    )

    ids: Optional[str] = Query(None)
    datetime: Optional[str] = Query(None)
    limit: Optional[int] = Query(10)
    query: Optional[str] = Query(None)
    token: Optional[str] = Query(None)
    fields: Optional[str] = Query(None)
    sortby: Optional[str] = Query(None)

    def __post_init__(self):
        """Post Init."""
        if self.collections:
            self.kwargs["collections"] = self.collections.split(",")
        if self.ids:
            self.kwargs["ids"] = self.ids.split(",")
        if self.datetime:
            self.kwargs["datetime"] = self.datetime
        if self.limit:
            self.kwargs["limit"] = self.limit
        if self.query:
            self.kwargs["query"] = self.query
        if self.token:
            self.kwargs["token"] = self.token
        if self.fields:
            self.kwargs["fields"] = self.fields.split(",")
        if self.sortby:
            self.kwargs["sortby"] = self.sortby.split(",")


@attr.s
class TilesSearchExtension(ApiExtension):
    """Custom Titiler Extension.

    Custom extension for sending query results to a titiler DynamicSTAC endpoint
    """

    client: CoreCrudClient = attr.ib(default=attr.Factory(CoreCrudClient))

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        dynamic_stac_endpoint = MosaicTilerFactory(
            reader=DynamicStacBackend,
            reader_options={"client": self.client},
            # path_dependency=MosaicParams,
            dataset_reader=STACReader,
            dataset_dependency=DatasetDependency,
            layer_dependency=AssetParams,
            router_prefix="test-dynamic-search",
        )

        app.include_router(
            dynamic_stac_endpoint.router, prefix="/dynamic-stac", tags=["Dynamic STAC"]
        )
