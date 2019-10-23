#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import datetime





deptcode = "91500108MA5U8F7536"
transType = "3"
transSubType = "21"


#源文件的路径
readData = open("D:/千方/互联网金融/上报正式数据/lmk/6月/201806补报.txt",encoding='GBK')
#生成文件的路径
writePath = "D:/千方/互联网金融/上报正式数据/lmk/6月补报"
txtName = "121EXPORTTRADEINFO.txt"

lineList = []
writeData = ""
if not os.path.exists(writePath):
    os.makedirs(writePath)
    writeFile = open(writePath+"/"+txtName,"a+",encoding='GBK')
else:
    writeFile = open(writePath+"/"+txtName,"a+",encoding='GBK')
i = "first"
for line in readData:
    if i == "first":
        i = "sfsf"
        continue
        
    writeData = ""
    lineList = line.split(",")
    creditAmount = round(int(lineList[12]))/100
    balance = round(int(lineList[24]))/100

    overdueAmount = 0.0
    if lineList[35] == "C" or lineList[35] == "C\n" or lineList[35] == "*" or lineList[35] == "*\n":
        overdueAmount = 0.0
    else:
        overdueAmount = round(int(lineList[26]))/100

    if lineList[35] == "*" or lineList[35] == "*\n":
        billingDate = lineList[9]
    else:
        billingDate = lineList[19]

    writeData = lineList[1]+","+lineList[2]+","+lineList[3]+","+deptcode+","+lineList[7]+","+transType+","+transSubType+","
    writeData = writeData + lineList[9]+","+lineList[10]+","+str(int(creditAmount))+","+billingDate+","+str(int(balance))+","+str(int(overdueAmount))+","+lineList[35]+"\n"
    writeFile.write(writeData)
writeFile.close()



