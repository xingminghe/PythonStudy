from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')
# print(soup)
# bs自动转码
content = soup.prettify()

print("==" * 12)
# print(soup.head)
print("==" * 12)
print(soup.meta)
print("==" * 12)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("==" * 12)
print("==" * 12)
print("==" * 12)
print(soup)
