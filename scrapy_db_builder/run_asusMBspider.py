__author__ = 'lotso'
from scrapy import cmdline

# cmdline.execute("scrapy crawl asusMBspider -o asusMB.json".split())
cmdline.execute("scrapy shell http://www.asus.com/Motherboards/Intel_Platform_Products/".split())
