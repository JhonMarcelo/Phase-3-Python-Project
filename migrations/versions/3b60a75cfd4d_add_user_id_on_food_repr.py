"""add user_id on food repr

Revision ID: 3b60a75cfd4d
Revises: 39840d3c689b
Create Date: 2023-08-25 00:25:09.667877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b60a75cfd4d'
down_revision: Union[str, None] = '39840d3c689b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###