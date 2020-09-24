import requests
from bs4 import BeautifulSoup as bs

# user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
headers = {'user-agent': user_agent}
response = requests.get('https://movie.douban.com/top250', headers=headers)

bs_info = bs(response.text, 'html.parser')

for tag in bs_info.find_all('div', attrs={'class': 'hd'}):
    a_tag = tag.a  # div 的下级
    print(a_tag.get('href'))
    print(a_tag.find('span').text)
