# Scrapy settings for stockscrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stockscrape'

SPIDER_MODULES = ['stockscrape.spiders']
NEWSPIDER_MODULE = 'stockscrape.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stockscrape (+http://www.yourdomain.com)'
