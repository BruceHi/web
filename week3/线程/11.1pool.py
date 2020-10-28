import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'https://www.baidu.com',
    'https://www.sina.com.cn',
    'https://www.163.com',
    'https://www.qq.com',
    'https://www.taobao.com',
]

pool = ThreadPool(4)
res = pool.map(requests.get, urls)
pool.close()
pool.join()

for i in res:
    print(i.url)
