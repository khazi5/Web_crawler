# !/usr/bin/env python3
# --coding:utf-8 --
# @Time: 2019/1/3 
# @Author: Wujiaqi

import pymysql
# 打开数据库连接
db = pymysql.connect('localhost', 'test', 'test', 'tess')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
insert_sql = """INSERT INTO testperson 
                (FIRST_NAME, LAST_NAME, AGE, INCOME) 
                VALUES ('JACK', 'MA', 50, 1.23) """
try:
    # 执行SQL语句
    cursor.execute(insert_sql)
    # 提交修改
    db.commit()
except:
    print('error')
    # 发生错误时回滚
    db.rollback()
# 关闭连接
db.close()
