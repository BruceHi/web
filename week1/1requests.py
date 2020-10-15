import requests

# user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
headers = {'user-agent': user_agent}
response = requests.get('https://movie.douban.com/top250', headers=headers)

print(type(response))

print(type(response.text))  # str 类型
print('返回码', response.status_code)  # 200 正常返回，418 没有正常得到


