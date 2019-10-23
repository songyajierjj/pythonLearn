#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from urllib import parse,request
import time
import json

import http.client

data = open("C:/python/data.txt",encoding='GBK')
writePath = "C:/python/result.txt"
writeFile = open(writePath,"a+",encoding='GBK')

requestDict = {}
userDict = {}

readData = json.loads(open("c:/python/config.txt").read())
ip = readData['ip']
url = readData['url']
port = readData['port']

if port == "":
    connection = http.client.HTTPConnection(ip)
else:
    connection = http.client.HTTPConnection(ip,int(port))
# connection = http.client.HTTPConnection('localhost',8082)
headers = {'Content-type': 'application/json',"Accept": "text/plain"}

for line in data:
    line = line.replace("\n","")
    if line == "":
        break
    lineList = line.split(",")
    nowTime = time.time()
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
    userDict['userId'] = nowTime
    userDict['userName'] = lineList[0]
    userDict['identityId'] = lineList[1]
    userDict['phone'] = lineList[2]
    userDict['personalCreditCfcaNo'] = lineList[3]
    userDict['createTime'] = lineList[4]
    requestDict['userMap'] = userDict
    requestDict['sendId'] = str(nowTime)
    requestDict['transType'] = "4"

    
    json_foo = json.dumps(requestDict)

    connection.request('POST', url, json_foo, headers)
    
    response = connection.getresponse()
    writeFile.write(line.replace("\n","")+","+str(eval(response.read().decode())['result'])+"\n")
data.close()
writeFile.close()



