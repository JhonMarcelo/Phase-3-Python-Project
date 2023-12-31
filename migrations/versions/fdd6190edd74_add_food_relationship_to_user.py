"""add food relationship to user

Revision ID: fdd6190edd74
Revises: a058324d01a6
Create Date: 2023-08-24 23:43:11.368983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdd6190edd74'
down_revision: Union[str, None] = 'a058324d01a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key("user_food", 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.drop_constraint("user_food", type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
