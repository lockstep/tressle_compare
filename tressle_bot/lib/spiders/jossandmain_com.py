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


class Jossandmain(BasePortiaSpider):
    name = "www.jossandmain.com"
    allowed_domains = [u'www.jossandmain.com']
    start_urls = [
        u'https://www.jossandmain.com/Blair-Rug-ASTG4325.html',
        u'https://www.jossandmain.com/Graham-76-Sofa-MCRR1218.html?piid%5B0%5D=14310059']
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
                u'#pd',
                [
                    Field(
                        u'primary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(1) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(2) > .Breadcrumbs-item *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.clearfix > .ProductDetailImagesBlock > .mainpdimg > .ProductDetailImagesBlock-carouselWrap > .ProductDetailImagesBlock-carousel > .js-slider-container > div:nth-child(1) > .ProductDetailImagesBlock-carousel-link > .ProductDetailImagesBlock-carousel-image::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .ProductDetailInfoBlock-header > .ProductDetailInfoBlock-header-title *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .ProductDetailInfoBlock-review > .ProductDetailInfoBlock-review-link > .ReviewStars-wrapper > .ReviewStars-reviews *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .js-pricing-block > .ProductDetailInfoBlock-pricing > .ProductDetailInfoBlock-pricing-amountWrap > .ProductDetailInfoBlock-pricing-amount > span *::text',
                        []),
                    Field(
                        u'original_price',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .js-pricing-block > .ProductDetailInfoBlock-pricing > .ProductDetailInfoBlock-pricing-discountWrap > .js-consumer-discount-block > span:nth-child(1) > .ProductDetailInfoBlock-pricing-strikethrough *::text',
                        []),
                    Field(
                        u'description',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > div:nth-child(1) > .js-product-nova-information > .ProductDetailSpecifications > .ProductDetailSpecifications-expandableContent > .js-content-contain > div:nth-child(1) *::text',
                        []),
                    Field(
                        u'rating',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ReviewStars-wrapper > .ReviewStars-reviews *::text',
                        [])])]]
