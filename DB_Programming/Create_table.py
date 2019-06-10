# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/1/3 
# @Author: Wujiaqi

import pymysql
import configparser

db = pymysql.connect(host='localhost', user='root', password='root', db='tess')

cursor = db.cursor()
sql1 = "DROP TABLE IF EXISTS testperson"
cursor.execute(sql1)
sql2 = """create table testperson (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        INCOME FLOAT)"""
cursor.execute(sql2)
db.close()