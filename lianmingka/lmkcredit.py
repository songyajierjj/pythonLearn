#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import datetime
import os
import os.path

tradeInfoTitle = "NAME,CERTTYPE,CERTNO,DEPTCODE,GENERALTYPE,TYPE,ACCOUNT,AREACODE,DATEOPENED,DATECLOSED,CURRENCY,CREDITLIMIT,SHAREACCOUNT," 
tradeInfoTitle = tradeInfoTitle + "MAXDEBT,GUARANTEEWAY,TERMSFREQ,MONTHDURATION,MONTHUNPAID,BILLINGDATE,RECENTPAYDATE,RECENTPAYAMOUNT,SCHEDULEDAMOUNT,ACTUALPAYAMOUNT,"
tradeInfoTitle = tradeInfoTitle + "BALANCE,CURTERMSPASTDUE,AMOUNTPASTDUE,AMOUNTPASTDUE30,AMOUNTPASTDUE60,AMOUNTPASTDUE90,APASTDUE180,TERMSPASTDUE,MAXTERMSPASTDUE,CLASS5STAT,"
tradeInfoTitle = tradeInfoTitle + "ACCOUNTSTAT,PAYSTAT24MONTH,UNPAID180,FIRSTPAYDATE,RATE,BRATE"
tradeInfoTxtName = "EXPORTTRADEINFO.txt"
addressInfoTitle = "NAME,CERTTYPE,CERTNO,DEPTCODE,RESIDENCE,RESZIP,RESCONDITION"
addredsTxtName = "EXPORTADDRESSINFO.txt"
empInfoTitle = "NAME,CERTTYPE,CERTNO,DEPTCODE,OCCUPATION,COMPANY,INDUSTRY,OCCADDRESS,OCCZIP,STARTYEAR,DUTY,CASTE,ANNUALINCOME"
empInfoTxtName = "EXPORTEMPINFO.txt"
personInfoTitle = "NAME,CERTTYPE,CERTNO,DEPTCODE,GENDER,BIRTHDAY,MARRIAGE,EDULEVEL,EDUDEGREE,SPOUSE_NAME,SPOUSE_CERTNO,SPOUSE_CERTTYPE,SPOUSE_OFFICE,SPOUSE_TEL,HOMETEL,MOBILETEL,OFFICETEL,EMAIL,ADDRESS,ZIP,RESIDENCE"
personInfoTxtName = "EXPORTPERSONINFO.txt"

#生成文件的路径
path = "D:/千方/风控平台/人行征信/个人征信报送/报送数据/联名卡/2019年4月/"

#源文件的路径
readData = open("D:/千方/风控平台/人行征信/个人征信报送/报送源数据/联名卡/联名卡4月上报最终版本.txt",encoding='GBK')
i = "first"

deptCode = "N10156530H0081"
addressMode = ",999999,9"
empMode = ",6,暂缺,Z,,,,9,9,"
personMode1 = ",90,99,9,,,,,,,"
personMode2 = ",,,"
personMode3 = ",999999,"

