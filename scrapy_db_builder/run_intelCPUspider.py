__author__ = 'lotso'
from scrapy import cmdline

cmdline.execute("scrapy crawl intelCPUSpider -o intelCPU.json".split())
# cmdline.execute("scrapy shell http://ark.intel.com/search/advanced?s=t".split())
