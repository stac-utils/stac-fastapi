"""FastAPI application."""
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request

from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.config import ApiSettings, inject_settings
from stac_api.create_app import create_transactions_router
from stac_api.errors import DEFAULT_STATUS_CODES, add_exception_handlers
from stac_api.resources import collection, conformance, item, mgmt
from stac_api.utils.dependencies import READER, WRITER

app = FastAPI()
settings = ApiSettings()
inject_settings(settings)

app.debug = settings.debug
app.include_router(mgmt.router)
app.include_router(conformance.router)
app.include_router(collection.router)
app.include_router(item.router)

transaction_client = TransactionsClient()
app.include_router(create_transactions_router(transaction_client))

add_exception_handlers(app, DEFAULT_STATUS_CODES)


@app.on_event("startup")
async def on_startup():
    """Create database engines and sessions on startup"""
    app.state.ENGINE_READER = create_engine(settings.reader_connection_string)
    app.state.ENGINE_WRITER = create_engine(settings.writer_connection_string)
    app.state.DB_READER = sessionmaker(
        autocommit=False, autoflush=False, bind=app.state.ENGINE_READER
    )
    app.state.DB_WRITER = sessionmaker(
        autocommit=False, autoflush=False, bind=app.state.ENGINE_WRITER
    )


@app.on_event("shutdown")
async def on_shutdown():
    """Dispose of database engines and sessions on app shutdown"""
    app.state.ENGINE_READER.dispose()
    app.state.ENGINE_WRITER.dispose()


@app.middleware("http")
async def create_db_connection(request: Request, call_next):
    """Create a new database connection for each request"""
    reader = request.app.state.DB_READER()
    writer = request.app.state.DB_WRITER()
    READER.set(reader)
    WRITER.set(writer)
    resp = await call_next(request)
    reader.close()
    writer.close()
    return resp
