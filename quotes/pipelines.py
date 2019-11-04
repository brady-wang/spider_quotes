# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QuotesPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='xx', user='root', passwd='xx', db='spider', charset='utf8')
        self.cur = self.conn.cursor()

    def open_spider(self,spider):
        print('spider start')

    def process_item(self, item, spider):

        try:
            import time
            # 格式化成2016-03-20 11:45:39形式
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sql = "insert ignore  into test(author,content,created_at) values('{}','{}','{}')".format(item['author'],item['content'],now)
            reCount = self.cur.execute(sql)
            self.conn.commit()
        except Exception as  e:
            print(str(e))

        return item
