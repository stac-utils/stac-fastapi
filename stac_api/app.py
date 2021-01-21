"""FastAPI application."""
from stac_api.api.app import StacApi
from stac_api.api.extensions import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TilesExtension,
    TransactionExtension,
)
from stac_api.clients.postgres.core import CoreCrudClient, Session
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.config import ApiSettings

settings = ApiSettings()
api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(client=TransactionsClient()),
        FieldsExtension(),
        QueryExtension(),
        SortExtension(),
        TilesExtension(),
    ],
    client=CoreCrudClient(
        session=Session(
            settings.reader_connection_string, settings.writer_connection_string
        ),
        pagination_client=PaginationTokenClient(),
    ),
)
app = api.app
