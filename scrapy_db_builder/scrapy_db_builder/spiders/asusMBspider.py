
__author__ = 'euri10'

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy_db_builder.scrapy_db_builder.items import asusMBitem


class asusMBSpider(CrawlSpider):
    name = 'asusMBSpider'
    allowed_domains = ['asus.com']
    start_urls = ['http://www.asus.com/Motherboards/AllProducts/']

    rules = (
        Rule(LxmlLinkExtractor(allow_domains=allowed_domains,
                               restrict_xpaths='.//*[contains(@id,"sh*")]/table/tbody/tr/td/ul/li[*]/a',
                               process_value=None), callback='parse_mb'),
    )

    def parse_mb(self, response):
        item = asusMBitem()

