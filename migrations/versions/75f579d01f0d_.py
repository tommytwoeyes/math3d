"""empty message

Revision ID: 75f579d01f0d
Revises: 25f4f234760c
Create Date: 2017-05-06 23:15:02.228272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75f579d01f0d'
down_revision = '25f4f234760c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('graphs', sa.Column('short_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('graphs', 'short_url')
    # ### end Alembic commands ###