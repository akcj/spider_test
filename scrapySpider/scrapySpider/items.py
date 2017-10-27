# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiuxiaowoItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()

class WymusicItem(scrapy.Item):
    ranking = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
