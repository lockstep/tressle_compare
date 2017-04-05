from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class ProductInfoItem(PortiaItem):
    tertiary_category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    secondary_category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    color = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    ratings_count = scrapy.Field(
        input_processor=Number(),
        output_processor=Join(),
    )
    sku = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    menufacturer = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    name = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    original_price = scrapy.Field(
        input_processor=Price(),
        output_processor=Join(),
    )
    current_price = scrapy.Field(
        input_processor=Price(),
        output_processor=Join(),
    )
    primary_category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    rating = scrapy.Field(
        input_processor=Number(),
        output_processor=Join(),
    )
    material = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    primary_image_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class HomeProductAItem(PortiaItem):
    current_price_max = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    secondary_category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    manufacturer = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    sku = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    current_price_min = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    brand = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    dimensions = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    ratings_count = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    primary_image_url = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    original_price = scrapy.Field(
        input_processor=Price(),
        output_processor=Join(),
    )
    tertiary_category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    rating_count = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    current_price = scrapy.Field(
        input_processor=Price(),
        output_processor=Join(),
    )
    name = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    material = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    primary_category = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    rating = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    average_rating = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    color = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
