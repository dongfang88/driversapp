"""为cars增加一列owner_id

Revision ID: 4855b5afa6d6
Revises: 8ecc4a3a4983
Create Date: 2025-06-05 09:02:28.834291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4855b5afa6d6'
down_revision: Union[str, None] = '8ecc4a3a4983'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cars', 'drivers', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cars', type_='foreignkey')
    op.drop_column('cars', 'owner_id')
    # ### end Alembic commands ###
