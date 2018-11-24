# -*- coding: utf-8 -*-
import scrapy
import re
from liu.items import LiuItem
from scrapy.crawler import CrawlerProcess
class PiSpider(scrapy.Spider):
    name = 'hhh'
    allowed_domains = ['14epep.com']
    offset = 396870
    base_url = 'http://www.14epep.com/arts/'
    start_urls = [base_url+str(offset)]
    k=0
    def parse(self, response):
        content = response.text
        tp = re.compile(r'src.+?"(.+?jpg)"')
        data = re.findall(tp,content)
        if not data:
            return
        for i in data:              
            item = LiuItem()
            item['name']=k
            item['image_urls'] = str(i)
            k+=1
            yield item
        if self.offset < 396873:
            self.offset+=1
            yield scrapy.Request('http://www.14epep.com/arts/'+str(self.offset))

