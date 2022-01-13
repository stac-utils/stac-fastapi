"""mongodb config."""
import os

from pymongo import MongoClient, errors

DOMAIN = os.getenv("MONGO_HOST")
PORT = os.getenv("MONGO_PORT")


def MongoSettings():
    """Connect to mongodb."""
    try:
        client = MongoClient(
            host=[str(DOMAIN) + ":" + str(PORT)],
            serverSelectionTimeoutMS=3000,
            username=os.getenv("MONGO_USER"),
            password=os.getenv("MONGO_PASS"),
        )

        return client

    except errors.ServerSelectionTimeoutError as err:
        client = None
        print("pymongo ERROR:", err)

        return None
