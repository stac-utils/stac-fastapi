"""FastAPI application."""
from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TransactionExtension,
)
from stac_fastapi.extensions.third_party import BulkTransactionExtension
from stac_fastapi.mongo.config import MongoSettings
from stac_fastapi.mongo.core import CoreCrudClient
from stac_fastapi.mongo.session import Session
from stac_fastapi.mongo.transactions import (
    # BulkTransactionsClient,
    TransactionsClient,
)
from stac_fastapi.mongo.types.search import SQLAlchemySTACSearch

settings = MongoSettings()
session = Session.create_from_settings(settings)
api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(
            client=TransactionsClient(session=session), settings=settings
        ),
        # BulkTransactionExtension(client=BulkTransactionsClient(session=session)),
        FieldsExtension(),
        QueryExtension(),
        SortExtension(),
    ],
    client=CoreCrudClient(session=session),
    search_request_model=SQLAlchemySTACSearch,
)
app = api.app


def run():
    """Run app from command line using uvicorn if available."""
    try:
        import uvicorn

        uvicorn.run(
            "stac_fastapi.mongo.app:app",
            host=settings.app_host,
            port=settings.app_port,
            log_level="info",
            reload=settings.reload,
        )
    except ImportError:
        raise RuntimeError("Uvicorn must be installed in order to use command")


if __name__ == "__main__":
    run()


def create_handler(app):
    """Create a handler to use with AWS Lambda if mangum available."""
    try:
        from mangum import Mangum

        return Mangum(app)
    except ImportError:
        return None


handler = create_handler(app)
