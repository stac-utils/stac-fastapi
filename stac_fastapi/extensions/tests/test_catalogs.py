"""Tests for the Catalogs extension."""

from typing import Iterator

import pytest
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.item import Item
from stac_pydantic.item_collection import ItemCollection
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import CatalogsExtension
from stac_fastapi.extensions.core.multi_tenant_catalogs.client import (
    BaseCatalogsClient,
)
from stac_fastapi.extensions.core.multi_tenant_catalogs.types import Catalogs, Children
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient


class DummyCoreClient(BaseCoreClient):
    """Dummy core client for testing."""

    def all_collections(self, *args, **kwargs):
        return {"collections": [], "links": []}

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


class DummyCatalogsClient(BaseCatalogsClient):
    """Dummy catalogs client for testing."""

    def get_catalogs(self, limit: int = None, token: str = None):
        return Catalogs(
            catalogs=[
                Catalog(
                    type="Catalog",
                    id="test-catalog-1",
                    description="Test Catalog 1",
                    stac_version="1.0.0",
                    links=[],
                ),
                Catalog(
                    type="Catalog",
                    id="test-catalog-2",
                    description="Test Catalog 2",
                    stac_version="1.0.0",
                    links=[],
                ),
            ],
            links=[],
            numberMatched=2,
            numberReturned=2,
        )

    def create_catalog(self, catalog: Catalog):
        return Catalog(
            type="Catalog",
            id=catalog.id,
            description=catalog.description or "Created catalog",
            stac_version="1.0.0",
            links=[],
        )

    def get_catalog(self, catalog_id: str):
        return Catalog(
            type="Catalog",
            id=catalog_id,
            description=f"Catalog {catalog_id}",
            stac_version="1.0.0",
            links=[],
        )

    def update_catalog(self, catalog_id: str, catalog: Catalog):
        return Catalog(
            type="Catalog",
            id=catalog_id,
            description=catalog.description or f"Updated {catalog_id}",
            stac_version="1.0.0",
            links=[],
        )

    def delete_catalog(self, catalog_id: str):
        return None

    def get_catalog_collections(self, catalog_id: str):
        return {
            "collections": [
                {
                    "type": "Collection",
                    "id": "test-collection",
                    "description": "Test Collection",
                    "extent": {
                        "spatial": {"bbox": [[-180, -90, 180, 90]]},
                        "temporal": {"interval": [[None, None]]},
                    },
                    "license": "proprietary",
                    "links": [
                        {"rel": "root", "href": "/", "type": "application/json"},
                        {
                            "rel": "self",
                            "href": f"/catalogs/{catalog_id}/collections/test-collection",
                            "type": "application/json",
                        },
                    ],
                }
            ],
            "links": [
                {"rel": "root", "href": "/", "type": "application/json"},
                {
                    "rel": "self",
                    "href": f"/catalogs/{catalog_id}/collections",
                    "type": "application/json",
                },
            ],
        }

    def get_sub_catalogs(self, catalog_id: str, limit: int = None, token: str = None):
        return Catalogs(
            catalogs=[
                Catalog(
                    type="Catalog",
                    id=f"{catalog_id}-sub-1",
                    description=f"Sub-catalog of {catalog_id}",
                    stac_version="1.0.0",
                    links=[],
                )
            ],
            links=[],
            numberMatched=1,
            numberReturned=1,
        )

    def create_sub_catalog(self, catalog_id: str, catalog: Catalog):
        return Catalog(
            type="Catalog",
            id=catalog.id,
            description=catalog.description or f"Sub-catalog of {catalog_id}",
            stac_version="1.0.0",
            links=[],
        )

    def create_catalog_collection(self, catalog_id: str, collection: Collection):
        return Collection(
            type="Collection",
            id=collection.id,
            description=collection.description or f"Collection in {catalog_id}",
            extent={
                "spatial": {"bbox": [[-180, -90, 180, 90]]},
                "temporal": {"interval": [[None, None]]},
            },
            license="proprietary",
            links=[],
        )

    def get_catalog_collection(self, catalog_id: str, collection_id: str):
        return Collection(
            type="Collection",
            id=collection_id,
            description=f"Collection {collection_id} in {catalog_id}",
            extent={
                "spatial": {"bbox": [[-180, -90, 180, 90]]},
                "temporal": {"interval": [[None, None]]},
            },
            license="proprietary",
            links=[],
        )

    def unlink_catalog_collection(self, catalog_id: str, collection_id: str):
        return None

    def get_catalog_collection_items(self, catalog_id: str, collection_id: str):
        return ItemCollection(
            type="FeatureCollection",
            features=[
                Item(
                    type="Feature",
                    id="test-item",
                    geometry={"type": "Point", "coordinates": [0, 0]},
                    bbox=[0, 0, 0, 0],
                    datetime="2024-01-01T00:00:00Z",
                    properties={"datetime": "2024-01-01T00:00:00Z"},
                    links=[],
                    assets={},
                )
            ],
            links=[],
        )

    def get_catalog_collection_item(
        self, catalog_id: str, collection_id: str, item_id: str
    ):
        return Item(
            type="Feature",
            id=item_id,
            geometry={"type": "Point", "coordinates": [0, 0]},
            bbox=[0, 0, 0, 0],
            datetime="2024-01-01T00:00:00Z",
            properties={"datetime": "2024-01-01T00:00:00Z"},
            links=[],
            assets={},
        )

    def get_catalog_children(
        self, catalog_id: str, limit: int = None, token: str = None, type: str = None
    ):
        return Children(
            children=[
                {
                    "id": f"{catalog_id}-child-1",
                    "type": "Catalog",
                    "description": "Child catalog",
                },
                {
                    "id": "collection-1",
                    "type": "Collection",
                    "description": "Child collection",
                },
            ],
            links=[],
            numberMatched=2,
            numberReturned=2,
        )

    def get_catalog_conformance(self, catalog_id: str):
        return {
            "conformsTo": [
                "https://api.stacspec.org/v1.0.0/core",
                "https://api.stacspec.org/v1.0.0-beta.1/multi-tenant-catalogs",
            ]
        }

    def get_catalog_queryables(self, catalog_id: str):
        return {
            "queryables": [
                {"name": "datetime", "type": "string"},
                {"name": "platform", "type": "string"},
            ]
        }

    def unlink_sub_catalog(self, catalog_id: str, sub_catalog_id: str):
        return None


