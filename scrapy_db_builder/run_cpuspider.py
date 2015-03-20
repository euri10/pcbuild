__author__ = 'lotso'
from scrapy import cmdline
#cmdline.execute("scrapy crawl togspider".split())
cmdline.execute("scrapy crawl cpuspider -o items.json".split())
#cmdline.execute("scrapy shell http://www.lecture-en-ligne.com/manga/towerofgod/".split())
