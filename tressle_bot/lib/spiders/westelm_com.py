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


class Westelm(BasePortiaSpider):
    name = "www.westelm.com"
    allowed_domains = [u'www.westelm.com']
    start_urls = [u'http://www.westelm.com/',
                  u'http://www.westelm.com/shop/furniture/',
                  u'http://www.westelm.com/shop/outdoor/',
                  u'http://www.westelm.com/shop/rugs-windows/',
                  u'http://www.westelm.com/shop/bedding/',
                  u'http://www.westelm.com/shop/lighting/',
                  u'http://www.westelm.com/shop/accessories-pillows/',
                  u'http://www.westelm.com/shop/wall-decor-mirrors/',
                  u'http://www.westelm.com/shop/dining-kitchen/',
                  u'http://www.westelm.com/shop/sale/',
                  {u'url': u'http://',
                   u'fragments': [{u'type': u'fixed',
                                   u'value': u'http://'}],
                   u'type': u'generated'}]
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
                u'.main-content',
                [
                    Field(
                        u'primary_category',
                        u'.breadcrumb-list > li:nth-child(2) > a > span *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumb-list > li:nth-child(3) > a > span *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.purchasing-container > .pip-media > .image-container > .hero-container > .hero-image > .overlayTrigger > img::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.purchasing-container > .pip-info > .pip-summary > h1 *::text',
                        []),
                    Field(
                        u'current_price_min',
                        u'.purchasing-container > .pip-info > .pip-summary > .simple-subset > .subset-section > .product-subset > .subset-skus > .subset-selection > .subset-pricing > .product-price > .price-state > span:nth-child(1) > .price-amount *::text',
                        []),
                    Field(
                        u'current_price_max',
                        u'.purchasing-container > .pip-info > .pip-summary > .simple-subset > .subset-section > .product-subset > .subset-skus > .subset-selection > .subset-pricing > .product-price > .price-state > span:nth-child(2) > .price-amount *::text',
                        []),
                    Field(
                        u'description',
                        u'.purchasing-container > .pip-info > .pip-summary > .accordion-component > dd.active > .accordion-contents > .accordion-tab-copy > p:nth-child(1) *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.main-content',
                [
                    Field(
                        u'primary_category',
                        u'.breadcrumb-list > li:nth-child(2) > a > span *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumb-list > li:nth-child(3) > a > span *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.breadcrumb-list > li:nth-child(4) > a > span *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.purchasing-container > .pip-media > .image-container > .hero-container > .hero-image > .overlayTrigger > img::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.purchasing-container > .pip-info > .pip-summary > h1 *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.purchasing-container > .pip-info > .pip-summary > .product-subset > .subset-selection > .guided-pip > .price-details > .finalContainer > .product-price > .price-state > .currency > .price-amount *::text',
                        []),
                    Field(
                        u'description',
                        u'.guided-pip-content > .accordion-component > dd.active > .accordion-contents > .accordion-tab-copy > p:nth-child(1) *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.main-content',
                [
                    Field(
                        u'primary_category',
                        u'.breadcrumb-list > li:nth-child(2) > a > span *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumb-list > li:nth-child(3) > a > span *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.breadcrumb-list > li:nth-child(4) > a > span *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.purchasing-container > .pip-media > .image-container > .hero-container > .hero-image > .overlayTrigger > img::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.purchasing-container > .pip-info > .pip-summary > h1 *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.purchasing-container > .pip-info > .pip-summary > .simple-subset > .subset-section > .product-subset > .subset-skus > .subset-selection > .subset-pricing > .product-price > .price-state *::text',
                        []),
                    Field(
                        u'description',
                        u'.purchasing-container > .pip-info > .pip-summary > .accordion-component > dd.active > .accordion-contents > .accordion-tab-copy > p:nth-child(1) *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.main-content',
                [
                    Field(
                        u'primary_category',
                        u'.breadcrumb-list > li:nth-child(2) > a > span *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumb-list > li:nth-child(3) > a > span *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.purchasing-container > .pip-media > .image-container > .hero-container > .hero-image > .overlayTrigger > img::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.purchasing-container > .pip-info > .pip-summary > h1 *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.purchasing-container > .pip-info > .pip-summary > .simple-subset > .subset-section > .product-subset > .subset-skus > .subset-selection > .subset-pricing > .product-price > .price-state *::text',
                        []),
                    Field(
                        u'description',
                        u'.purchasing-container > .pip-info > .pip-summary > .accordion-component > dd.active > .accordion-contents > .accordion-tab-copy > p:nth-child(1) *::text',
                        [])])]]
