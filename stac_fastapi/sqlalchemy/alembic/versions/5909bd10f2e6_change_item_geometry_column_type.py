"""change item geometry column type

Revision ID: 5909bd10f2e6
Revises: 821aa04011e8
Create Date: 2021-11-23 10:14:17.974565

"""
from alembic import op

from stac_fastapi.sqlalchemy.models.database import GeojsonGeometry

# revision identifiers, used by Alembic.
revision = "5909bd10f2e6"
down_revision = "821aa04011e8"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        schema="data",
        table_name="items",
        column_name="geometry",
        type_=GeojsonGeometry("Geometry", srid=4326, spatial_index=True),
    )


def downgrade():
    op.alter_column(
        schema="data",
        table_name="items",
        column_name="geometry",
        type_=GeojsonGeometry("Polygon", srid=4326, spatial_index=True),
    )
