# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/1/3 
# @Author: Wujiaqi

import pymysql
import configparser


def get_config():
    parser = configparser.ConfigParser()
    parser.read(filenames='config.ini', encoding='utf-8')
    config = dict(parser['mysql'])
    config['port'] = int(config['port'])
    return config


db = pymysql.connect(**get_config())
cursor = db.cursor()
sql = """select DATABASE()"""
cursor.execute(sql)
data = cursor.fetchall()
print(data)
db.close()
