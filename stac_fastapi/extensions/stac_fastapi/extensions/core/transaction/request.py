"""Transaction extension request models."""

import json
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import ConfigDict, Field
from stac_pydantic.shared import BBox, StacBaseModel


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
        operations: List[PatchOperation] = []

        for key, value in data.copy().items():
            if value is None:
                operations.append(PatchRemove(op="remove", path=f"/{key}"))

            elif isinstance(value, dict):
                nested_operations = BasePartial.merge_to_operations(value)

                for nested_operation in nested_operations:
                    nested_operation.path = f"/{key}{nested_operation.path}"
                    operations.append(nested_operation)

            else:
                operations.append(
                    PatchAddReplaceTest(op="add", path=f"/{key}", value=value)
                )

        return operations

    def operations(self) -> List[PatchOperation]:
        """Equivalent RF6902 operations to merge of Partial.

        Returns:
            List[PatchOperation]: Equivalent list of RF6902 operations
        """
        return self.merge_to_operations(self.model_dump())


class PartialCollection(BasePartial):
    """Partial STAC Collection."""

    type: Optional[str] = None
    stac_version: Optional[str] = None
    stac_extensions: Optional[List[str]] = None
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    links: Optional[Dict[str, Any]] = None
    keywords: Optional[List[str]] = None
    license: Optional[str] = None
    providers: Optional[List[Dict[str, Any]]] = None
    extent: Optional[Dict[str, Any]] = None
    summaries: Optional[Dict[str, Any]] = None
    assets: Optional[Dict[str, Any]] = None


class PartialItem(BasePartial):
    """Partial STAC Item."""

    type: Optional[Literal["Feature"]] = None
    stac_version: Optional[str] = None
    stac_extensions: Optional[List[str]] = None
    id: Optional[str] = None
    geometry: Optional[Dict[str, Any]] = None
    bbox: Optional[BBox] = None
    properties: Optional[Dict[str, Any]] = None
    links: Optional[List[Dict[str, Any]]] = None
    assets: Optional[Dict[str, Any]] = None
    collection: Optional[str] = None
