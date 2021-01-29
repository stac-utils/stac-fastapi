"""transactions extension client"""

import json
import logging
from typing import Dict, List, Optional, Type

import attr
from sqlalchemy import create_engine

from stac_api.clients.base import BaseTransactionsClient, BulkTransactionsClient
from stac_api.clients.postgres.session import Session
from stac_api.errors import NotFoundError
from stac_api.models import database, schemas

logger = logging.getLogger(__name__)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations"""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    collection_table: Type[database.Collection] = attr.ib(default=database.Collection)
    item_table: Type[database.Item] = attr.ib(default=database.Item)

    def create_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """create item"""
        data = self.item_table.from_schema(model)
        with self.session.writer.context_session() as session:
            session.add(data)
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Item.from_orm(data)

    def create_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """create collection"""
        data = self.collection_table.from_schema(model)
        with self.session.writer.context_session() as session:
            session.add(data)
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Collection.from_orm(data)

    def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """update item"""
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
        """update collection"""
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

    def delete_item(self, id: str, **kwargs) -> schemas.Item:
        """delete item"""
        with self.session.writer.context_session() as session:
            query = session.query(self.item_table).filter(self.item_table.id == id)
            data = query.first()
            if not data:
                raise NotFoundError(f"Item {id} not found")
            query.delete()
            data.base_url = str(kwargs["request"].base_url)
            return schemas.Item.from_orm(data)

    def delete_collection(self, id: str, **kwargs) -> schemas.Collection:
        """delete collection"""
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
class PostgresBulkTransactions(BulkTransactionsClient):
    """postgres bulk transactions"""

    connection_str: str = attr.ib()
    debug: bool = attr.ib(default=False)

    def __attrs_post_init__(self):
        """create sqlalchemy engine"""
        self.engine = create_engine(self.connection_str, echo=self.debug)

    @staticmethod
    def _preprocess_item(item) -> Dict:
        """
        preprocess items to match data model
        # TODO: dedup with GetterDict logic (ref #58)
        """
        item["geometry"] = json.dumps(item["geometry"])
        item["collection_id"] = item.pop("collection")
        item["datetime"] = item["properties"].pop("datetime")
        return item

    def bulk_item_insert(
        self, items: List[Dict], chunk_size: Optional[int] = None
    ) -> None:
        """
        bulk item insertion using sqlalchemy core
        https://docs.sqlalchemy.org/en/13/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow
        """
        items = [self._preprocess_item(item) for item in items]
        if chunk_size:
            for chunk in self._chunks(items, chunk_size):
                self.engine.execute(database.Item.__table__.insert(), chunk)
            return

        self.engine.execute(database.Item.__table__.insert(), items)
        return
