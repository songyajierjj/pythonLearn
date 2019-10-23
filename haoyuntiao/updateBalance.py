#!/usr/bin/python
# -*- coding: UTF-8 -*-

data = open("D:/千方/好运条/用户信息/白名单用户统计/20181126/1.txt",encoding='GBK')

writeResultPath = "D:/千方/好运条/用户信息/白名单用户统计/20181126/result.txt"
writeResultFile = open(writeResultPath,"a+",encoding='GBK')

i = 1
sql = "update t_user_center_white_list set type = '正常用户' where USER_ID in ("
for line in data:
    data = line.replace("\n","")
    sql = sql + "'"+data+"',"

writeResultFile.write(sql)
