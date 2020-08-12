from base64 import urlsafe_b64encode
from dataclasses import dataclass
import os

from starlette.requests import Request

from .base_crud import BaseCrudClient
from ..models import database

from ..errors import DatabaseError


@dataclass
class PaginationTokenClient(BaseCrudClient):
    def insert(self, keyset: str, tries: int = 0) -> str:
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


def pagination_token_client_factory(request: Request) -> PaginationTokenClient:
    return PaginationTokenClient(
        reader_session=request.app.state.DB_READER,
        writer_session=request.app.state.DB_WRITER,
        table=database.PaginationToken,
    )
