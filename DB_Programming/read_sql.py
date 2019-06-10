# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/2/25 
# @Author: Wujiaqi

import pandas as pd
from numpy import np
import pymysql
import os
from sqlalchemy import create_engine
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DATABASE = 'bs_alarms'
DB_USER = 'root'
DB_PASS = 'root'

connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)
engine = create_engine(connect_string)

s_a = pd.read_sql_table('standard_alarms', con=engine)
print(s_a)
print(s_a.dtypes)

# # sql_to_csv
# path = os.path.abspath('C:/Users/Administrator/Desktop/')
# filename = 'aaa.csv'
# filepath = os.path.join(path, filename)
# s_a.to_csv(filepath)
# aaa = pd.read_csv(filepath, sep=',', engine='python')
# aaa['告警发生时间'] = pd.to_datetime(aaa['告警发生时间'])
# aaa['告警恢复时间'] = pd.to_datetime(aaa['告警恢复时间'])
