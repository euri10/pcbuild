__author__ = 'lotso'
from scrapy import cmdline

cmdline.execute("scrapy crawl cpuspider -o cpu.json".split())
# cmdline.execute("scrapy shell http://ark.intel.com/search/advanced?s=t".split())
