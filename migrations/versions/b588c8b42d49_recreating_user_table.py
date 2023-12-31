"""Recreating user table

Revision ID: b588c8b42d49
Revises: ab55fded6711
Create Date: 2023-08-26 09:31:13.659022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b588c8b42d49'
down_revision: Union[str, None] = 'ab55fded6711'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('activity_level', sa.Integer(), nullable=True),
    sa.Column('goal', sa.String(), nullable=True),
    sa.Column('target_calorie', sa.Integer(), nullable=True),
    sa.Column('current_calorie', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('food_name', sa.String(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('calorie', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foods')
    op.drop_table('users')
    # ### end Alembic commands ###
