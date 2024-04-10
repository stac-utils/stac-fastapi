"""Request model for the Free-text extension."""

from typing import Optional

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class FreeTextExtensionGetRequest(APIRequest):
    """Free-text Extension GET request model."""

    q: Optional[str] = attr.ib(default=None)


class FreeTextExtensionPostRequest(BaseModel):
    """Free-text Extension POST request model."""

    q: Optional[str] = attr.ib(default=None)
