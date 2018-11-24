# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy import settings
class LiuPipeline(object):
    IMAGES_STORE=r'F:\刘畅\学习\html\tp'
    def process_item(self, item, spider):
        #item['image_paths'] = self.IMAGES_STORE+"/"+item['name']+".jpg"
        file_name = os.path.join(self.IMAGES_STORE,item['name']+'.jpg')
        with open(file_name,'wb') as fp:
            fp.write(res.read())
