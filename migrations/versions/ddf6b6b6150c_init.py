"""init

Revision ID: ddf6b6b6150c
Revises: 
Create Date: 2023-11-05 11:40:03.265882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddf6b6b6150c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_telegram', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('language_code', sa.String(length=255), nullable=True),
    sa.Column('is_bot', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_telegram')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('category_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('kind', sa.Enum('INCOME', 'EXPENSE', name='kindoperationenum'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'name', 'kind', name='_unique_catagory_user')
    )
    op.create_index(op.f('ix_category_user_id'), 'category_user', ['id'], unique=False)
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('category_user_id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.Enum('INCOME', 'EXPENSE', name='kindoperationenum'), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_user_id'], ['category_user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_id'), 'operation', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operation_id'), table_name='operation')
    op.drop_table('operation')
    op.drop_index(op.f('ix_category_user_id'), table_name='category_user')
    op.drop_table('category_user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
