import scrapy
from tibiaBooks.items import TibiabooksItem
from scrapy.loader import ItemLoader

class BooksSpider(scrapy.Spider):
    name = "booksT"
    start_urls = [
        'http://tibia.wikia.com/wiki/Library'
    ]

    def parse(self, response):
        for libraries in response.xpath('//li/a[contains(@href,"_Librar")]/@href').extract_first():
            yield response.follow(libraries, callback=self.parse_library)

    def parse_library(self, response):
        for book in response.xpath('//a[contains(@href,"(Book)")]/@href').extract_first():
            yield response.follow(book, callback=self.parse_book)

    def parse_book(self, response):
        id = 0
        id = id + 1
        location = response.css('aside div.pi-data-value a::text')[0].extract()
        author = response.css('aside div.pi-data-value::text')[1].extract()
        shortDescription = response.css('aside div.pi-data-value::text')[0].extract()
        text = response.css('blockquote.book::text').extract_first()

        l = ItemLoader(item=TibiabooksItem(), response=response)
        l.add_value('id', id)
        l.add_css('name', 'h1.page-header__title::text')
        l.add_value('location', location)
        l.add_value('author', author)
        l.add_value('shortDescription', shortDescription)
        l.add_value('text', shortDescription)
        return l.load_item()

