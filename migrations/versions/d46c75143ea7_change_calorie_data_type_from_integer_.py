"""change calorie data type from integer to float

Revision ID: d46c75143ea7
Revises: 3b60a75cfd4d
Create Date: 2023-08-25 00:32:07.655168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd46c75143ea7'
down_revision: Union[str, None] = '3b60a75cfd4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.drop_column('calorie')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('calorie', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
