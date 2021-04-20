"""use timestamptz rather than timestamp

Revision ID: 77c019af60bf
Revises: 131aab4d9e49
Create Date: 2021-03-02 11:51:43.539119

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "77c019af60bf"
down_revision = "131aab4d9e49"
branch_labels = None
depends_on = None


def upgrade():
    """upgrade to this revision"""
    op.execute(
        """
        ALTER TABLE
            data.items
            ALTER COLUMN datetime
            TYPE timestamptz
        ;
    """
    )


def downgrade():
    """downgrade from this revision"""
    op.execute(
        """
        ALTER TABLE
            data.items
            ALTER COLUMN datetime
            TYPE timestamp
        ;
    """
    )
