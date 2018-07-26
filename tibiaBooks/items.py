# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


def lower_case(value):
    if( isinstance(value[0], str) ):
        return value[0].lower()
    else:
        return value[0]
        pass    

class TibiabooksItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    name = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    location = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    author = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    shortDescription = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    text = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
