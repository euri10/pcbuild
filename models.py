__author__ = 'euri10'

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base


DeclarativeBase = declarative_base()


class PC(DeclarativeBase):
    __tablename__ = 'PC'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cpu_id = Column(Integer, ForeignKey('CPU.id'))
    cooler_id = Column(Integer, ForeignKey('CPUCooler.id'))
    motherboard_id = Column(Integer, ForeignKey('MB.id'))
    ram_id = Column(Integer, ForeignKey('RAM.id'))
    gpu_id = Column(Integer, ForeignKey('GPU.id'))
    storage_id = Column(Integer, ForeignKey('Storage.id'))
    case_id = Column(Integer, ForeignKey('Case.id'))
    psu_id = Column(Integer, ForeignKey('PSU.id'))


class CPU(DeclarativeBase):
    __tablename__ = 'CPU'
    id = Column(Integer, primary_key=True)
    cpubrand_id = Column(Integer, ForeignKey('CPUBrand.id'))
    processor_name = Column(String)
    processor_type = Column(String)
    cache = Column(Integer)
    lithography = Column(Integer)
    cores = Column(Integer)
    thread = Column(Integer)
    base_freq = Column(Float)
    max_freq = Column(Float)
    tdp = Column(Integer)
    mem_types = Column(String)
    max_mem_channels = Column(Integer)
    max_mem_bandwidth = Column(Float)
    ECC = Column(Boolean)
    processor_graphics = Column(String)
    graph_base_freq = Column(Integer)
    graph_max_dyn_freq = Column(Float)
    graph_max_mem = Column(Float)
    pcie_revision = Column(Float)
    max_pcie_lanes = Column(Integer)
    pcie_config = Column(String)
    socket = Column(Integer, ForeignKey('Socket.id'))


class Socket(DeclarativeBase):
    __tablename__ = 'Socket'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class CPUCooler(DeclarativeBase):
    __tablename__ = 'CPUCooler'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class MB(DeclarativeBase):
    __tablename__ = 'MB'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class RAM(DeclarativeBase):
    __tablename__ = 'RAM'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class GPU(DeclarativeBase):
    __tablename__ = 'GPU'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Storage(DeclarativeBase):
    __tablename__ = 'Storage'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Case(DeclarativeBase):
    __tablename__ = 'Case'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class PSU(DeclarativeBase):
    __tablename__ = 'PSU'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class CPUBrand(DeclarativeBase):
    __tablename__ = 'CPUBrand'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)