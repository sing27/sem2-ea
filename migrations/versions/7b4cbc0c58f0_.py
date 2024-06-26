"""empty message

Revision ID: 7b4cbc0c58f0
Revises: e2200a76689f
Create Date: 2024-04-27 05:59:54.502818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b4cbc0c58f0'
down_revision = 'e2200a76689f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price_range', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('served_during',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('served_time', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coupon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('price_id', sa.Integer(), nullable=True),
    sa.Column('Served_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Served_id'], ['served_during.id'], ),
    sa.ForeignKeyConstraint(['price_id'], ['price.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupon')
    op.drop_table('served_during')
    op.drop_table('price')
    # ### end Alembic commands ###
