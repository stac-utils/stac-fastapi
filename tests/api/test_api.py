from datetime import datetime, timedelta

from starlette.testclient import TestClient

from stac_api.api.app import StacApi
from stac_api.api.extensions import QueryExtension, SortExtension, TransactionExtension
from stac_api.models.schemas import Collection, Item

from ..conftest import ApiSettings, MockStarletteRequest

STAC_CORE_ROUTES = [
    "GET /",
    "GET /collections",
    "GET /collections/{collectionId}",
    "GET /collections/{collectionId}/items",
    "GET /collections/{collectionId}/items/{itemId}",
    "GET /conformance",
    "GET /search",
    "POST /search",
]

STAC_TRANSACTION_ROUTES = [
    "DELETE /collections/{collectionId}",
    "DELETE /collections/{collectionId}/items/{itemId}",
    "POST /collections",
    "POST /collections/{collectionId}/items",
    "PUT /collections",
    "PUT /collections/{collectionId}/items",
]


def test_core_router(postgres_core):
    api = StacApi(settings=ApiSettings(), client=postgres_core,)

    core_routes = set(STAC_CORE_ROUTES)
    api_routes = set(
        [f"{list(route.methods)[0]} {route.path}" for route in api.app.routes]
    )
    assert not core_routes - api_routes


def test_transactions_router(postgres_transactions, postgres_core):
    api = StacApi(
        settings=ApiSettings(),
        client=postgres_core,
        extensions=[TransactionExtension(postgres_transactions)],
    )
    transaction_routes = set(STAC_TRANSACTION_ROUTES)
    api_routes = set(
        [f"{list(route.methods)[0]} {route.path}" for route in api.app.routes]
    )
    assert not transaction_routes - api_routes


def test_app_transaction_extension(
    postgres_core, postgres_transactions, load_test_data
):
    api = StacApi(
        settings=ApiSettings(),
        client=postgres_core,
        extensions=[TransactionExtension(postgres_transactions)],
    )

    with TestClient(api.app) as client:
        collection = load_test_data("test_collection.json")
        resp = client.post("/collections", json=collection)
        assert resp.status_code == 200

        item = load_test_data("test_item.json")
        resp = client.post(f"/collections/{item['collection']}/items", json=item)
        assert resp.status_code == 200


def test_app_query_extension(load_test_data, postgres_core, postgres_transactions):
    api = StacApi(
        settings=ApiSettings(),
        client=postgres_core,
        extensions=[TransactionExtension(postgres_transactions), QueryExtension()],
    )

    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    test_item = load_test_data("test_item.json")
    item = Item.parse_obj(test_item)
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    with TestClient(api.app) as client:
        params = {
            "query": {"proj:epsg": {"gt": test_item["properties"]["proj:epsg"] + 1}}
        }
        resp = client.post("/search", json=params)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert len(resp_json["features"]) == 0


def test_app_sort_extension(load_test_data, postgres_core, postgres_transactions):
    api = StacApi(
        settings=ApiSettings(),
        client=postgres_core,
        extensions=[TransactionExtension(postgres_transactions), SortExtension()],
    )

    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    first_item = load_test_data("test_item.json")
    item_date = datetime.strptime(
        first_item["properties"]["datetime"], "%Y-%m-%dT%H:%M:%SZ"
    )
    postgres_transactions.create_item(
        Item.parse_obj(first_item), request=MockStarletteRequest
    )

    second_item = load_test_data("test_item.json")
    second_item["id"] = "another-item"
    another_item_date = item_date - timedelta(days=1)
    second_item["properties"]["datetime"] = another_item_date.strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    postgres_transactions.create_item(
        Item.parse_obj(second_item), request=MockStarletteRequest
    )

    with TestClient(api.app) as client:
        params = {
            "collections": [first_item["collection"]],
            "sortby": [{"field": "datetime", "direction": "desc"}],
        }
        resp = client.post("/search", json=params)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert resp_json["features"][0]["id"] == first_item["id"]
        assert resp_json["features"][1]["id"] == second_item["id"]
