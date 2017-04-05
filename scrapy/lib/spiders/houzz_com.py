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


class Houzz(BasePortiaSpider):
    name = "www.houzz.com"
    allowed_domains = [u'www.houzz.com', u'www.houzz.com']
    start_urls = [u'https://www.houzz.com/',
                  u'http://www.houzz.com/photos/kitchen-and-dining',
                  u'http://www.houzz.com/photos/bath-products',
                  u'http://www.houzz.com/photos/bedroom-products',
                  u'http://www.houzz.com/photos/living-products',
                  u'http://www.houzz.com/photos/lighting',
                  u'http://www.houzz.com/photos/furniture',
                  u'http://www.houzz.com/photos/home-decor',
                  u'http://www.houzz.com/photos/home-improvement',
                  u'http://www.houzz.com/photos/outdoor-products']
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
                u'.noBorders',
                [
                    Field(
                        u'manufacturer',
                        u'.rightSideBarWide > .hzProduct > div > .detailBox > .seller-shipping-info > .curMpListing > .list-unstyled > .listing > .text-bold > a *::text',
                        []),
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
                        u'primary_image_url',
                        u'.leftSideContentNarrow > .spaceContent > .viewSpaceImage > .mainImageWrap > .viewImage::attr(src)',
                        []),
                    Field(
                        u'rating',
                        u'.leftSideContentNarrow > .spaceContent > .product-reviews > .clearfix > .clearfix > .review-avg *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.leftSideContentNarrow > .spaceContent > .product-reviews > .clearfix > .clearfix > .reviews-count > span *::text',
                        []),
                    Field(
                        u'name',
                        u'.rightSideBarWide > .marketplace > div > .productTitle > .header-1 *::text',
                        [],
                        True),
                    Field(
                        u'current_price',
                        u'.rightSideBarWide > .marketplace > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .product-price *::text',
                        [],
                        True),
                    Field(
                        u'original_price',
                        u'.rightSideBarWide > .marketplace > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .text-m *::text',
                        []),
                    Field(
                        u'description',
                        u'.rightSideBarWide > .marketplace > div > .detailBox > .description *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.noBorders',
                [
                    Field(
                        u'manufacturer',
                        u'.rightSideBarWide > .hzProduct > div > .detailBox > .seller-shipping-info > .curMpListing > .list-unstyled > .listing > .text-bold > a::attr(href)',
                        []),
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
                        u'primary_image_url',
                        u'.leftSideContentNarrow > .spaceContent > .viewSpaceImage > .mainImageWrap > .viewImage::attr(src)',
                        []),
                    Field(
                        u'rating',
                        u'.leftSideContentNarrow > .spaceContent > .product-reviews > .clearfix > .clearfix > .review-avg *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.leftSideContentNarrow > .spaceContent > .product-reviews > .clearfix > .clearfix > .reviews-count > span *::text',
                        []),
                    Field(
                        u'name',
                        u'.rightSideBarWide > .hzProduct > div > .productTitle > .header-1 *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.rightSideBarWide > .hzProduct > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .product-price *::text',
                        []),
                    Field(
                        u'original_price',
                        u'.rightSideBarWide > .hzProduct > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .text-m *::text',
                        []),
                    Field(
                        u'description',
                        u'.rightSideBarWide > .hzProduct > div > .detailBox > .description *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.noBorders',
                [
                    Field(
                        u'manufacturer',
                        u'.rightSideBarWide > .hzProduct > div > .detailBox > .seller-shipping-info > .curMpListing > .list-unstyled > .listing > .text-bold > a::attr(href)',
                        []),
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
                        u'primary_image_url',
                        u'.leftSideContentNarrow > .spaceContent > .viewSpaceImage > .mainImageWrap > .viewImage::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.rightSideBarWide > .hzProduct > div > .productTitle > .header-1 *::text',
                        []),
                    Field(
                        u'current_price',
                        u'.rightSideBarWide > .hzProduct > div > .buyBox > .buyContainer > .clearfix > .row > .col-xs-12 > .product-price *::text',
                        []),
                    Field(
                        u'description',
                        u'.rightSideBarWide > .hzProduct > div > .detailBox > .description *::text',
                        [])])]]
