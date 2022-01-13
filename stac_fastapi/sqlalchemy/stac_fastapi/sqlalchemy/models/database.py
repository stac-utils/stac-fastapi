"""SQLAlchemy ORM models."""

import json
from typing import Optional

import geoalchemy2 as ga
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

from stac_fastapi.sqlalchemy.extensions.query import Queryables, QueryableTypes

BaseModel = declarative_base()


class GeojsonGeometry(ga.Geometry):
    """Custom geoalchemy type which returns GeoJSON."""

    from_text = "ST_GeomFromGeoJSON"

    def result_processor(self, dialect: str, coltype):
        """Override default processer to return GeoJSON."""

        def process(value: Optional[bytes]):
            if value is not None:
                geom = ga.shape.to_shape(
                    ga.elements.WKBElement(
                        value, srid=self.srid, extended=self.extended
                    )
                )
                return json.loads(json.dumps(geom.__geo_interface__))

        return process


class Collection(BaseModel):  # type:ignore
    """Collection orm model."""

    __tablename__ = "collections"
    __table_args__ = {"schema": "data"}

    id = sa.Column(sa.VARCHAR(1024), nullable=False, primary_key=True)
    stac_version = sa.Column(sa.VARCHAR(300))
    stac_extensions = sa.Column(sa.ARRAY(sa.VARCHAR(300)), nullable=True)
    title = sa.Column(sa.VARCHAR(1024))
    description = sa.Column(sa.VARCHAR(1024), nullable=False)
    keywords = sa.Column(sa.ARRAY(sa.VARCHAR(300)))
    version = sa.Column(sa.VARCHAR(300))
    license = sa.Column(sa.VARCHAR(300), nullable=False)
    providers = sa.Column(JSONB)
    summaries = sa.Column(JSONB, nullable=True)
    extent = sa.Column(JSONB)
    links = sa.Column(JSONB)
    children = sa.orm.relationship("Item", lazy="dynamic")
    type = sa.Column(sa.VARCHAR(300), nullable=False)


class Item(BaseModel):  # type:ignore
    """Item orm model."""

    __tablename__ = "items"
    __table_args__ = {"schema": "data"}

    id = sa.Column(sa.VARCHAR(1024), nullable=False, primary_key=True)
    stac_version = sa.Column(sa.VARCHAR(300))
    stac_extensions = sa.Column(sa.ARRAY(sa.VARCHAR(300)), nullable=True)
    geometry = sa.Column(GeojsonGeometry("GEOMETRY", srid=4326, spatial_index=True))
    bbox = sa.Column(sa.ARRAY(sa.NUMERIC), nullable=False)
    properties = sa.Column(JSONB)
    assets = sa.Column(JSONB)
    collection_id = sa.Column(
        sa.VARCHAR(1024), sa.ForeignKey(Collection.id), nullable=False, primary_key=True
    )
    parent_collection = sa.orm.relationship("Collection", back_populates="children")
    datetime = sa.Column(sa.TIMESTAMP(timezone=True), nullable=False)
    links = sa.Column(JSONB)

    @classmethod
    def get_field(cls, field_name):
        """Get a model field."""
        try:
            return getattr(cls, field_name)
        except AttributeError:
            # Use a JSONB field
            return cls.properties[(field_name)].cast(
                getattr(QueryableTypes, Queryables(field_name).name)
            )


class PaginationToken(BaseModel):  # type:ignore
    """Pagination orm model."""

    __tablename__ = "tokens"
    __table_args__ = {"schema": "data"}

    id = sa.Column(sa.VARCHAR(100), nullable=False, primary_key=True)
    keyset = sa.Column(sa.VARCHAR(1000), nullable=False)
