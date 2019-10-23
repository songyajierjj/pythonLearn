#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

#conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='risk-cms', charset='utf8')
conn = pymysql.connect(host='172.17.4.59', port=3306, user='root', passwd='root', db='rule_engine', charset='utf8')
cursor = conn.cursor()
cursor = conn.cursor()

sql = "SELECT rulescore from tb_deal_receive_data "
aa = cursor.execute(sql)	
info = cursor.fetchmany(aa)
bairongSpecialList = 0 #特殊名单
bairongExecution = 0 #法院被执行
bairongApplyLoan = 0 #多次申请
qianhai8075 = 0 #欺诈
qianhai8036 = 0 #风险度
qianhai8005 = 0 #好信度
qianhai8037 = 0 #常贷客
for ii in info:
	if ii[0].find('r2=') > 0 or ii[0].find('bairong2=') > 0:
		bairongSpecialList += 1
	if ii[0].find('r3=') > 0 or ii[0].find('bairong3=') > 0:
		bairongExecution += 1
	if ii[0].find('r4=') > 0 or ii[0].find('bairong4=') > 0:
		bairongApplyLoan += 1
	if ii[0].find('qianhai12=') > 0:
		qianhai8075 += 1
	if ii[0].find('qianhai21=') > 0 or ii[0].find('qianhai22=') > 0:
		qianhai8036 += 1
	if ii[0].find('qianhai23=') > 0:
		qianhai8005 += 1
	if ii[0].find('qianhai24=') > 0:
		qianhai8037 += 1

print("特殊名单="+str(bairongSpecialList))
print("法院被执行="+str(bairongExecution))
print("多次申请="+str(bairongApplyLoan))
print("欺诈度="+str(qianhai8075))
print("风险度="+str(qianhai8036))
print("好信度="+str(qianhai8005))
print("常贷客="+str(qianhai8037))
