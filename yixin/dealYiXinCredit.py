#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = open("D:/千方/风控平台/批量数据/20180817/yiXinCreditEvaluationCustomized.json",encoding='UTF-8')
writeFile = open("D:/千方/风控平台/批量数据/20180817/yiXinCreditEvaluationCustomized.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["name"]+","+readData["idNo"]+","+str(readData["success"])+","+readData["code"]
    if "loanRecords" in readData:
        if "historyOverdue" in readData["loanRecords"]:
            writeData = writeData + "," + str(readData["loanRecords"]["historyOverdue"])
        else:
            writeData = writeData + ","
        if "historyOverdueM3" in readData["loanRecords"]:
            writeData = writeData + "," + str(readData["loanRecords"]["historyOverdueM3"])
        else:
            writeData = writeData + ","
        if "historyOverdueM6" in readData["loanRecords"]:
            writeData = writeData + "," + str(readData["loanRecords"]["historyOverdueM6"])
        else:
            writeData = writeData + ","
    else:
        writeData = writeData + ",,,"

    if "queriedHistory" in readData:
        if "otherOrgCount" in readData["queriedHistory"]:
            writeData = writeData + "," + str(readData["queriedHistory"]["otherOrgCount"])
        else:
            writeData = writeData + ","
        if "orgCountTotal" in readData["queriedHistory"]:
            writeData = writeData + "," + str(readData["queriedHistory"]["orgCountTotal"])
        else:
            writeData = writeData + ","
    else:
        writeData = writeData + ",,"
    writeData = writeData + "\n"
    writeFile.write(writeData)

