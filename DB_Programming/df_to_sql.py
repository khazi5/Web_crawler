# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/2/25 
# @Author: Wujiaqi

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Integer, BigInteger, DATETIME, TEXT
import os
import pymysql
pymysql.install_as_MySQLdb()
path = os.path.abspath('C:/Users/Administrator/Desktop/IT2018/data/')

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DATABASE = 'bs_alarms'
DB_USER = 'root'
DB_PASS = 'root'

connect_string = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)
engine = create_engine(connect_string)
# ENGINE = create_engine("mssql+pymssql://" +
#                        config.get_local('CEDS_USERNAME') + ':' +
#                        config.get_local('CEDS_PASSWORD') + '@' +
#                        config.get_local('CEDS_SERVER') + '/' +
#                        config.get_local('CEDS_DATABASE'),
#                        encoding="utf-8")

try:
    df = pd.read_csv(path+'standard_alarms.csv', header=None, sep=',', engine='python',
                     names=['告警流水号', '告警号', '告警发生时间', '告警恢复时间', '告警对象名称',
                            '告警对象ID', '区县ID', '工程状态', '城市ID', '省份ID']
                     )
# 设置数据表的列类型
    dtypedict = {
        '告警号': NVARCHAR(length=255),
        '告警发生时间': DATETIME,
        '告警恢复时间': DATETIME,
        '告警对象名称': TEXT,
        '工程状态': NVARCHAR(length=255),
        '告警流水号': BigInteger(),
        '告警对象ID': BigInteger(),
        '区县ID': BigInteger(),
        '城市ID': Integer(),
        '省份ID': Integer()
    }
    df.to_sql('standard_alarms', con=engine, if_exists='fail', index=False, dtype=dtypedict)
except Exception as e:
    print(e)
