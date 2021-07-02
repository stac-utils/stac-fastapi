"""Queryable data types for sqlalchemy backend."""

from dataclasses import dataclass

import sqlalchemy as sa


@dataclass
class QueryableTypes:
    """Defines a set of queryable fields.

    # TODO: Let the user define these in a config file
    # TODO: There is a much better way of defining this field <> type mapping than two enums with same keys
    """

    orientation = sa.String
    gsd = sa.Float
    epsg = sa.Integer
    height = sa.Integer
    width = sa.Integer
    minzoom = sa.Integer
    maxzoom = sa.Integer
    dtype = sa.String
