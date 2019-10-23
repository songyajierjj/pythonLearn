#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = open("D:/千方/风控平台/批量数据/20180817/yiXinFraudScreeningBase.json",encoding='UTF-8')
writeFile = open("D:/千方/风控平台/批量数据/20180817/yiXinFraudScreeningBase.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["name"]+","+readData["idNo"]+","+readData["mobile"]+","+readData["code"]
    if "riskResultList" in readData:
        for i in range(len(readData["riskResultList"])):
            if "dataType" in readData["riskResultList"][i]:
                writeData = writeData + "," + readData["riskResultList"][i]["dataType"]
            else:
                writeData = writeData + ","
        if len(readData["riskResultList"]) == 0:
            writeData = writeData + ",,,"
        if len(readData["riskResultList"]) == 1:
            writeData = writeData + ",,"
        if len(readData["riskResultList"]) == 2:
            writeData = writeData + ","
    else:
        writeData = writeData + ",,,"
    if "socialNetwork" in readData:
        if "secondOrderBlackCnt" in readData["socialNetwork"]:
            writeData = writeData + "," + str(readData["socialNetwork"]["secondOrderBlackCnt"])
        else:
            writeData = writeData + "," 
    else:
        writeData = writeData + "," 
    writeData = writeData + "\n"
    writeFile.write(writeData) 
