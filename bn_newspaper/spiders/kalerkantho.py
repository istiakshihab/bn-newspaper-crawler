from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class KalerkanthoSpider(CrawlSpider):
    name = 'kalerkantho'
    allowed_domains = ['kalerkantho.com']
    start_urls = ['https://www.kalerkantho.com/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/online/.*/\d+/\d+/\d+'),
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
            'ol.breadcrumb:nth-child(1) > li:nth-child(2) > a:nth-child(1)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item

