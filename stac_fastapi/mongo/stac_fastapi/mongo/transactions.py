"""transactions extension client."""

import logging

import attr

from datetime import datetime
from stac_pydantic.shared import DATETIME_RFC339

# from stac_fastapi.extensions.third_party.bulk_transactions import (
#     BaseBulkTransactionsClient,
#     Items,
# )
from stac_fastapi.mongo.mongo_config import MongoSettings
from stac_fastapi.mongo.session import Session
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import BaseTransactionsClient
from stac_fastapi.types.errors import ConflictError, ForeignKeyError, NotFoundError
from stac_fastapi.types.links import CollectionLinks, ItemLinks
from stac_fastapi.mongo.serializers import ItemSerializer
logger = logging.getLogger(__name__)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    db = MongoSettings()

    def create_item(self, model: stac_types.Item, **kwargs):
        """Create item."""
        base_url = str(kwargs["request"].base_url)
        item_links = ItemLinks(
            collection_id=model["collection"], item_id=model["id"], base_url=base_url
        ).create_links()
        model["links"] = item_links

        if not self.db.stac_collection.count_documents(
            {"id": model["collection"]}, limit=1
        ):
            raise ForeignKeyError(f"Collection {model['collection']} does not exist")

        if self.db.stac_item.count_documents(
            {"id": model["id"], "collection": model["collection"]}, limit=1
        ):
            raise ConflictError(
                f"Item {model['id']} in collection {model['collection']} already exists"
            )
        else:
            now = datetime.utcnow().strftime(DATETIME_RFC339)
            if "created" not in model["properties"]:
                model["properties"]["created"] = str(now)
            self.db.stac_item.insert_one(model)
            return ItemSerializer.db_to_stac(model, base_url)

    def create_collection(self, model: stac_types.Collection, **kwargs):
        """Create collection."""
        base_url = str(kwargs["request"].base_url)
        collection_links = CollectionLinks(
            collection_id=model["id"], base_url=base_url
        ).create_links()
        model["links"] = collection_links

        if self.db.stac_collection.count_documents({"id": model["id"]}, limit=1):
            raise ConflictError(f"Collection {model['id']} already exists")
        else:
            self.db.stac_collection.insert_one(model)

    def update_item(self, model: stac_types.Item, **kwargs):
        """Update item."""
        base_url = str(kwargs["request"].base_url)
        if not self.db.stac_collection.count_documents(
            {"id": model["collection"]}, limit=1
        ):
            raise ForeignKeyError(f"Collection {model['collection']} does not exist")

        if (
            self.db.stac_item.count_documents(
                {"id": model["id"], "collection": model["collection"]}
            )
            == 0
        ):
            raise NotFoundError(
                f"Item {model['id']} in collection {model['collection']} not found"
            )
        self.delete_item(item_id=model["id"], collection_id=model["collection"])
        now = datetime.utcnow().strftime(DATETIME_RFC339)
        model["properties"]["updated"] = str(now)
        self.create_item(model, **kwargs)
        return ItemSerializer.db_to_stac(model, base_url)

    def update_collection(self, model: stac_types.Collection, **kwargs):
        """Update collection."""
        if self.db.stac_collection.count_documents({"id": model["id"]}) == 0:
            raise NotFoundError(f"Collection {model['id']} not found")
        self.delete_collection(model["id"])
        self.create_collection(model, **kwargs)

    def delete_item(self, item_id: str, collection_id: str, **kwargs):
        """Delete item."""
        if (
            self.db.stac_item.count_documents(
                {"id": item_id, "collection": collection_id}
            )
            == 0
        ):
            raise NotFoundError(f"Item {item_id} does not exist")
        self.db.stac_item.delete_one({"id": item_id, "collection": collection_id})

    def delete_collection(self, collection_id: str, **kwargs):
        """Delete collection."""
        if self.db.stac_collection.count_documents({"id": collection_id}) == 0:
            raise NotFoundError(f"Collection {collection_id} does not exist")
        self.db.stac_collection.delete_one({"id": collection_id})


# @attr.s
# class BulkTransactionsClient(BaseBulkTransactionsClient):
#     """Postgres bulk transactions."""

#     session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
#     debug: bool = attr.ib(default=False)
#     item_table: Type[database.Item] = attr.ib(default=database.Item)
#     item_serializer: Type[serializers.Serializer] = attr.ib(
#         default=serializers.ItemSerializer
#     )

#     def __attrs_post_init__(self):
#         """Create sqlalchemy engine."""
#         pass
#         # self.engine = self.session.writer.cached_engine

#     def _preprocess_item(self, item: stac_types.Item) -> stac_types.Item:
#         """Preprocess items to match data model.

#         # TODO: dedup with GetterDict logic (ref #58)
#         """
#         db_model = self.item_serializer.stac_to_db(item)
#         return self.item_serializer.row_to_dict(db_model)

#     def bulk_item_insert(
#         self, items: Items, chunk_size: Optional[int] = None, **kwargs
#     ) -> str:
#         """Bulk item insertion using sqlalchemy core.

#         https://docs.sqlalchemy.org/en/13/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow
#         """
#         # Use items.items because schemas.Items is a model with an items key
#         processed_items = [self._preprocess_item(item) for item in items]
#         return_msg = f"Successfully added {len(processed_items)} items."
#         if chunk_size:
#             for chunk in self._chunks(processed_items, chunk_size):
#                 self.engine.execute(self.item_table.__table__.insert(), chunk)
#             return return_msg

#         self.engine.execute(self.item_table.__table__.insert(), processed_items)
#         return return_msg