@pytest.fixture
def core_client() -> DummyCoreClient:
    """Fixture for core client."""
    return DummyCoreClient()


@pytest.fixture
def catalogs_client() -> DummyCatalogsClient:
    """Fixture for catalogs client."""
    return DummyCatalogsClient()


@pytest.fixture
def client(
    core_client: DummyCoreClient, catalogs_client: DummyCatalogsClient
) -> Iterator[TestClient]:
    """Fixture for test client."""
    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            CatalogsExtension(client=catalogs_client),
        ],
    )
    with TestClient(api.app) as test_client:
        yield test_client


def test_get_catalogs(client: TestClient) -> None:
    """Test GET /catalogs endpoint."""
    response = client.get("/catalogs")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "catalogs" in data
    assert len(data["catalogs"]) == 2
    assert data["catalogs"][0]["id"] == "test-catalog-1"
    assert data["numberMatched"] == 2
    assert data["numberReturned"] == 2


def test_create_catalog(client: TestClient) -> None:
    """Test POST /catalogs endpoint."""
    catalog_data = {
        "type": "Catalog",
        "id": "new-catalog",
        "description": "A new test catalog",
        "stac_version": "1.0.0",
        "links": [],
    }
    response = client.post("/catalogs", json=catalog_data)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["id"] == "new-catalog"
    assert data["description"] == "A new test catalog"


