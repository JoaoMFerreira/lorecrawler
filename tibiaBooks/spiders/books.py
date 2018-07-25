import scrapy

class BooksSpider(scrapy.Spider):
    name = "booksT"
    start_urls = [
        'https://www.tibiawiki.com.br/wiki/Academia_de_Rookgaard'
    ]

    def parse(self, response):
        books = []
        for link in response.xpath('//a[contains(@href,"(Book)")]/@href').extract_first():
                yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response):
        
        response.xpath('//div[@id="mw-content-text"]/div/table//tr/td/b').extract()
