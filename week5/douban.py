import scrapy
from scrapy.selector import Selector
from movie.items import MovieItem
from selenium import webdriver
import time


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/1292064/']

    def parse(self, response, **kwargs):
        # star_to_num = {
        #     '力荐': 5,
        #     '推荐': 4,
        #     '还行': 3,
        #     '较差': 2,
        #     '很差': 1,
        # }
        # item = MovieItem()
        # content = Selector(response=response).xpath('//*[@id="hot-comments"]')
        # comments = content.xpath('./div')
        # for comment in comments:
        #     star = star_to_num[comment.xpath('./div/h3/span[2]/span[2]/@title').get()]
        #     short = comment.xpath('./div/p/span/text()').get()
        #     record_time = comment.xpath('./div/h3/span[2]/span[3]/text()').get().strip()
        #     print(star, short, record_time)
        # print(response)  # <200 https://movie.douban.com/subject/1291546/>
        # print(type(response))  # <class 'scrapy.http.response.html.HtmlResponse'>
        # print(response.urljoin(link))  # 原来路径得到新的绝对路径
        # print(link)

        link = Selector(response=response).xpath('//*[@id="hot-comments"]/a/@href').get()
        # 路径拼接：response.urljoin(link)
        yield scrapy.Request(url=response.urljoin(link), callback=self.parse3)
        yield scrapy.Request(url=response.urljoin(link), callback=self.parse2)

    def parse2(self, response):
        driver = webdriver.Chrome()
        url = response.urljoin('')
        driver.get(url)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="paginator"]/a').click()
        time.sleep(2)
        yield scrapy.Request(url=driver.current_url, callback=self.parse3)

    def parse3(self, response):
        star_to_num = {
            '力荐': 5,
            '推荐': 4,
            '还行': 3,
            '较差': 2,
            '很差': 1,
        }
        item = MovieItem()
        # 最后 class 空格不能省略 /div[@class="comment-item "]
        comments = Selector(response=response).xpath('//*[@id="comments"]/div[@class="comment-item "]')
        for comment in comments:
            short = comment.xpath('./div[2]/p/span/text()').get()
            star = star_to_num[comment.xpath('./div[2]/h3/span[2]/span[2]/@title').get()]
            record_time = comment.xpath('./div[2]/h3/span[2]/span[3]/text()').get().strip()

            # str, int, str
            item['short'] = short
            item['star'] = star
            item['record_time'] = record_time
            print(type(short), type(star), type(record_time))
            yield item
            # print(short, star, record_time)
