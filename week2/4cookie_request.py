import requests
from fake_useragent import UserAgent

import sys

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login?source=movie',
}

s = requests.Session()

# 此时的 refer 并没有什么作用，只是为了得到 cookie。
pre_login = 'https://accounts.douban.com/passport/login'
pre_res = s.get(pre_login, headers=headers)  # 获取 cookies


# header 的 refer只是为了下面的使用
login_url = 'https://accounts.douban.com/j/mobile/login/basic'

form_data = {
    'ck': '',
    'name': '123456@qq.com',
    'password': '123456',
    'remember': False
}

response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)

print(response.status_code)
print(response.text)

# 下载网页时考虑 text
# text：Content of the response, in unicode.
# 下载图片时考虑 content
# content："""Content of the response, in bytes."""

