# import the MongoClient class
from pymongo import MongoClient, errors

# global variables for MongoDB host (default port is 27017)
DOMAIN = 'host.docker.internal'
PORT = 27018

def MongoSettings():

    # use a try-except indentation to catch MongoClient() errors
    try:
        # try to instantiate a client instance
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = "dev",
            password = "stac",
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