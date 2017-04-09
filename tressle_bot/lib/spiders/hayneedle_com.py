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
    #     base_path + '/hayneedle-1.html',
    #     base_path + '/hayneedle-2.html'
    # ]

    allowed_domains = [u'www.hayneedle.com']
    start_urls = [
        u'http://www.hayneedle.com/baby-and-kids/',
        u'http://www.hayneedle.com/bathroom/',
        u'http://www.hayneedle.com/bed-and-bath/',
        u'http://www.hayneedle.com/bedroom/',
        u'http://www.hayneedle.com/accents-and-decor/',
        u'http://www.hayneedle.com/dining-room/',
        u'http://www.hayneedle.com/dorm-life/',
        u'http://www.hayneedle.com/entryway/',
        u'http://www.hayneedle.com/fan-gear/',
        u'http://www.hayneedle.com/apparel/',
        u'http://www.hayneedle.com/front-porch/',
        u'http://www.hayneedle.com/furniture/',
        u'http://www.hayneedle.com/game-room-&-bar/',
        u'http://www.hayneedle.com/games-and-hobbies/',
        u'http://www.hayneedle.com/garage/',
        u'http://www.hayneedle.com/gifts/',
        u'http://www.hayneedle.com/home-gym/',
        u'http://www.hayneedle.com/home-improvement-and-maintenance/',
        u'http://www.hayneedle.com/home-office/',
        u'http://www.hayneedle.com/kitchen/',
        u'http://www.hayneedle.com/kitchen-and-dining/',
        u'http://www.hayneedle.com/laundry-room/',
        u'http://www.hayneedle.com/lighting/',
        u'http://www.hayneedle.com/living-room/',
        u'http://www.hayneedle.com/nursery/',
        u'http://www.hayneedle.com/outdoor/',
        u'http://www.hayneedle.com/pets/',
        u'http://www.hayneedle.com/playroom/',
        u'http://www.hayneedle.com/seasonal/',
        u'http://www.hayneedle.com/sports-and-fitness/',
        u'http://www.hayneedle.com/storage-and-organization/',
        u'http://www.hayneedle.com/on-sale/'
    ]
    rules = [
        Rule(
            LinkExtractor(
                allow=('product', '_\d{6}'),
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
                        u'manufacturer',
                        u"//script[contains(., 'brand')]/text()",
                        [Regex('"brand":(.*?),')]), #need to remove "" when importing data
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
