from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Crateandbarrel(BasePortiaSpider):
    name = "www.crateandbarrel.com"
    allowed_domains = [u'www.crateandbarrel.com']
    start_urls = [
        u'https://www.crateandbarrel.com/furniture/',
        u'https://www.crateandbarrel.com/outdoor-furniture/',
        u'https://www.crateandbarrel.com/dining-and-entertaining/',
        u'https://www.crateandbarrel.com/kitchen-and-food/',
        u'https://www.crateandbarrel.com/decorating-and-accessories/',
        u'https://www.crateandbarrel.com/rugs-and-curtains/',
        u'https://www.crateandbarrel.com/lighting/',
        u'https://www.crateandbarrel.com/bed-and-bath/',
        u'https://www.crateandbarrel.com/organizing-and-storage/']
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
                u'#bodyWrap',
                [
                    Field(
                        u'primary_category',
                        u'div:nth-child(4) > div > span:nth-child(3) > a::attr(href)',
                        []),
                    Field(
                        u'secondary_category',
                        u'div:nth-child(4) > div > span:nth-child(5) > a::attr(href)',
                        []),
                    Field(
                        u'tertiary_category',
                        u'div:nth-child(4) > div > span:nth-child(7) > a::attr(href)',
                        []),
                    Field(
                        u'name',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > div:nth-child(4) > .html5 > fieldset > .jsFormContent > .shoppingBar > .productHeader *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > div:nth-child(4) > .html5 > fieldset > .jsFormContent > .shoppingBar > .productReviewPrice > .productPrice > .reg > .regPrice *::text',
                        []),
                    Field(
                        u'sku',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > div:nth-child(4) > .html5 > fieldset > .jsFormContent > .shoppingBar > .sku *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > div:nth-child(4) > .html5 > fieldset > .jsFormContent > .divProductCarousel > .jcarousel-container > .jcarousel-clip > .productCarousel > .jsActivePinItItem > .jsZoomLarge::attr(src)',
                        []),
                    Field(
                        u'description',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > div:nth-child(4) > .html5 > fieldset > .jsFormContent > .productPageSection > .productDescription *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'#bodyWrap',
                [
                    Field(
                        u'primary_category',
                        u'div:nth-child(4) > div > span:nth-child(3) > a::attr(href)',
                        []),
                    Field(
                        u'secondary_category',
                        u'div:nth-child(4) > div > span:nth-child(5) > a::attr(href)',
                        []),
                    Field(
                        u'tertiary_category',
                        u'div:nth-child(4) > div > span:nth-child(7) > a::attr(href)',
                        []),
                    Field(
                        u'name',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .shoppingBar > .productHeader *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .shoppingBar > .productReviewPrice > .productPrice > .sale > .salePrice *::text',
                        []),
                    Field(
                        u'original_price',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .shoppingBar > .productReviewPrice > .productPrice > .sale > .regPrice *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .hwProductPgTop > .zoomControl > .productImageWrap > .jsZoomLarge::attr(src)',
                        []),
                    Field(
                        u'description',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .hwProductPgTop > .hwRightDetail > div:nth-child(1) > .mT20 > .mB0 *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'#bodyWrap',
                [
                    Field(
                        u'primary_category',
                        u'div:nth-child(4) > div > span:nth-child(3) > a::attr(href)',
                        []),
                    Field(
                        u'secondary_category',
                        u'div:nth-child(4) > div > span:nth-child(5) > a::attr(href)',
                        []),
                    Field(
                        u'tertiary_category',
                        u'div:nth-child(4) > div > span:nth-child(7) > a::attr(href)',
                        []),
                    Field(
                        u'name',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .shoppingBar > .productHeader *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .shoppingBar > .productReviewPrice > .productPrice > .reg > .regPrice *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .divProductCarousel > .jcarousel-container > .jcarousel-clip > .productCarousel > .jsActivePinItItem > .jsZoomLarge::attr(src)',
                        []),
                    Field(
                        u'description',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .sectionDescription > .productDescription *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'#bodyWrap',
                [
                    Field(
                        u'primary_category',
                        u'div:nth-child(4) > div > span:nth-child(3) > a::attr(href)',
                        []),
                    Field(
                        u'secondary_category',
                        u'div:nth-child(4) > div > span:nth-child(5) > a::attr(href)',
                        []),
                    Field(
                        u'tertiary_category',
                        u'div:nth-child(4) > div > span:nth-child(7) > a::attr(href)',
                        []),
                    Field(
                        u'name',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .hwProductPage > .html5 > fieldset > .jsFormContent > .shoppingBar > .productHeader *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .hwProductPage > .html5 > fieldset > .jsFormContent > .shoppingBar > .productReviewPrice > .productPrice > .reg > .regPrice *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .hwProductPage > .html5 > fieldset > .jsFormContent > .hw-product-top > div:nth-child(1) > .zoomControl > .productImageWrap > .jsZoomLarge::attr(src)',
                        []),
                    Field(
                        u'description',
                        u'.jsGrowlContainer > .content > div:nth-child(2) > .hwProductPage > .html5 > fieldset > .jsFormContent > .hw-product-top > .hwRightDetail > .tabs > .hwOverview > .content > p *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.jsPIPItem > fieldset > .jsFormContent',
                [
                    Field(
                        u'name',
                        u'.shoppingBar > .productHeader *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.shoppingBar > .productReviewPrice > .productPrice > .reg > .regPrice *::text',
                        []),
                    Field(
                        u'color',
                        u'.shoppingBar > .shoppingBarSwatchArea > .shoppingBarSwatchInfo > span:nth-child(2) > .jsColor *::text',
                        []),
                    Field(
                        u'sku',
                        u'.shoppingBar > .shoppingBarSwatchArea > .shoppingBarSwatchInfo > .sku *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.divProductCarousel > .jcarousel-container > .jcarousel-clip > .productCarousel > .jsActivePinItItem > .jsZoomLarge::attr(src)',
                        []),
                    Field(
                        u'description',
                        u'.productPageSection > .productDescription *::text',
                        [])])]]
