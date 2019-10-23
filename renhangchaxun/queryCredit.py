#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from urllib import parse,request
import time
import json

import http.client
import logging

logging.basicConfig(filename='D:/python/message.log', filemode="w", level=logging.DEBUG)

data = open("D:/python/联名卡2000人查询.txt",encoding='GBK')
writeCreditPath = "D:/python/credit.txt"
writeCreditFile = open(writeCreditPath,"a+",encoding='GBK')

connection = http.client.HTTPConnection('localhost',8081)
headers = {'Content-type': 'application/json',"Accept": "text/plain"}

requestDict = {}

for line in data:
    lineList = line.split(",")
    requestDict['certtype'] = "0"
    requestDict['certno'] = lineList[2]
    requestDict['name'] = lineList[1]
    requestDict['qryreason'] = '01'
    requestDict['qryformat'] = '30'
    requestDict['qrystrategy'] = '1'
    requestDict['effectday'] = '30'
    requestDict['customerId'] = lineList[7]
    dateList = lineList[6].split("/")
    if len(dateList[1]) == 1:
        dateList[1] = "0"+dateList[1]
    if len(dateList[2]) == 1:
        dateList[2] = "0"+dateList[2]
    requestDict['authdate'] = dateList[0]+dateList[1]+dateList[2]+":000000"
    requestDict['partner'] = '自营'
    requestDict['proid'] = '联名卡'
    try:
        json_foo = json.dumps(requestDict)
        logging.info("姓名:"+lineList[1]+",身份证号:"+lineList[3]+".开始调用征信查询")
        connection.request('POST', '/microcredit-creditweb/credit/queryCredit', json_foo, headers)  
        response = connection.getresponse()
        resultData = response.read().decode()
        logging.info("结果:"+resultData)

        responseDict = eval(resultData)
        logging.info("姓名:"+lineList[1]+",身份证号:"+lineList[3]+"结果:"+str(responseDict))
        writeData = line.replace("\n","")
        if "serialnumber" in responseDict:
            writeData = writeData + ","+responseDict['serialnumber']
        else:
            writeData = writeData + ","
        if "status" in responseDict:
            writeData = writeData + ","+responseDict['status']
        else:
            writeData = writeData + ","
        if "statuscode" in responseDict:
            writeData = writeData + ","+responseDict['statuscode']
        else:
            writeData = writeData + ","
        if "error" in responseDict:
            writeData = writeData + ","+responseDict['error']
        else:
            writeData = writeData + ","
        writeData = writeData + "\n"
        writeCreditFile.write(writeData)
    except Exception as err:
        logging.debug("调用credit异常:"+str(err))
    time.sleep(5)
data.close()
writeCreditFile.close()
connection.close()



