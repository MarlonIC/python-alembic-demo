"""add column to table account

Revision ID: a5de934dfbae
Revises: 978f0f3e6567
Create Date: 2020-07-15 02:53:26.732055-05:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5de934dfbae'
down_revision = '978f0f3e6567'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
