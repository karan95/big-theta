# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from py2neo import Graph
from py2neo import Node
from py2neo import Relationship

from scrapy.exporters import PprintItemExporter
from scrapy import signals
from scrapy import Spider

class EquationscraperPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


    def spider_opened(self, spider):
        file = open('%s_items' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = PprintItemExporter(file)
        self.exporter.start_exporting()


    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item