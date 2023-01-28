from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newspaper import Article
from bn_newspaper import utils

class ProthomaloSpider(CrawlSpider):
    name = 'prothomalo'
    allowed_domains = ['prothomalo.com']
    start_urls = ['https://www.prothomalo.com/bangladesh/coronavirus/0qx9w13xe8']

    rules = (
        Rule(
            LinkExtractor(
                allow = (r'/[a-z-]+/.+'),
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
            '.vXi2j::text'
        ).get()

        item = utils.return_items(
            article= article,
            top=False,
            category=category,
            language='bangla'
        )
        
        yield item
