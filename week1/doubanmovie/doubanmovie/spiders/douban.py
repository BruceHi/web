import scrapy
from bs4 import BeautifulSoup as bs
from doubanmovie.items import DoubanmovieItem
from scrapy.selector import Selector

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        for i in range(2):
            url = f'https://movie.douban.com/top250?start={i * 25}'
            # 默认为 false，表示受到 allowed_domains限制， 改为 True，不受限制。
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    # def parse(self, response, **kwargs):
    #     items = []
    #     soup = bs(response.text, 'html.parser')
    #     for tag in soup.find_all('div', attrs={'class': 'hd'}):
    #         item = DoubanmovieItem()
    #         title = tag.a.find('span').text
    #         link = tag.a.get('href')
    #         item['title'] = title
    #         item['link'] = link
    #         items.append(item)
    #         yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
    #
    # def parse2(self, response):  # 把 meta 传过去，不如没法最终写入到 item 里面去
    #     item = response.meta['item']
    #     soup = bs(response.text, 'html.parser')
    #     content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
    #     item['content'] = content
    #     yield item

    def parse(self, response, **kwargs):
        # SelectorList 类型
        movies = Selector(response=response).xpath('//div[@class="hd"]')  # 里面双引号，单引号都行，但是外面是单引号，里面双引号
        for movie in movies:  # movie : sector 类型
            title = movie.xpath('./a/span/text()')  # SelectorList
            link = movie.xpath('./a/@href')
            print(type(title))
            print(link)

            print(title.extract())  # list[str]
            print(type(title.extract()))
            print(link.extract())

            print(title.extract_first())  # str
            print(type(title.extract_first()))
            print(link.extract_first())

