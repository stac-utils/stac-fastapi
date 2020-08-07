from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import settings
from .resources import mgmt, collection, conformance, item


app = FastAPI()
app.debug = settings.DEBUG

stac_router = APIRouter()
stac_router.include_router(conformance.router)
stac_router.include_router(collection.router)
stac_router.include_router(item.router)

app.include_router(mgmt.router)
app.include_router(stac_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers="*",
    allow_origins="*"
)

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
