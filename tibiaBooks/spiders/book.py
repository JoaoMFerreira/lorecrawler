import scrapy
from tibiaBooks.items import TibiabooksItem
from scrapy.loader import ItemLoader

id = 0

class BooksSpider(scrapy.Spider):
    name = "book"
    start_urls = [
        'http://tibia.wikia.com/wiki/The_Formulas_of_Konios_(Book)'
    ]

    def parse(self, response):      
        global id
        id += 1
        location = response.css('aside div.pi-data-value a::text')[0].extract()
        
        try:
            author = response.css('aside div.pi-data-value::text')[1].extract()
        except IndexError:
            author = response.css('aside div.pi-data-value a::text')[1].extract()

        shortDescription = response.css('aside div.pi-data-value::text')[0].extract()
        text = response.css('blockquote.book::text').extract()

        l = ItemLoader(item=TibiabooksItem(), response=response)
        l.add_value('id', id)
        l.add_css('name', 'h1.page-header__title::text')
        l.add_value('location', location)
        l.add_value('author', author)
        l.add_value('shortDescription', shortDescription)
        l.add_value('text', text)
        return l.load_item()   

