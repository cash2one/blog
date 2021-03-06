"""initial migtation

Revision ID: 28b6e67ca082
Revises: None
Create Date: 2015-11-19 17:31:51.546644

"""

# revision identifiers, used by Alembic.
revision = '28b6e67ca082'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_user', sa.Column('last_login_date', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_user', 'last_login_date')
    ### end Alembic commands ###
