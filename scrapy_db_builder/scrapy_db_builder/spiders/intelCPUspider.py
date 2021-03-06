import urlparse
from scrapy_db_builder.scrapy_db_builder.items import intelCPUitem
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

from scrapy import Request


class intelCPUSpider(CrawlSpider):
    name = 'intelCPUSpider'
    allowed_domains = ['ark.intel.com']
    start_urls = ['http://ark.intel.com/#@Processors']

    rules = (
        Rule(LxmlLinkExtractor(allow_domains=allowed_domains,
                               restrict_xpaths='.//*[@id="Processors-DesktopProcessors-scrollpane"]/table/tbody/tr[*]/td[*]/a',
                               process_value=None), callback='parse_desktop_submenu'),
    )

    def parse_desktop_submenu(self, response):
        urllist = response.xpath('.//*[@id="tabs-Desktop"]/table/tbody/tr[*]/td[2]/a/@href').extract()
        for url in urllist:
            yield Request(urlparse.urljoin('http://ark.intel.com', url), callback=self.parse_cpu_page)


    def parse_cpu_page(self, response):
        item = intelCPUitem()
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
        item['max_mem_bandwidth'] = response.xpath('.//*[@id="MaxMemoryBandwidth"]/td[2]/text()').extract()
        item['ECC'] = response.xpath('.//*[@id="ECCMemory"]/td[2]/span/text()').extract()
        item['processor_graphics'] = response.xpath('.//*[@id="GraphicsModel"]/td[2]/text()').extract()
        item['graph_base_freq'] = response.xpath('.//*[@id="GraphicsFreq"]/td[2]/text()').extract()
        item['graph_max_dyn_freq'] = response.xpath('.//*[@id="GraphicsMaxFreq"]/td[2]/text()').extract()
        item['pcie_revision'] = response.xpath('.//*[@id="PCIExpressRevision"]/td[2]/text()').extract()
        item['max_pcie_lanes'] = response.xpath('.//*[@id="NumPCIExpressPorts"]/td[2]/text()').extract()
        item['pcie_config'] = response.xpath('.//*[@id="PCIExpressConfigs"]/td[2]/text()').extract()
        item['socket'] = response.xpath('.//*[@id="SocketsSupported"]/td[2]/text()').extract()
        item['link'] = response.url
        yield item


