#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import json
import os  
import os.path  
import gzip
import datetime
import smtplib
import socket
from email.mime.text import MIMEText
from email.utils import formataddr


date = datetime.datetime.now()
my_sender='qfjr@sinoiov.com' #发件人邮箱账号
my_user='qfjr@sinoiov.com' #收件人邮箱账号
ip=''
port=''
password=''


def execute():
	ret=True

	readData = json.loads(open("e:/ftpdir/lmk_fin/program/lianmingka.txt").read())
	#tar_path为压缩文件路径
	tar_path = readData['tar_path']
	addday = readData['addday']
	username = readData['username']
	password = readData['password']
	ip = readData['ip']
	dbname = readData['dbname']




	
	futureday = datetime.timedelta(days=int(addday))

	tar_path = tar_path.replace('xxxxxxxx',(date+futureday).strftime('%Y%m%d'))

	if os.path.exists(tar_path):
		i = 1;
		with gzip.open(tar_path, 'r') as pf:
			conn = pymysql.connect(host=ip, port=3306, user=username, passwd=password, db=dbname, charset='utf8')
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
							sql2 += "\""+str(v)+"\","
					sql += sql1[0:-1]+") values("
					sql += sql2[0:-1]+")"
				elif operationType == "update":
					sql = "update " + table +" set "
					for (k,v) in data.items():
						if v is None:
							sql1 += k + "= null,"
						else:
							sql1 += k + "= \""+str(v)+"\","
						if k == "id":
							sql2 += k + "= \""+ str(v) + "\""
					sql += sql1[0:-1] + " where " + sql2
				elif operationType == "delete":
					sql = "delete from " + table + " where "
					for (k,v) in data.items():
						if k == "id":
							sql1 += k + "= \""+ str(v) + "\""
					sql += sql1	
				print(i)
				i = i + 1
				if sql != "":
					cursor.execute(sql)	
			conn.commit()
			cursor.close()
			conn.close()
	else:
		print('the path [{}] is not exist!'.format(path))

	return ret

def mail():
	try:
		readData = json.loads(open("e:/ftpdir/lmk_fin/program/lianmingka.txt").read())
		my_sender = readData['emailsender']
		my_user = readData['emailuser']
		emailip = readData['emailip']
		port = readData['emailport']
		password = readData['emailpassword']

		msg=MIMEText('联名卡'+date.strftime('%Y%m%d')+'自动任务执行失败','plain','utf-8')
		msg['From']=formataddr(["千方金融",my_sender])
		msg['Subject']="联名卡自动任务处理结果"
		socket.setdefaulttimeout(10)
		server=smtplib.SMTP_SSL(emailip,port)
		server.login(my_sender,password)
		server.sendmail(my_sender,my_user.split(','),msg.as_string())
		server.quit()
	except Exception:
		print("发送失败")

ret=execute()
