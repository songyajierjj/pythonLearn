#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import datetime

startDate = '20180901'
endDate = '20180930'
year = 2018
month = 9
day = 30

#源文件的路径
readData = open("D:/千方/互联网金融/上报正式数据/etc/201809.txt",encoding='GBK')

deptcode = "91500108MA5U8F7536"
transType = "3"
transSubType = "21"



#生成文件的路径
writePath = "D:/千方/互联网金融/上报正式数据/etc/20180"+str(month)
txtName = "121EXPORTTRADEINFO.txt"

lineList = []
writeData = ""
if not os.path.exists(writePath):
    os.makedirs(writePath)
    writeFile = open(writePath+"/"+txtName,"a+",encoding='GBK')
else:
    writeFile = open(writePath+"/"+txtName,"a+",encoding='GBK')
name = ""
cardNo = ""

for line in readData:
    writeData = ""
    lineList = line.split(",")
    name = lineList[1]
    cardNo = lineList[2]
    d1 = datetime.datetime(year, month, day)
    d2 = datetime.datetime(int(lineList[5][0:4]),int(lineList[5][4:6]),int(lineList[5][6:8]))
    overduedays = (d1 - d2).days
    status = overduedays//30+1
    interest = int(lineList[3])*24*overduedays//36500
    overdueAmount = int(lineList[3])+interest
    lineList[7] = lineList[7].replace("\n","")
    if lineList[7] == "6" and int(lineList[4]) < int(startDate) :
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + endDate + ","+lineList[3]+","+str(overdueAmount)+","+str(status)+"\n"
        writeFile.write(writeData)
    elif lineList[7] == "6" and int(lineList[4]) >= int(startDate) and int(lineList[5]) <= int(endDate):
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + lineList[4]+","+lineList[3]+",0,*\n"
        writeFile.write(writeData)
        writeData = ""
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + endDate + ","+lineList[3]+","+str(overdueAmount)+","+str(status)+"\n"
        writeFile.write(writeData)
    elif lineList[7] == "6" and int(lineList[4]) >= int(startDate) and int(lineList[5]) > int(endDate):
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + lineList[4]+","+lineList[3]+",0,*\n"
        writeFile.write(writeData)
    elif lineList[7] == "8" and int(lineList[5]) <= int(endDate):
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + lineList[4]+","+lineList[3]+",0,*\n"
        writeFile.write(writeData)
        writeData = ""
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + lineList[5]+",0,0,C\n"
        writeFile.write(writeData)
    elif lineList[7] == "8" and int(lineList[5]) > int(endDate):
        writeData = writeData + name+",0,"+cardNo+","+deptcode+","+lineList[0]+","+transType+","+transSubType+","+lineList[4]+","+lineList[5]+","+lineList[3]+","
        writeData = writeData + lineList[4]+","+lineList[3]+",0,*\n"
        writeFile.write(writeData)
writeFile.close()
