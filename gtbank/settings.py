BOT_NAME = 'gtbank'

SPIDER_MODULES = ['gtbank.spiders']
NEWSPIDER_MODULE = 'gtbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'DEBUG'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
	'gtbank.pipelines.GtbankPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
