from urllib.parse import urlsplit

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.third_party.tiles import TilesClient, TilesExtension
from stac_fastapi.sqlalchemy.config import SqlalchemySettings

from ..conftest import MockStarletteRequest


@pytest.fixture
def tiles_extension_app(postgres_core, postgres_transactions, load_test_data):
    # Ingest test data for testing
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    settings = SqlalchemySettings()
    api = StacApi(
        settings=settings,
        client=postgres_core,
        extensions=[TilesExtension(TilesClient(postgres_core))],
    )
    with TestClient(api.app) as test_app:
        yield test_app

    # Cleanup test data
    postgres_transactions.delete_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    postgres_transactions.delete_collection(coll["id"], request=MockStarletteRequest)


def test_tiles_extension(tiles_extension_app, load_test_data):
    item = load_test_data("test_item.json")

    # Fetch the item
    resp = tiles_extension_app.get(
        f"/collections/{item['collection']}/items/{item['id']}"
    )
    resp_json = resp.json()
    assert resp.status_code == 200

    # Find the OGC tiles link
    link = None
    for link in resp_json["links"]:
        if link.get("title") == "tiles":
            break
    assert link

    # Request the TileSet resource
    tiles_path = urlsplit(link["href"]).path
    resp = tiles_extension_app.get(tiles_path)
    assert resp.status_code == 200
    tileset = resp.json()

    assert tileset["extent"]["bbox"][0] == item["bbox"]

    # We expect the tileset to have certain links
    link_titles = [link["title"] for link in tileset["links"]]
    assert "tiles" in link_titles
    assert "tilejson" in link_titles
    assert "viewer" in link_titles

    # Confirm templated links are actually templates
    for link in tileset["links"]:
        if link.get("templated"):
            # Since this is the `tile` extension checking against zoom seems reliable
            assert "{z}" in link["href"]
        else:
            assert "{z}" not in link["href"]
