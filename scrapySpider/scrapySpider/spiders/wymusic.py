# -*- coding: utf-8 -*-
import scrapy
from scrapySpider.items import WymusicItem

class WymusicSpider(scrapy.Spider):
    name = 'wymusic'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/#/discover/toplist?id=3779629']

    def parse(self, response):
        pass
        # items = []
        # for each in response.xpath("//tbody//tr"):
        #     item = XiuxiaowoItem()
        #     title = each.xpath('td')[0].xpath('div[@class="hd"]//span[@class="num"]/text()').extract()
        #     author = each.xpath("div[@class='author']//a/text()").extract()

        #     item['title'] = title[0]
        #     item['author'] = author[0]
           
        #     if item not in items:
        #         items.append(item)

        # return items