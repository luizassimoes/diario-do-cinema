"""empty message

Revision ID: 93e131b29942
Revises: 8e3b455f6ddc
Create Date: 2024-02-07 11:41:24.368544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93e131b29942'
down_revision = '8e3b455f6ddc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avg', sa.DECIMAL(precision=10, scale=2), nullable=True))
        batch_op.add_column(sa.Column('sd', sa.DECIMAL(precision=10, scale=2), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.drop_column('sd')
        batch_op.drop_column('avg')

    # ### end Alembic commands ###
