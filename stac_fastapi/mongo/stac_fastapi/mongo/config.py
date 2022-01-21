"""API configuration."""
import os
from typing import Set

from pymongo import GEO2D, GEOSPHERE, MongoClient, errors

from stac_fastapi.types.config import ApiSettings

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
        """Create mongo client."""
        try:
            client = MongoClient(
                host=[str(DOMAIN) + ":" + str(PORT)],
                serverSelectionTimeoutMS=3000,
                username=os.getenv("MONGO_USER"),
                password=os.getenv("MONGO_PASS"),
            )

            # create indices - they are only created if they don't already exist
            item_table = client.stac.stac_item
            item_table.create_index([("bbox", GEOSPHERE), ("properties.datetime", 1)])
            item_table.create_index([("geometry", GEOSPHERE)])
            item_table.create_index([("properties.datetime", 1)])
            item_table.create_index([("properties.created", 1)])
            item_table.create_index([("properties.updated", 1)])
            item_table.create_index([("bbox", GEOSPHERE)])
            item_table.create_index([("bbox", GEO2D)])

        except errors.ServerSelectionTimeoutError as err:
            client = None
            print("pymongo ERROR:", err)

        return client
