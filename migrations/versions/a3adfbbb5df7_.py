"""empty message

Revision ID: a3adfbbb5df7
Revises: 76662f7c0738
Create Date: 2024-08-12 22:30:33.949309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3adfbbb5df7'
down_revision: Union[str, None] = '76662f7c0738'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('is_billable', sa.Boolean(), nullable=True))
    op.add_column('projects', sa.Column('rate', sa.DECIMAL(precision=10, scale=2), nullable=True))
    op.add_column('tasks', sa.Column('earned', sa.DECIMAL(precision=10, scale=2), nullable=True))
    op.execute("UPDATE projects SET is_billable = false")
    op.alter_column("projects", "is_billable", nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'earned')
    op.drop_column('projects', 'rate')
    op.drop_column('projects', 'is_billable')
    # ### end Alembic commands ###
