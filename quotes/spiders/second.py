# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from quotes.items import QuotesItem

class SecondSpider(CrawlSpider):
    name = 'second'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("爬取页面 " + response.url)
        content_list = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').extract()
        auth_list = response.xpath('//div[@class="quote"]//small[@class="author"]/text()').extract()
        item = QuotesItem()
        for i, j in zip(auth_list, content_list):
            item['author'] = i
            item['content'] = eval(j)
            yield item
