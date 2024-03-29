"""Added required tables

Revision ID: 32c64cc56c28
Revises: 9485e117ca87
Create Date: 2024-01-08 19:54:22.631328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32c64cc56c28'
down_revision: Union[str, None] = '9485e117ca87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('dog', 'cat', name='typepet'), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photo',
    sa.Column('id_photo', sa.String(length=100), nullable=False),
    sa.Column('pet_id', sa.String(), nullable=False),
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo')
    op.drop_table('pet')
    # ### end Alembic commands ###
