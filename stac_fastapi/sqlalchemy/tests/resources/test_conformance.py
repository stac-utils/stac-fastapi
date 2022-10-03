import urllib.parse

import pytest


@pytest.fixture
def response(app_client):
    return app_client.get("/")


@pytest.fixture
def response_json(response):
    return response.json()


def get_link(landing_page, rel_type):
    return next(
        filter(lambda link: link["rel"] == rel_type, landing_page["links"]), None
    )


def test_landing_page_health(response):
    """Test landing page"""
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


# Parameters for test_landing_page_links test below.
# Each tuple has the following values (in this order):
#  - Rel type of link to test
#  - Expected MIME/Media Type
#  - Expected relative path
link_tests = [
    ("root", "application/json", "/"),
    ("conformance", "application/json", "/conformance"),
    ("service-doc", "text/html", "/api.html"),
    ("service-desc", "application/vnd.oai.openapi+json;version=3.0", "/api"),
]


@pytest.mark.parametrize("rel_type,expected_media_type,expected_path", link_tests)
def test_landing_page_links(
    response_json, app_client, rel_type, expected_media_type, expected_path
):
    link = get_link(response_json, rel_type)

    assert link is not None, f"Missing {rel_type} link in landing page"
    assert link.get("type") == expected_media_type

    link_path = urllib.parse.urlsplit(link.get("href")).path
    assert link_path == expected_path

    resp = app_client.get(link_path)
    assert resp.status_code == 200


# This endpoint currently returns a 404 for empty result sets, but testing for this response
# code here seems meaningless since it would be the same as if the endpoint did not exist. Once
# https://github.com/stac-utils/stac-fastapi/pull/227 has been merged we can add this to the
# parameterized tests above.
def test_search_link(response_json):
    search_link = get_link(response_json, "search")

    assert search_link is not None
    assert search_link.get("type") == "application/geo+json"

    search_path = urllib.parse.urlsplit(search_link.get("href")).path
    assert search_path == "/search"
