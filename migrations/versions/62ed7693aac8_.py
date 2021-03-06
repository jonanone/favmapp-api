"""empty message

Revision ID: 62ed7693aac8
Revises: None
Create Date: 2016-05-09 16:52:36.623641

"""

# revision identifiers, used by Alembic.
revision = '62ed7693aac8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    ### end Alembic commands ###
