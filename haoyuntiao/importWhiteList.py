#!/usr/bin/python
# -*- coding: UTF-8 -*-

data = open("D:/千方/好运条/用户信息/新老重复用户/2018双11推广用户/好运条授信8000.txt",encoding='GBK')

writeResultPath = "D:/千方/好运条/用户信息/新老重复用户/2018双11推广用户/insert8000.txt"
writeResultFile = open(writeResultPath,"a+",encoding='GBK')

writeResultPath1 = "D:/千方/好运条/用户信息/新老重复用户/2018双11推广用户/repeat8000.txt"
writeResultFile1 = open(writeResultPath1,"a+",encoding='GBK')


import pymysql
conn = pymysql.connect(host='172.17.4.63', port=3306, user='root', passwd='root', db='qfxd_luckloan', charset='utf8')
cursor = conn.cursor()

# i = 1
# sql = "insert into t_user_center_white_list values"
# writeData = ""
# userType = ""
# for line in data:
#     lineList = line.split(",")
#     if lineList[1].replace("\n","") == "1":
#         userType = '余额用户'
#     else:
#         userType = '正常用户'
#     if i%1000 == 0:
#         writeData = writeData + "('"+lineList[0]+"','"+userType+"');\n"
#         writeResultFile.write(sql+writeData)
#         writeData = ""
#     else:
#         writeData = writeData + "('"+lineList[0]+"','"+userType+"'),"
#     i = i +1
# if writeData != "":
#     writeResultFile.write(sql+writeData)

i = 1
sql = "insert into t_user_center_white_list values"
writeData = ""
writeData1 = ""
userType = "正常用户"
for line in data:
    line = line.replace("\n","") 
    sql1 = "SELECT user_id from t_user_center_white_list where user_id = '" + line + "'"
    aa = cursor.execute(sql1)
    info = cursor.fetchmany(aa)
    if len(info) == 0:
        if i%1000 == 0:
            writeData = writeData + "('"+line+"','"+userType+"',11);\n"
            writeResultFile.write(sql+writeData)
            writeData = ""
        else:
            writeData = writeData + "('"+line+"','"+userType+"',11),"
        i = i +1
    else:
        writeData1 = writeData1 + line +"\n"
if writeData != "":
    writeResultFile.write(sql+writeData)
if writeData1 != "":
    writeResultFile1.write(writeData1)

cursor.close()
conn.commit()
conn.close()
