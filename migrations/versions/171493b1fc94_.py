"""empty message

Revision ID: 171493b1fc94
Revises: 4dbd1acd2f7f
Create Date: 2020-01-04 19:04:02.199454

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '171493b1fc94'
down_revision = '4dbd1acd2f7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blend', sa.Column('blenddate', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blend', 'blenddate')
    # ### end Alembic commands ###