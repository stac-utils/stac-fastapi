"""FastAPI application."""
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TransactionExtension,
)
from stac_fastapi.extensions.third_party import (
    BulkTransactionExtension
)
from stac_fastapi.postgres.core import CoreCrudClient
from stac_fastapi.postgres.config import PostgresSettings
from stac_fastapi.postgres.session import Session
from stac_fastapi.postgres.transactions import (
    BulkTransactionsClient,
    TransactionsClient,
)

settings = PostgresSettings()
session = Session.create_from_settings(settings)
api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(client=TransactionsClient(session=session)),
        BulkTransactionExtension(client=BulkTransactionsClient(session=session)),
        FieldsExtension(),
        QueryExtension(),
        SortExtension()
    ],
    client=CoreCrudClient(session=session),
)
app = api.app
