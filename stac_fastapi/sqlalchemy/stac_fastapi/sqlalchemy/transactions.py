"""transactions extension client."""

import json
import logging
from typing import Dict, Optional, Type

import attr

# TODO: This import should come from `backend` module
from stac_fastapi.extensions.third_party.bulk_transactions import (
    BaseBulkTransactionsClient,
)
from stac_fastapi.sqlalchemy.models import database, schemas
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.types.core import BaseTransactionsClient
from stac_fastapi.types.errors import NotFoundError

logger = logging.getLogger(__name__)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    collection_table: Type[database.Collection] = attr.ib(default=database.Collection)
    item_table: Type[database.Item] = attr.ib(default=database.Item)

    def create_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Create item."""
        data = self.item_table.from_schema(model)
        with self.session.writer.context_session() as session:
            session.add(data)
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Item.from_orm(data)

    def create_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create collection."""
        data = self.collection_table.from_schema(model)
        data.type = "collection"
        with self.session.writer.context_session() as session:
            session.add(data)
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Collection.from_orm(data)

    def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Update item."""
        with self.session.reader.context_session() as session:
            query = session.query(self.item_table).filter(
                self.item_table.id == model.id
            )
            if not query.scalar():
                raise NotFoundError(f"Item {model.id} not found")
            # SQLAlchemy orm updates don't seem to like geoalchemy types
            data = self.item_table.get_database_model(model)
            data.pop("geometry", None)
            query.update(data)

            response = self.item_table.from_schema(model)
            response.base_url = str(kwargs["request"].base_url)
            return schemas.Item.from_orm(response)
        return model

    def update_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Update collection."""
        with self.session.reader.context_session() as session:
            query = session.query(self.collection_table).filter(
                self.collection_table.id == model.id
            )
            if not query.scalar():
                raise NotFoundError(f"Item {model.id} not found")
            # SQLAlchemy orm updates don't seem to like geoalchemy types
            data = self.collection_table.get_database_model(model)
            data.pop("geometry", None)
            query.update(data)
        return model

    def delete_item(self, item_id: str, collection_id: str, **kwargs) -> schemas.Item:
        """Delete item."""
        with self.session.writer.context_session() as session:
            query = session.query(self.item_table).filter(self.item_table.id == item_id)
            data = query.first()
            if not data:
                raise NotFoundError(f"Item {id} not found")
            query.delete()
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Item.from_orm(data)

    def delete_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Delete collection."""
        with self.session.writer.context_session() as session:
            query = session.query(self.collection_table).filter(
                self.collection_table.id == id
            )
            data = query.first()
            if not data:
                raise NotFoundError(f"Collection {id} not found")
            query.delete()
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Collection.from_orm(data)


@attr.s
class BulkTransactionsClient(BaseBulkTransactionsClient):
    """Postgres bulk transactions."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    debug: bool = attr.ib(default=False)

    def __attrs_post_init__(self):
        """Create sqlalchemy engine."""
        self.engine = self.session.writer.cached_engine

    @staticmethod
    def _preprocess_item(item: schemas.Item) -> Dict:
        """Preprocess items to match data model.

        # TODO: dedup with GetterDict logic (ref #58)
        """
        item = item.dict(exclude_none=True)
        item["geometry"] = json.dumps(item["geometry"])
        item["collection_id"] = item.pop("collection")
        item["datetime"] = item["properties"].pop("datetime")
        return item

    def bulk_item_insert(
        self, items: schemas.Items, chunk_size: Optional[int] = None, **kwargs
    ) -> str:
        """Bulk item insertion using sqlalchemy core.

        https://docs.sqlalchemy.org/en/13/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow
        """
        # Use items.items because schemas.Items is a model with an items key
        processed_items = [self._preprocess_item(item) for item in items.items]
        return_msg = f"Successfully added {len(processed_items)} items."
        if chunk_size:
            for chunk in self._chunks(processed_items, chunk_size):
                self.engine.execute(database.Item.__table__.insert(), chunk)
            return return_msg

        self.engine.execute(database.Item.__table__.insert(), processed_items)
        return return_msg
