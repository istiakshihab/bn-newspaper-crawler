from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class DailystarSpider(CrawlSpider):
    name = 'dailystar'
    allowed_domains = ['bangla.thedailystar.net']
    start_urls = ['http://bangla.thedailystar.net/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/.*/news-\d+'),
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
            'div.category > a:nth-child(1)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item
