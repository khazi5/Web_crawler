# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:khazi
# datetime:2018/12/28

# https://zhuanlan.zhihu.com/p/20423182

import requests
from bs4 import BeautifulSoup
import codecs
from selenium import webdriver

DOWNLOAD_URL = 'http://movie.douban.com/top250'


def download_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url).content
    return data


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    movie_name_list = []
    star_score_list = []
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()
        star_detail = movie_li.find('div', {'class':'star'})
        star_score = star_detail.find('span', attrs={'class': 'rating_num', 'property': 'v:average'}).getText()
        movie_name_list.append(movie_name)
        star_score_list.append(star_score)
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, star_score_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, star_score_list, None


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies.txt', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, scores, url = parse_html(html)
            info = zip(movies, scores)
            for i in info:
                fp.write(u'{movies} {scores}\n'.format(movies=i[0], scores=i[1]))


if __name__ == '__main__':
    main()

