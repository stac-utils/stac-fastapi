"""Collection crud client."""

import logging
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Type

from fastapi import Depends

from sqlakeyset import Page, get_page
from stac_api import errors
from stac_api.clients.base import BaseCollectionClient
from stac_api.clients.postgres.base import PostgresClient
from stac_api.clients.postgres.tokens import (
    PaginationTokenClient,
    pagination_token_client_factory,
)
from stac_api.models import database

logger = logging.getLogger(__name__)


@dataclass
class CollectionCrudClient(PostgresClient, BaseCollectionClient):
    """Collection specific CRUD operations"""

    table: Type[database.Collection] = database.Collection
    pagination_client: Optional[PaginationTokenClient] = None

    def all_collections(self) -> List[database.Collection]:
        """Read all collections from the database"""
        try:
            items = self.reader_session.query(self.table).all()
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting item collection"
            )
        return items

    def get_collection(self, id: str) -> Any:
        """Get collection by id"""
        return self.lookup_id(id).first()

    def item_collection(
        self, id: str, limit: int = 10, token: str = None
    ) -> Tuple[Page, int]:
        """Read an item collection from the database"""
        try:
            collection_children = (
                self.lookup_id(id)
                .first()
                .children.order_by(database.Item.datetime.desc(), database.Item.id)
            )
            count = collection_children.count()
            token = self.pagination_client.get(token) if token else token
            page = get_page(collection_children, per_page=limit, page=(token or False))
            # Create dynamic attributes for each page
            page.next = (
                self.pagination_client.insert(keyset=page.paging.bookmark_next)
                if page.paging.has_next
                else None
            )
            page.previous = (
                self.pagination_client.insert(keyset=page.paging.bookmark_previous)
                if page.paging.has_previous
                else None
            )
        except errors.NotFoundError:
            raise
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting collection children"
            )
        return page, count


def collection_crud_client_factory(
    pagination_client: PaginationTokenClient = Depends(pagination_token_client_factory),
) -> CollectionCrudClient:
    """FastAPI dependency"""
    return CollectionCrudClient(
        table=database.Collection, pagination_client=pagination_client,
    )
