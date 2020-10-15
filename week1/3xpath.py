import requests
from lxml import etree
import pandas as pd


# 每次 user_agent 都要更换吗？最好还是使用浏览器的agent，不要使用每个网站上的 agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
headers = {'user-agent': user_agent}
response = requests.get('https://movie.douban.com/subject/1292052/', headers=headers)

# xml化处理
selector = etree.HTML(response.text)

file_name, = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'影片：{file_name}')

plan_date, = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_date}')

rating, = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{rating}')

df = pd.DataFrame([file_name, plan_date, rating])
df.to_csv('movie.csv', header=False, index=False)

