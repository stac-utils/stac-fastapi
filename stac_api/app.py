from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import settings
from .errors import add_exception_handlers, DEFAULT_STATUS_CODES
from .resources import mgmt, collection, conformance, item


app = FastAPI()
app.debug = settings.DEBUG
app.include_router(mgmt.router)
app.include_router(conformance.router)
app.include_router(collection.router)
app.include_router(item.router)

add_exception_handlers(app, DEFAULT_STATUS_CODES)


@app.on_event("startup")
async def on_startup():
    """Create database engines and sessions on startup"""
    app.state.ENGINE_READER = create_engine(settings.SQLALCHEMY_DATABASE_READER)
    app.state.ENGINE_WRITER = create_engine(settings.SQLALCHEMY_DATABASE_WRITER)
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
