from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Url, Image, Regex
from ..items import PortiaItem


class Worldmarket(BasePortiaSpider):
    name = "www.worldmarket.com"
    allowed_domains = [u'www.worldmarket.com']
    start_urls = [
        u'https://www.worldmarket.com/category/furniture.do',
        u'https://www.worldmarket.com/category/outdoor.do',
        u'https://www.worldmarket.com/category/rugs-curtains.do',
        u'https://www.worldmarket.com/category/lighting.do',
        u'https://www.worldmarket.com/category/home-decor-pillows.do',
        u'https://www.worldmarket.com/category/bed-bath.do',
        u'https://www.worldmarket.com/category/dining.do',
        u'https://www.worldmarket.com/category/kitchen.do',
        u'https://www.worldmarket.com/category/food-and-drink.do']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.ml-body-wrapper',
                [
                    Field(
                        u'primary_category',
                        u'.breadcrumb > li:nth-child(2) > a::attr(href)',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumb > li:nth-child(3) > a::attr(href)',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.breadcrumb > li:nth-child(4) > a::attr(href)',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-image > div > .ml-product-alt-ii-container > .ml-product-alt-detailimgcontainer > .detailImage > a > .cloudzoom::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-info > .ml-product-name > div > h1 *::text',
                        []),
                    Field(
                        u'sku',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-info > span > .ml-product-code *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-info > .ml-product-pricing > .ml-product-tableitem > .productPricing > .ml-item-price *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.ml-body-wrapper',
                [
                    Field(
                        u'primary_category',
                        u'.breadcrumb > li:nth-child(2) > a::attr(href)',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumb > li:nth-child(3) > a::attr(href)',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.breadcrumb > li:nth-child(4) > a::attr(href)',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-image > div > .ml-product-alt-ii-container > .ml-product-alt-detailimgcontainer > .detailImage > a > .cloudzoom::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-info > .ml-product-name > div > h1 *::text',
                        []),
                    Field(
                        u'sku',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-info > span > .ml-product-code *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.ml-product-wrapper > span > .mainForm > .ml-product-detail > .ml-product-detail-wrapper > .ml-product-alt-detail-info > .ml-product-pricing > .ml-product-tableitem > .productPricing > .ml-item-price *::text',
                        [])])]]
