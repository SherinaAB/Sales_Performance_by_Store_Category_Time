"""recreating db

Revision ID: 1eda8feea5e5
Revises: 
Create Date: 2023-08-10 14:04:03.550867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1eda8feea5e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('product_description', sa.String(), nullable=True),
    sa.Column('sku', sa.Integer(), nullable=True),
    sa.Column('wholesale', sa.Integer(), nullable=True),
    sa.Column('retail', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('store_number', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('market', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('national', sa.String(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('sales_quantity', sa.Integer(), nullable=True),
    sa.Column('sales_dollar_amount', sa.Integer(), nullable=True),
    sa.Column('cost_dollar_amount', sa.Integer(), nullable=True),
    sa.Column('gross_profit_dollar_amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    op.drop_table('stores')
    op.drop_table('products')
    # ### end Alembic commands ###
