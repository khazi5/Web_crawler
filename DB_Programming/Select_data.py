# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2018/12/29 
# @Author: Wujiaqi

import pymysql

db = pymysql.connect("localhost", 'test', 'test', 'tess')
cursor = db.cursor()
sql = """select * from testperson"""
try:
    cursor.execute(sql)
    db.commit()
except:
    print('error')
    db.rollback()
# 读取操作
data = cursor.fetchall()
print(data)

db.close()
