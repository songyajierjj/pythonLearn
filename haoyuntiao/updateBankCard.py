#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


conn = pymysql.connect(host='172.17.4.63', port=3306, user='root', passwd='root', db='qfxd_luckloan', charset='utf8')
cursor = conn.cursor()

writePath = "D:/千方/好运条/result.txt"
writeFile = open(writePath,"a+",encoding='GBK')

sql = "SELECT * from tmp_repeat_bank_card1 order by user_id,id desc"
aa = cursor.execute(sql)
info = cursor.fetchmany(aa)
bankCard = {}
writeData = ""
for ii in info:
	if (str(ii[1])+","+ii[2]) in bankCard:
		writeData = writeData + str(ii[0])+","
	else:
		bankCard[str(ii[1])+","+ii[2]] = ii[0]

writeFile.write(writeData)
print(len(bankCard))
