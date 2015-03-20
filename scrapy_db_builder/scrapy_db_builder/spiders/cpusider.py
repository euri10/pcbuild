__author__ = 'euri10'

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy_db_builder.items import CPUscrapy
from scrapy import Request

class CPUSpider(CrawlSpider):


    name = 'cpuspider'
    allowed_domains = ['ark.intel.com']
    start_urls = ['http://ark.intel.com/search/advanced?s=t']

    rules = (
            Rule(LxmlLinkExtractor(allow_domains=allowed_domains,
                                   restrict_xpaths='.//*[@id="grid-03-shb"]/div[1]/div[5]/div/div[4]/table/tbody/tr[*]/td[2]/a',
                                   process_value=None), callback='parse_cpu_page'),
        )

    def parse_cpu_page(self, response):
        item = CPUscrapy()
        print response.xpath('.//*[@id="ProcessorNumber"]/td[2]/text()')
        item['processor'] = response.xpath('.//*[@id="ProcessorNumber"]/td[2]/text()').extract()
        item['cache'] = response.xpath('.//*[@id="Cache"]/td[2]/text()').extract()
        item['lithography'] = response.xpath('.//*[@id="Lithography"]/td[2]/text()').extract()
        item['cores'] = response.xpath('.//*[@id="CoreCount"]/td[2]/text()').extract()
        item['thread'] = response.xpath('.//*[@id="ThreadCount"]/td[2]/text()').extract()
        item['base_freq'] = response.xpath('.//*[@id="ClockSpeed"]/td[2]/text()').extract()
        item['max_freq'] = response.xpath('.//*[@id="ClockSpeedMax"]/td[2]/text()').extract()
        item['tdp'] = response.xpath('.//*[@id="MaxTDP"]/td[2]/text()').extract()
        item['mem_types'] = response.xpath('.//*[@id="MemoryTypes"]/td[2]/text()').extract()
        item['max_mem_channels'] = response.xpath('.//*[@id="NumMemoryChannels"]/td[2]/text()').extract()
        # item['max_mem_bandwidth'] = response.xpath().extract()
        item['ECC'] = response.xpath('.//*[@id="ECCMemory"]/td[2]/span/text()').extract()
        item['processor_graphics'] = response.xpath('.//*[@id="GraphicsModel"]/td[2]/text()').extract()
        # item['graph_base_freq'] = response.xpath().extract()
        # item['graph_max_dyn_freq'] = response.xpath().extract()
        # item['graph_max_mem'] = response.xpath().extract()
        # item['pcie_revision'] = response.xpath().extract()
        # item['max_pcie_lanes'] = response.xpath().extract()
        # item['pcie_config'] = response.xpath().extract()
        # item['socket'] = response.xpath().extract()
        yield item


