"""Request model for the Sort Extension."""

from typing import List, Optional

import attr
from fastapi import Query
from pydantic import BaseModel
from stac_pydantic.api.extensions.sort import SortExtension as PostSortModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest, str2list


@attr.s
class SortExtensionGetRequest(APIRequest):
    """Sortby Parameter for GET requests."""

    sortby: Annotated[Optional[str], Query()] = attr.ib(default=None, converter=str2list)


class SortExtensionPostRequest(BaseModel):
    """Sortby parameter for POST requests."""

    sortby: Optional[List[PostSortModel]] = None
