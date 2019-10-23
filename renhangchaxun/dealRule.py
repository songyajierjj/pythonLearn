#!/usr/bin/python
# -*- coding: UTF-8 -*-

data = open("D:/新建文本文档.txt",encoding='GBK')
writeCreditPath = "D:/result.txt"
writeCreditFile = open(writeCreditPath,"a+",encoding='GBK')

for line in data:
	line = line.replace("\n","")
	lineList = line.split(",")
	writeData = ""
	if lineList[4] == "ZR0102":
		writeData = line.replace("\n","")+",1,,,,,,,,,,,,,,,,,,,,\n"
	if lineList[4] == "ZR0103":
		writeData = line.replace("\n","")+",,1,,,,,,,,,,,,,,,,,,,\n"
	if lineList[4] == "ZR0104":
		writeData = line.replace("\n","")+",,,1,,,,,,,,,,,,,,,,,,\n"
	if lineList[4] == "ZR0301":
		writeData = line.replace("\n","")+",,,,1,,,,,,,,,,,,,,,,,\n"
	if lineList[4] == "ZR0303":
		writeData = line.replace("\n","")+",,,,,1,,,,,,,,,,,,,,,,\n"
	if lineList[4] == "BL0201":
		writeData = line.replace("\n","")+",,,,,,1,,,,,,,,,,,,,,,\n"
	if lineList[4] == "HR0101":
		writeData = line.replace("\n","")+",,,,,,,1,,,,,,,,,,,,,,\n"
	if lineList[4] == "HR0102":
		writeData = line.replace("\n","")+",,,,,,,,1,,,,,,,,,,,,,\n"
	if lineList[4] == "HR0103":
		writeData = line.replace("\n","")+",,,,,,,,,1,,,,,,,,,,,,\n"
	if lineList[4] == "HR0104":
		writeData = line.replace("\n","")+",,,,,,,,,,1,,,,,,,,,,,\n"
	if lineList[4] == "HR0105":
		writeData = line.replace("\n","")+",,,,,,,,,,,1,,,,,,,,,,\n"
	if lineList[4] == "HR0106":
		writeData = line.replace("\n","")+",,,,,,,,,,,,1,,,,,,,,,\n"
	if lineList[4] == "HR0107":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,1,,,,,,,,\n"
	if lineList[4] == "HR0108":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,1,,,,,,,\n"
	if lineList[4] == "HR0109":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,1,,,,,,\n"
	if lineList[4] == "HR0201":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,1,,,,,\n"
	if lineList[4] == "HR0202":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,,1,,,,\n"
	if lineList[4] == "HR0203":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,,,1,,,\n"
	if lineList[4] == "HR0204":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,,,,1,,\n"
	if lineList[4] == "HR0205":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,,,,,1,\n"
	if lineList[4] == "HR0206":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,,,,,,1\n"
	if lineList[4] == "0000":
		writeData = line.replace("\n","")+",,,,,,,,,,,,,,,,,,,,,\n"
	writeCreditFile.write(writeData)
