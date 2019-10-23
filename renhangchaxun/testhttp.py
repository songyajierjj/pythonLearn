#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from urllib import parse,request
import time
import json

import http.client

writePath = "d:/result.txt"
writeFile = open(writePath,"a+",encoding='GBK')

connection = http.client.HTTPConnection("9.16.15.119",80)
# connection = http.client.HTTPConnection('localhost',8082)
headers = {'Content-type': 'application/json',"Accept": "text/plain"}
writeFile.write("开始请求连接\n")
connection.request('GET', "http://9.16.15.119/shcreditunion", "", headers)
writeFile.write("开始获取连接\n")
response = connection.getresponse()
writeFile.write("请求结果"+line.replace("\n","")+","+str(eval(response.read().decode()))+"\n")
writeFile.close()



