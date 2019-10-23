#!/usr/bin/python
# -*- coding: UTF-8 -*-

data = open("D:/千方/风控平台/人行征信/查询/联名卡2000人查询/联名卡2000人查询.txt",encoding='GBK')
writePath = "D:/千方/风控平台/人行征信/查询/联名卡2000人查询/"
i = 1
j = 200
for line in data:
	if i%j != 0:
		writeFile = open(writePath+str(i//j+1)+".txt","a+",encoding='GBK')
		writeFile.write(line)
	else:
		writeFile = open(writePath+str(i//j)+".txt","a+",encoding='GBK')
		writeFile.write(line)
	i = i + 1

