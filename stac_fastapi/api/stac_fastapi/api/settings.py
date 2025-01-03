import os

KEYCLOAK_BASE_URL = os.getenv("KEYCLOAK_BASE_URL", "default_base_url")
REALM = os.getenv("REALM", "default_realm")
CLIENT_ID = os.getenv("CLIENT_ID", "default_client_id")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "default_client_secret")
CACHE_CONTROL_HEADERS = os.getenv("CACHE_CONTROL_HEADERS", "max-age=300, stale-while-revalidate=300")
CACHE_CONTROL_CATALOGS = os.getenv("CACHE_CONTROL_CATALOGS", "supported-datasets")
CACHE_CONTROL_CATALOGS_LIST = CACHE_CONTROL_CATALOGS.split(',')