from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class Bdnews24Spider(CrawlSpider):
    name = 'bdnews24'
    allowed_domains = ['bangla.bdnews24.com']
    start_urls = ['http://bangla.bdnews24.com/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/[a-z-]+/.*'),
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
            '.breadcrumb-wrapper > a:nth-child(3)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item


