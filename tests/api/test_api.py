from datetime import datetime, timedelta

from starlette.testclient import TestClient

from stac_api.api import create_app
from stac_api.api.routers import create_core_router, create_transactions_router
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
    settings = ApiSettings()
    router = create_core_router(postgres_core, settings)
    assert STAC_CORE_ROUTES == sorted(
        [f"{list(route.methods)[0]} {route.path}" for route in router.routes]
    )


def test_transactions_router(postgres_transactions):
    settings = ApiSettings()
    router = create_transactions_router(postgres_transactions, settings)
    assert STAC_TRANSACTION_ROUTES == sorted(
        [f"{list(route.methods)[0]} {route.path}" for route in router.routes]
    )


def test_app_transaction_extension(load_test_data):
    settings = ApiSettings(stac_api_extensions=["transaction"])
    app = create_app(settings)

    with TestClient(app) as client:
        collection = load_test_data("test_collection.json")
        resp = client.post("/collections", json=collection)
        assert resp.status_code == 200

        item = load_test_data("test_item.json")
        resp = client.post(f"/collections/{item['collection']}/items", json=item)
        assert resp.status_code == 200


def test_app_context_extension(load_test_data, postgres_transactions):
    settings = ApiSettings(stac_api_extensions=["context"])
    app = create_app(settings)

    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    item = Item.parse_obj(load_test_data("test_item.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    with TestClient(app) as client:
        resp = client.get("/search", params={"collections": ["test-collection"]})
        assert resp.status_code == 200
        resp_json = resp.json()

        assert "context" in resp_json
        assert resp_json["context"]["returned"] == resp_json["context"]["matched"] == 1


def test_app_fields_extension(load_test_data, postgres_transactions):
    settings = ApiSettings(stac_api_extensions=["fields"])
    app = create_app(settings)

    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    item = Item.parse_obj(load_test_data("test_item.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    with TestClient(app) as client:
        resp = client.get("/search", params={"collections": ["test-collection"]})
        assert resp.status_code == 200
        resp_json = resp.json()
        assert list(resp_json["features"][0]["properties"]) == ["datetime"]


def test_app_query_extension(load_test_data, postgres_transactions):
    settings = ApiSettings(stac_api_extensions=["query"],)
    app = create_app(settings)

    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    test_item = load_test_data("test_item.json")
    item = Item.parse_obj(test_item)
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    with TestClient(app) as client:
        params = {
            "query": {"proj:epsg": {"gt": test_item["properties"]["proj:epsg"] + 1}}
        }
        resp = client.post("/search", json=params)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert len(resp_json["features"]) == 0


def test_app_sort_extension(load_test_data, postgres_transactions):
    settings = ApiSettings(stac_api_extensions=["sort"],)
    app = create_app(settings)

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

    with TestClient(app) as client:
        params = {
            "collections": [first_item["collection"]],
            "sortby": [{"field": "datetime", "direction": "desc"}],
        }
        resp = client.post("/search", json=params)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert resp_json["features"][0]["id"] == first_item["id"]
        assert resp_json["features"][1]["id"] == second_item["id"]
