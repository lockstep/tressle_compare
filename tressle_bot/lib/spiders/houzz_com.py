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


class Houzz(BasePortiaSpider):
    name = "houzz"
    # To test against local files uncomment the following, comment out
    # the allowed domains, change the allow rule to 'file', follow to False,
    # and use the terminal command: scrapy crawl wayfair
    # base_path = 'file:///Users/Bird/Tripler/tressle_compare/tressle_bot/lib/samples'
    # start_urls = [
    #     base_path + '/houzz-1.html'
    # ]

    allowed_domains = [u'www.houzz.com']
    start_urls = [
        u'http://www.houzz.com/photos/furniture',
        u'http://www.houzz.com/photos/lighting',
        u'http://www.houzz.com/photos/home-decor',
        u'http://www.houzz.com/photos/kitchen-and-dining',
        u'http://www.houzz.com/photos/bath-products',
        u'http://www.houzz.com/photos/bedroom-products',
        u'http://www.houzz.com/photos/storage-and-organization',
        u'http://www.houzz.com/photos/home-improvement',
        u'http://www.houzz.com/photos/outdoor-products',
        u'http://www.houzz.com/photos/baby-and-kids',
        u'http://www.houzz.com/photos/housekeeping-and-laundry',
        u'http://www.houzz.com/photos/holiday-decorations',
        u'http://www.houzz.com/photos/pet-supplies',
    ]

    rules = [
        Rule(
            LinkExtractor(
                allow=(u'photos\/\d+\/'),
                deny=()
            ),
            callback='parse_item',
            follow=True,
        ),
        Rule(
            LinkExtractor(
                allow=(u'photos\/[a-zA-Z]+'),
                deny=()
            )
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'#mainContent',
                [
                    Field(
                        u'name',
                        u'.rightSideBarWide > .marketplace > div > .productTitle > .header-1 *::text',
                        [],
                        True),
                    Field(
                        u'description',
                        u'.rightSideBarWide > .marketplace > div > .detailBox > .description *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.leftSideContentNarrow > .spaceContent > .viewSpaceImage > .mainImageWrap > .viewImage::attr(src)',
                        []),
                    Field(
                        u'manufacturer',
                        u"//script[contains(., 'manuName')]/text()",
                        [Regex('manuName":"(.*?)"')]),
                    Field(
                        u'manufacturer_sku',
                        u"//script[contains(., 'sku')]/text()",
                        [Regex('sku":"(.*?)"')]),
                    Field(
                        u'primary_category',
                        u'.leftSideContentNarrow > .navigationTopicBreadcrumbs > .breadcrumb > li:nth-child(3) > .breadcrumb-item-link > span *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.leftSideContentNarrow > .navigationTopicBreadcrumbs > .breadcrumb > li:nth-child(5) > .breadcrumb-item-link > span *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.leftSideContentNarrow > .navigationTopicBreadcrumbs > .breadcrumb > li:nth-child(7) > .breadcrumb-item-link > span *::text',
                        []),
                    Field(
                        u'average_rating',
                        u'.review-avg::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.leftSideContentNarrow > .spaceContent > .product-reviews > .clearfix > .clearfix > .reviews-count > span *::text',
                        []),
                    Field(
                        u'original_price',
                        u'.rightSideBarWide > .marketplace > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .text-m *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.rightSideBarWide > .marketplace > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .product-price *::text',
                        [],
                        False)
                ]
            )
        ]
    ]

