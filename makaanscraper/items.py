# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MakaanscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Makaanscrape(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_sufix = scrapy.Field()
    per_area_price = scrapy.Field()
    area = scrapy.Field()
    area_sufix = scrapy.Field()
    status =scrapy.Field()