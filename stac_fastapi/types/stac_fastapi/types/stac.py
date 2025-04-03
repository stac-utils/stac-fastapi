"""STAC types."""

import json
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import ConfigDict, Field
from stac_pydantic.shared import BBox, StacBaseModel
from typing_extensions import TypedDict

NumType = Union[float, int]


class Catalog(TypedDict, total=False):
    """STAC Catalog."""

    type: str
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    title: Optional[str]
    description: str
    links: List[Dict[str, Any]]


class LandingPage(Catalog, total=False):
    """STAC Landing Page."""

    conformsTo: List[str]


class Conformance(TypedDict):
    """STAC Conformance Classes."""

    conformsTo: List[str]


class Collection(Catalog, total=False):
    """STAC Collection."""

    keywords: List[str]
    license: str
    providers: List[Dict[str, Any]]
    extent: Dict[str, Any]
    summaries: Dict[str, Any]
    assets: Dict[str, Any]


class Item(TypedDict, total=False):
    """STAC Item."""

    type: Literal["Feature"]
    stac_version: str
    stac_extensions: Optional[List[str]]
    id: str
    geometry: Dict[str, Any]
    bbox: BBox
    properties: Dict[str, Any]
    links: List[Dict[str, Any]]
    assets: Dict[str, Any]
    collection: str


class ItemCollection(TypedDict, total=False):
    """STAC Item Collection."""

    type: Literal["FeatureCollection"]
    features: List[Item]
    links: List[Dict[str, Any]]
    numberMatched: Optional[int]
    numberReturned: Optional[int]


class Collections(TypedDict, total=False):
    """All collections endpoint.
    https://github.com/radiantearth/stac-api-spec/tree/master/collections
    """

    collections: List[Collection]
    links: List[Dict[str, Any]]
    numberMatched: Optional[int] = None
    numberReturned: Optional[int] = None


class PatchAddReplaceTest(StacBaseModel):
    """Add, Replace or Test Operation."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"op": "add", "path": "/properties/foo", "value": "bar"},
                {"op": "replace", "path": "/properties/foo", "value": "bar"},
                {"op": "test", "path": "/properties/foo", "value": "bar"},
            ]
        }
    )

    path: str
    op: Literal["add", "replace", "test"]
    value: Any

    @property
    def json_value(self) -> str:
        """JSON dump of value field.

        Returns:
            str: JSON-ised value
        """
        return json.dumps(self.value)


class PatchRemove(StacBaseModel):
    """Remove Operation."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "op": "remove",
                    "path": "/properties/foo",
                }
            ]
        }
    )

    path: str
    op: Literal["remove"]


class PatchMoveCopy(StacBaseModel):
    """Move or Copy Operation."""

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "examples": [
                {
                    "op": "copy",
                    "path": "/properties/foo",
                    "from": "/properties/bar",
                },
                {
                    "op": "move",
                    "path": "/properties/foo",
                    "from": "/properties/bar",
                },
            ]
        },
    )

    path: str
    op: Literal["move", "copy"]
    from_: str = Field(alias="from")


PatchOperation = Union[PatchAddReplaceTest, PatchMoveCopy, PatchRemove]


class BasePartial(StacBaseModel):
    """Base Partial Class."""

    @staticmethod
    def merge_to_operations(data: Dict) -> List[PatchOperation]:
        """Convert merge operation to list of RF6902 operations.

        Args:
            data: dictionary to convert.

        Returns:
            List: list of RF6902 operations.
        """
        operations = []

        for key, value in data.copy().items():
            if value is None:
                operations.append(PatchRemove(op="remove", path=key))

            elif isinstance(value, dict):
                nested_operations = BasePartial.merge_to_operations(value)

                for nested_operation in nested_operations:
                    nested_operation.path = f"{key}/{nested_operation.path}"
                    operations.append(nested_operation)

            else:
                operations.append(PatchAddReplaceTest(op="add", path=key, value=value))

        return operations

    def operations(self) -> List[PatchOperation]:
        """Equivalent RF6902 operations to merge of Partial.

        Returns:
            List[PatchOperation]: Equivalent list of RF6902 operations
        """
        return self.merge_to_operations(self.model_dump())


class PartialCollection(BasePartial):
    """Partial STAC Collection."""

    type: Optional[str]
    stac_version: Optional[str]
    stac_extensions: Optional[List[str]]
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    links: List[Dict[str, Any]]
    keywords: Optional[List[str]]
    license: Optional[str]
    providers: Optional[List[Dict[str, Any]]]
    extent: Optional[Dict[str, Any]]
    summaries: Optional[Dict[str, Any]]
    assets: Optional[Dict[str, Any]]
    numberMatched: Optional[int] = None
    numberReturned: Optional[int] = None


class PartialItem(BasePartial):
    """Partial STAC Item."""

    type: Optional[Literal["Feature"]]
    stac_version: Optional[str]
    stac_extensions: Optional[List[str]]
    id: Optional[str]
    geometry: Optional[Dict[str, Any]]
    bbox: Optional[BBox]
    properties: Optional[Dict[str, Any]]
    links: Optional[List[Dict[str, Any]]]
    assets: Optional[Dict[str, Any]]
    collection: Optional[str]
