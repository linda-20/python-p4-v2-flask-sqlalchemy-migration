"""add Department

Revision ID: 3613f55275e4
Revises: f75224a8893a
Create Date: 2024-04-03 07:00:08.314759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3613f55275e4'
down_revision = 'f75224a8893a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
