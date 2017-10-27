# -*- coding: utf-8 -*-

import scrapy
from scrapySpider.items import XiuxiaowoItem


class XiuxiaowoSpider(scrapy.Spider):
    name = 'xiuxiaowo'
    allowed_domains = ['www.xiuxiaowo.com']
    start_urls = ['https://www.xiuxiaowo.com/']

    def parse(self, response):
        items = []
        for each in response.xpath("//div[@class='caption']"):
            item = XiuxiaowoItem()
            title = each.xpath("div[@class='title']//a/text()").extract()
            author = each.xpath("div[@class='author']//a/text()").extract()

            item['title'] = title[0]
            item['author'] = author[0]
           
            if item not in items:
                items.append(item)

        return items