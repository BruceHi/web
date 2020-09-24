html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup as bs
soup = bs(html_doc, 'html.parser')

print(soup.prettify())

print(soup.text)  # 只有文本内容
print(soup.title)
print('--------------')
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup.title.name)  # str，名字
print(type(soup.title.string))  # <class 'bs4.element.NavigableString'>

print(type(soup.title.parent))
print(soup.title.parent.name)

print(type(soup.p))  # 并非 string 类型，而是 bs4.element.Tag
print(soup.p['class'])  # 属性值是 list 类型，多值属性返回 list，唯一属性，比如 id 返回 str
print(type(soup.p['class']))

print(type(soup.find_all('a')))  # <class 'bs4.element.ResultSet'>
print(soup.find_all('a')[0].string)

print(soup.find(id='link3'))

a = soup.find_all('a')[0]
print(a.get('class'))  # tag 的方法 get

print(soup.get_text())  # 只有文本内容

print(soup.find_all(id='link3'))
print('---------------------')

print(soup.body)
print(soup.body.p)
print(soup.body.p.b)