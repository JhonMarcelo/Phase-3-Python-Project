"""added activity_level on my repr

Revision ID: 096d72c2af0e
Revises: 891c94f2d3b0
Create Date: 2023-08-24 02:37:42.493618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '096d72c2af0e'
down_revision: Union[str, None] = '891c94f2d3b0'
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
