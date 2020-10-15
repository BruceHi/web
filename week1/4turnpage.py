import requests
from bs4 import BeautifulSoup as bs
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
headers = {'user-agent': user_agent}  # 键要注意，是短杠，不是下划线


def get_url_name(myurl):
    reponse = requests.get(myurl, headers=headers)  # 切记，必须要用关键字参数
    soup = bs(reponse.text, 'html.parser')
    for tag in soup.find_all('div', attrs={'class': 'hd'}):
        a_tag = tag.a
        print(a_tag.get('href'))
        print(a_tag.find('span').text)


urls = (f'https://movie.douban.com/top250?start={n * 25}&filter=' for n in range(10))

# time.sleep(10)

for url in urls:
    get_url_name(url)
    time.sleep(5)

