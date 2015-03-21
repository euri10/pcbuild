__author__ = 'lotso'
from scrapy import cmdline

cmdline.execute("scrapy crawl cpuspider".split())
#cmdline.execute("scrapy shell http://ark.intel.com/search/advanced?s=t".split())
