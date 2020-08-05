from fastapi import FastAPI, APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import settings
from .resources import mgmt, collection, conformance, item
from .utils import dependencies


app = FastAPI()
app.debug = settings.DEBUG

stac_router = APIRouter()
stac_router.include_router(conformance.router)
stac_router.include_router(collection.router)
stac_router.include_router(item.router)

app.include_router(mgmt.router)
app.include_router(stac_router)

@app.on_event("startup")
async def on_startup():
    """Create database engines and sessions on startup"""
    dependencies.ENGINE_READER = create_engine(settings.SQLALCHEMY_DATABASE_READER)
    dependencies.ENGINE_WRITER = create_engine(settings.SQLALCHEMY_DATABASE_WRITER)
    dependencies.DB_READER = sessionmaker(
        autocommit=False, autoflush=False, bind=dependencies.ENGINE_READER
    )
    dependencies.DB_WRITER = sessionmaker(
        autocommit=False, autoflush=False, bind=dependencies.ENGINE_WRITER
    )


@app.on_event("shutdown")
async def on_shutdown():
    """Dispose of database engines and sessions on app shutdown"""
    dependencies.ENGINE_READER.dispose()
    dependencies.ENGINE_WRITER.dispose()
