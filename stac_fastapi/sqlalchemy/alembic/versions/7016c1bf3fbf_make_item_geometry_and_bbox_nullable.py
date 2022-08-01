"""Make item geometry and bbox nullable

Revision ID: 7016c1bf3fbf
Revises: 5909bd10f2e6
Create Date: 2022-04-28 10:40:06.856826

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "7016c1bf3fbf"
down_revision = "5909bd10f2e6"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        schema="data",
        table_name="items",
        column_name="geometry",
        nullable=True,
    )
    op.alter_column(
        schema="data",
        table_name="items",
        column_name="bbox",
        nullable=True,
    )


def downgrade():
    # Downgrading will require the user to update or remove all null geometry
    # cases from the DB, otherwise the downgrade migration will fail.
    op.alter_column(
        schema="data",
        table_name="items",
        column_name="geometry",
        nullable=False,
    )
    op.alter_column(
        schema="data",
        table_name="items",
        column_name="bbox",
        nullable=False,
    )
