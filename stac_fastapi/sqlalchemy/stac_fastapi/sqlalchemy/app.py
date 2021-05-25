"""FastAPI application."""
from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TransactionExtension,
)
from stac_fastapi.extensions.third_party import BulkTransactionExtension
from stac_fastapi.sqlalchemy.config import SqlalchemySettings
from stac_fastapi.sqlalchemy.core import CoreCrudClient
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.transactions import (
    BulkTransactionsClient,
    TransactionsClient,
)

from stac_fastapi.sqlalchemy.models import database, schemas
import sqlalchemy as sa


def triple_underscore_to_colon(string: str) -> str:
    return string.replace("___", ":")

# Pydantic model extensions (which define responses and documentation)
class ScientificCitationItem(schemas.Item):
    sci___doi: str = "default_doi"
    sci___citation: str = "default_citation"
    sci___publications: str = "publication1, publication2, publication3"

    class Config:
        alias_generator = triple_underscore_to_colon

class ScientificCitationCollection(schemas.Collection):
    sci___doi: str = "default_doi"
    sci___citation: str = "default_citation"
    sci___publications: str = "publication1, publication2, publication3"

    class Config:
        alias_generator = triple_underscore_to_colon

"""SqlAlchemy model extensions (which define database interactions)
    These classes are currently not used, as they result in errors without
    modifications to the database and joplin ingest; provided here as
    demonstration of a possible customization strategy for this backend
"""
class ScientificCitationItemDB(database.Item):
    sci_doi = sa.Column(sa.VARCHAR(300))
    sci_citation = sa.Column(sa.VARCHAR(300))
    sci_publications = sa.Column(sa.VARCHAR(300))

class ScientificCitationCollectionDB(database.Collection):
    sci_doi = sa.Column(sa.VARCHAR(300))
    sci_citation = sa.Column(sa.VARCHAR(300))
    sci_publications = sa.Column(sa.VARCHAR(300))

custom_models = {
    "pydantic": {
        "item": ScientificCitationItem,
        "collection": ScientificCitationCollection
    },
    "sqlalchemy": {
        "item": ScientificCitationItemDB,
        "collection": ScientificCitationCollectionDB
    }
}

settings = SqlalchemySettings(custom_models=custom_models)
session = Session.create_from_settings(settings)
api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(client=TransactionsClient(session=session)),
        BulkTransactionExtension(client=BulkTransactionsClient(session=session)),
        FieldsExtension(),
        QueryExtension(),
        SortExtension(),
    ],
    client=CoreCrudClient(session=session)
)
app = api.app
