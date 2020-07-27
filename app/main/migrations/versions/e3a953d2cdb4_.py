"""empty message

Revision ID: e3a953d2cdb4
Revises: 88bdd4c223e4
Create Date: 2020-07-27 19:49:56.334922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3a953d2cdb4'
down_revision = '88bdd4c223e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=50), nullable=True),
    sa.Column('lastName', sa.String(length=50), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###