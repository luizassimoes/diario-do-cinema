"""tchau weird keys

Revision ID: 5c0d836e0c0c
Revises: c3bc9d14203d
Create Date: 2024-01-15 17:47:12.980661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5c0d836e0c0c'
down_revision = 'c3bc9d14203d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calculations', schema=None) as batch_op:
        batch_op.drop_constraint('calculations_ibfk_1', type_='foreignkey')
        batch_op.drop_column('movie_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calculations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('movie_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('calculations_ibfk_1', 'movies', ['movie_id'], ['id'])

    # ### end Alembic commands ###
