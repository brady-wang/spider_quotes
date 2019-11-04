# -*- coding: utf-8 -*-
import scrapy


from quotes.items import QuotesItem

class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print("爬取页面 "+ response.url)
        content_list = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').extract()
        auth_list = response.xpath('//div[@class="quote"]//small[@class="author"]/text()').extract()
        item = QuotesItem()
        for i,j in zip(auth_list,content_list):
            item['author'] = i
            item['content'] = eval(j)
            yield item



