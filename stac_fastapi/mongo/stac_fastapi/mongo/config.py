"""Mongo API configuration."""
from typing import Set

from stac_fastapi.types.config import ApiSettings

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import pymongo
from motor.motor_tornado import MotorClient
import motor
import yaml

load_dotenv()

class MongoSettings(ApiSettings):
    """Mongo-specific API settings.

    Attributes:
        conn_string: Mongo db connection string.
    """

    conn_str: os.getenv("MONGO_CONN_STRING")

    # Fields which are defined by STAC but not included in the database model
    forbidden_fields: Set[str] = {"type"}

    # Fields which are item properties but indexed as distinct fields in the database model
    indexed_fields: Set[str] = {"datetime"}

    # def load_config() -> dict:
    #     with open('config/config.yml') as yaml_file:
    #         conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    #     return conf

    # CONF = load_config()

    # conn_str = os.getenv("MONGO_CONN_STRING")

    # conn_string = "mongodb://dev:stac@mongo:27017"

    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
    DB = client.stac

    # def close_db_client():
    #     DB_CLIENT.close()

    @property
    def reader_connection_string(self):
        """Create reader psql connection string."""
        return f"{self.conn_str}"

    @property
    def writer_connection_string(self):
        """Create writer psql connection string."""
        return f"{self.conn_str}"
