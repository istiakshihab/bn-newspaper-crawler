from spiders.amadershomoy import AmadershomoySpider
from spiders.bangladeshtoday import BangladeshtodaySpider
from spiders.banglatribune import BanglatribuneSpider
from spiders.bdnews24 import Bdnews24Spider
from spiders.dailynayadiganta import DailynayadigantaSpider
from spiders.dailystar import DailystarSpider
from spiders.ittefaq import IttefaqSpider
from spiders.janakantha import JanakanthaSpider
from spiders.kalerkantho import KalerkanthoSpider
from spiders.tbsbangla import TbsbanglaSpider
from spiders.prothomalo import ProthomaloSpider

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

settings = get_project_settings()
process = CrawlerProcess(settings=settings)

process.crawl(AmadershomoySpider)
process.crawl(BangladeshtodaySpider)
process.crawl(BanglatribuneSpider)
process.crawl(Bdnews24Spider)
process.crawl(DailynayadigantaSpider)
process.crawl(DailystarSpider)
process.crawl(IttefaqSpider)
process.crawl(JanakanthaSpider)
process.crawl(KalerkanthoSpider)
process.crawl(TbsbanglaSpider)
process.crawl(ProthomaloSpider)
process.start()
