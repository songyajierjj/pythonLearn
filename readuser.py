#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

fuser = open("D:/千方/CMS+决策引擎/批量数据/tb_person_detail.sql",encoding='UTF-8')
fail = open("D:/千方/CMS+决策引擎/批量数据/20180306/fail2017.txt",encoding='GBK')
failresult = open("D:/千方/CMS+决策引擎/批量数据/20180306/failresult2017.txt","a",encoding='GBK')

userdict = {}
for i in fuser.readlines():
	i = i.replace("'","")
	i = i.replace(",","")

	userlist = i.split(" ")
	userdict[userlist[5]] = "&"+userlist[8]+"&"+userlist[10]

for i in fail.readlines():
	userlist = i.split("&")
	if(userlist[0] in userdict):
		failresult.write(userlist[0]+"&"+userlist[1]+"&"+userlist[2]+"&"+userlist[3]+userdict[userlist[0]]+"\n")
	else:
		failresult.write(userlist[0]+"&"+userlist[1]+"&"+userlist[2]+"\n")