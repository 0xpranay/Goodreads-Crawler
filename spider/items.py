# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,Join,TakeFirst
from w3lib.html import remove_tags

def remove_quotations(word):
    return word.replace(u"\u201d", ' ').replace(u"\u201c", ' ')
def remove_spaces(author_value):
    return author_value[5:-2].strip('\n')


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field(
        input_processor = MapCompose(str.strip , remove_quotations),
        output_processor = TakeFirst()
    )
    author = scrapy.Field(
        input_processor = MapCompose(remove_tags , remove_spaces),
        output_processor = TakeFirst()
    )
    tags = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(',')
    )
    pass
