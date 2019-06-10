# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/3/5 
# @Author: Wujiaqi
# Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_doc, 'html.parser')

# soup.title  # title 元素
# # <title>The Dormouse's story</title>
#
# soup.p  # 第一个 p 元素
# # <p class="title"><b>The Dormouse's story</b></p>
#
# soup.p['class']  # p 元素的 class 属性
# # ['title']
#
# soup.p.b  # p 元素下的 b 元素
# # <b>The Dormouse's story</b>
#
# soup.p.parent.name  # p 元素的父节点的标签
# # body

# # 并不是所有信息都可以简单地通过结构化获取，通常使用 find 和 find_all 方法进行查找：
# soup.find_all('a')  # 所有 a 元素
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# soup.find(id='link3')  # id 为 link3 的元素
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
#
# x = soup.find(class_='story')
# x.get_text()  # 仅可见文本内容
# # 'Once upon a time there were three little sisters; and their names were\nElsie,
# # \nLacie and\nTillie;\nand they lived at the bottom of a well.'
# x.prettify()  # 元素完整内容
#
# # 如果你有前端开发经验，对 CSS 选择器很熟悉，bs 也为你提供了相应的方法：
# soup.select('html head title')
# # [<title>The Dormouse's story</title>]
# soup.select('p > #link1')
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
