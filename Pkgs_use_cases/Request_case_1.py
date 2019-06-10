# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/3/5 
# @Author: Wujiaqi

# http://docs.python-requests.org/zh_CN/latest/index.html
import requests
# 请求网页
r1 = requests.get('http://httpbin.org/get')
print(r1.status_code)
print(r1.encoding)
print(r1.text)
print(r1.json())

# 下载图片
r2 = requests.get("https://www.baidu.com/img/bd_logo1.png")
with open('image.png', 'wb') as f:
    f.write(r2.content)

# 提交一个 POST 请求，同时增加请求头、cookies、代理等信息（此处使用的代理地址不是真实的，测试代码时需去掉）：
url = 'http://httpbin.org/post'
cookies = dict(some_cookie='working')
headers = {'user-agent': 'chrome'}
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}
data = {'key1': 'value1', 'key2': 'value2'}
r3 = requests.get(
    url,
    data=data,
    cookies=cookies,
    proxies=proxies,
    headers=headers
)
print(r3.text)

# Session会话对象
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r4 = s.get("http://httpbin.org/cookies")
print(r4.text)
