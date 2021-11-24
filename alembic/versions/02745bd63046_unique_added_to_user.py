"""unique_added_to_user

Revision ID: 02745bd63046
Revises: 8d2529e71670
Create Date: 2021-11-21 03:05:32.253145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02745bd63046'
down_revision = '8d2529e71670'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'bot_users', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bot_users', type_='unique')
    # ### end Alembic commands ###
