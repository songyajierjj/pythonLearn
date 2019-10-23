#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import json
import os  
import os.path  
import gzip
import datetime

#tar_path为压缩文件路径
readData = json.loads(open("e:\ftpdir\lmk_fin\lianmingka.txt").read())

tar_path = readData['tar_path']
addday = readData['addday']
username = readData['username']
password = readData['password']
ip = readData['ip']

date = datetime.datetime.now()
futureday = datetime.timedelta(days=int(addday))

tar_path = tar_path.replace('xxxxxxxx',(date+futureday).strftime('%Y%m%d'))

if os.path.exists(tar_path):
	with gzip.open(tar_path, 'r') as pf:
		conn = pymysql.connect(host=ip, port=3306, user=username, passwd=password, db='lmk_finance', charset='utf8')
		cursor = conn.cursor()
		for line in pf:
			s = json.loads(str(line,encoding="utf-8"))
			table = s['table']
			operationType = s['type']
			data = s['data']
			sql = ""
			sql1 = ""
			sql2 = ""
			if operationType == "insert":
				sql = "insert into "+ table + " ("
				for (k,v) in data.items():
					sql1 += k+",";
					if v is None:
						sql2 += "null,"
					else:
						sql2 += "'"+str(v)+"',"
				sql += sql1[0:-1]+") values("
				sql += sql2[0:-1]+")"
			elif operationType == "update":
				sql = "update " + table +" set "
				for (k,v) in data.items():
					if v is None:
						sql1 += k + "= null,"
					else:
						sql1 += k + "= '"+str(v)+"',"
					if k == "id":
						sql2 += k + "= '"+ str(v) + "'"
				sql += sql1[0:-1] + " where " + sql2
			elif operationType == "delete":
				sql = "delete from " + table + " where "
				for (k,v) in data.items():
					if k == "id":
						sql1 += k + "= '"+ str(v) + "'"
				sql += sql1
			if sql != "":
				cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()
else:
	print('the path [{}] is not exist!'.format(path))
