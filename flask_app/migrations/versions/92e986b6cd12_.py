"""empty message

Revision ID: 92e986b6cd12
Revises: 
Create Date: 2023-01-16 15:56:09.070579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92e986b6cd12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.drop_index('ix_cat_name')

    op.drop_table('cat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('breed', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cat_pkey')
    )
    with op.batch_alter_table('cat', schema=None) as batch_op:
        batch_op.create_index('ix_cat_name', ['name'], unique=False)

    # ### end Alembic commands ###
