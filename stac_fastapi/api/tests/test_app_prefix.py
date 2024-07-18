import urllib
from typing import Optional

import pytest
from fastapi import APIRouter
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.types.config import ApiSettings


def get_link(landing_page, rel_type, method: Optional[str] = None):
    return next(
        filter(
            lambda link: link["rel"] == rel_type
            and (not method or link.get("method") == method),
            landing_page["links"],
        ),
        None,
    )


@pytest.mark.parametrize("prefix", ["", "/a_prefix"])
def test_api_prefix(TestCoreClient, prefix):
    api_settings = ApiSettings(
        openapi_url=f"{prefix}/api",
        docs_url=f"{prefix}/api.html",
    )

    api = StacApi(
        settings=api_settings,
        client=TestCoreClient(),
        router=APIRouter(prefix=prefix),
    )

    with TestClient(api.app, base_url="http://stac.io") as client:
        landing = client.get(f"{prefix}/")
        assert landing.status_code == 200, landing.json()

        service_doc = client.get(f"{prefix}/api.html")
        assert service_doc.status_code == 200, service_doc.text

        service_desc = client.get(f"{prefix}/api")
        assert service_desc.status_code == 200, service_desc.json()

        conformance = client.get(f"{prefix}/conformance")
        assert conformance.status_code == 200, conformance.json()

        # NOTE: The collections/collection/items/item links do not have the prefix
        # because they are created in the fixtures
        collections = client.get(f"{prefix}/collections")
        assert collections.status_code == 200, collections.json()
        collection_id = collections.json()["collections"][0]["id"]

        collection = client.get(f"{prefix}/collections/{collection_id}")
        assert collection.status_code == 200, collection.json()

        items = client.get(f"{prefix}/collections/{collection_id}/items")
        assert items.status_code == 200, items.json()

        item_id = items.json()["features"][0]["id"]
        item = client.get(f"{prefix}/collections/{collection_id}/items/{item_id}")
        assert item.status_code == 200, item.json()

        link_tests = [
            ("root", "application/json", "/"),
            ("conformance", "application/json", "/conformance"),
            ("data", "application/json", "/collections"),
            ("search", "application/geo+json", "/search"),
            ("service-doc", "text/html", "/api.html"),
            ("service-desc", "application/vnd.oai.openapi+json;version=3.0", "/api"),
        ]

        for rel_type, expected_media_type, expected_path in link_tests:
            link = get_link(landing.json(), rel_type)

            assert link is not None, f"Missing {rel_type} link in landing page"
            assert link.get("type") == expected_media_type

            link_path = urllib.parse.urlsplit(link.get("href")).path
            assert link_path == prefix + expected_path

            resp = client.get(prefix + expected_path)
            assert resp.status_code == 200


@pytest.mark.parametrize("prefix", ["", "/a_prefix"])
def test_async_api_prefix(AsyncTestCoreClient, prefix):
    api_settings = ApiSettings(
        openapi_url=f"{prefix}/api",
        docs_url=f"{prefix}/api.html",
    )

    api = StacApi(
        settings=api_settings,
        client=AsyncTestCoreClient(),
        router=APIRouter(prefix=prefix),
    )

    with TestClient(api.app, base_url="http://stac.io") as client:
        landing = client.get(f"{prefix}/")
        assert landing.status_code == 200, landing.json()

        service_doc = client.get(f"{prefix}/api.html")
        assert service_doc.status_code == 200, service_doc.text

        service_desc = client.get(f"{prefix}/api")
        assert service_desc.status_code == 200, service_desc.json()

        conformance = client.get(f"{prefix}/conformance")
        assert conformance.status_code == 200, conformance.json()

        collections = client.get(f"{prefix}/collections")
        assert collections.status_code == 200, collections.json()
        collection_id = collections.json()["collections"][0]["id"]

        collection = client.get(f"{prefix}/collections/{collection_id}")
        assert collection.status_code == 200, collection.json()

        items = client.get(f"{prefix}/collections/{collection_id}/items")
        assert items.status_code == 200, items.json()

        item_id = items.json()["features"][0]["id"]
        item = client.get(f"{prefix}/collections/{collection_id}/items/{item_id}")
        assert item.status_code == 200, item.json()

        link_tests = [
            ("root", "application/json", "/"),
            ("conformance", "application/json", "/conformance"),
            ("data", "application/json", "/collections"),
            ("search", "application/geo+json", "/search"),
            ("service-doc", "text/html", "/api.html"),
            ("service-desc", "application/vnd.oai.openapi+json;version=3.0", "/api"),
        ]

        for rel_type, expected_media_type, expected_path in link_tests:
            link = get_link(landing.json(), rel_type)

            assert link is not None, f"Missing {rel_type} link in landing page"
            assert link.get("type") == expected_media_type

            link_path = urllib.parse.urlsplit(link.get("href")).path
            assert link_path == prefix + expected_path

            resp = client.get(prefix + expected_path)
            assert resp.status_code == 200
