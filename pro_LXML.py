import json

import requests
import lxml.html
from lxml import etree

#html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

#tree = lxml.html.document_fromstring(html)
#title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

#print(title)  # выводим полученный заголовок страницы
#print(tree)

tree = etree.parse('Welcome to Python.org.htm', lxml.html.HTMLParser())
ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')

#//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[1]/a
#//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[1]
#//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[1]/time

for li in ul:
    a = li.find('a')
    d= li.find('time')
    print (a.text)
    print(d.get('datetime'))