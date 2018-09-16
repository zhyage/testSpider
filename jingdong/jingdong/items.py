# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    ID = scrapy.Field() #product ID
    name = scrapy.Field() #product name
    comment = scrapy.Field() #comments people number
    shopName = scrapy.Field() # shop name
    price = scrapy.Field() # price
    link = scrapy.Field() #link
    commentsNum = scrapy.Field()
    score1Count = scrapy.Field() # comment as one
    score2Count = scrapy.Field()
    score3Count = scrapy.Field()
    score4Count = scrapy.Field()
    score5Count = scrapy.Field()
