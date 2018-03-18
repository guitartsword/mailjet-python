"""change type of columns

Revision ID: dc1e2820c8e7
Revises: 6648c905e371
Create Date: 2018-03-18 12:24:32.236262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc1e2820c8e7'
down_revision = '6648c905e371'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('notification_configuration', sa.Column('html', sa.TEXT))
    op.alter_column('notification_configuration', sa.Column('text', sa.TEXT))
    pass


def downgrade():
    op.alter_column('notification_configuration', sa.Column('html', sa.String(100)))
    op.alter_column('notification_configuration', sa.Column('text', sa.String(100)))
    pass
