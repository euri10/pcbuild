from scrapy.item import Item, Field


class asusMBitem(Item):
    name = Field()
    brand = Field
    form = Field()
    chipset = Field()
    sata3 = Field()
    sata6 = Field()
    dimm = Field()
    memory_max_ = Field()
    memory_max_u = Field()
    memory_type = Field()




class intelCPUitem(Item):
    cpubrand_id = Field()
    processor = Field()
    processor_name = Field()
    processor_type = Field()
    cache = Field()
    cache_u = Field()
    lithography = Field()
    lithography_u = Field()
    cores = Field()
    thread = Field()
    base_freq = Field()
    base_freq_u = Field()
    max_freq = Field()
    max_freq_u = Field()
    tdp = Field()
    tdp_u = Field()
    mem_types = Field()
    max_mem_channels = Field()
    max_mem_bandwidth = Field()
    max_mem_bandwidth_u = Field()
    ECC = Field()
    processor_graphics = Field()
    graph_base_freq = Field()
    graph_base_freq_u = Field()
    graph_max_dyn_freq = Field()
    graph_max_dyn_freq_u = Field()
    pcie_revision = Field()
    max_pcie_lanes = Field()
    pcie_config = Field()
    socket = Field()
    link = Field()
