# coding = utf-8

from bs4 import BeautifulSoup
import requests
url = 'http://example.webscraping.com/sitemap.xml'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')
links = soup.find_all('loc')
htmls = []
for link in links:
    html = link.get_text()
    htmls.append(html)
print(htmls)
