from scrapy.item import Item, Field


class CPUscrapy(Item):
    processor = Field()
    cache = Field()
    lithography = Field()
    cores = Field()
    thread = Field()
    base_freq = Field()
    max_freq = Field()
    tdp = Field()
    mem_types = Field()
    max_mem_channels = Field()
    max_mem_bandwidth = Field()
    ECC = Field()
    processor_graphics = Field()
    graph_base_freq = Field()
    graph_max_dyn_freq = Field()
    graph_max_mem = Field()
    pcie_revision = Field()
    max_pcie_lanes = Field()
    pcie_config = Field()
    socket = Field()
