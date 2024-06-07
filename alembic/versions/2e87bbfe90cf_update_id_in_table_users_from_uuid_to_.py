"""Update id in table users from UUID to Integer

Revision ID: 2e87bbfe90cf
Revises: bbc49a9fe5d8
Create Date: 2024-06-07 13:51:02.130537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e87bbfe90cf'
down_revision: Union[str, None] = 'bbc49a9fe5d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=sa.BINARY(length=16),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=sa.Integer(),
               type_=sa.BINARY(length=16),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
