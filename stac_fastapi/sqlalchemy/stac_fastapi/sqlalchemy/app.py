"""FastAPI application."""
from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_request_model
from stac_fastapi.extensions.core import (
    FieldsExtension,
    SortExtension,
    TokenPaginationExtension,
    TransactionExtension,
)
from stac_fastapi.extensions.third_party import BulkTransactionExtension
from stac_fastapi.sqlalchemy.config import SqlalchemySettings
from stac_fastapi.sqlalchemy.core import CoreCrudClient
from stac_fastapi.sqlalchemy.extensions import QueryExtension
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.transactions import (
    BulkTransactionsClient,
    TransactionsClient,
)
from stac_fastapi.types.search import BaseSearchGetRequest, BaseSearchPostRequest

settings = SqlalchemySettings()
session = Session.create_from_settings(settings)
extensions = [
    TransactionExtension(client=TransactionsClient(session=session), settings=settings),
    BulkTransactionExtension(client=BulkTransactionsClient(session=session)),
    FieldsExtension(),
    QueryExtension(),
    SortExtension(),
    TokenPaginationExtension(),
]

GET_REQUEST_MODEL = create_request_model(
    "SearchGetRequest",
    base_model=BaseSearchGetRequest,
    extensions=extensions,
    request_type="GET",
)

POST_REQUEST_MODEL = create_request_model(
    "SearchPostRequest",
    base_model=BaseSearchPostRequest,
    extensions=extensions,
    request_type="POST",
)

api = StacApi(
    settings=settings,
    extensions=extensions,
    client=CoreCrudClient(
        session=session, extensions=extensions, post_request_model=POST_REQUEST_MODEL
    ),
    search_get_request_model=GET_REQUEST_MODEL,
    search_post_request_model=POST_REQUEST_MODEL,
)
app = api.app


def run():
    """Run app from command line using uvicorn if available."""
    try:
        import uvicorn

        uvicorn.run(
            "stac_fastapi.sqlalchemy.app:app",
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
