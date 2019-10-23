#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

fuser = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/用户身份证姓名.txt",encoding='GBK')
userdict = {}
for i in fuser.readlines():
	userlist = i.split(" ")
	if(len(userlist) > 2):
		userdict[userlist[1]+"_"+userlist[2].replace("\n","")] = "123"

#w写文本文件 wb写二进制文件 a追加写文件
fapplyloan = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/bairongApplyLoanStr.json",encoding='UTF-8')
fbairongapply = open("D:/千方/CMS+决策引擎/批量数据/20171220/qianfang/applyloan.txt","a",encoding='GBK')

for i in fapplyloan.readlines():
	readData = json.loads(i)
	key = readData['userName']+"_"+readData['idEntityId']
	if(key in userdict):
		if(readData['code'] == '00'):
			writeData = readData['userName']+" "+readData['phone']+" "+readData['idEntityId']+" "+readData['createTime']+" "+readData['code']+" "+readData['flag_applyloanstr']+" "+readData['swift_number']
			if("als_d7_id_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_id_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_id_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_pp_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_pp_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d7_cell_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_d7_cell_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_cell_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_d15_cell_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_d15_id_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_d15_id_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_id_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_id_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m1_cell_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m1_cell_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m3_id_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_id_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_id_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_bank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_id_bank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_id_nbank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_id_nbank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m3_cell_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_cell_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_cell_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_bank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_cell_bank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m3_cell_nbank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m3_cell_nbank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m6_id_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_id_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_id_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_bank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_id_bank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_id_nbank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_id_nbank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m6_cell_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_cell_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_cell_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_bank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_cell_bank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m6_cell_nbank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m6_cell_nbank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_selfnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_selfnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_p2p_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_p2p_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_mc_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_mc_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_ca_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_ca_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_cf_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_cf_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_com_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_com_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_oth_allnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_oth_allnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_p2p_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_p2p_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_mc_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_mc_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_ca_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_ca_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_cf_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_cf_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_com_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_com_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_oth_orgnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_oth_orgnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m12_id_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_id_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_id_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_bank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_id_bank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_id_nbank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_id_nbank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m12_cell_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_cell_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_cell_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_bank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_cell_bank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_tot_mons" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_tot_mons"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_avg_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_avg_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_max_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_max_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_min_monnum" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_min_monnum"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_max_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_max_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_m12_cell_nbank_min_inteday" in readData):
				writeData = writeData + " " + readData["als_m12_cell_nbank_min_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_fst_id_bank_inteday" in readData):
				writeData = writeData + " " + readData["als_fst_id_bank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_fst_id_nbank_inteday" in readData):
				writeData = writeData + " " + readData["als_fst_id_nbank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_fst_cell_bank_inteday" in readData):
				writeData = writeData + " " + readData["als_fst_cell_bank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_fst_cell_nbank_inteday" in readData):
				writeData = writeData + " " + readData["als_fst_cell_nbank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_id_bank_inteday" in readData):
				writeData = writeData + " " + readData["als_lst_id_bank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_id_bank_consnum" in readData):
				writeData = writeData + " " + readData["als_lst_id_bank_consnum"]
			else:
			    writeData = writeData + " *"
			if("als_lst_id_bank_csinteday" in readData):
				writeData = writeData + " " + readData["als_lst_id_bank_csinteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_id_nbank_inteday" in readData):
				writeData = writeData + " " + readData["als_lst_id_nbank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_id_nbank_consnum" in readData):
				writeData = writeData + " " + readData["als_lst_id_nbank_consnum"]
			else:
			    writeData = writeData + " *"
			if("als_lst_id_nbank_csinteday" in readData):
				writeData = writeData + " " + readData["als_lst_id_nbank_csinteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_cell_bank_inteday" in readData):
				writeData = writeData + " " + readData["als_lst_cell_bank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_cell_bank_consnum" in readData):
				writeData = writeData + " " + readData["als_lst_cell_bank_consnum"]
			else:
			    writeData = writeData + " *"
			if("als_lst_cell_bank_csinteday" in readData):
				writeData = writeData + " " + readData["als_lst_cell_bank_csinteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_cell_nbank_inteday" in readData):
				writeData = writeData + " " + readData["als_lst_cell_nbank_inteday"]
			else:
			    writeData = writeData + " *"
			if("als_lst_cell_nbank_consnum" in readData):
				writeData = writeData + " " + readData["als_lst_cell_nbank_consnum"]
			else:
			    writeData = writeData + " *"
			if("als_lst_cell_nbank_csinteday" in readData):
				writeData = writeData + " " + readData["als_lst_cell_nbank_csinteday"]
			else:
			    writeData = writeData + " *"

			writeData = writeData + "\n"

			fbairongapply.write(writeData)