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


class Hayneedle(BasePortiaSpider):
    name = "www.hayneedle.com"
    allowed_domains = [u'www.hayneedle.com']
    start_urls = [
        u'http://www.hayneedle.com/furniture/sofas-sectionals_501782',
        u'http://www.hayneedle.com/lighting/outdoor-wall-lights_list_188100?categoryId=188100&selectedFacets=&page=1&sortBy=customerRating%3Adesc&checkCache=true&pageType=PRODUCT_CATEGORY&view=48',
        u'http://www.hayneedle.com/outdoor/conversation-patio-sets_list_181973?categoryId=181973&selectedFacets=&page=1&sortBy=preferred%3Adesc&checkCache=true&pageType=PRODUCT_CATEGORY&view=48',
        u'http://www.hayneedle.com/outdoor/dining-patio-sets_list_181974',
        u'http://www.hayneedle.com/outdoor/conversation-patio-sets_list_181973',
        u'http://www.hayneedle.com/outdoor/outdoor-furniture-collections_category-adirondack-chairs_list_500180_169019?categoryId=500180&selectedFacets=&page=1&sortBy=&checkCache=true&pageType=COLLECTION_CATEGORY&view=24']
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
    items = [[]]
