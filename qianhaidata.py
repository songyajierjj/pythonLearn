#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
f = open("D:/千方/CMS+决策引擎/批量数据/20171108/qianfang/qianhaimsc.json",encoding='UTF-8')


a8005 = 0
a8036 = 0
a8037 = 0
a8075 = 0

for i in f.readlines():
	readData = json.loads(i)
	if 'rtCode8005' in readData:
		rtCode8005 = readData['rtCode8005']
		if rtCode8005 == 'E000000':
			result8005 = json.loads(readData['result8005'])
			records = result8005['records']
			for j in range(len(records)):
				if records[j].get('erCode') == 'E000000':
					a8005 = a8005 + 1
					break
	if 'rtCode8036' in readData:
		rtCode8036 = readData['rtCode8036']
		if rtCode8036 == 'E000000':
			result8036 = json.loads(readData['result8036'])
			records = result8036['records']
			for j in range(len(records)):
				if records[j].get('erCode') == 'E000000':
					a8036 = a8036 + 1
					break
	if 'rtCode8037' in readData:
		rtCode8037 = readData['rtCode8037']
		if rtCode8037 == 'E000000':
			result8037 = json.loads(readData['result8037'])
			records = result8037['records']
			for j in range(len(records)):
				if records[j].get('erCode') == 'E000000':
					a8037 = a8037 + 1
					break

	if 'rtCode8075' in readData:
		rtCode8075 = readData['rtCode8075']
		if rtCode8075 == 'E000000':
			result8075 = json.loads(readData['result8075'])
			records = result8075['records']
			for j in range(len(records)):
				if records[j].get('erCode') == 'E000000':
					a8075 = a8075 + 1
					break

print("8005=",a8005)
print("8036=",a8036)
print("8037=",a8037)
print("8075=",a8075)