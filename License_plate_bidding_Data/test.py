# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/5/31 
# @Author: Wujiaqi

from bs4 import BeautifulSoup
import requests
import lxml
import re
# http://jt.gz.bendibao.com/news/20171025/235791.shtml
# http://jt.gz.bendibao.com/news/2019527/250716.shtml
r1 = requests.get('http://jt.gz.bendibao.com/news/2019225/248233.shtml')
html_doc = r1.text.encode('ISO-8859-1').decode('utf8')
soup = BeautifulSoup(html_doc, 'lxml')
# next_url = soup.find_all(target='_blank')[20]['href']
try:
	next_url = soup.find('strong', text=re.compile('竞价情况')).next_sibling['href']
except TypeError:
	next_url = soup.find_all(target='_blank')[20]['href']
