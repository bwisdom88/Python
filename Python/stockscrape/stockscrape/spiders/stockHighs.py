from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from stockscrape.items import StockscrapeItem

class highScrape(BaseSpider):
	name = "stockhighs"
	allowed_domains = ["barchart.com"]
	start_urls = ["http://www.barchart.com/stocks/high.php?_dtp1=0"]

	def parse(self, response):
		sel = HtmlXPathSelector(response)
		sites = sel.select('//tbody/tr')
		items = []
		for site in sites:
			item = StockscrapeItem()
			item['symbol'] = site.select("td[contains(@class, 'ds_symbol')]/a/text()").extract()
			item['name'] = site.select("td[contains(@class, 'ds_name')]/a/text()").extract()
			item['price'] = site.select("td[contains(@class, 'ds_last')]/a/text()").extract()
			items.append(item)
		return items
