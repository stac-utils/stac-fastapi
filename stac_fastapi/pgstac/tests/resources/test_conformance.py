import urllib.parse

import pytest


@pytest.fixture(scope="module")
async def response(app_client):
    return await app_client.get("/")


@pytest.fixture(scope="module")
async def response_json(response):
    return response.json()


def get_link(landing_page, rel_type):
    return next(
        filter(lambda link: link["rel"] == rel_type, landing_page["links"]), None
    )


def test_landing_page_health(response):
    """Test landing page"""
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


def test_search_link(response_json):
    search_link = get_link(response_json, "search")

    assert search_link is not None
    assert search_link.get("type") == "application/geo+json"

    search_path = urllib.parse.urlsplit(search_link.get("href")).path
    assert search_path == "/search"

    # This endpoint currently returns a 404 for empty result sets, but testing for this response
    # code here seems meaningless since it would be the same as if the endpoint did not exist. Until
    # https://github.com/stac-utils/stac-fastapi/pull/227 has been merged, we simply test that the
    # path is correct.
    #
    # resp = await app_client.get(search_path)
    # assert resp.status_code == 200


@pytest.mark.asyncio
async def test_conformance_link(response_json, app_client):
    conformance_link = get_link(response_json, "conformance")

    assert conformance_link is not None
    assert conformance_link.get("type") == "application/json"

    conformance_path = urllib.parse.urlsplit(conformance_link.get("href")).path
    assert conformance_path == "/conformance"

    resp = await app_client.get(conformance_path)
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_docs_link(response_json, app_client):
    docs_link = get_link(response_json, "docs")

    assert docs_link is not None
    assert docs_link.get("type") == "application/json"

    docs_path = urllib.parse.urlsplit(docs_link.get("href")).path
    assert docs_path == "/docs"

    resp = await app_client.get(docs_path)
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_service_desc_link(response_json, app_client):
    service_desc_link = get_link(response_json, "service-desc")

    assert service_desc_link is not None
    assert (
        service_desc_link.get("type") == "application/vnd.oai.openapi+json;version=3.0"
    )

    service_desc_path = urllib.parse.urlsplit(service_desc_link.get("href")).path
    assert service_desc_path == "/openapi.json"

    resp = await app_client.get(service_desc_path)
    assert resp.status_code == 200
