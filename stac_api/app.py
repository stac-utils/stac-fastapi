"""FastAPI application."""
from stac_api.api.app import StacApi
from stac_api.api.extensions import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TilesExtension,
    TransactionExtension,
)
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.config import ApiSettings

api = StacApi(
    settings=ApiSettings(),
    extensions=[
        TransactionExtension(client=TransactionsClient()),
        FieldsExtension(),
        QueryExtension(),
        SortExtension(),
        TilesExtension(),
    ],
    client=CoreCrudClient(pagination_client=PaginationTokenClient()),
)
app = api.app
