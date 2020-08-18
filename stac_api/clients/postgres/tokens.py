"""Pagination token client."""

import os
from base64 import urlsafe_b64encode
from dataclasses import dataclass

from fastapi import Depends
from sqlalchemy.orm import Session

from stac_api.clients.postgres.base import PostgresClient
from stac_api.errors import DatabaseError
from stac_api.models import database
from stac_api.utils.dependencies import database_reader_factory, database_writer_factory


@dataclass
class PaginationTokenClient(PostgresClient):
    """Pagination token specific CRUD operations"""

    def insert(self, keyset: str, tries: int = 0) -> str:  # type:ignore
        """Insert a keyset into the database"""
        # uid has collision chance of 1e-7 percent
        uid = urlsafe_b64encode(os.urandom(6)).decode()
        try:
            token = database.PaginationToken(id=uid, keyset=keyset)
            self.writer_session.add(token)
            self.commit()
            return token.id
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


def pagination_token_client_factory(
    reader_session: Session = Depends(database_reader_factory),
    writer_session: Session = Depends(database_writer_factory),
) -> PaginationTokenClient:
    """FastAPI dependency"""
    return PaginationTokenClient(
        reader_session=reader_session,
        writer_session=writer_session,
        table=database.PaginationToken,
    )
