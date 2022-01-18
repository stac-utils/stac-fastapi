"""API configuration."""
from typing import Set

from stac_fastapi.types.config import ApiSettings
import os

from pymongo import MongoClient, errors

DOMAIN = os.getenv("MONGO_HOST")
PORT = os.getenv("MONGO_PORT")

class MongoSettings(ApiSettings):
    """API settings."""
    
    # Fields which are defined by STAC but not included in the database model
    forbidden_fields: Set[str] = {"type"}

    # Fields which are item properties but indexed as distinct fields in the database model
    indexed_fields: Set[str] = {"datetime"}

    @property
    def create_client(self):
        try:
            client = MongoClient(
                host=[str(DOMAIN) + ":" + str(PORT)],
                serverSelectionTimeoutMS=3000,
                username=os.getenv("MONGO_USER"),
                password=os.getenv("MONGO_PASS"),
            )

        except errors.ServerSelectionTimeoutError as err:
            client = None
            print("pymongo ERROR:", err)

        return client