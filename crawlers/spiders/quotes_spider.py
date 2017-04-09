import scrapy

class Item(scrapy.Item):
    URL = scrapy.Field()
    Price = scrapy.Field()
    ProductDetails = scrapy.Field()
    

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.liveyoursport.com/squash/'
    ]

    def parse(self, response):
        for quote in response.css('ul.ProductList li'):
                item=Item()
                item['URL'] = quote.css('div.ProductDetails a::attr(href)').extract()[0],
                item['Price'] = quote.css('li div.ProductDetails em ::text').extract()[0],
                item['ProductDetails'] = quote.css('div.ProductDetails a::text').extract()[0],
                yield item

        next_page = response.css('ul.PagingList a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)