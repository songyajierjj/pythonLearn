#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='qf_zxqz', charset='utf8')
cursor = conn.cursor()

sql = "SELECT xml from tb_resultinfo;"
data = cursor.execute(sql)
# result = cursor.fetchall()
info = cursor.fetchmany(data)

for ii in info:
	print(ii[0])