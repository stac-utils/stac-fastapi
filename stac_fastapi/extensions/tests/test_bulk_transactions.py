"""Tests for the Bulk Transactions extension."""

from typing import Iterator
from unittest.mock import Mock

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.third_party.bulk_transactions import (
    AsyncBaseBulkTransactionsClient,
    BaseBulkTransactionsClient,
    BulkTransactionExtension,
    BulkTransactionMethod,
    Items,
)
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient

# --- UNIT TESTS ---


def test_items_model_iteration():
    """Test the Items pydantic model and its custom iterator."""
    item_data = {
        "id1": {"type": "Feature", "id": "id1"},
        "id2": {"type": "Feature", "id": "id2"},
    }
    bulk_items = Items(items=item_data, method=BulkTransactionMethod.INSERT)

    # Test iteration returns values, not keys
    items_list = list(bulk_items)
    assert len(items_list) == 2
    assert {"type": "Feature", "id": "id1"} in items_list
    assert bulk_items.method == "insert"


def test_base_client_chunks():
    """Test the static _chunks method on BaseBulkTransactionsClient."""
    test_list = [1, 2, 3, 4, 5, 6, 7]

    # Chunk by 3
    chunks = list(BaseBulkTransactionsClient._chunks(test_list, 3))
    assert chunks == [[1, 2, 3], [4, 5, 6], [7]]

    # Chunk by larger than list
    chunks_large = list(BaseBulkTransactionsClient._chunks(test_list, 10))
    assert chunks_large == [[1, 2, 3, 4, 5, 6, 7]]


def test_bulk_transaction_extension_defaults():
    """Test the default instantiation of the BulkTransactionExtension."""
    mock_client = Mock(spec=AsyncBaseBulkTransactionsClient)
    ext = BulkTransactionExtension(client=mock_client)

    assert ext.client == mock_client
    assert ext.schema_href is None
    assert ext.conformance_classes == []


def test_bulk_transaction_extension_customization():
    """Test instantiating BulkTransactionExtension with custom arguments."""
    mock_client = Mock(spec=AsyncBaseBulkTransactionsClient)
    custom_conformance = ["https://example.com/bulk-spec"]
    custom_schema = "https://example.com/bulk-schema.json"

    ext = BulkTransactionExtension(
        client=mock_client,
        conformance_classes=custom_conformance,
        schema_href=custom_schema,
    )

    assert ext.conformance_classes == custom_conformance
    assert ext.schema_href == custom_schema


# --- INTEGRATION TESTS ---


class DummyCoreClient(BaseCoreClient):
    """Dummy core client for routing purposes."""

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


class DummyBulkTransactionsClient(AsyncBaseBulkTransactionsClient):
    """Dummy client returning a success message to verify routing and parsing."""

    async def bulk_item_insert(self, items: Items, **kwargs) -> str:
        """Mock bulk insert that just returns a string confirming the count."""
        count = len(list(items))
        method = items.method.value
        return f"Successfully processed {count} items via {method}."


@pytest.fixture
def core_client() -> DummyCoreClient:
    return DummyCoreClient()


@pytest.fixture
def bulk_transactions_client() -> DummyBulkTransactionsClient:
    return DummyBulkTransactionsClient()


@pytest.fixture
def client(
    core_client: DummyCoreClient, bulk_transactions_client: DummyBulkTransactionsClient
) -> Iterator[TestClient]:
    """Fixture to set up the TestClient with the BulkTransactionExtension."""
    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            BulkTransactionExtension(client=bulk_transactions_client),
        ],
    )
    with TestClient(api.app) as client:
        yield client


@pytest.fixture
def item() -> dict:
    """A standard STAC Item dictionary."""
    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "stac_extensions": [],
        "id": "test_item",
        "geometry": {"type": "Point", "coordinates": [-105, 40]},
        "bbox": [-105, 40, -105, 40],
        "properties": {"datetime": "2020-06-13T13:00:00Z"},
        "links": [],
        "assets": {},
        "collection": "a-collection",
    }


def test_bulk_item_insert(client: TestClient, item: dict) -> None:
    """Test the bulk insert endpoint processes items correctly."""
    payload = {
        "items": {item["id"]: item, "test_item_2": {**item, "id": "test_item_2"}},
        "method": "insert",
    }

    response = client.post("/collections/a-collection/bulk_items", json=payload)

    assert response.is_success, response.text
    assert response.json() == "Successfully processed 2 items via insert."


def test_bulk_item_upsert(client: TestClient, item: dict) -> None:
    """Test the bulk insert endpoint properly passes the 'upsert' method."""
    payload = {"items": {item["id"]: item}, "method": "upsert"}

    response = client.post("/collections/a-collection/bulk_items", json=payload)

    assert response.is_success, response.text
    assert response.json() == "Successfully processed 1 items via upsert."


def test_bulk_item_invalid_method(client: TestClient, item: dict) -> None:
    """Test that pydantic catches invalid bulk transaction methods."""
    payload = {"items": {item["id"]: item}, "method": "invalid_method"}

    response = client.post("/collections/a-collection/bulk_items", json=payload)

    assert response.status_code == 400
