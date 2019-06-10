# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:khazi
# datetime:2019-01-15

import requests
from lxml import etree


DOWNLOAD_URL = 'http://movie.douban.com/top250'

def download_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url).content
    return data

def parse_html(html):
    html = etree.HTML(html)
    movie_name_list = []
    # src = '''
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
    # '''
    src ='''
    //div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/ol[@class='grid_view']
    /li[position()<26]/div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title'][1]
    '''
    result = html.xpath(src)
    for i in range(len(result)):
        movie_name_list.append(result[i].text)
    return movie_name_list

def main():
    url = DOWNLOAD_URL
    html = download_page(url)
    print(parse_html(html))

if __name__ == '__main__':
    main()