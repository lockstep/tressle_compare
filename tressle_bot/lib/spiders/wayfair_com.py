from __future__ import absolute_import

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.processors import Item, Field, Text, Regex
from ..items import HomeProductItem


class Wayfair(BasePortiaSpider):
    name = "wayfair"
    # To test against local files uncomment the following, comment out
    # the allowed domains, change the allow rule to 'file', follow to False,
    # and use the terminal command: scrapy crawl wayfair
    # base_path = 'file:///Users/Admin/Lockstep/apps/tressle_compare/tressle_bot/lib/samples'
    # start_urls = [
    #     base_path + '/wayfair-1.html'
    # ]

    allowed_domains = [u'www.wayfair.com']

    start_urls = [
        u'https://www.wayfair.com/Madison-Home-USA-Reversible-Chaise-Sectional-MHUS1049.html',
        u'https://www.wayfair.com/Andover-Mills%C2%AE-Russ-Sectional-ANDO2369.html'
    ]

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
                HomeProductItem,
                None,
                u'#pd',
                [
                    Field(
                        u'primary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(1) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(2) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(4) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'manufacturer',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(5) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'manufacturer_sku',
                        u"//script[contains(., 'part_number')]/text()",
                        [Regex('part_number":"(.*?)"')]),
                    Field(
                        u'sku',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(6) > .Breadcrumbs-item *::text',
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
                        u'current_price',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .js-pricing-block > .ProductDetailInfoBlock-pricing > .ProductDetailInfoBlock-pricing-amountWrap > .ProductDetailInfoBlock-pricing-amount > span *::text',
                        []),
                    Field(
                        u'original_price',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .js-pricing-block > .ProductDetailInfoBlock-pricing > .ProductDetailInfoBlock-pricing-discountWrap > .js-consumer-discount-block > span:nth-child(1) > .ProductDetailInfoBlock-pricing-strikethrough *::text',
                        []),
                    Field(
                        u'description',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > div:nth-child(1) > .js-product-nova-information > .ProductDetailSpecifications > .ProductDetailSpecifications-expandableContent > .js-content-contain > p *::text',
                        []),
                    Field(
                        u'rating',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ReviewStars-wrapper > .ReviewStars-reviews *::text',
                        []),
                    Field(
                        u'rating_count',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ProductDetailReviews-totals-based > span *::text',
                        [])]),
            Item(
                HomeProductItem,
                None,
                u'#pd',
                [
                    Field(
                        u'primary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(1) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(2) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(4) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'manufacturer',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(5) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'manufacturer_sku',
                        u"//script[contains(., 'part_number')]/text()",
                        [Regex('part_number":"(.*?)"')]),
                    Field(
                        u'sku',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(6) > .Breadcrumbs-item *::text',
                        []),
                    Field(
                        u'primary_image_url',
                        u'.clearfix > .ProductDetailImagesBlock > .mainpdimg > .ProductDetailImagesBlock-carouselWrap > .ProductDetailImagesBlock-carousel > .js-slider-container > div:nth-child(1) > .ProductDetailImagesBlock-carousel-link > .ProductDetailImagesBlock-carousel-image::attr(src)',
                        []),
                    Field(
                        u'name',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .ProductDetailInfoBlock-header > .ProductDetailInfoBlock-header-title *::text',
                        [
                            Text()]),
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
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > div:nth-child(1) > .js-product-nova-information > .ProductDetailSpecifications > .ProductDetailSpecifications-expandableContent > .js-content-contain > p *::text',
                        []),
                    Field(
                        u'average_rating',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ReviewStars-wrapper > .ReviewStars-reviews *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ProductDetailReviews-totals-based > span *::text',
                        [])]),
            Item(
                HomeProductItem,
                None,
                u'#pd',
                [
                    Field(
                        u'primary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(1) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'secondary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(2) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'tertiary_category',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(4) > .js-breadcrumb *::text',
                        []),
                    Field(
                        u'sku',
                        u'.clearfix > .ProductDetailBreadcrumbs > .Breadcrumbs > .Breadcrumbs-list > li:nth-child(6) > .Breadcrumbs-item *::text',
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
                        u'manufacturer',
                        u'.clearfix > .ProductDetailInfoBlock > .ProductDetailInfoBlock-wrap > .ProductDetailInfoBlock-header > .ProductDetailInfoBlock-header-manu > .ProductDetailInfoBlock-header-link *::text',
                        []),
                    Field(
                        u'manufacturer_sku',
                        u"//script[contains(., 'part_number')]/text()",
                        [Regex('part_number":"(.*?)"')]),
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
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > div:nth-child(1) > .js-product-nova-information > .ProductDetailSpecifications > .ProductDetailSpecifications-expandableContent > .js-content-contain > p *::text',
                        []),
                    Field(
                        u'rating',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ReviewStars-wrapper > .ReviewStars-reviews *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ProductDetailReviews-totals-based *::text',
                        [])])]]
