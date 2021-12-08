"""transactions extension client."""

import logging
from typing import Optional, Type

import attr

from stac_fastapi.extensions.third_party.bulk_transactions import (
    BaseBulkTransactionsClient,
    Items,
)
from stac_fastapi.sqlalchemy import serializers
from stac_fastapi.sqlalchemy.models import database
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import BaseTransactionsClient
from stac_fastapi.types.errors import NotFoundError

logger = logging.getLogger(__name__)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    collection_table: Type[database.Collection] = attr.ib(default=database.Collection)
    item_table: Type[database.Item] = attr.ib(default=database.Item)
    item_serializer: Type[serializers.Serializer] = attr.ib(
        default=serializers.ItemSerializer
    )
    collection_serializer: Type[serializers.Serializer] = attr.ib(
        default=serializers.CollectionSerializer
    )

    def create_item(self, model: stac_types.Item, **kwargs) -> stac_types.Item:
        """Create item."""
        base_url = str(kwargs["request"].base_url)
        data = self.item_serializer.stac_to_db(model)
        with self.session.writer.context_session() as session:
            session.add(data)
            return self.item_serializer.db_to_stac(data, base_url)

    def create_collection(
        self, model: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Create collection."""
        base_url = str(kwargs["request"].base_url)
        data = self.collection_serializer.stac_to_db(model)
        with self.session.writer.context_session() as session:
            session.add(data)
            return self.collection_serializer.db_to_stac(data, base_url=base_url)

    def update_item(self, model: stac_types.Item, **kwargs) -> stac_types.Item:
        """Update item."""
        base_url = str(kwargs["request"].base_url)
        with self.session.reader.context_session() as session:
            query = session.query(self.item_table).filter(
                self.item_table.id == model["id"]
            )
            query = query.filter(self.item_table.collection_id == model["collection"])
            if not query.scalar():
                raise NotFoundError(
                    f"Item {model['id']} in collection {model['collection']}"
                )
            # SQLAlchemy orm updates don't seem to like geoalchemy types
            db_model = self.item_serializer.stac_to_db(model)
            query.update(self.item_serializer.row_to_dict(db_model))
            stac_item = self.item_serializer.db_to_stac(db_model, base_url)

            return stac_item

    def update_collection(
        self, model: stac_types.Collection, **kwargs
    ) -> stac_types.Collection:
        """Update collection."""
        base_url = str(kwargs["request"].base_url)
        with self.session.reader.context_session() as session:
            query = session.query(self.collection_table).filter(
                self.collection_table.id == model["id"]
            )
            if not query.scalar():
                raise NotFoundError(f"Item {model['id']} not found")

            # SQLAlchemy orm updates don't seem to like geoalchemy types
            db_model = self.collection_serializer.stac_to_db(model)
            query.update(self.collection_serializer.row_to_dict(db_model))

            return self.collection_serializer.db_to_stac(db_model, base_url)

    def delete_item(
        self, item_id: str, collection_id: str, **kwargs
    ) -> stac_types.Item:
        """Delete item."""
        base_url = str(kwargs["request"].base_url)
        with self.session.writer.context_session() as session:
            query = session.query(self.item_table).filter(
                self.item_table.collection_id == collection_id
            )
            query = query.filter(self.item_table.id == item_id)
            data = query.first()
            if not data:
                raise NotFoundError(
                    f"Item {item_id} not found in collection {collection_id}"
                )
            query.delete()
            return self.item_serializer.db_to_stac(data, base_url=base_url)

    def delete_collection(self, collection_id: str, **kwargs) -> stac_types.Collection:
        """Delete collection."""
        base_url = str(kwargs["request"].base_url)
        with self.session.writer.context_session() as session:
            query = session.query(self.collection_table).filter(
                self.collection_table.id == collection_id
            )
            data = query.first()
            if not data:
                raise NotFoundError(f"Collection {collection_id} not found")
            query.delete()
            return self.collection_serializer.db_to_stac(data, base_url=base_url)


@attr.s
class BulkTransactionsClient(BaseBulkTransactionsClient):
    """Postgres bulk transactions."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    debug: bool = attr.ib(default=False)
    item_table: Type[database.Item] = attr.ib(default=database.Item)
    item_serializer: Type[serializers.Serializer] = attr.ib(
        default=serializers.ItemSerializer
    )

    def __attrs_post_init__(self):
        """Create sqlalchemy engine."""
        self.engine = self.session.writer.cached_engine

    def _preprocess_item(self, item: stac_types.Item) -> stac_types.Item:
        """Preprocess items to match data model.

        # TODO: dedup with GetterDict logic (ref #58)
        """
        db_model = self.item_serializer.stac_to_db(item)
        return self.item_serializer.row_to_dict(db_model)

    def bulk_item_insert(
        self, items: Items, chunk_size: Optional[int] = None, **kwargs
    ) -> str:
        """Bulk item insertion using sqlalchemy core.

        https://docs.sqlalchemy.org/en/13/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow
        """
        # Use items.items because schemas.Items is a model with an items key
        processed_items = [self._preprocess_item(item) for item in items]
        return_msg = f"Successfully added {len(processed_items)} items."
        if chunk_size:
            for chunk in self._chunks(processed_items, chunk_size):
                self.engine.execute(self.item_table.__table__.insert(), chunk)
            return return_msg

        self.engine.execute(self.item_table.__table__.insert(), processed_items)
        return return_msg
