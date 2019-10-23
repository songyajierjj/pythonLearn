#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

success = open("D:/千方/CMS+决策引擎/批量数据/20180306/success.txt","a",encoding='GBK')
fail = open("D:/千方/CMS+决策引擎/批量数据/20180306/fail2017.txt","a",encoding='GBK')

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='risk-cms', charset='utf8')
cursor = conn.cursor()

#id > 158442 and 
# sql = "SELECT DISTINCT(uid),realname from tb_deal_receive_data where decisionResult = 1"
# aa = cursor.execute(sql)	
# info = cursor.fetchmany(aa)
# for ii in info:
# 	success.write(ii[0]+"&"+ii[1]+"\n")
sql = "SELECT uid,realname,rulescore,decisionresult,receiveDate from tb_deal_receive_data where decisionResult = -98 and receiveDate <= \"2017-12-31 23:59:59\""
aa = cursor.execute(sql)	
info = cursor.fetchmany(aa)
for ii in info:
    if ii[2].find('qianhai12=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&qianhai12=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('qianhai21=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&qianhai21=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('qianhai22=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&qianhai22=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('qianhai23=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&qianhai23=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('qianhai24=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&qianhai24=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('bairong2=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&bairong2=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('bairong3=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&bairong3=0&"+str(ii[4])+"&"+ii[3]+"\n")
    elif ii[2].find('bairong4=0') > 0:
        fail.write(ii[0]+"&"+ii[1]+"&bairong4=0&"+str(ii[4])+"&"+ii[3]+"\n")

cursor.close()
conn.commit()
conn.close()