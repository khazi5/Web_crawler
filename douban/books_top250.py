# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:khazi
# datetime:2019-06-03

import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_PAGE = 'http://book.douban.com/top250/'


def download_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url).content
    return data


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    book_list_soup = soup.find('div', attrs={'class': 'article'})
    book_name_list = []
    star_score_list = []
    for book_table in book_list_soup.find_all('table'):
        book_name_detail = book_table.find('div', attrs={'class': 'pl2'})
        book_name = book_name_detail.find('a').get_text(strip=True)
        star_detail = book_table.find('div', attrs={'class': 'star clearfix'})
        star_score = star_detail.find('span', attrs={'class': 'rating_nums'}).get_text()
        book_name_list.append(book_name)
        star_score_list.append(star_score)
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return book_name_list, star_score_list, next_page['href']
    return book_name_list, star_score_list, None


def main():
    url = DOWNLOAD_PAGE

    with codecs.open('books.txt', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            books, scores, url = parse_html(html)
            info = zip(books, scores)
            for i in info:
                fp.write(u'{movies} {scores}\n'.format(movies=i[0], scores=i[1]))


if __name__ == '__main__':
    main()
