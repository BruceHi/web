import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    # def parse(self, response):
    #     pass

    def parse(self, response, **kwargs):
        print(response.text)
