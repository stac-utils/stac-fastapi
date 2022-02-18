from typing import List, Type

from stac_fastapi.api.app import StacApi
from stac_fastapi.types import config, core
from stac_fastapi.types.extension import ApiExtension


class DummyCoreClient(core.BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        ...

    def get_collection(self, *args, **kwargs):
        ...

    def get_item(self, *args, **kwargs):
        ...

    def get_search(self, *args, **kwargs):
        ...

    def post_search(self, *args, **kwargs):
        ...

    def item_collection(self, *args, **kwargs):
        ...


def build_api(extensions: List[Type[ApiExtension]] = [], **overrides):
    settings = config.ApiSettings()
    return StacApi(
        **{
            "settings": settings,
            "client": DummyCoreClient(),
            "extensions": extensions,
            **overrides,
        }
    )
