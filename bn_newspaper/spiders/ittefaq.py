from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class IttefaqSpider(CrawlSpider):
    name = 'ittefaq'
    allowed_domains = ['ittefaq.com.bd']
    start_urls = ['http://www.ittefaq.com.bd/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/\d+/.+'),
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
            '.breadcrumb > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1) > strong:nth-child(1)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item