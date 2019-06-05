# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/5/29 
# @Author: Wujiaqi
from bs4 import BeautifulSoup
import requests
import lxml
import re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
url_list = []
monthly_personal = []
monthly_company = []


# 从最新的“广州本地宝”文章中获取竞价成交均价:http://jt.gz.bendibao.com/z/chepai/
# 获取最新价格的新闻url
def find_latest_news_url(bdb_url="http://jt.gz.bendibao.com/z/chepai/"):
	# bdb_url = "http://jt.gz.bendibao.com/z/chepai/"
	r1 = requests.get(bdb_url)
	html_doc = r1.text.encode('ISO-8859-1').decode('gbk')
	soup = BeautifulSoup(html_doc, 'lxml')
	latest_news_title = soup.find_all('a', text=re.compile('竞价结果'))[0].string
	latest_news_url = soup.find_all('a', text=re.compile('竞价结果'))[0]['href']
	url_list.append(latest_news_url)
	return url_list


# 从新闻里面抓取平均成交价及之前的新闻url
def get_ave_price(url):
	# 'http://jt.gz.bendibao.com/news/2019527/250716.shtml'
	r1 = requests.get(url)
	html_doc = r1.text.encode('ISO-8859-1').decode('utf8')
	soup = BeautifulSoup(html_doc, 'lxml')
	raw_info_price = soup.find_all('p', text=re.compile('平均成交价'))
	personal_ave_price = int(re.findall(r"\d+\.?\d*", raw_info_price[0].string.strip())[0])
	company_ave_price = int(re.findall(r"\d+\.?\d*", raw_info_price[1].string.strip())[0])
	monthly_personal.append(personal_ave_price)
	monthly_company.append(company_ave_price)
	return monthly_personal, monthly_company


# 爬取每个新闻的下一个链接
# 目前爬到17年3月 中间有多月缺失url
def get_next_url(url):
	r1 = requests.get(url)
	html_doc = r1.text.encode('ISO-8859-1').decode('utf8')
	soup = BeautifulSoup(html_doc, 'lxml')
	try:
		next_url = soup.find('strong', text=re.compile('竞价情况')).next_sibling['href']
	except TypeError:
		next_url = soup.find_all(target='_blank')[20]['href']
		# next_url = soup.find('strong', text=re.compile('竞价情况')).parent.next_sibling['href']
	url_list.append(next_url)
	return url_list


def main():
	find_latest_news_url()
	for i in range(10):
		get_ave_price(url_list[-1])
		get_next_url(url_list[-1])
	print(monthly_personal)
	print(monthly_company)


if __name__ == '__main__':
	main()
