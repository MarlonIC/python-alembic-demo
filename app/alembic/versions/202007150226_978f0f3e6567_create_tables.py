"""create tables

Revision ID: 978f0f3e6567
Revises: 
Create Date: 2020-07-15 02:26:35.493333-05:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '978f0f3e6567'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('account')
