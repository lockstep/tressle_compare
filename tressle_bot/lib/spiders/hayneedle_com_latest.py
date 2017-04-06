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


class HayneedleComLatest(BasePortiaSpider):
    name = "www.hayneedle.com_latest"
    allowed_domains = [u'www.hayneedle.com']
    start_urls = [u'http://www.hayneedle.com/']
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
    items = []
