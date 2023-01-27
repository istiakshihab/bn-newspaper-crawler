from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class BangladeshtodaySpider(CrawlSpider):
    name = 'bangladeshtoday'
    allowed_domains = ['bangladeshtoday.net']
    start_urls = ['http://bangladeshtoday.net/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/article/\d+'),
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

        item = utils.return_items(
            article= article,
            top=False,
            category="",
            language='bangla'
        )
        
        yield item