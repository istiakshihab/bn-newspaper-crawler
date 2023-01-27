from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class AmadershomoySpider(CrawlSpider):
    name = 'amadershomoy'
    allowed_domains = ['amadershomoy.com']
    start_urls = ['http://amadershomoy.com/']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/[a-z-]+/article/\d+/.+'),
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
            '.active > a:nth-child(1)::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item