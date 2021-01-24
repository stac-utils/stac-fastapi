"""Pagination token client."""

import logging
import os
from base64 import urlsafe_b64encode
from typing import Type

import attr

from stac_api.clients.postgres.base import PostgresClient
from stac_api.errors import DatabaseError, NotFoundError
from stac_api.models import database

logger = logging.getLogger(__name__)


@attr.s
class PaginationTokenClient(PostgresClient):
    """Pagination token specific CRUD operations"""

    table: Type[database.PaginationToken] = attr.ib(default=database.PaginationToken)

    def insert(self, keyset: str, tries: int = 0) -> str:  # type:ignore
        """Insert a keyset into the database"""
        # uid has collision chance of 1e-7 percent
        uid = urlsafe_b64encode(os.urandom(6)).decode()
        with self.session.writer.context_session() as session:
            try:
                token = database.PaginationToken(id=uid, keyset=keyset)
                session.add(token)
                return uid
            except DatabaseError:
                # Try again if uid already exists in the database
                # TODO: Explicitely check for ConflictError (if insert fails for other reasons it should be raised)
                if tries > 5:
                    raise
                self.insert(keyset, tries=tries + 1)

    def get(self, token_id: str) -> str:
        """Retrieve a keyset from the database"""
        with self.session.reader.context_session() as session:
            try:
                token = (
                    session.query(self.table).filter(self.table.id == token_id).first()
                )
            except Exception as e:
                logger.error(e, exc_info=True)
                raise DatabaseError("Error fetching token from database")

            if not token:
                raise NotFoundError(f"Could not find token {token_id}")

            return token.keyset


def pagination_token_client_factory() -> PaginationTokenClient:
    """FastAPI dependency"""
    return PaginationTokenClient()
