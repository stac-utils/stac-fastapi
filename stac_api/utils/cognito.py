import boto3
from pycognito import Cognito
from jose.utils import base64url_decode
from jose import jwt

from .config import (
    account_id,
    region,
    pool_id,
    identity_pool_id,
    client_id,
    client_secret,
    aws_access_key_id,
    aws_secret_access_key,
)
from .auth import decode_jwt, get_key_dict


async def get_tokens(username: str, password: str):
    # Get keys from AWS async
    key_dict_future = get_key_dict()

    # Meanwhile, authenticate with User Pool
    access_kwargs = {
        'username':username,
        'access_key':aws_access_key_id,
        'secret_key': aws_secret_access_key
        }
    if client_secret:
        access_kwargs['client_secret'] = client_secret

    user = Cognito(
        pool_id,
        client_id,
        **access_kwargs
    )
    user.authenticate(password=password)

    # Await key response
    key_dict_response = await key_dict_future
    key_dict = key_dict_response.json()

    # Extract tokens and metadata
    groups = user.get_groups()
    region = user.user_pool_region
    id_token = user.id_token
    access_token = user.access_token
    refresh_token = user.refresh_token
    logins = {f"cognito-idp.{region}.amazonaws.com/{pool_id}": id_token}

    # Decode tokens
    id = decode_jwt(id_token, key_dict, client_id)
    access = decode_jwt(access_token, key_dict, client_id)

    # Fetch credentials from Identity Pool
    credentials = get_credentials(logins)

    return {
        "id": id,
        "access": access,
        "id_token": id_token,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "credentials": credentials,
    }


def get_credentials(logins):
    # Get identity_id from Identity Pool
    client = boto3.client(
        "cognito-identity",
        region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    response = client.get_id(
        AccountId=account_id, IdentityPoolId=identity_pool_id, Logins=logins
    )

    identity_id = response["IdentityId"]

    # Get AWS credentials from Identity Pool
    credential_response = client.get_credentials_for_identity(
        IdentityId=identity_id, Logins=logins
    )

    access_key_id = credential_response["Credentials"]["AccessKeyId"]
    secret_key = credential_response["Credentials"]["SecretKey"]
    session_token = credential_response["Credentials"]["SessionToken"]
    # breakpoint()
    return {
        "identity_id": identity_id,
        "access_key_id": access_key_id,
        "secret_key": secret_key,
        "session_token": session_token,
    }
