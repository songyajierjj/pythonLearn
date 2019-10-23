#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymssql

conn = pymssql.connect(host='211.149.200.103', user='sa', password='_abc123789?', database='hydb')
cursor = conn.cursor()

fail = open("E:/1.txt","a",encoding='UTF-8')



aa = cursor.execute("select  file5,JsonText from gd_gstotalandLegaldetail")
print(type(aa))
info = cursor.fetchall()


print(len(info))
cursor.close()
conn.commit()
conn.close()
