import scrapy

from scrapy.loader import ItemLoader

from ..items import GtbankItem
from itemloaders.processors import TakeFirst


class GtbankSpider(scrapy.Spider):
	name = 'gtbank'
	start_urls = ['https://www.gtbank.com/media-centre/all-content']

	def parse(self, response):
		print(response.body)
		post_links = response.xpath('//div[@class="article-list-item-title"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@rel="next"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="block-item block-text "]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description if '{' not in p]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="article-list-item-header"]/span[@class="post-date"]/text()').get()

		item = ItemLoader(item=GtbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
