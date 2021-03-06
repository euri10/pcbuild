# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_db_builder project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_db_builder'

SPIDER_MODULES = ['scrapy_db_builder.spiders']
NEWSPIDER_MODULE = 'scrapy_db_builder.spiders'
DOWNLOADER_MIDDLEWARES = {'scrapy_db_builder.middlewares.ProxyMiddleware': 1}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_db_builder (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'scrapy_db_builder.pipelines.cpuIntelPipeline': 300,
    'scrapy_db_builder.pipelines.intoSQLPipeline': 400,
}


