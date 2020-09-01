"""Pagination token client."""

import os
from base64 import urlsafe_b64encode
from dataclasses import dataclass
from typing import Type

from stac_api.clients.postgres.base import PostgresClient
from stac_api.errors import DatabaseError
from stac_api.models import database


@dataclass
class PaginationTokenClient(PostgresClient):
    """Pagination token specific CRUD operations"""

    table: Type[database.PaginationToken] = database.PaginationToken

    def insert(self, keyset: str, tries: int = 0) -> str:  # type:ignore
        """Insert a keyset into the database"""
        # uid has collision chance of 1e-7 percent
        uid = urlsafe_b64encode(os.urandom(6)).decode()
        try:
            token = database.PaginationToken(id=uid, keyset=keyset)
            self.writer_session.add(token)
            self.commit()
            return uid
        except DatabaseError:
            # Try again if uid already exists in the database
            # TODO: Explicitely check for ConflictError (if insert fails for other reasons it should be raised)
            self.insert(keyset, tries=tries + 1)
            if tries > 5:
                raise

    def get(self, token_id: str) -> str:
        """Retrieve a keyset from the database"""
        row = self.lookup_id(token_id).first()
        return row.keyset


def pagination_token_client_factory() -> PaginationTokenClient:
    """FastAPI dependency"""
    return PaginationTokenClient()
