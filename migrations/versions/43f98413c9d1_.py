"""empty message

Revision ID: 43f98413c9d1
Revises: f6fd4a24faf3
Create Date: 2020-02-21 15:49:06.682355

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '43f98413c9d1'
down_revision = 'f6fd4a24faf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    op.drop_table('roles_users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles_users',
                    sa.Column('user_id', sa.INTEGER(), nullable=True),
                    sa.Column('role_id', sa.INTEGER(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
                    )
    op.create_table('role',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=80), nullable=True),
                    sa.Column('description', sa.VARCHAR(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    # ### end Alembic commands ###
