import os
from dotenv import load_dotenv


load_dotenv()


account_id = os.environ.get("ACCOUNT_ID")
pool_id = os.environ.get("POOL_ID")
region = os.environ.get("REGION")
identity_pool_id = os.environ.get("IDENTITY_POOL_ID")
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
jwk_url = os.environ.get("JWK_URL")

