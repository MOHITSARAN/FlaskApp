import scrapy

class Item(scrapy.Item):
    URL = scrapy.Field()
    Price = scrapy.Field()
    ProductDetails = scrapy.Field()
    Description = scrapy.Field()
    

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.liveyoursport.com/squash'
    ]

    def parse(self, response):
        for href in response.css('div.ProductDetails a::attr(href)'):
            url = response.urljoin(href.extract())
            print url
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item=Item()
        item['URL'] = response.css('div.ProductDetails a::attr(href)').extract()[0],
        item['Description'] = response.css('div.prod-short-desc ::text').extract()[0],
        item['Price'] = response.css('li div.ProductDetails em ::text').extract()[0],
        item['ProductDetails'] = response.css('div.ProductDetails a::text').extract()[0],
        yield item

        next_page = response.css('ul.PagingList a::attr(href)').extract()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)