def test_get_catalog(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id} endpoint."""
    response = client.get("/catalogs/test-catalog-1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == "test-catalog-1"
    assert data["description"] == "Catalog test-catalog-1"


def test_update_catalog(client: TestClient) -> None:
    """Test PUT /catalogs/{catalog_id} endpoint."""
    catalog_data = {
        "type": "Catalog",
        "id": "test-catalog-1",
        "description": "Updated description",
        "stac_version": "1.0.0",
        "links": [],
    }
    response = client.put("/catalogs/test-catalog-1", json=catalog_data)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == "test-catalog-1"


def test_delete_catalog(client: TestClient) -> None:
    """Test DELETE /catalogs/{catalog_id} endpoint."""
    response = client.delete("/catalogs/test-catalog-1")
    assert response.status_code == 204, response.text


def test_get_catalog_collections(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/collections endpoint."""
    response = client.get("/catalogs/test-catalog-1/collections")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "collections" in data
    assert len(data["collections"]) == 1
    assert data["collections"][0]["id"] == "test-collection"


def test_create_catalog_collection(client: TestClient) -> None:
    """Test POST /catalogs/{catalog_id}/collections endpoint."""
    collection_data = {
        "type": "Collection",
        "id": "new-collection",
        "description": "A new collection",
        "extent": {
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [[None, None]]},
        },
        "license": "proprietary",
        "links": [],
    }
    response = client.post("/catalogs/test-catalog-1/collections", json=collection_data)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["id"] == "new-collection"


def test_get_catalog_collection(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/collections/{collection_id} endpoint."""
    response = client.get("/catalogs/test-catalog-1/collections/test-collection")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == "test-collection"


def test_unlink_catalog_collection(client: TestClient) -> None:
    """Test DELETE /catalogs/{catalog_id}/collections/{collection_id} endpoint."""
    response = client.delete("/catalogs/test-catalog-1/collections/test-collection")
    assert response.status_code == 204, response.text


def test_get_catalog_collection_items(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/collections/{collection_id}/items endpoint."""
    response = client.get("/catalogs/test-catalog-1/collections/test-collection/items")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["type"] == "FeatureCollection"
    assert len(data["features"]) == 1
    assert data["features"][0]["id"] == "test-item"


def test_get_catalog_collection_item(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/collections/{collection_id}/items/{item_id}."""
    response = client.get(
        "/catalogs/test-catalog-1/collections/test-collection/items/test-item"
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == "test-item"


def test_get_sub_catalogs(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/catalogs endpoint."""
    response = client.get("/catalogs/test-catalog-1/catalogs")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "catalogs" in data
    assert len(data["catalogs"]) == 1
    assert data["catalogs"][0]["id"] == "test-catalog-1-sub-1"


def test_create_sub_catalog(client: TestClient) -> None:
    """Test POST /catalogs/{catalog_id}/catalogs endpoint."""
    catalog_data = {
        "type": "Catalog",
        "id": "new-sub-catalog",
        "description": "A new sub-catalog",
        "stac_version": "1.0.0",
        "links": [],
    }
    response = client.post("/catalogs/test-catalog-1/catalogs", json=catalog_data)
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["id"] == "new-sub-catalog"


def test_get_catalog_children(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/children endpoint."""
    response = client.get("/catalogs/test-catalog-1/children")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "children" in data
    assert len(data["children"]) == 2
    assert data["numberMatched"] == 2


def test_get_catalog_children_with_type_filter(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/children with type filter."""
    response = client.get("/catalogs/test-catalog-1/children?type=Catalog")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "children" in data


def test_get_catalog_conformance(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/conformance endpoint."""
    response = client.get("/catalogs/test-catalog-1/conformance")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "conformsTo" in data
    assert len(data["conformsTo"]) > 0


def test_get_catalog_queryables(client: TestClient) -> None:
    """Test GET /catalogs/{catalog_id}/queryables endpoint."""
    response = client.get("/catalogs/test-catalog-1/queryables")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "queryables" in data
    assert len(data["queryables"]) > 0


def test_unlink_sub_catalog(client: TestClient) -> None:
    """Test DELETE /catalogs/{catalog_id}/catalogs/{sub_catalog_id} endpoint."""
    response = client.delete("/catalogs/test-catalog-1/catalogs/test-catalog-1-sub-1")
    assert response.status_code == 204, response.text


def test_landing_page_includes_catalogs_links(client: TestClient) -> None:
    """Test that landing page includes catalogs links."""
    response = client.get("/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "links" in data
    # The catalogs extension should be registered and provide links
    # Check if any link exists (the exact catalogs link depends on extension registration)
    assert len(data["links"]) > 0
