# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    houseName = scrapy.Field() # the house's name
	houseType = scrapy.Field() # like "三室一厅"
	houseSize = scrapy.Field() # like "155m2"
	houseFloor = scrapy.Field() # like "中层（共11层）"
    houseConstructionTime = scrapy.Field() # like "2015"
	houseAddress = scrapy.Field() # 
	houseTags = scrapy.Field()
	detPrice = scrapy.Field()
	unitPrice = scrapy.Field()
	# 这是今天的演示代码
	pass
