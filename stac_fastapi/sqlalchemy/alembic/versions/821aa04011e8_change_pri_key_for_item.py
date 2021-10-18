"""Change pri key for Item

Revision ID: 821aa04011e8
Revises: 407037cb1636
Create Date: 2021-10-11 12:10:34.148098

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "821aa04011e8"
down_revision = "407037cb1636"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint("items_pkey", "items", schema="data")
    op.create_primary_key("items_pkey", "items", ["id", "collection_id"], schema="data")


def downgrade():
    op.drop_constraint("items_pkey", "items", schema="data")
    op.create_primary_key("items_pkey", "items", ["id"], schema="data")
