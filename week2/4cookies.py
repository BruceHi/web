import requests

s = requests.Session()

# 使用 get 方式传递cookie，模拟 post
s.get('http://httpbin.org/cookies/set/sessioncookie/12345678')
# r = s.get('http://httpbin.org/cookies')

print(s.cookies)


# with requests.Session() as s:
#     s.get('http://httpbin.org/cookies/set/sessioncookie/12345678')
#     r = s.get('http://httpbin.org/cookies')
#
#     print(r.json())
