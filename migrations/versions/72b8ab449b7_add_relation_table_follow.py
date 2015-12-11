"""add relation table Follow

Revision ID: 72b8ab449b7
Revises: 30743a3b7fe3
Create Date: 2015-12-11 17:51:02.225033

"""

# revision identifiers, used by Alembic.
revision = '72b8ab449b7'
down_revision = '30743a3b7fe3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('follow_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['blog_user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['blog_user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_follows')
    ### end Alembic commands ###
