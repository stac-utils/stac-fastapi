# import the MongoClient class
from pymongo import MongoClient, errors
import os

DOMAIN = os.getenv("MONGO_HOST")
PORT = os.getenv("MONGO_PORT")

def MongoSettings():

    # use a try-except indentation to catch MongoClient() errors
    try:
        # try to instantiate a client instance
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = os.getenv("MONGO_USER"),
            password = os.getenv("MONGO_PASS"),
        )

        # print the version of MongoDB server if connection successful
        print ("server version:", client.server_info()["version"])

        # get the database_names from the MongoClient()
        database_names = client.list_database_names()

        print ("\ndatabases:", database_names)

        return client.stac

    except errors.ServerSelectionTimeoutError as err:
        # set the client and DB name list to 'None' and `[]` if exception
        client = None
        database_names = []

        # catch pymongo.errors.ServerSelectionTimeoutError
        print ("pymongo ERROR:", err)

        return None