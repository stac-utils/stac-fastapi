"""Queryable data types for sqlalchemy backend."""

from dataclasses import dataclass

import sqlalchemy as sa


@dataclass
class QueryableTypes:
    """Defines a set of queryable fields.

    # TODO: Let the user define these in a config file
    # TODO: There is a much better way of defining this field <> type mapping than two enums with same keys
    """

    orientation = sa.Text
    gsd = sa.Float
    epsg = sa.Integer
    height = sa.Integer
    width = sa.Integer
    minzoom = sa.Integer
    maxzoom = sa.Integer
    dtype = sa.Text
    start_datetime = sa.Text
    end_datetime = sa.Text
    created = sa.Text
    updated = sa.Text
    supercell_id = sa.Text
    tile_id = sa.Text
    data_type = sa.Text
    block_overlap = sa.Integer
    nodata = sa.Integer
    GRID1MIL = sa.Text
    GRID100K = sa.Text
    MGRS_UTM = sa.Text
    latitude_band = sa.Text    
    sequence = sa.Text
    product_id = sa.Text
    grid_square = sa.Text
    utm_zone = sa.Integer
    data_coverage = sa.Float
    cloud_cover = sa.Float
