"""Migrate all v4

Revision ID: bcdecf3b0f65
Revises: a636d69ac1fa
Create Date: 2020-07-15 12:19:06.423106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcdecf3b0f65'
down_revision = 'a636d69ac1fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    # ### end Alembic commands ###