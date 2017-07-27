"""added key to comments.subreddit_id

Revision ID: 2959fa8d7ad8
Revises: 05a831a5db7b
Create Date: 2017-07-26 19:53:29.818965

"""

# revision identifiers, used by Alembic.
revision = '2959fa8d7ad8'
down_revision = '05a831a5db7b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_development():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_posts_subreddit_id'), 'posts', ['subreddit_id'], unique=False)
    ### end Alembic commands ###


def downgrade_development():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_subreddit_id'), table_name='posts')
    ### end Alembic commands ###


def upgrade_test():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_posts_subreddit_id'), 'posts', ['subreddit_id'], unique=False)
    ### end Alembic commands ###


def downgrade_test():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_subreddit_id'), table_name='posts')
    ### end Alembic commands ###


def upgrade_production():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_posts_subreddit_id'), 'posts', ['subreddit_id'], unique=False)
    ### end Alembic commands ###


def downgrade_production():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_subreddit_id'), table_name='posts')
    ### end Alembic commands ###

