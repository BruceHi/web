# xml化处理
from lxml import etree

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<div class='a b'>test</div>
<p class="story">...</p>
"""

selector = etree.HTML(html_doc)
print(type(selector))

file_name = selector.xpath('//*[@class="story"]/text()')
print(file_name)

# 只写一个属性取不到值
a = selector.xpath('//div[@class="a"]/text()')
print(a)


