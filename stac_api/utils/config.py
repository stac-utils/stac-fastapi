import os
from dotenv import load_dotenv

EXTERNAL_CONFIG = "EXTERNAL_{0}"

load_dotenv()


def check_external_config(env_var):
    """
    Check for external confiration options at container level
    """
    return os.environ.get(EXTERNAL_CONFIG.format(env_var), os.environ.get(env_var))
# End check_external_config function

account_id = check_external_config("ACCOUNT_ID")
pool_id = check_external_config("POOL_ID")
region = check_external_config("REGION")
identity_pool_id = check_external_config("IDENTITY_POOL_ID")
client_id = check_external_config("CLIENT_ID")
client_secret = check_external_config("CLIENT_SECRET")
aws_access_key_id = check_external_config("AWS_ACCESS_KEY_ID")
aws_secret_access_key = check_external_config("AWS_SECRET_ACCESS_KEY")
jwk_url = check_external_config("JWK_URL")

