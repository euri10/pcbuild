# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from scrapy.exceptions import DropItem
import re
from app import models
from config import SQLALCHEMY_DATABASE_URI


class cpuIntelPipeline(object):

    """ take item created from scrapy parser and put them in the right shape so that it can be inserted
    in the database easily
    """

    def process_item(self, item, spider):

        # this is intel cpu, brand id is 1

        for k in item.keys():
            if k != 'link':
                if len(item[k]):
                    item[k] = item[k][0]
                else:
                    item[k] = None

        item['cpubrand_id'] = 1

        # process string only
        for label in ['ECC', 'mem_types', 'processor_graphics', 'pcie_revision', 'pcie_config', 'socket']:
            print label
            if item[label] is not None:
                item[label] = unicode(item[label])

        if re.match(r"(.*)-(.*)", item['processor']):
            m = re.match(r"(.*)-(.*)", item['processor'])
            item['processor_name'] = m.group(1)
            item['processor_type'] = m.group(2)
            item['processor'] = item['processor']

        # process int or float and unit
        for label in ['cache', 'lithography', 'base_freq', 'max_freq', 'tdp', 'max_mem_bandwidth', 'graph_base_freq',
                      'graph_max_dyn_freq']:
            print label
            if item[label] is not None:
                if re.match(r"(\d+(.\d+)?) (.*)", item[label]):
                    m = re.match(r"(\d+(.\d+)?) (.*)", item[label])
                    item[label] = float(m.group(1))
                    labelu = label + '_u'
                    item[labelu] = m.group(3)

        # process int only
        for label in ['cores', 'thread', 'max_mem_channels', 'max_pcie_lanes']:
            print label
            if item[label] is not None:
                item[label] = int(item[label])

        return item



class intoSQLPipeline(object):
    """ this serves as a pipeline into the database

    """

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

        """Save cpu in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        cpu = models.CPU(**item)

        try:
            session.add(cpu)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
