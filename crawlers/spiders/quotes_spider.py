import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.liveyoursport.com/squash/'
    ]

    def parse(self, response):
        for quote in response.css('ul.ProductList'):
            yield {
                'price': quote.css('li div.ProductDetails em ::text').extract(),
                'url': quote.css('div.ProductDetails a::attr(href)').extract(),
                'ProductDetails': quote.css('li div.ProductDetails a::text').extract(),
            }

        next_page = response.css('ul.PagingList a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)