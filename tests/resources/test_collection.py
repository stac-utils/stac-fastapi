from stac_api.errors import DatabaseError
from stac_api.clients import collection_crud_client_factory
from stac_api.clients.collection_crud import CollectionCrudClient

from ..conftest import create_test_client_with_error


def test_create_and_delete_collection(app_client, load_test_data):
    """Test creation and deletion of a collection"""
    test_collection = load_test_data("test_collection.json")
    test_collection["id"] = "test"

    resp = app_client.post(f"/collections", json=test_collection)
    assert resp.status_code == 200

    resp = app_client.delete(f"/collections/{test_collection['id']}")
    assert resp.status_code == 200


def test_create_collection_conflict(app_client, load_test_data):
    """Test creation of a collection which already exists"""
    # This collection ID is created in the fixture, so this should be a conflict
    test_collection = load_test_data("test_collection.json")
    resp = app_client.post(f"/collections", json=test_collection)
    assert resp.status_code == 409


def test_delete_missing_collection(app_client):
    """Test deletion of a collection which does not exist"""
    resp = app_client.delete(f"/collections/missing-collection")
    assert resp.status_code == 404


def test_update_collection_already_exists(app_client, load_test_data):
    """Test updating a collection which already exists"""
    test_collection = load_test_data("test_collection.json")
    test_collection["keywords"].append("test")
    resp = app_client.put("/collections", json=test_collection)
    assert resp.status_code == 200

    resp = app_client.get(f"/collections/{test_collection['id']}")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert "test" in resp_json["keywords"]


def test_update_new_collection(app_client, load_test_data):
    """Test updating a collection which does not exist (same as creation)"""
    test_collection = load_test_data("test_collection.json")
    test_collection["id"] = "new-test-collection"

    resp = app_client.put(f"/collections", json=test_collection)
    assert resp.status_code == 200

    resp = app_client.get(f"/collections/{test_collection['id']}")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["id"] == test_collection["id"]


def test_get_all_collections(app_client, load_test_data):
    """Test reading all collections"""
    test_collection = load_test_data("test_collection.json")
    test_collection["id"] = "new-test-collection"

    resp = app_client.post(f"/collections", json=test_collection)
    assert resp.status_code == 200

    resp = app_client.get("/collections")
    assert resp.status_code == 200
    resp_json = resp.json()

    assert test_collection["id"] in [coll["id"] for coll in resp_json]


def test_collection_not_found(app_client):
    """Test read a collection which does not exist"""
    resp = app_client.get(f"/collections/does-not-exist")
    assert resp.status_code == 404


def test_create_collection_database_error(load_test_data):
    """Test 424 is raised on database error"""
    test_collection = load_test_data("test_collection.json")
    with create_test_client_with_error(
        client=CollectionCrudClient,
        mocked_method="create",
        dependency=collection_crud_client_factory,
        error=DatabaseError(message="error"),
    ) as test_client:
        resp = test_client.post("/collections", json=test_collection)
        assert resp.status_code == 424


def test_update_collection_database_error(load_test_data):
    """Test 424 is raised on database error"""
    test_collection = load_test_data("test_collection.json")
    with create_test_client_with_error(
        client=CollectionCrudClient,
        mocked_method="update",
        dependency=collection_crud_client_factory,
        error=DatabaseError(message="error"),
    ) as test_client:
        resp = test_client.put("/collections", json=test_collection)
        assert resp.status_code == 424


def tet_get_all_collections_database_error():
    """Test 424 is raised on database error"""
    with create_test_client_with_error(
        client=CollectionCrudClient,
        mocked_method="get_all_collections",
        dependency=collection_crud_client_factory,
        error=DatabaseError(message="error"),
    ) as test_client:
        resp = test_client.get("/collections")
        assert resp.status_code == 424


def test_get_collection_database_error(load_test_data):
    """Test 424 is raised on database error"""
    test_collection = load_test_data("test_collection.json")
    with create_test_client_with_error(
        client=CollectionCrudClient,
        mocked_method="read",
        dependency=collection_crud_client_factory,
        error=DatabaseError(message="error"),
    ) as test_client:
        resp = test_client.get(f"/collections/{test_collection['id']}")
        assert resp.status_code == 424


def test_delete_collection_database_error(load_test_data):
    """Test 424 is raised on database error"""
    test_collection = load_test_data("test_collection.json")
    with create_test_client_with_error(
        client=CollectionCrudClient,
        mocked_method="delete",
        dependency=collection_crud_client_factory,
        error=DatabaseError(message="error"),
    ) as test_client:
        resp = test_client.delete(f"/collections/{test_collection['id']}")
        assert resp.status_code == 424
