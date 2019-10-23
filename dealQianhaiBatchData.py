#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

fuser = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/用户身份证姓名.txt",encoding='GBK')
# userdict = {}
mobiledict = {}
for i in fuser.readlines():
	userlist = i.split(" ")
	if(len(userlist) > 2):
		# userdict[userlist[0]+"_"+userlist[1].replace("\n","")] = "123"
		mobiledict[userlist[2].replace("\n","")] = "123"

#w写文本文件 wb写二进制文件 a追加写文件
fqianhai = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/qianhaimsc.json",encoding='UTF-8')
# f8005 = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/8005.txt","a",encoding='UTF-8')
# f8037 = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/8037.txt","a",encoding='UTF-8')
f8075 = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/8075.txt","a",encoding='UTF-8')

for i in fqianhai.readlines():
	readData = json.loads(i)
	# if 'rtCode8005' in readData:
	# 	rtCode8005 = readData['rtCode8005']
	# 	if rtCode8005 == 'E000000':
	# 		result8005 = json.loads(readData['result8005'])
	# 		records = result8005['records']
	# 		for j in range(len(records)):
	# 			if records[j].get('erCode') == 'E000000':
	# 				key = records[j].get('name')+"_"+records[j].get('idNo')
	# 				if(key in userdict):
	# 					f8005.write(
	# 						records[j].get('name')+" "+records[j].get('idNo')+" "+records[j].get('idType')+" "+records[j].get('mobileNo')+" "+records[j].get('actionScore')+" "+
	# 						records[j].get('bseInfoScore')+" "+records[j].get('credooScore')+" "+records[j].get('dataBuildTime')+" "+records[j].get('erCode')+" "+
	# 						records[j].get('erMsg')+" "+records[j].get('finRequireScore')+" "+records[j].get('payAbilityScore')+" "+records[j].get('performScore')+" "+records[j].get('seqNo')+" "+
	# 						records[j].get('sourceId')+" "+records[j].get('trendScore')+" "+records[j].get('virAssetScore')+"\n"
	# 						)

	# if 'rtCode8037' in readData:
	# 	rtCode8037 = readData['rtCode8037']
	# 	if rtCode8037 == 'E000000':
	# 		result8037 = json.loads(readData['result8037'])
	# 		records = result8037['records']
	# 		for j in range(len(records)):
	# 			if records[j].get('erCode') == 'E000000':
	# 				key = records[j].get('name')+"_"+records[j].get('idNo')
	# 				if(key in userdict):
	# 					f8037.write(
	# 						records[j].get('name')+" "+records[j].get('idNo')+" "+records[j].get('idType')+" "+records[j].get('amount')+" "+records[j].get('bnkAmount')+" "+
	# 						records[j].get('busiDate')+" "+records[j].get('cnssAmount')+" "+records[j].get('erCode')+" "+records[j].get('erMsg')+" "+
	# 						records[j].get('industry')+" "+records[j].get('p2pAmount')+" "+records[j].get('queryAmt')+" "+records[j].get('queryAmtM3')+" "+records[j].get('queryAmtM6')+" "+
	# 						records[j].get('reasonCode')+" "+records[j].get('seqNo')+"\n"
	# 						)

	if 'rtCode8075' in readData:
		rtCode8075 = readData['rtCode8075']
		if rtCode8075 == 'E000000':
			result8075 = json.loads(readData['result8075'])
			records = result8075['records']
			for j in range(len(records)):
				if records[j].get('erCode') == 'E000000':
					key = records[j].get('mobileNo')
					if(key in mobiledict):
						print(records[j])
						writedata = records[j].get('mobileNo')
						if("ip" in records[j]):
							writedata = writedata + " " + records[j].get('ip')
						else:
							writedata = writedata + " *"
						if("seqNo" in records[j]):
							writedata = writedata + " " + records[j].get('seqNo')
						else:
							writedata = writedata + " *"
						if("isMachdForce" in records[j] and records[j].get('isMachdForce') != ""):
							writedata = writedata + " " + records[j].get('isMachdForce')
						else:
							writedata = writedata + " *"
						if("isMachdDNS" in records[j] and records[j].get('isMachdDNS') != ""):
							writedata = writedata + " " + records[j].get('isMachdDNS')
						else:
							writedata = writedata + " *"
						if("isMachdMailServ" in records[j] and records[j].get('isMachdMailServ') != ""):
							writedata = writedata + " " + records[j].get('isMachdMailServ')
						else:
							writedata = writedata + " *"
						if("isMachdSEO" in records[j] and records[j].get('isMachdSEO') != ""):
							writedata = writedata + " " + records[j].get('isMachdSEO')
						else:
							writedata = writedata + " *"
						if("isMachdOrg" in records[j] and records[j].get('isMachdOrg') != ""):
							writedata = writedata + " " + records[j].get('isMachdOrg')
						else:
							writedata = writedata + " *"
						if("isMachdCrawler" in records[j] and records[j].get('isMachdCrawler') != ""):
							writedata = writedata + " " + records[j].get('isMachdCrawler')
						else:
							writedata = writedata + " *"
						if("isMachdProxy" in records[j] and records[j].get('isMachdProxy') != ""):
							writedata = writedata + " " + records[j].get('isMachdProxy')
						else:
							writedata = writedata + " *"
						if("isMachdBlacklist" in records[j] and records[j].get('isMachdBlacklist') != ""):
							writedata = writedata + " " + records[j].get('isMachdBlacklist')
						else:
							writedata = writedata + " *"
						if("isMachdWebServ" in records[j] and records[j].get('isMachdWebServ') != ""):
							writedata = writedata + " " + records[j].get('isMachdWebServ')
						else:
							writedata = writedata + " *"
						if("isMachdVPN" in records[j] and records[j].get('isMachdVPN') != ""):
							writedata = writedata + " " + records[j].get('isMachdVPN')
						else:
							writedata = writedata + " *"
						if("rskScore" in records[j] and records[j].get('rskScore') != ""):
							writedata = writedata + " " + records[j].get('rskScore')
						else:
							writedata = writedata + " *"
						if("iUpdateDate" in records[j] and records[j].get('iUpdateDate') != ""):
							writedata = writedata + " " + records[j].get('iUpdateDate')
						else:
							writedata = writedata + " *"
						if("isMachdBlMakt" in records[j] and records[j].get('isMachdBlMakt') != ""):
							writedata = writedata + " " + records[j].get('isMachdBlMakt')
						else:
							writedata = writedata + " *"
						if("isMachCraCall" in records[j] and records[j].get('isMachCraCall') != ""):
							writedata = writedata + " " + records[j].get('isMachCraCall')
						else:
							writedata = writedata + " *"
						if("isMachFraud" in records[j] and records[j].get('isMachFraud') != ""):
							writedata = writedata + " " + records[j].get('isMachFraud')
						else:
							writedata = writedata + " *"
						if("isMachEmpty" in records[j] and records[j].get('isMachEmpty') != ""):
							writedata = writedata + " " + records[j].get('isMachEmpty')
						else:
							writedata = writedata + " *"
						if("isMachYZmobile" in records[j] and records[j].get('isMachYZmobile') != ""):
							writedata = writedata + " " + records[j].get('isMachYZmobile')
						else:
							writedata = writedata + " *"
						if("isMachSmallNo" in records[j] and records[j].get('isMachSmallNo') != ""):
							writedata = writedata + " " + records[j].get('isMachSmallNo')
						else:
							writedata = writedata + " *"
						if("isMachSZNo" in records[j] and records[j].get('isMachSZNo') != ""):
							writedata = writedata + " " + records[j].get('isMachSZNo')
						else:
							writedata = writedata + " *"
						if("mUpdateDate" in records[j] and records[j].get('mUpdateDate') != ""):
							writedata = writedata + " " + records[j].get('mUpdateDate')
						else:
							writedata = writedata + " *"
						if("iRskDesc" in records[j] and records[j].get('iRskDesc') != ""):
							writedata = writedata + " " + records[j].get('iRskDesc')
						else:
							writedata = writedata + " *"
						if("mRskDesc" in records[j] and records[j].get('mRskDesc') != ""):
							writedata = writedata + " " + records[j].get('mRskDesc')
						else:
							writedata = writedata + " *"
						if("badInfoDesc" in records[j] and records[j].get('badInfoDesc') != ""):
							writedata = writedata + " " + records[j].get('badInfoDesc')
						else:
							writedata = writedata + " *"
						if("badInfoTime" in records[j] and records[j].get('badInfoTime') != ""):
							writedata = writedata + " " + records[j].get('badInfoTime')
						else:
							writedata = writedata + " *"
						if("erCode" in records[j] and records[j].get('erCode') != ""):
							writedata = writedata + " " + records[j].get('erCode')
						else:
							writedata = writedata + " *"
						if("erMsg" in records[j] and records[j].get('erMsg') != ""):
							writedata = writedata + " " + records[j].get('erMsg')
						else:
							writedata = writedata + " *"
						writedata = writedata + "\n"
						f8075.write(writedata)




			


