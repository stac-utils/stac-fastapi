"""add-stac-1.0.0-fields

Revision ID: 407037cb1636
Revises: 77c019af60bf
Create Date: 2021-07-07 16:10:03.196942

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "407037cb1636"
down_revision = "77c019af60bf"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "collections",
        sa.Column("type", sa.VARCHAR(300), default="collection", nullable=False),
        schema="data",
    )


def downgrade():
    op.drop_column("collections", "type")
