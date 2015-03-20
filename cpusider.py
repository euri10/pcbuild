__author__ = 'euri10'

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

from scrapy import Request

class CPUSpider(CrawlSpider):


    name = ''
    allowed_domains = ['ark.intel.com']
    start_urls = ['http://ark.intel.com/#@Processors']

    rules = (
            Rule(LxmlLinkExtractor(allow_domains=allowed_domains,
                                   restrict_xpaths='.//*[@id="Processors-DesktopProcessors-scrollpane"]/table/tbody/*/*/a',
                                   process_value=None), callback='parse_cpu_page'),
        )

    def parse_cpu_page(self, response):
        url_cpu = response.xpath('.//*[@id="tabs-Desktop"]/table/tbody/tr[*]/td[2]/a')
        for cpu in url_cpu:
            yield Request(cpu, callback=self.parse_cpu)

    def parse_cpu(self, response):

        item = CPUscrapy()
        item['processor'] = response.xpath('.//*[@id="ProcessorNumber"]/td[2]')
        yield item


