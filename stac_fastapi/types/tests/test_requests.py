from typing import Optional

import pytest
from fastapi import Request
from fastapi.routing import APIRouter

from stac_fastapi.api.app import StacApi
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.requests import get_base_url


class DummyCoreClient(BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        raise NotImplementedError

    def get_collection(self, *args, **kwargs):
        raise NotImplementedError

    def get_item(self, *args, **kwargs):
        raise NotImplementedError

    def get_search(self, *args, **kwargs):
        raise NotImplementedError

    def post_search(self, *args, **kwargs):
        raise NotImplementedError

    def item_collection(self, *args, **kwargs):
        raise NotImplementedError


@pytest.mark.parametrize(
    "base_url,, prefix, req_scope_dict, expected_base_url",
    [
        (
            "http://localhost:8000/",
            "/api",
            {
                "type": "http",
                "app_root_path": "bar",
                "headers": {},
            },
            "http://localhost:8000/api/",
        ),
        (
            "http://localhost:8000/",
            None,
            {
                "type": "http",
                "app_root_path": "bar",
                "headers": {},
            },
            "http://localhost:8000/",
        ),
        (
            None,
            None,
            {
                "type": "http",
                "app_root_path": "foo",
                "headers": {},
            },
            "foo/",
        ),
    ],
)
def test_base_url(
    req_scope_dict: dict,
    expected_base_url: str,
    base_url: Optional[str],
    prefix: Optional[str],
):
    api = StacApi(
        client=DummyCoreClient(),
        settings=ApiSettings(
            base_url=base_url,
        ),
        router=APIRouter(prefix=prefix if prefix else ""),
    )
    app = api.app
    req_scope_dict.update({"app": app})
    req = Request(scope=req_scope_dict)
    assert get_base_url(req) == expected_base_url
