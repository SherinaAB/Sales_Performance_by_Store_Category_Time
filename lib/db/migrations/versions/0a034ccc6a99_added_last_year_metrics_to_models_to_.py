"""added last year metrics to models to models file

Revision ID: 0a034ccc6a99
Revises: afe8cfe9c2ae
Create Date: 2023-08-09 10:27:51.680187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a034ccc6a99'
down_revision: Union[str, None] = 'afe8cfe9c2ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dates', sa.Column('ly_week_number', sa.Integer(), nullable=True))
    op.add_column('dates', sa.Column('ly_week', sa.String(), nullable=True))
    op.add_column('dates', sa.Column('ly_month', sa.String(), nullable=True))
    op.add_column('dates', sa.Column('ly_quarter', sa.String(), nullable=True))
    op.add_column('dates', sa.Column('ly_year', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dates', 'ly_year')
    op.drop_column('dates', 'ly_quarter')
    op.drop_column('dates', 'ly_month')
    op.drop_column('dates', 'ly_week')
    op.drop_column('dates', 'ly_week_number')
    # ### end Alembic commands ###