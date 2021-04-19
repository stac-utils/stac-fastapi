"""FastAPI application using PGStac."""
from stac_fastapi.api.app import StacApi
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.pgstac.config import Settings
from stac_fastapi.pgstac.db import connect_to_db, close_db_connection
from stac_fastapi.pgstac.core import CoreCrudClient
from stac_fastapi.pgstac.transactions import TransactionsClient
from stac_fastapi.pgstac.types.search import PgstacSearch
import uvicorn

from stac_fastapi.extensions.core import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TransactionExtension,
)

settings = Settings()

api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(client=TransactionsClient, endpoint_factory=create_async_endpoint),
        QueryExtension(),
        SortExtension(),
        FieldsExtension()
    ],
    client=CoreCrudClient(),
    endpoint_factory=create_async_endpoint,
    search_request_model=PgstacSearch,
)
app = api.app

@app.on_event("startup")
async def startup_event():
    """ Connect to database on startup """
    await connect_to_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    await close_db_connection(app)

if __name__ == "__main__":
    uvicorn.run("stac_fastapi.pgstac.app:app", host="0.0.0.0", port=8000, log_level="info", reload=True)