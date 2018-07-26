# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags



def lower_case(value):
    newValue = []
    if( isinstance(value, list) ):
        for word in value:
            newValue.append(word.lower())
        return newValue
    else:
        return value            
                

        

class TibiabooksItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    location = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    author = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    shortDescription = scrapy.Field(input_processor=lower_case, output_processor=TakeFirst())
    text = scrapy.Field(input_processor=lower_case, output_processor=Join())
