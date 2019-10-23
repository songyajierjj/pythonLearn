#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

data = open("D:/python/htmlData.txt",encoding='GBK')

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='risk-cms', charset='utf8')
cursor = conn.cursor()
for line in data.readlines():
    lineList = line.split(",")
    sql = "SELECT html from tb_resultinfo where certno = '" + lineList[2] + "'"
    print(sql)
    aa = cursor.execute(sql)    
    info = cursor.fetchmany(aa)
    for ii in info:
        print(type(ii[0]))
        print(bytes.decode(ii[0]))


