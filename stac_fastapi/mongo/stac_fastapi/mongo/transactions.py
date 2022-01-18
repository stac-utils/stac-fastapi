"""transactions extension client."""

import logging
from datetime import datetime

import attr
from stac_pydantic.shared import DATETIME_RFC339

from stac_fastapi.extensions.third_party.bulk_transactions import (
    BaseBulkTransactionsClient,
    Items,
)
from stac_fastapi.mongo.config import MongoSettings
from stac_fastapi.mongo.serializers import ItemSerializer
from stac_fastapi.mongo.session import Session
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.core import BaseTransactionsClient
from stac_fastapi.types.errors import ConflictError, ForeignKeyError, NotFoundError
from stac_fastapi.types.links import CollectionLinks, ItemLinks

logger = logging.getLogger(__name__)


@attr.s
class TransactionsClient(BaseTransactionsClient):
    """Transactions extension specific CRUD operations."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    settings = MongoSettings()
    client = settings.create_client

    def _check_collection_foreign_key(self, model: stac_types.Item, session):
        if not self.client.stac.stac_collection.count_documents(
            {"id": model["collection"]}, limit=1, session=session
        ):
            raise ForeignKeyError(
                f"Collection {model['collection']} does not exist"
            )

    def _check_collection_conflict(self, model, session):
        if self.client.stac.stac_collection.count_documents(
            {"id": model["id"]}, limit=1, session=session
        ):
            raise ConflictError(f"Collection {model['id']} already exists")

    def _check_collection_not_found(self, collection_id, session):
        if (
            self.client.stac.stac_collection.count_documents(
                {"id": collection_id}, session=session
            )
            == 0
        ):
            raise NotFoundError(f"Collection {collection_id} not found")

    def _check_item_conflict(self, model: stac_types.Item, session):
        if self.client.stac.stac_item.count_documents(
            {"id": model["id"], "collection": model["collection"]},
            limit=1,
            session=session,
        ):
            raise ConflictError(
                f"Item {model['id']} in collection {model['collection']} already exists"
            )

    def _check_item_not_found(self, item_id, collection_id, session):
        if (
            self.client.stac.stac_item.count_documents(
                {"id": item_id, "collection": collection_id},
                session=session,
            )
            == 0
        ):
            raise NotFoundError(
                f"Item {item_id} in collection {collection_id} not found"
            )


    def create_item(self, model: stac_types.Item, **kwargs):
        """Create item."""
        base_url = str(kwargs["request"].base_url)
        item_links = ItemLinks(
            collection_id=model["collection"], item_id=model["id"], base_url=base_url
        ).create_links()
        model["links"] = item_links
        with self.client.start_session(causal_consistency=True) as session:
            self._check_collection_foreign_key(model, session=session)
            self._check_item_conflict(model, session=session)
            now = datetime.utcnow().strftime(DATETIME_RFC339)
            if "created" not in model["properties"]:
                model["properties"]["created"] = str(now)
            self.client.stac.stac_item.insert_one(model, session=session)
            return ItemSerializer.db_to_stac(model, base_url)

    def create_collection(self, model: stac_types.Collection, **kwargs):
        """Create collection."""
        base_url = str(kwargs["request"].base_url)
        collection_links = CollectionLinks(
            collection_id=model["id"], base_url=base_url
        ).create_links()
        model["links"] = collection_links

        with self.client.start_session(causal_consistency=True) as session:
            self._check_collection_conflict(model, session=session)
            self.client.stac.stac_collection.insert_one(model, session=session)

    def update_item(self, model: stac_types.Item, **kwargs):
        """Update item."""
        base_url = str(kwargs["request"].base_url)

        with self.client.start_session(causal_consistency=True) as session:
            self._check_collection_foreign_key(model, session=session)
            self._check_item_not_found(model["id"], model["collection"], session)
            self.delete_item(
                item_id=model["id"], collection_id=model["collection"], session=session
            )
        now = datetime.utcnow().strftime(DATETIME_RFC339)
        model["properties"]["updated"] = str(now)
        self.create_item(model, **kwargs)
        return ItemSerializer.db_to_stac(model, base_url)

    def update_collection(self, model: stac_types.Collection, **kwargs):
        """Update collection."""
        with self.client.start_session(causal_consistency=True) as session:
            self._check_collection_not_found(model["id"], session=session)
        self.delete_collection(model["id"])
        self.create_collection(model, **kwargs)

    def delete_item(self, item_id: str, collection_id: str, **kwargs):
        """Delete item."""
        with self.client.start_session(causal_consistency=True) as session:
            self._check_item_not_found(item_id, collection_id, session)
            self.client.stac.stac_item.delete_one(
                {"id": item_id, "collection": collection_id}, session=session
            )

    def delete_collection(self, collection_id: str, **kwargs):
        """Delete collection."""
        with self.client.start_session(causal_consistency=True) as session:
            self._check_collection_not_found(collection_id, session=session)
            self.client.stac.stac_collection.delete_one(
                {"id": collection_id}, session=session
            )


@attr.s
class BulkTransactionsClient(BaseBulkTransactionsClient):
    """Postgres bulk transactions."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))

    def __attrs_post_init__(self):
        """Create mongo engine."""
        settings = MongoSettings()
        self.client = settings.create_client

    def _check_collection_exists(self, model: stac_types.Item, session):
        if not self.client.stac.stac_collection.count_documents(
            {"id": model["collection"]}, limit=1, session=session
        ):
            raise ForeignKeyError(
                f"Collection {model['collection']} does not exist"
            )

    def _preprocess_item(self, model: stac_types.Item, base_url) -> stac_types.Item:
        """Preprocess items to match data model."""
        item_links = ItemLinks(
            collection_id=model["collection"], item_id=model["id"], base_url=base_url
        ).create_links()
        model["links"] = item_links

        with self.client.start_session(causal_consistency=True) as session:
            self._check_collection_exists(model, session=session)

            if self.client.stac.stac_item.count_documents(
                {"id": model["id"], "collection": model["collection"]},
                limit=1,
                session=session,
            ):
                raise ConflictError(
                    f"Item {model['id']} in collection {model['collection']} already exists"
                )
            else:
                now = datetime.utcnow().strftime(DATETIME_RFC339)
                if "created" not in model["properties"]:
                    model["properties"]["created"] = str(now)
                return model

    def bulk_item_insert(self, items: Items, **kwargs) -> str:
        """Bulk item insertion using mongodb and pymongo."""
        try:
            base_url = str(kwargs["request"].base_url)
        except Exception:
            base_url = ""
        processed_items = [self._preprocess_item(item, base_url) for item in items]
        return_msg = f"Successfully added {len(processed_items)} items."
        with self.client.start_session(causal_consistency=True) as session:
            self.client.stac.stac_item.insert_many(processed_items, session=session)
            return return_msg
