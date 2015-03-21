from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Drive = Table('Drive', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
)

PC = Table('PC', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('cpu_id', Integer),
    Column('cooler_id', Integer),
    Column('motherboard_id', Integer),
    Column('ram_id', Integer),
    Column('gpu_id', Integer),
    Column('storage_id', Integer),
    Column('case_id', Integer),
    Column('psu_id', Integer),
    Column('drive_d', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Drive'].create()
    post_meta.tables['PC'].columns['drive_d'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['Drive'].drop()
    post_meta.tables['PC'].columns['drive_d'].drop()
