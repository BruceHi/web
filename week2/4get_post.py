import requests

# get 方法
r = requests.get('https://httpbin.org/')
print(r.status_code)
print(type(r.headers))  # <class 'requests.structures.CaseInsensitiveDict'>
print(r.headers['content-type'])
# 编码
print(r.encoding)
# print(r.json())
# 只有在 可以 json 化时，才可以转化为 json 否则报错
# print(r.text)

# post 方法，要加上对应的数据
r = requests.post('https://httpbin.org/post', data={'key': 'val'})
# print(r.text)
print(r.json())
