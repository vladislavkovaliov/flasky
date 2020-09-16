"""update user model

Revision ID: 3fbb244363a8
Revises: 5d4d7e1b112e
Create Date: 2020-09-13 16:13:28.522133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbb244363a8'
down_revision = '5d4d7e1b112e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'location')
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###