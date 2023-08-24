"""create meals table

Revision ID: aecfbc7cd421
Revises: ca5825e1d6bd
Create Date: 2023-08-23 23:24:25.372681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aecfbc7cd421'
down_revision: Union[str, None] = 'ca5825e1d6bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('food_name', sa.String(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('calorie', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meals')
    # ### end Alembic commands ###
