from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
CPU = Table('CPU', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cpubrand_id', Integer),
    Column('processor', String),
    Column('processor_name', String),
    Column('processor_type', String),
    Column('cache', Integer),
    Column('cache_u', String),
    Column('lithography', Integer),
    Column('lithography_u', String),
    Column('cores', Integer),
    Column('thread', Integer),
    Column('base_freq', Float),
    Column('base_freq_u', String),
    Column('max_freq', Float),
    Column('max_freq_u', String),
    Column('tdp', Integer),
    Column('tdp_u', String),
    Column('mem_types', String),
    Column('max_mem_channels', Integer),
    Column('max_mem_bandwidth', Float),
    Column('max_mem_bandwidth_u', String),
    Column('ECC', String),
    Column('processor_graphics', String),
    Column('graph_base_freq', Integer),
    Column('graph_base_freq_u', String),
    Column('graph_max_dyn_freq', Float),
    Column('graph_max_dyn_freq_u', String),
    Column('pcie_revision', String),
    Column('max_pcie_lanes', Integer),
    Column('pcie_config', String),
    Column('socket', String),
    Column('link', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['CPU'].columns['link'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['CPU'].columns['link'].drop()
