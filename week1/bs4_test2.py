from bs4 import BeautifulSoup
import bs4
html = '''
<div class="movie-hover-title" title="我的女友是机器人">
<span class="hover-tag">类型:</span>
爱情／喜剧
</div>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.div.contents)
print(type(soup.div.contents[1]))
# print(soup)
# print(soup.text)
#
# print('------------')
print(soup.div)
print(soup.div.text)
print(soup.div.string)
print(soup.div.strings)
print(soup.div.get_text())
print(soup.div.prettify())

# print(soup.span)
# print(soup.name)
# print(soup.div.name)

print('--------------')
# print(soup.div.contents)
# print(soup.div.contents[-1].strip())
#
# print(soup.find(class_='hover-tag'))
# print(soup.find_all('span'))
# print(soup('span'))
#
# print(soup.find('span').string)
# print(type(soup.find('span').string))
# print(type(soup.div.text))
# print(type(soup.div.get_text()))
# print(type(soup.div.prettify()))
#
# print(isinstance(soup.find('span').string, str))
#
# print(soup.span.name)

# html = '''
# <b class="verybold" id='1'>Extremely bold</b>
# '''
# soup = BeautifulSoup(html, 'html.parser')
# print(type(soup.b.attrs))
# print(soup.b.attrs)
# print(soup.b['class'])
# print(soup.b['id'])
#
# print(soup.b['class'])
# print(soup.b.attrs['class'])
#
#
# html = '''
# <p>
# <b class="verybold" id='1'>Extremely <b class='good'>bold</b></b>
#
# dddd</p>
# <b>bold</b>
# '''
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find_all('b', class_='good'))
# print(soup.find_all('b', attrs={'class', 'good'}))
#
# print(bs4.__version__)
#
# print(soup.b)