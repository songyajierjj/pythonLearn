#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from urllib import parse,request
import time
import json

import http.client
import logging

logging.basicConfig(filename='D:/python/message.log', filemode="w", level=logging.DEBUG)
connection = http.client.HTTPConnection('localhost',8081)
headers = {'Content-type': 'application/json',"Accept": "text/plain"}

data = open("D:/python/credit.txt",encoding='GBK')
writeResultPath = "D:/python/result.txt"
writeResultFile = open(writeResultPath,"a+",encoding='GBK')
requestDict = {}

for line in data:
    time.sleep(1)
    lineList = line.split(",")
    print(line)
    print(len(lineList))

    requestDict['serialnumber'] = lineList[8]
    if lineList[9] == "0":
        try:
            json_foo = json.dumps(requestDict)
            logging.info("姓名:"+lineList[1]+",身份证号:"+lineList[3]+".开始调用征信结果")
            connection.request('POST', '/microcredit-creditweb/credit/queryResult', json_foo, headers)  
            response = connection.getresponse()
            resultData = response.read().decode()
            responseDict = eval(resultData)
            logging.info("姓名:"+lineList[1]+",身份证号:"+lineList[3])
            writeData = line.replace("\n","")
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
            writeResultFile.write(writeData)
        except Exception as err:
            logging.debug("调用result异常:"+str(err))
    else:
        writeResultFile.write(line)
data.close()
writeResultFile.close()
connection.close()


