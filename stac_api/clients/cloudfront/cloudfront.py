"""cloudfront"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

from botocore.signers import CloudFrontSigner


@dataclass
class Signer:
    """creates cloudfront signed urls"""

    cloudfront_domain: str
    signer: CloudFrontSigner

    def __call__(self, path: str, ttl: Optional[int] = 2628000):
        """
        :param path: path to sign
        :param ttl: expiration (in seconds -- defaults to 1 month)
        """
        url = f"https://{self.cloudfront_domain}{path}"
        expire_date = datetime.utcnow() + timedelta(seconds=ttl)
        signed_url = self.signer.generate_presigned_url(
            url=url, date_less_than=expire_date
        )
        return signed_url
