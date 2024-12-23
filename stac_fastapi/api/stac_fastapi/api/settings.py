import os

KEYCLOAK_BASE_URL = os.getenv("KEYCLOAK_BASE_URL", "default_base_url")
REALM = os.getenv("REALM", "default_realm")
CLIENT_ID = os.getenv("CLIENT_ID", "default_client_id")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "default_client_secret")