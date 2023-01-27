from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class JanakanthaSpider(CrawlSpider):
    name = 'janakantha'
    allowed_domains = ['dailyjanakantha.com']
    start_urls = ['http://dailyjanakantha.com/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/[a-z-]+/[a-z-]+/\d+'),
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
            '.InnerCatTitle > a:nth-child(1) > h2:nth-child(1)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item