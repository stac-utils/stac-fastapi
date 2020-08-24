"""Collection crud client."""

import logging
from dataclasses import dataclass
from typing import List, Optional, Type

from fastapi import Depends

from sqlakeyset import get_page
from stac_api import config, errors
from stac_api.clients.base import BaseCollectionClient
from stac_api.clients.postgres.base import PostgresClient
from stac_api.clients.postgres.tokens import (
    PaginationTokenClient,
    pagination_token_client_factory,
)
from stac_api.config import ApiExtensions
from stac_api.models import database, schemas
from stac_pydantic import ItemCollection
from stac_pydantic.api.extensions.paging import PaginationLink
from stac_pydantic.shared import Relations

logger = logging.getLogger(__name__)


@dataclass
class CollectionCrudClient(PostgresClient, BaseCollectionClient):
    """Collection specific CRUD operations"""

    table: Type[database.Collection] = database.Collection
    pagination_client: Optional[PaginationTokenClient] = None

    def all_collections(self, **kwargs) -> List[schemas.Collection]:
        """Read all collections from the database"""
        try:
            collections = self.reader_session.query(self.table).all()
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting item collection"
            )

        response = []
        for collection in collections:
            collection.base_url = str(kwargs["request"].base_url)
            response.append(schemas.Collection.from_orm(collection))
        return response

    def get_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Get collection by id"""
        collection = self.lookup_id(id).first()
        collection.base_url = str(kwargs["request"].base_url)
        return schemas.Collection.from_orm(collection)

    def item_collection(
        self, id: str, limit: int = 10, token: str = None, **kwargs
    ) -> ItemCollection:
        """Read an item collection from the database"""
        try:
            collection_children = (
                self.lookup_id(id)
                .first()
                .children.order_by(database.Item.datetime.desc(), database.Item.id)
            )
            count = None
            if config.settings.api_extension_is_enabled(config.ApiExtensions.context):
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

        links = []
        if page.next:
            links.append(
                PaginationLink(
                    rel=Relations.next,
                    type="application/geo+json",
                    href=f"{kwargs['request'].base_url}collections/{id}/items?token={page.next}&limit={limit}",
                    method="GET",
                )
            )
        if page.previous:
            links.append(
                PaginationLink(
                    rel=Relations.previous,
                    type="application/geo+json",
                    href=f"{kwargs['request'].base_url}collections/{id}/items?token={page.previous}&limit={limit}",
                    method="GET",
                )
            )

        response_features = []
        for item in page:
            item.base_url = str(kwargs["request"].base_url)
            response_features.append(schemas.Item.from_orm(item))

        context_obj = None
        if config.settings.api_extension_is_enabled(ApiExtensions.context):
            context_obj = {"returned": len(page), "limit": limit, "matched": count}

        return ItemCollection(
            type="FeatureCollection",
            context=context_obj,
            features=response_features,
            links=links,
        )


def collection_crud_client_factory(
    pagination_client: PaginationTokenClient = Depends(pagination_token_client_factory),
) -> CollectionCrudClient:
    """FastAPI dependency"""
    return CollectionCrudClient(
        table=database.Collection, pagination_client=pagination_client,
    )
