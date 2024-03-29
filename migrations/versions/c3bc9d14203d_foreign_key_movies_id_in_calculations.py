"""foreign key movies.id in Calculations

Revision ID: c3bc9d14203d
Revises: 1d4d3304c7c5
Create Date: 2024-01-15 17:37:45.461171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3bc9d14203d'
down_revision = '1d4d3304c7c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calculations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('movie_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'movies', ['movie_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calculations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('movie_id')

    # ### end Alembic commands ###
