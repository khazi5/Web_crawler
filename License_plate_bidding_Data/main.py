# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/5/28 
# @Author: Wujiaqi
# 爬取广州车牌竞价系统历史数据，并可视化输出。

from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=14)
sns.set(font=myfont.get_name())

url = "http://www.gzqcjj.com/jjjg.shtml"
r1 = requests.get(url)
# print(r1.status_code)
# print(r1.encoding)
# print('------------------------')

html_doc = r1.text.encode('ISO-8859-1').decode('utf8')
soup = BeautifulSoup(html_doc, 'html.parser')
raw_data = soup.find_all('td')
data = [i.get_text() for i in raw_data]

period = []
personal_lowest_price = []
company_lowest_price = []
for i in range(1, int(len(data)/3)):
	period.append(data[i*3][0:8])
	personal_lowest_price.append(int(data[i*3+1]))
	company_lowest_price.append(int(data[i*3+2]))
# print(period, personal_lowest_price, company_lowest_price)

dt = {data[1]: personal_lowest_price, data[2]: company_lowest_price}
df = pd.DataFrame(dt, index=period)
# print(df.dtypes)

plt.figure(figsize=(14, 9))
sns.lineplot(data=df)
plt.xticks(rotation=270)
plt.show()
