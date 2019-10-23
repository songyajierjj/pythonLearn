#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = open("D:/千方/风控平台/批量数据/20180817/xinYanOperator.json",encoding='UTF-8')
writeFile = open("D:/千方/风控平台/批量数据/20180817/xinYanOperator.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["mobile"]+","+str(readData["success"])
    if readData["success"] == True:
        writeData = writeData + ","+readData["fee"]
        if "length" in readData:
        	writeData = writeData + "," + readData["length"]
        else:
        	writeData = writeData + ","
        if "status" in readData:
        	writeData = writeData + "," + readData["status"]
        else:
        	writeData = writeData + ","
        writeData = writeData +",,"
    else:
        writeData = writeData + ",,,," + readData["errorCode"]+","+readData["errorMsg"]
    writeData = writeData +"\n"
    writeFile.write(writeData)

