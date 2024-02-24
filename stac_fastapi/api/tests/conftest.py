import pytest
from stac_pydantic import Collection, Item
from stac_pydantic.api.utils import link_factory

collection_links = link_factory.CollectionLinks("/", "test").create_links()
item_links = link_factory.ItemLinks("/", "test", "test").create_links()


@pytest.fixture
def _collection():
    return Collection(
        id="test_collection",
        title="Test Collection",
        description="A test collection",
        keywords=["test"],
        license="proprietary",
        extent={
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [["2000-01-01T00:00:00Z", None]]},
        },
        links=collection_links,
    )


@pytest.fixture
def collection(_collection: Collection):
    return _collection.model_dump_json()


@pytest.fixture
def collection_dict(_collection: Collection):
    return _collection.model_dump(mode="json")


@pytest.fixture
def _item():
    return Item(
        id="test_item",
        type="Feature",
        geometry={"type": "Point", "coordinates": [0, 0]},
        bbox=[-180, -90, 180, 90],
        properties={"datetime": "2000-01-01T00:00:00Z"},
        links=item_links,
        assets={},
    )


@pytest.fixture
def item(_item: Item):
    return _item.model_dump_json()


@pytest.fixture
def item_dict(_item: Item):
    return _item.model_dump(mode="json")
