from __future__ import absolute_import

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.processors import Item, Field, Text, Number, Price, Url, Image, Regex
from ..items import HomeProductItem


class Hayneedle(BasePortiaSpider):
    name = "hayneedle"
    # To test against local files uncomment the following, comment out
    # the allowed domains, and use the terminal command: scrapy crawl hayneedle
    # base_path = 'file:///Users/oeam/projects/tressle_compare/tressle_bot/lib/samples'
    # start_urls = [
    #     base_path + '/hayneedle-1.html'
    # ]

    allowed_domains = [u'www.hayneedle.com']
    start_urls = [
        u'http://www.hayneedle.com/furniture/sofas-sectionals_501782',
        u'http://www.hayneedle.com/lighting/outdoor-wall-lights_list_188100?categoryId=188100&selectedFacets=&page=1&sortBy=customerRating%3Adesc&checkCache=true&pageType=PRODUCT_CATEGORY&view=48',
        u'http://www.hayneedle.com/outdoor/conversation-patio-sets_list_181973?categoryId=181973&selectedFacets=&page=1&sortBy=preferred%3Adesc&checkCache=true&pageType=PRODUCT_CATEGORY&view=48',
        u'http://www.hayneedle.com/outdoor/dining-patio-sets_list_181974',
        u'http://www.hayneedle.com/outdoor/conversation-patio-sets_list_181973',
        u'http://www.hayneedle.com/outdoor/outdoor-furniture-collections_category-adirondack-chairs_list_500180_169019?categoryId=500180&selectedFacets=&page=1&sortBy=&checkCache=true&pageType=COLLECTION_CATEGORY&view=24'
    ]
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'product', u'collections'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                HomeProductItem,
                None,
                u'#app-container',
                [
                    Field(
                        u'primary_image',
                        u'.content-container > product-page-image-desktop > div > img::attr(src)',
                        []),
                    Field(
                        u'primary_category',
                        u'.breadcrumbs > .container > a:nth-child(3) *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.breadcrumbs > .container > a:nth-child(5) *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.breadcrumbs > div > span.text-small > a *::text',
                        []),
                    Field(
                        u'current_price',
                        u'#product-page-container .display-price-container.label > div *::text',
                        []),
                    Field(
                        u'original_price',
                        u'#product-page-container .list-price-container > div.list-price > span *::text',
                        []),
                    Field(
                        u'name',
                        u'.title-container > view > h1 *::text',
                        []),
                    Field(
                        u'sku',
                        u'.sku-display > span:nth-child(2) *::text',
                        []),
                    Field(
                        u'description',
                        u'.desc-section .desc-html p *::text',
                        []),
                    Field(
                        u'average_rating',
                        u'.pr-snapshot-rating.rating > span *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.pr-snapshot-rating.rating > p > span *::text',
                        [])])]]
