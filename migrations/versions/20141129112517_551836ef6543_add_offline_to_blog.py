"""Add offline to Blog

Revision ID: 551836ef6543
Revises: 22d1bd4d3452
Create Date: 2014-11-29 11:25:17.207021

"""

# revision identifiers, used by Alembic.
revision = '551836ef6543'
down_revision = '22d1bd4d3452'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('offline', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'offline')
    ### end Alembic commands ###
