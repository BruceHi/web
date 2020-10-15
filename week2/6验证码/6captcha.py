import requests
from PIL import Image
import pytesseract

# img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599,4127074888&fm=26&gp=0.jpg'
# r = requests.get(img_url)
#
# with open('captcha.jpg', 'wb') as f:
#     f.write(r.content)
#
# im = Image.open('captcha.jpg')
# im.show()
#
# # 灰度图
# gray = im.convert('L')
# gray.show()
# gray.save('gray.jpg')
# im.close()

# 二值化
# tables = [0] * 100 + [1] * 156
# im = Image.open('gray.jpg')
# out = im.point(tables, '1')
# out.show()
# out.save('th.jpg')

im = Image.open('th.jpg')
print(pytesseract.image_to_string(im, lang='eng').strip())
