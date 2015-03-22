__author__ = 'euri10'

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app import db


class PC(db.Model):
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
    drive_d = Column(Integer, ForeignKey('Drive.id'))


class Drive(db.Model):
    __tablename__ = 'Drive'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class CPU(db.Model):
    __tablename__ = 'CPU'
    id = Column(Integer, primary_key=True)
    cpubrand_id = Column(Integer, ForeignKey('CPUBrand.id'))
    processor = Column(String, unique=True)
    processor_name = Column(String)
    processor_type = Column(String)
    cache = Column(Integer)
    cache_u = Column(String)
    lithography = Column(Integer)
    lithography_u = Column(String)
    cores = Column(Integer)
    thread = Column(Integer)
    base_freq = Column(Float)
    base_freq_u = Column(String)
    max_freq = Column(Float)
    max_freq_u = Column(String)
    tdp = Column(Integer)
    tdp_u = Column(String)
    mem_types = Column(String)
    max_mem_channels = Column(Integer)
    max_mem_bandwidth = Column(Float)
    max_mem_bandwidth_u = Column(String)
    ECC = Column(String)
    processor_graphics = Column(String)
    graph_base_freq = Column(Integer)
    graph_base_freq_u = Column(String)
    graph_max_dyn_freq = Column(Float)
    graph_max_dyn_freq_u = Column(String)
    pcie_revision = Column(String)
    max_pcie_lanes = Column(Integer)
    pcie_config = Column(String)
    socket = Column(String, ForeignKey('Socket.name'))
    link = Column(String)


class Socket(db.Model):
    __tablename__ = 'Socket'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class CPUCooler(db.Model):
    __tablename__ = 'CPUCooler'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class MB(db.Model):
    __tablename__ = 'MB'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class RAM(db.Model):
    __tablename__ = 'RAM'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class GPU(db.Model):
    __tablename__ = 'GPU'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Storage(db.Model):
    __tablename__ = 'Storage'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Case(db.Model):
    __tablename__ = 'Case'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class PSU(db.Model):
    __tablename__ = 'PSU'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class CPUBrand(db.Model):
    __tablename__ = 'CPUBrand'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)