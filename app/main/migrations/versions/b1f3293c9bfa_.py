"""empty message

Revision ID: b1f3293c9bfa
Revises: 
Create Date: 2020-07-27 21:38:54.136847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1f3293c9bfa'
down_revision = None
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
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('room', sa.Integer(), nullable=True),
    sa.Column('characteristic', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    op.drop_table('user')
    # ### end Alembic commands ###