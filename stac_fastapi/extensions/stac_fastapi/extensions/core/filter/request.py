"""Filter extension request models."""

from typing import Any, Dict, Literal, Optional

import attr
from fastapi import Query
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest

FilterLang = Literal["cql2-json", "cql2-text"]


@attr.s
class FilterExtensionGetRequest(APIRequest):
    """Filter extension GET request model."""

    filter_expr: Annotated[
        Optional[str],
        Query(
            alias="filter",
            description="""A CQL2 filter expression for filtering items.\n
Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
Remember to URL encode the CQL2-JSON if using GET""",
            openapi_examples={
                "user-provided": {"value": None},
                "landsat8-item": {
                    "value": "id='LC08_L1TP_060247_20180905_20180912_01_T1_L1TP' AND collection='landsat8_l1tp'"  # noqa: E501
                },
            },
        ),
    ] = attr.ib(default=None)
    filter_crs: Annotated[
        Optional[str],
        Query(
            alias="filter-crs",
            description="The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`",  # noqa: E501
        ),
    ] = attr.ib(default=None)
    filter_lang: Annotated[
        Optional[FilterLang],
        Query(
            alias="filter-lang",
            description="The CQL filter encoding that the 'filter' value uses.",
        ),
    ] = attr.ib(default="cql2-text")


class FilterExtensionPostRequest(BaseModel):
    """Filter extension POST request model."""

    filter_expr: Optional[Dict[str, Any]] = Field(
        None,
        alias="filter",
        description="A CQL filter expression for filtering items.",
        json_schema_extra={
            "examples": [
                # user-provided
                None,
                # landsat8-item
                {
                    "op": "and",
                    "args": [
                        {
                            "op": "=",
                            "args": [
                                {"property": "id"},
                                "LC08_L1TP_060247_20180905_20180912_01_T1_L1TP",
                            ],
                        },
                        {
                            "op": "=",
                            "args": [{"property": "collection"}, "landsat8_l1tp"],
                        },
                    ],
                },
            ],
        },
    )
    filter_crs: Optional[str] = Field(
        None,
        alias="filter-crs",
        description="The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`",  # noqa: E501
    )
    filter_lang: Optional[Literal["cql2-json"]] = Field(
        "cql2-json",
        alias="filter-lang",
        description="The CQL filter encoding that the 'filter' value uses.",
    )
