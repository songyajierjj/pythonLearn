#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = open("D:/千方/风控平台/批量数据/20180817/xinYanRadar.json",encoding='UTF-8')
writeFile = open("D:/千方/风控平台/批量数据/20180817/xinYanRadar.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["idName"]+","+readData["idNo"]+","+readData["phoneNo"]+","
    writeData = writeData + str(readData["success"])+","+readData["code"]+","+readData["desc"]+","+readData["fee"]
    if "applyReportDetail" in readData:
        applyReportDetailData = readData["applyReportDetail"]
        writeData = writeData + ","+applyReportDetailData["queryOrgCount"]+","+applyReportDetailData["queryCashCount"]
        writeData = writeData + ","+applyReportDetailData["querySumCount"]+","+applyReportDetailData["latestOneMonth"]
        writeData = writeData + ","+applyReportDetailData["latestThreeMonth"]+","+applyReportDetailData["latestSixMonth"]
    else:
        writeData = writeData + ",,,,,,"
    if "behaviorReportDetail" in readData:
        behaviorReportDetailData = readData["behaviorReportDetail"]
        writeData = writeData + ","+behaviorReportDetailData["loansOrgCount"]+","+behaviorReportDetailData["loansCashCount"]
        writeData = writeData + ","+behaviorReportDetailData["historyFailFee"]
    else:
        writeData = writeData + ",,,"
    writeData = writeData +"\n"
    writeFile.write(writeData)
