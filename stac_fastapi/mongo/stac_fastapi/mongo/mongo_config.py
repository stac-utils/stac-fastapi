"""Connect to mongodb."""
import os

from pymongo import MongoClient, errors

DOMAIN = os.getenv("MONGO_HOST")
PORT = os.getenv("MONGO_PORT")


def MongoSettings():
    """Connect to mongodb."""
    try:
        client = MongoClient(
            host=[str(DOMAIN) + ":" + str(PORT)],
            serverSelectionTimeoutMS=3000,  # 3 second timeout
            username=os.getenv("MONGO_USER"),
            password=os.getenv("MONGO_PASS"),
        )

        print("server version:", client.server_info()["version"])
        database_names = client.list_database_names()
        print("\ndatabases:", database_names)

        return client.stac

    except errors.ServerSelectionTimeoutError as err:
        client = None
        database_names = []

        # catch pymongo.errors.ServerSelectionTimeoutError
        print("pymongo ERROR:", err)

        return None
