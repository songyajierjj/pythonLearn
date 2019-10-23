#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = open("D:/download/1.txt",encoding='UTF-8')
writeFile = open("D:/download/2.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = i.split(",")
    length = len(readData)
    writeData = readData[6].split(":")[1]+","+readData[7].split(":")[1]+","+readData[8].split(":")[1]+","+readData[length-2]+","+readData[length-1]+","+readData[length]+"\n"

    writeFile.write(writeData)
