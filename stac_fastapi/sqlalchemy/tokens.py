"""Pagination token client."""
import abc
import logging
import os
from base64 import urlsafe_b64encode
from typing import Type

import attr
from sqlalchemy.orm import Session as SqlSession

from stac_fastapi.sqlalchemy.models import database
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.types.errors import DatabaseError

logger = logging.getLogger(__name__)


@attr.s
class PaginationTokenClient(abc.ABC):
    """Pagination token specific CRUD operations."""

    session: Session = attr.ib(default=attr.Factory(Session.create_from_env))
    token_table: Type[database.PaginationToken] = attr.ib(
        default=database.PaginationToken
    )

    @staticmethod
    @abc.abstractmethod
    def _lookup_id(
        id: str, table: Type[database.BaseModel], session: SqlSession
    ) -> Type[database.BaseModel]:
        """Lookup row by id."""
        ...

    def insert_token(self, keyset: str, tries: int = 0) -> str:  # type:ignore
        """Insert a keyset into the database."""
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
                self.insert_token(keyset, tries=tries + 1)

    def get_token(self, token_id: str) -> str:
        """Retrieve a keyset from the database."""
        with self.session.reader.context_session() as session:
            token = self._lookup_id(token_id, self.token_table, session)
            return token.keyset
