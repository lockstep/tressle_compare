from __future__ import absolute_import

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.processors import Item, Field, Text, Regex
from ..items import HomeProductItem

# OBSERVATIONS:
# Links that are categories as opposed to products seem to take the following
# form, with what appears to be a "category id" towards the end starting with C:
# https://www.wayfair.com/Kitchen-and-Dining-Tables-C46129.html
# They also appear with a ~ symbol followed by the category:
# https://www.wayfair.com/Kitchen-and-Dining-Sets-l145-c46025-O1253~Vinyl.html
# Or have curated-collections in the url:
# https://www.wayfair.com/curated-collections/Kitchen-&-Dining-Finds~E66740.html
# Other non-product indicators include:
# [ 'similar-to-event', 'login.php' ]


class Wayfair(BasePortiaSpider):
    name = "wayfair"
    # To test against local files uncomment the following, comment out
    # the allowed domains, change the allow rule to 'file', follow to False,
    # and use the terminal command: scrapy crawl wayfair
    # base_path = 'file:///Users/Admin/Lockstep/apps/tressle_compare/tressle_bot/lib/samples'
    # start_urls = [
    #     base_path + '/wayfair-1.html',
    #     base_path + '/wayfair-2.html'
    # ]

    allowed_domains = [u'www.wayfair.com']

    start_urls = [
        u'https://www.wayfair.com/Furniture-C45974.html',
        u'https://www.wayfair.com/Rugs-C215385.html',
        u'https://www.wayfair.com/Outdoor-C32334.html',
        u'https://www.wayfair.com/D%C3%A9cor-C45752.html',
        u'https://www.wayfair.com/Bed-and-Bath-C215329.html',
        u'https://www.wayfair.com/Lighting-C215735.html',
        u'https://www.wayfair.com/Kitchen-C45667.html',
        u'https://www.wayfair.com/Window-Treatments-C416567.html',
        u'https://www.wayfair.com/Storage-and-Organization-C215875.html',
        u'https://www.wayfair.com/Baby-and-Kids-C45226.html',
        u'https://www.wayfair.com/Home-Improvement-C45342.html',
        u'https://www.wayfair.com/Mattresses-C414871.html',
        u'https://www.wayfair.com/All-Pet-Furniture-C504273.html',
        u'https://www.wayfair.com/Seasonal-and-Holiday-Decor-C1859601.html',
    ]

    rules = [
        # Rule(
        #     LinkExtractor(
        #         allow=('file')
        #     ),
        #     callback='parse_item'
        # )
        Rule(
            LinkExtractor(
                allow=('-C\d+\.html'),
                deny=()
            ),
            follow=True # This is the default if no callback
        ),
        Rule(
            LinkExtractor(
                allow=('-[A-Z]{2,}\d+\.html'),
                deny=()
            ),
            callback='parse_item',
            follow=False # This is the default if callback present
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
                        [],
                        True),
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
                        u'average_rating',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ReviewStars-wrapper > .ReviewStars-reviews *::text',
                        []),
                    Field(
                        u'ratings_count',
                        u'.ProductDetail-content > .ProductDetail-wrap > .ProductDetail-leftCol > .ProductDetailReviews > .track_visibility > .ProductDetailReviews-header > .ProductDetailReviews-totals > .ProductDetailReviews-totals-based *::text',
                        [])])]]
