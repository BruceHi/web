import requests
from PIL import Image
import matplotlib.pyplot as plt

# 小文件下载
# image_url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'
# r = requests.get(image_url)
#
# # 二进制
# # print(r.content)
#
# with open('python_log.png', 'wb') as f:
#     f.write(r.content)

# with Image.open('python_log.png') as img:
#     img.show()

# 大文件下载
file_url = 'https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf'
r = requests.get(file_url, stream=True)
with open('ImageNet.pdf', 'wb') as pdf:
    i = 1
    for chunk in r.iter_content(chunk_size=1024):
        pdf.write(chunk)
        print(f'写入分块{i}')
        i += 1

