"""create initial schema

Revision ID: 131aab4d9e49
Revises:
Create Date: 2020-02-09 13:03:09.336631

"""  # noqa
import sqlalchemy as sa
from alembic import op
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision = "131aab4d9e49"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """upgrade to this revision"""
    op.execute("CREATE SCHEMA data")
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")

    # Create collections table
    op.create_table(
        "collections",
        sa.Column("id", sa.VARCHAR(1024), nullable=False, primary_key=True),
        sa.Column("stac_version", sa.VARCHAR(300)),
        sa.Column("title", sa.VARCHAR(1024)),
        sa.Column("stac_extensions", sa.ARRAY(sa.VARCHAR(300)), nullable=True),
        sa.Column("description", sa.VARCHAR(1024), nullable=False),
        sa.Column("keywords", sa.ARRAY(sa.VARCHAR(300))),
        sa.Column("version", sa.VARCHAR(300)),
        sa.Column("license", sa.VARCHAR(300), nullable=False),
        sa.Column("providers", JSONB),
        sa.Column("summaries", JSONB, nullable=True),
        sa.Column("extent", JSONB),
        sa.Column("links", JSONB, nullable=True),
        schema="data",
    )

    # Create items table
    op.create_table(
        "items",
        sa.Column("id", sa.VARCHAR(1024), nullable=False, primary_key=True),
        sa.Column("stac_version", sa.VARCHAR(300)),
        sa.Column("stac_extensions", sa.ARRAY(sa.VARCHAR(300)), nullable=True),
        sa.Column("geometry", Geometry("POLYGON", srid=4326, spatial_index=True)),
        sa.Column("bbox", sa.ARRAY(sa.NUMERIC), nullable=False),
        sa.Column("properties", JSONB),
        sa.Column("assets", JSONB),
        sa.Column("collection_id", sa.VARCHAR(1024), nullable=False, index=True),
        # These are usually in properties but defined as their own fields for indexing
        sa.Column("datetime", sa.TIMESTAMP, nullable=False, index=True),
        sa.Column("links", JSONB, nullable=True),
        sa.ForeignKeyConstraint(["collection_id"], ["data.collections.id"]),
        schema="data",
    )

    # Create pagination token table
    op.create_table(
        "tokens",
        sa.Column("id", sa.VARCHAR(100), nullable=False, primary_key=True),
        sa.Column("keyset", sa.VARCHAR(1000), nullable=False),
        schema="data",
    )


def downgrade():
    """downgrade to previous revision"""
    op.execute("DROP TABLE data.items")
    op.execute("DROP TABLE data.collections")
    op.execute("DROP TABLE data.tokens")
    op.execute("DROP SCHEMA data")
    op.execute("DROP EXTENSION IF EXISTS postgis")
