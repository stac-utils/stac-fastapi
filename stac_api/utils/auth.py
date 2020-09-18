from typing import Dict, Optional
from pydantic import HttpUrl
import httpx
import json
from jose.utils import base64url_decode
from jose import jwt

from stac_api.utils.config import jwk_url, client_id


async def get_key_dict(url: HttpUrl = jwk_url) -> Dict:
    """
    Get JWK keys from AWS Cognito
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response


def get_header(token: str) -> Dict:
    """
    Get the decoded header of the JWT

    The header contains information about how it was encoded
    """
    header_encoded = token.split('.')[0]
    header_decoded = base64url_decode(header_encoded.encode('utf-8'))
    header = json.loads(header_decoded)

    return header


def get_key(header: Dict, key_dict: Dict) -> Dict:
    """
    Find the appropriate JWK key to use to decode the token
    """
    kid = header['kid']
    keys = key_dict['keys']
    for key in keys:
        if key['kid'] == kid:
            return key


def decode_jwt(token: str, key_dict: Dict = None, audience: Optional[str] = client_id) -> Dict:
    """
    Decode a JWT from Cognito

    jwt is a JSON Web Token
    key_dict is a dictionary containing JWK keys from:
    https://cognito-idp.{aws-region}.amazonaws.com/{user-pool-id}/.well-known/jwks.json
    audience is the Cognito client_id
    """
    header = get_header(token)
    key = get_key(header, key_dict)

    payload = jwt.decode(token, key, algorithms=key['alg'], audience=audience)

    return payload


if __name__ == '__main__':
    pass
