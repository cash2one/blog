"""add head_img field for User

Revision ID: 4db6fe551d5a
Revises: 59d86417acee
Create Date: 2015-12-04 17:25:56.605882

"""

# revision identifiers, used by Alembic.
revision = '4db6fe551d5a'
down_revision = '59d86417acee'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_user', sa.Column('head_img', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_user', 'head_img')
    ### end Alembic commands ###
