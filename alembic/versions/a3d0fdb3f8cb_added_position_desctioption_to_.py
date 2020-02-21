"""Added Position Desctioption to Application Table

Revision ID: a3d0fdb3f8cb
Revises: 3b326ec0f722
Create Date: 2020-02-11 16:52:08.594261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3d0fdb3f8cb'
down_revision = '3b326ec0f722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('position', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('application', 'position')
    # ### end Alembic commands ###
