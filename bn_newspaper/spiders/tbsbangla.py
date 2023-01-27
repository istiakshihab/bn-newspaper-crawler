from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class TbsbanglaSpider(CrawlSpider):
    name = 'tbsbangla'
    allowed_domains = ['tbsnews.net']
    start_urls = ['https://www.tbsnews.net/bangla/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/bangla/.*/news-details-.*'),
                deny = (r'/bangla/%E0%A6%AD%E0%A6%BF%E0%A6%A1%E0%A6%BF%E0%A6%93/.*'),
                unique= True,
                ), 
            callback="parse", 
            follow=True
            ), 
        )
        
    def parse(self, response):
        article = Article(
            url = response.url,
            html = response.text,
            language = 'bn'
            )
        article.download()
        article.parse()
        article.nlp()
        category = response.css(
            'h2.color-red > a:nth-child(1)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item
