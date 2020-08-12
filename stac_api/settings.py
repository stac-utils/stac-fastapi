from starlette.config import Config

config = Config(".env")


ENVIRONMENT = config("ENVIRONMENT", cast=str)
DEBUG = config("DEBUG", cast=bool, default=False)
TESTING = config("TESTING", cast=bool, default=False)


# Database config
POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASS = config("POSTGRES_PASS", cast=str)
POSTGRES_DBNAME = config("POSTGRES_DBNAME", cast=str)
POSTGRES_PORT = config("POSTGRES_PORT", cast=str)
POSTGRES_HOST_READER = config("POSTGRES_HOST_READER", cast=str)
POSTGRES_HOST_WRITER = config("POSTGRES_HOST_WRITER", cast=str)


# Database connection strings
SQLALCHEMY_DATABASE_READER = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST_READER}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"
SQLALCHEMY_DATABASE_WRITER = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST_WRITER}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"


# Fields which are defined by STAC but not included in the database model
FORBIDDEN_FIELDS = {"type", "stac_version"}


# Fields which are item properties but indexed as distinct fields in the database model
INDEXED_FIELDS = {"datetime"}


# Fields which are always included in the response (fields extension)
DEFAULT_INCLUDES = {
    "id",
    "type",
    "geometry",
    "bbox",
    "links",
    "assets",
    "properties.datetime",
    "properties.updated",
    "properties.created",
    "properties.eo:gsd",
    "properties.eo:bands",
    "properties.proj:epsg",
    "properties.naip:quadrant",
    "properties.naip:cell_id",
    "properties.naip:statename",
}