lineList = []
for line in readData:
    if i == "first":
        i = "sfsf"
        continue
    else:
        line = line.replace("\\N","")
        lineList = line.split(",")

        tradeWriteData = ""
        openDate = ""
        reportDate = ""
        closeDate = ""
        billingDate = ""
        recentDate = ""
        isOpen = "2"
        isReallyOpen = "2"

        addressWriteData = ""
        empWritedata = ""
        personWriteData = ""
        for j in range(len(lineList)):

            if lineList[35] == "*":
                isOpen = "1"
                if lineList[9] == lineList[19]:
                    isReallyOpen = "1"
            else:
                isOpen = "2"
            if j == 0:
                continue
            elif j > 39:
                break
            elif j == 9:
                openDate = datetime.datetime.strptime(lineList[j],'%Y%m%d').strftime('%Y%m%d')
                tradeWriteData = tradeWriteData + openDate + ","
                if isOpen == "1":
                    reportDate = (datetime.datetime.strptime(lineList[19],'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
            elif j == 10:
                closeDate = datetime.datetime.strptime(lineList[j],'%Y%m%d').strftime('%Y%m%d')
                tradeWriteData = tradeWriteData + closeDate + ","
            elif j == 12 or j == 13 or j == 14 or j == 21 or j == 22 or j == 23 or j == 24 or j == 26 or j == 27 or j == 28 or j == 29 or j == 30: 
                if lineList[j] == "":
                    amount = 0
                else:
                    amount = round(int(lineList[j])/100)
                tradeWriteData = tradeWriteData + str(amount) + ","
            elif j == 19:
                if isOpen == "2":
                    reportDate = (datetime.datetime.strptime(lineList[j],'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
                billingDate = datetime.datetime.strptime(lineList[j],'%Y%m%d').strftime('%Y%m%d')
                tradeWriteData = tradeWriteData + billingDate + ","
            elif j == 20:
                if isOpen == "1":
                    recentDate = datetime.datetime.strptime(lineList[9],'%Y%m%d').strftime('%Y%m%d')
                    tradeWriteData = tradeWriteData + recentDate + ","
                if isOpen == "2":
                    recentDate = datetime.datetime.strptime(lineList[j],'%Y%m%d').strftime('%Y%m%d')
                    tradeWriteData = tradeWriteData + recentDate + ","
            elif j == 22:
                if isOpen == "1":
                    tradeWriteData = tradeWriteData + "0,"
                else:
                    tradeWriteData = tradeWriteData + lineList[j] + ","
            else:
                tradeWriteData = tradeWriteData + lineList[j] + ","
        tradeWriteData = tradeWriteData[0:-1]

        txtPath = path+reportDate
        if not os.path.exists(txtPath):
            os.makedirs(txtPath)
            tradeFile = open(txtPath+"/"+tradeInfoTxtName,"a+",encoding='GBK')
            tradeFile.write(tradeInfoTitle+"\n")
            if isOpen == "1" and isReallyOpen == "1":
                addressFile = open(txtPath+"/"+addredsTxtName,"a+",encoding='GBK')
                addressFile.write(addressInfoTitle+"\n")
                empFile = open(txtPath+"/"+empInfoTxtName,"a+",encoding='GBK')
                empFile.write(empInfoTitle+"\n")
                personFile = open(txtPath+"/"+personInfoTxtName,"a+",encoding='GBK')
                personFile.write(personInfoTitle+"\n")
        else:
            tradeFile = open(txtPath+"/"+tradeInfoTxtName,"a+",encoding='GBK')
            if isOpen == "1" and isReallyOpen == "1":
                addressFile = open(txtPath+"/"+addredsTxtName,"a+",encoding='GBK')
                empFile = open(txtPath+"/"+empInfoTxtName,"a+",encoding='GBK')
                personFile = open(txtPath+"/"+personInfoTxtName,"a+",encoding='GBK')

        tradeFile.write(tradeWriteData+"\n")
        tradeFile.close()

        if isOpen == "1" and isReallyOpen == "1":
            address = lineList[43]
            address = address.strip()
            if len(address) > 30:
                address = address[0:29]
            addressFile.write(lineList[1] +","+lineList[2]+","+lineList[3]+","+deptCode+","+address+addressMode+"\n")
            addressFile.close()

            empFile.write(lineList[1] +","+lineList[2]+","+lineList[3]+","+deptCode+empMode+"\n")
            empFile.close()

            gender = int(lineList[3][16:17])
            if gender%2 == 0:
                gender = 2
            else:
                gender = 1

            personFile.write(lineList[1] +","+lineList[2]+","+lineList[3]+","+deptCode+","+str(gender)+","+lineList[41]+personMode1+lineList[42]+personMode2+address+personMode3+address+"\n")
            personFile.close()