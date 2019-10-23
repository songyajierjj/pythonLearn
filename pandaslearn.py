#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import json

filepath = "d:/download/query_result_2018-04-25T03_24_51.454Z.xlsx"

#sheetname指定为读取几个sheet，sheet数目从0开始
#如果sheetname=[0,2]，那代表读取第0页和第2页的sheet
#skiprows=[0]代表读取跳过的行数第0行，不写代表不跳过标题
data = pd.read_excel(filepath,sheetname=[1],skiprows=[-1])
fuser = open("d:/download/1.txt","a",encoding='GBK')

list = []
newList = []
for k,v in data.items():
	list = v.values.tolist()

print(len(list))
for i in range(len(list)):

	jsonData = json.loads(list[i][0])
	if("telephoneNo" in jsonData):
		fuser.write(jsonData['telephoneNo']+"\n")
	else:
		fuser.write("\n")



