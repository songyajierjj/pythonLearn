#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import datetime
import os
import os.path
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='GBK')


filepath = "D:/千方/风控平台/人行征信/企业征信报送/20180917去无中征码-所有企业机构信用码信息录入.xlsx"

writePath = "D:/千方/风控平台/人行征信/企业征信报送/20180917/"

def getValue(value):
    if value == "nan" or value == "NaT":
        return ""
    else:
        return value
def getDate(value):
    if value == "nan" or value == "NaT":
        return ""
    else:
        return ""

base = pd.read_excel(filepath,sheet_name=[1,1])
baseTxtName = "base.txt"
baseTxtTitle = "CUSTID,REPORTORG,DEPTCODE,ORGCODE,CUSTTYPE,ORGCRDNO,ORGNO,RERETP,RERECODE,GENTAXNO,LOCTAXNO,ACCPERMITNO,LNCARDNO\n"
baseExcel = {}
baseDict = {}
baseCustIdDict = {}
for k,v in base.items():
    baseExcel = v.to_dict()
for i in range(len(baseExcel['CUSTID'])):
    value1 = str(baseExcel['CUSTID'][i])
    value2 = str(baseExcel['REPORTORG'][i])
    value3 = str(baseExcel['DEPTCODE'][i])
    value4 = str(baseExcel['ORGCODE'][i])
    value5 = str(baseExcel['CUSTTYPE'][i])
    value6 = str(baseExcel['ORGCRDNO'][i])
    value7 = str(baseExcel['ORGNO'][i])
    value8 = str(baseExcel['RERETP'][i])
    value9 = str(baseExcel['RERECODE'][i])
    value10 = str(baseExcel['GENTAXNO'][i])
    value11 = str(baseExcel['LOCTAXNO'][i])
    value12 = getValue(str(baseExcel['ACCPERMITNO'][i]))

    value13 = str(baseExcel['LNCARDNO'][i])
    baseDict[value13] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+","+value10+","+value11+","+value12+","+value13+"\n"
    baseCustIdDict[value13] = value1


attribute = pd.read_excel(filepath,sheet_name=[2,2])
attributeTxtName = "attribute.txt"
attributeTxtTitle = "CUSTID,REPORTORG,OCNM,OFNM,REGADD,NATION,REGION,REREDT,LICRETDT,BUSSCOPE,REGCAPCUR,REGCAPITAL,ORGTYPE,ORGCATEGORY,INDUCLASS,ECONOMICTYPE\n"
attributeExcel = {}
attributeDict = {}
for k,v in attribute.items():
    attributeExcel = v.to_dict()
for i in range(len(attributeExcel['CUSTID'])):
    value1 = str(attributeExcel['CUSTID'][i])
    value2 = str(attributeExcel['REPORTORG'][i])
    value3 = str(attributeExcel['OCNM'][i])
    value4 = getValue(str(attributeExcel['OFNM'][i]))
    value5 = str(attributeExcel['REGADD'][i])
    value6 = str(attributeExcel['NATION'][i])
    value7 = str(attributeExcel['REGION'][i])
    value8 = str(attributeExcel['REREDT'][i])
    value9 = str(attributeExcel['LICRETDT'][i])
    value10 = str(attributeExcel['BUSSCOPE'][i])
    value11 = str(attributeExcel['REGCAPCUR'][i])
    value12 = str(attributeExcel['REGCAPITAL'][i])
    value13 = str(attributeExcel['ORGTYPE'][i])
    value14 = str(attributeExcel['ORGCATEGORY'][i])
    value15 = getValue(str(attributeExcel['INDUCLASS'][i]))
    value16 = str(attributeExcel['ECONOMICTYPE'][i])
    attributeDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+","+value10+","
    attributeDict[value1] = attributeDict[value1] + value11+","+value12+","+value13+","+value14+","+value15+","+value16+"\n"


status = pd.read_excel(filepath,sheet_name=[3,3])
statusTxtName = "status.txt"
statusTxtTitle = "CUSTID,REPORTORG,ACCSTATUS,ENTSCALE,ORGSTATUS\n"
statusExcel={}
statusDict = {}
for k,v in status.items():
    statusExcel = v.to_dict()
for i in range(len(statusExcel['CUSTID'])):
    value1 = str(statusExcel['CUSTID'][i])
    value2 = str(statusExcel['REPORTORG'][i])
    value3 = str(statusExcel['ACCSTATUS'][i])
    value4 = str(statusExcel['ENTSCALE'][i])
    value5 = str(statusExcel['ORGSTATUS'][i])
    statusDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+"\n"


contact = pd.read_excel(filepath,sheet_name=[4,4])
contactTxtName = "contact.txt"
contactTxtTitle = "CUSTID,REPORTORG,ORGADDRESS,ORGTEL,FINDEPTEL\n"
contactExcel = {}
contactDict = {}
for k,v in contact.items():
    contactExcel = v.to_dict()
for i in range(len(contactExcel['CUSTID'])):
    value1 = str(contactExcel['CUSTID'][i])
    value2 = str(contactExcel['REPORTORG'][i])
    value3 = str(contactExcel['ORGADDRESS'][i])
    value4 = getValue(str(contactExcel['ORGTEL'][i]))
    value5 = getValue(str(contactExcel['FINDEPTEL'][i]))
    contactDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+"\n"


executive = pd.read_excel(filepath,sheet_name=[5,5])
executiveTxtName = "executive.txt"
executiveTxtTitle = "CUSTID,REPORTORG,EXECUTIVETP,NAME,CERTTYPE,CERTNO\n"
executiveExcel = {}
executiveDict = {}
for k,v in executive.items():
    executiveExcel = v.to_dict()
for i in range(len(executiveExcel['CUSTID'])):
    value1 = str(executiveExcel['CUSTID'][i])
    value2 = str(executiveExcel['REPORTORG'][i])
    value3 = str(executiveExcel['EXECUTIVETP'][i])
    value4 = str(executiveExcel['NAME'][i])
    value5 = str(executiveExcel['CERTTYPE'][i])
    value6 = str(executiveExcel['CERTNO'][i])
    executiveDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+"\n"


stock = pd.read_excel(filepath,sheet_name=[6,6])
stockTxtName = "stock.txt"
stockTxtTitle = "CUSTID,REPORTORG,STOHOLTYPE,STOHOLNAME,CERTTYPE,CERTNO,ORGNO,ORGCRDNO,STAKERATIO\n"
stockExcel = {}
stockDict = {}
for k,v in stock.items():
    stockExcel = v.to_dict()
for i in range(len(stockExcel['CUSTID'])):
    value1 = str(stockExcel['CUSTID'][i])
    value2 = str(stockExcel['REPORTORG'][i])
    value3 = str(stockExcel['STOHOLTYPE'][i])
    value4 = str(stockExcel['STOHOLNAME'][i])
    if stockExcel['CERTTYPE'][i] == 0:
        value5 = "0"
    else:
        value5 = "07"
    value6 = str(stockExcel['CERTNO'][i])
    value7 = getValue(str(stockExcel['ORGNO'][i]))
    value8 = getValue(str(stockExcel['ORGCRDNO'][i]))
    value9 = str(stockExcel['STAKERATIO'][i])
    stockDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+"\n"


relatedent = pd.read_excel(filepath,sheet_name=[7,7])
relatedentTxtName = "relatedent.txt"
relatedentTxtTitle = "CUSTID,REPORTORG,RELTYPE,RELNAME,RERETP,RERECODE,ORGNO,ORGCRDNO\n"
relatedentExcel = {}
relatedentDict = {}
for k,v in relatedent.items():
    relatedentExcel = v.to_dict()
for i in range(len(relatedentExcel['CUSTID'])):
    value1 = str(relatedentExcel['CUSTID'][i])
    value2 = str(relatedentExcel['REPORTORG'][i])
    value3 = str(relatedentExcel['RELTYPE'][i])
    value4 = str(relatedentExcel['RELNAME'][i])
    value5 = str(relatedentExcel['RERETP'][i])
    value6 = str(relatedentExcel['RERECODE'][i])
    value7 = str(relatedentExcel['ORGNO'][i])
    value8 = getValue(str(relatedentExcel['ORGCRDNO'][i]))
    relatedentDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+"\n"


superiororg = pd.read_excel(filepath,sheet_name=[8,8])
superiororgTxtName = "superiororg.txt"
superiororgTxtTitle = "CUSTID,REPORTORG,SUPERNAME,RERETP,RERECODE,ORGNO,ORGCRDNO\n"
superiororgExcel = {}
superiororgDict = {}
for k,v in superiororg.items():
    superiororgExcel = v.to_dict()
for i in range(len(superiororgExcel['CUSTID'])):
    value1 = str(superiororgExcel['CUSTID'][i])
    value2 = str(superiororgExcel['REPORTORG'][i])
    value3 = str(superiororgExcel['SUPERNAME'][i])
    value4 = str(superiororgExcel['RERETP'][i])
    value5 = str(superiororgExcel['RERECODE'][i])
    value6 = str(superiororgExcel['ORGNO'][i])
    value7 = str(superiororgExcel['ORGCRDNO'][i])
    superiororgDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+"\n"


loanCon = pd.read_excel(filepath,sheet_name=[9,9])
loanConTxtName = "EXPORTLOANCONINFO.txt"
loanConTxtTitle = "LNCONTCODE,DEPTCODE,BUSSDT,BORRNM,LNCARDNO,PROTCODE,CONTLNDT,CONTENDDT,BANKSIGN,CONTEST\n"
loanConExcel = {}
loanConDict = {}
loanConStatusDict = {}
for k,v in loanCon.items():
    loanConExcel = v.to_dict()
for i in range(len(loanConExcel['LNCONTCODE'])):
    value1 = str(loanConExcel['LNCONTCODE'][i])
    value2 = str(loanConExcel['DEPTCODE'][i])
    value3 = str(loanConExcel['BUSSDT'][i])
    value4 = str(loanConExcel['BORRNM'][i])
    value5 = str(loanConExcel['LNCARDNO'][i])
    value6 = getValue(str(loanConExcel['PROTCODE'][i]))
    value7 = str(loanConExcel['CONTLNDT'][i])
    value8 = str(loanConExcel['CONTENDDT'][i])
    value9 = str(loanConExcel['BANKSIGN'][i])
    value10 = str(loanConExcel['CONTEST'][i])
    loanConDict[value1] = value3
    if "2" == value10:
        loanConStatusDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+",2\n"
    reportDate = (datetime.datetime.strptime(value3,'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+loanConTxtName):
        loanConFile = open(loanPath+"/"+loanConTxtName,"a+",encoding='GBK')
        loanConFile.write(loanConTxtTitle)
    else:
        loanConFile = open(loanPath+"/"+loanConTxtName,"a+",encoding='GBK')

    loanConFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+",1\n")

    if value5 in baseCustIdDict:
        orgPath = writePath+reportDate+"org"
        if not os.path.exists(orgPath):
            os.makedirs(orgPath)

        baseFile = open(orgPath+"/"+baseTxtName,"a+",encoding='GBK')
        baseFile.write(baseDict[value5])
        baseFile.close()
        if baseCustIdDict[value5] in attributeDict:
            attributeFile = open(orgPath+"/"+attributeTxtName,"a+",encoding='GBK')
            attributeFile.write(attributeDict[baseCustIdDict[value5]])
            attributeFile.close()
        if baseCustIdDict[value5] in statusDict:
            statusFile = open(orgPath+"/"+statusTxtName,"a+",encoding='GBK')
            statusFile.write(statusDict[baseCustIdDict[value5]])
            statusFile.close()
        if baseCustIdDict[value5] in contactDict:
            contactFile = open(orgPath+"/"+contactTxtName,"a+",encoding='GBK')
            contactFile.write(contactDict[baseCustIdDict[value5]])
            contactFile.close()
        if baseCustIdDict[value5] in executiveDict:
            executiveFile = open(orgPath+"/"+executiveTxtName,"a+",encoding='GBK')
            executiveFile.write(executiveDict[baseCustIdDict[value5]])
            executiveFile.close()
        if baseCustIdDict[value5] in stockDict:
            stockFile = open(orgPath+"/"+stockTxtName,"a+",encoding='GBK')
            stockFile.write(stockDict[baseCustIdDict[value5]])
            stockFile.close()
        if baseCustIdDict[value5] in relatedentDict:
            relatedentFile = open(orgPath+"/"+relatedentTxtName,"a+",encoding='GBK')
            relatedentFile.write(relatedentDict[baseCustIdDict[value5]])
            relatedentFile.close()
        if baseCustIdDict[value5] in superiororgDict:
            superiororgFile = open(orgPath+"/"+superiororgTxtName,"a+",encoding='GBK')
            superiororgFile.write(superiororgDict[baseCustIdDict[value5]])
            superiororgFile.close()
        baseCustIdDict.pop(value5)


dueBill = pd.read_excel(filepath,sheet_name=[11,11])
dueBillTxtName = "EXPORTDUEBILLINFO.txt"
dueBillTxtTitle = "LNCONTCODE,DUECODE,DEPTCODE,LNCARDNO,BUSSDT,CURTP,LNDUEAMT,DUELNDT,DUELNRETDT,LNTP,LNMODA,LNHABIT,LNPURP,LNTYPE,FOURCLASS,FIVECLASS,BRATE,RATE\n"
dueBillExcel = {}
dueBillDict = {}
dueBillCountDict = {}
for k,v in dueBill.items():
    dueBillExcel = v.to_dict()
isDueBillTitleWrite = "2"
for i in range(len(dueBillExcel['LNCONTCODE'])):
    value1 = str(dueBillExcel['LNCONTCODE'][i])
    value2 = str(dueBillExcel['DUECODE'][i])
    value3 = str(dueBillExcel['DEPTCODE'][i])
    value4 = str(dueBillExcel['LNCARDNO'][i])
    value5 = str(dueBillExcel['BUSSDT'][i])
    value6 = str(dueBillExcel['CURTP'][i])
    value7 = str(dueBillExcel['LNDUEAMT'][i])
    value8 = str(dueBillExcel['DUELNDT'][i])
    value9 = str(dueBillExcel['DUELNRETDT'][i])
    value10 = str(dueBillExcel['LNTP'][i])
    value11 = str(dueBillExcel['LNMODA'][i])
    value12 = str(dueBillExcel['LNHABIT'][i])
    value13 = str(dueBillExcel['LNPURP'][i])
    value14 = str(dueBillExcel['LNTYPE'][i])
    value15 = getValue(str(dueBillExcel['FOURCLASS'][i]))
    value16 = str(dueBillExcel['FIVECLASS'][i])
    value17 = str(dueBillExcel['BRATE'][i])
    value18 = str(dueBillExcel['RATE'][i])
    dueBillDict[value1+"_"+value5] = value7
    if value1 in dueBillCountDict:
        dueBillCountDict[value1] = dueBillCountDict[value1] + float(value7)
    else:
        dueBillCountDict[value1] = float(value7)
    reportDate = (datetime.datetime.strptime(value5,'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+dueBillTxtName):
        dueBillFile = open(loanPath+"/"+dueBillTxtName,"a+",encoding='GBK')
        dueBillFile.write(dueBillTxtTitle)
    else:
        dueBillFile = open(loanPath+"/"+dueBillTxtName,"a+",encoding='GBK')
    
    dueBillFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+","+value10+",")
    dueBillFile.write(value11+","+value12+","+value13+","+value14+","+value15+","+value16+","+value17+","+value18+"\n")
    dueBillFile.close()


loanAmt = pd.read_excel(filepath,sheet_name=[10,10])
loanAmtTxtName = "EXPORTLOANAMTINFO.txt"
loanAmtTxtTitle = "LNCONTCODE,DEPTCODE,LNCARDNO,BUSSDT,CURTP,LNCONTAMT,USINGBAL\n"
loanAmtExcel = {}
for k,v in loanAmt.items():
    loanAmtExcel = v.to_dict()
for i in range(len(loanAmtExcel['LNCONTCODE'])):
    value1 = str(loanAmtExcel['LNCONTCODE'][i])
    value2 = str(loanAmtExcel['DEPTCODE'][i])
    value3 = str(loanAmtExcel['LNCARDNO'][i])
    value4 = str(loanAmtExcel['BUSSDT'][i])
    value5 = str(loanAmtExcel['CURTP'][i])
    value6 = str(loanAmtExcel['LNCONTAMT'][i])

    reportDate = (datetime.datetime.strptime(value4,'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+loanAmtTxtName):
        loanAmtFile = open(loanPath+"/"+loanAmtTxtName,"a+",encoding='GBK')
        loanAmtFile.write(loanAmtTxtTitle)
    else:
        loanAmtFile = open(loanPath+"/"+loanAmtTxtName,"a+",encoding='GBK')

    if (value1+"_"+value4) in dueBillDict:
        billAmount = dueBillDict[value1+"_"+value4]
        useAmount = round(float(value6)-float(billAmount),2)
        loanAmtFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+str(useAmount)+"\n")
    else:
        loanAmtFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value6+"\n")
    loanAmtFile.close()


# inteInfo = pd.read_excel(filepath,sheet_name=[13,13])
# inteInfoTxtName = "EXPORTINTEINFO.txt"
# inteInfoTxtTitle = "LNCARDNO,DEPTCODE,BUSSDT,CURTP,DEBTBAL,DEBTTYPE,BALALTDT\n"
# inteInfoExcel = {}
# for k,v in inteInfo.items():
#     inteInfoExcel = v.to_dict()
# for i in range(len(inteInfoExcel['LNCARDNO'])):
#     value1 = str(loanPayExcel['LNCARDNO'])
#     value2 = str(loanPayExcel['DEPTCODE'])
#     value3 = str(loanPayExcel['BUSSDT'])
#     value4 = str(loanPayExcel['CURTP'])
#     value5 = str(loanPayExcel['DEBTBAL'])
#     value6 = str(loanPayExcel['DEBTTYPE'])
#     value7 = str(loanPayExcel['BALALTDT'])

#     reportDate = (datetime.datetime.strptime(value3,'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
#     loanPath = writePath+reportDate+"loan"
#     if not os.path.exists(loanPath):
#         os.makedirs(loanPath)
#         inteInfoFile = open(loanPath+"/"+inteInfoTxtName,"a+",encoding='GBK')
#         inteInfoFile.write(inteInfoTxtTitle)
#     else:
#         inteInfoFile = open(loanPath+"/"+inteInfoTxtName,"a+",encoding='GBK')

#     inteInfoFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+"\n")


guarrela = pd.read_excel(filepath,sheet_name=[14,14])
guarrelaTxtName = "EXPORTGUARRELAINFO.txt"
guarrelaTxtTitle = "MAINCONTNO,MAINDEPTCODE,GUARCONTNO,GUARDEPTCODE,GUARTYPE,CREDITTYPE,BUSSDT,CONTEST\n"
guarrelaExcel = {}
guarrelaDict = {}
guarrelaStatusDict = {}
guarcontDict = {}
for k,v in guarrela.items():
    guarrelaExcel = v.to_dict()
for i in range(len(guarrelaExcel['MAINCONTNO'])):
    value1 = str(guarrelaExcel['MAINCONTNO'][i])
    value2 = str(guarrelaExcel['MAINDEPTCODE'][i])
    value3 = str(guarrelaExcel['GUARCONTNO'][i])
    value4 = str(guarrelaExcel['GUARDEPTCODE'][i])
    value5 = str(guarrelaExcel['GUARTYPE'][i])
    value6 = str(guarrelaExcel['CREDITTYPE'][i])
    value7 = str(guarrelaExcel['BUSSDT'][i])
    value8 = str(guarrelaExcel['CONTEST'][i])
    guarrelaStatusDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+",2\n"
    if value1 in guarcontDict:
        guarcontDict[value1] = guarcontDict[value1] + "," + value3
    else:
        guarcontDict[value1] = value3
    if value1 in loanConDict:
        reportDate = (datetime.datetime.strptime(loanConDict[value1],'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
        reportDate = getDate(reportDate)
        guarrelaDict[value3] = reportDate
        loanPath = writePath+reportDate+"loan"
        if not os.path.exists(loanPath):
            os.makedirs(loanPath)
        if not os.path.exists(loanPath+"/"+guarrelaTxtName):
            guarrelaFile = open(loanPath+"/"+guarrelaTxtName,"a+",encoding='GBK')
            guarrelaFile.write(guarrelaTxtTitle)
        else:
            guarrelaFile = open(loanPath+"/"+guarrelaTxtName,"a+",encoding='GBK')

        guarrelaFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+",1\n")
        guarrelaFile.close()


guarantee = pd.read_excel(filepath,sheet_name=[15,15])
guaranteeTxtName = "EXPORTGUARANTEEINFO.txt"
guaranteeTxtTitle = "GUARCONTNO,DEPTCODE,CONTDT,ASSUTP,CONTEST\n"
guaranteeExcel = {}
guaranteeDict = {}
for k,v in guarantee.items():
    guaranteeExcel = v.to_dict()
for i in range(len(guaranteeExcel['GUARCONTNO'])):
    value1 = str(guaranteeExcel['GUARCONTNO'][i])
    value2 = str(guaranteeExcel['DEPTCODE'][i])
    value3 = str(guaranteeExcel['CONTDT'][i])
    value4 = str(guaranteeExcel['ASSUTP'][i])
    value5 = str(guaranteeExcel['CONTEST'][i])

    reportDate = guarrelaDict[value1]
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+guaranteeTxtName):
        guaranteeFile = open(loanPath+"/"+guaranteeTxtName,"a+",encoding='GBK')
        guaranteeFile.write(guaranteeTxtTitle)
    else:
        guaranteeFile = open(loanPath+"/"+guaranteeTxtName,"a+",encoding='GBK')

    guaranteeFile.write(value1+","+value2+","+value3+","+value4+",1\n")
    guaranteeFile.close()
    guaranteeDict[value1] = value1+","+value2+","+value3+","+value4+",2\n"


guarent = pd.read_excel(filepath,sheet_name=[16,16])
guarentTxtName = "EXPORTGUARENTINFO.txt"
guarentTxtTitle = "GUARCONTNO,DEPTCODE,ASSNM,GLNCARDNO,CURTP,ASSAMT,CONTEST\n"
guarentExcel = {}
guarentDict = {}
for k,v in guarent.items():
    guarentExcel = v.to_dict()
for i in range(len(guarentExcel['GUARCONTNO'])):
    value1 = str(guarentExcel['GUARCONTNO'][i])
    value2 = str(guarentExcel['DEPTCODE'][i])
    value3 = str(guarentExcel['ASSNM'][i])
    value4 = str(guarentExcel['GLNCARDNO'][i])
    value5 = str(guarentExcel['CURTP'][i])
    value6 = str(guarentExcel['ASSAMT'][i])
    value7 = str(guarentExcel['CONTEST'][i])

    reportDate = guarrelaDict[value1]
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+guarentTxtName):
        guarentFile = open(loanPath+"/"+guarentTxtName,"a+",encoding='GBK')
        guarentFile.write(guarentTxtTitle)
    else:
        guarentFile = open(loanPath+"/"+guarentTxtName,"a+",encoding='GBK')

    guarentFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+",1\n")
    guarentFile.close()
    guarentDict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+",2\n"


guarantee32 = pd.read_excel(filepath,sheet_name=[17,17])
guarantee32TxtName = "EXPORTGUARANTEE32INFO.txt"
guarantee32TxtTitle = "GUARCONTNO,DEPTCODE,CONTDT,ASSUTP,CONTEST\n"
guarantee32Excel = {}
guarantee32Dict = {}
for k,v in guarantee32.items():
    guarantee32Excel = v.to_dict()
for i in range(len(guarantee32Excel['GUARCONTNO'])):
    value1 = str(guarantee32Excel['GUARCONTNO'][i])
    value2 = str(guarantee32Excel['DEPTCODE'][i])
    value3 = str(guarantee32Excel['CONTDT'][i])
    value4 = str(guarantee32Excel['ASSUTP'][i])
    value5 = str(guarantee32Excel['CONTEST'][i])

    reportDate = guarrelaDict[value1]
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+guarantee32TxtName):
        guarantee32File = open(loanPath+"/"+guarantee32TxtName,"a+",encoding='GBK')
        guarantee32File.write(guarantee32TxtTitle)
    else:
        guarantee32File = open(loanPath+"/"+guarantee32TxtName,"a+",encoding='GBK')

    guarantee32File.write(value1+","+value2+","+value3+","+value4+",1\n")
    guarantee32File.close()
    guarantee32Dict[value1] = value1+","+value2+","+value3+","+value4+",2\n"

guarent32 = pd.read_excel(filepath,sheet_name=[18,18])
guarent32TxtName = "EXPORTGUARENT32INFO.txt"
guarent32TxtTitle = "GUARCONTNO,DEPTCODE,ASSNM,CERTTYPE,CERTNO,CURTP,ASSAMT,CONTEST\n"
guarent32Excel = {}
guarent32Dict = {}
for k,v in guarent32.items():
    guarent32Excel = v.to_dict()
for i in range(len(guarent32Excel['GUARCONTNO'])):
    value1 = str(guarent32Excel['GUARCONTNO'][i])
    value2 = str(guarent32Excel['DEPTCODE'][i])
    value3 = str(guarent32Excel['ASSNM'][i])
    value4 = str(guarent32Excel['CERTTYPE'][i])
    value5 = str(guarent32Excel['CERTNO'][i])
    value6 = str(guarent32Excel['CURTP'][i])
    value7 = str(guarent32Excel['ASSAMT'][i])
    value7 = str(round(float(value7),2))
    value8 = str(guarent32Excel['CONTEST'][i])

    reportDate = guarrelaDict[value1]
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+guarent32TxtName):
        guarent32File = open(loanPath+"/"+guarent32TxtName,"a+",encoding='GBK')
        guarent32File.write(guarent32TxtTitle)
    else:
        guarent32File = open(loanPath+"/"+guarent32TxtName,"a+",encoding='GBK')

    guarent32File.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+",1\n")
    guarent32File.close()
    guarent32Dict[value1] = value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+",2\n"


loanPay = pd.read_excel(filepath,sheet_name=[12,12])
loanPayTxtName = "EXPORTLOANPAYINFO.txt"
loanPayTxtTitle = "LNCONTCODE,DUECODE,DEPTCODE,LNCARDNO,BUSSDT,REPAYDT,REPAYTMS,REPAYMODE,REPAYAMT\n"
loanPayExcel = {}
loanPayDict = {}
for k,v in loanPay.items():
    loanPayExcel = v.to_dict()
loanNo = ""
repayAmount = 0.0
reportDate = ""
value1 = ""
for i in range(len(loanPayExcel['LNCONTCODE'])):
    value1 = str(loanPayExcel['LNCONTCODE'][i])
    value2 = str(loanPayExcel['DUECODE'][i])
    value3 = str(loanPayExcel['DEPTCODE'][i])
    value4 = str(loanPayExcel['LNCARDNO'][i])
    value5 = str(loanPayExcel['BUSSDT'][i])
    value6 = str(loanPayExcel['REPAYDT'][i])
    value7 = getValue(str(loanPayExcel['REPAYTMS'][i]))
    value8 = str(loanPayExcel['REPAYMODE'][i])
    if value8 == "1":
        value8 = "01"
    value9 = str(loanPayExcel['REPAYAMT'][i])
    value9 = str(round(float(value9),2))
    if loanNo == "":
        loanNo = value1
    if loanNo == value1:
        repayAmount = float(value9) + repayAmount
    else:
        if loanNo in dueBillCountDict:
            if dueBillCountDict[loanNo] <= repayAmount:
                loanPayDict[loanNo] = reportDate
        repayAmount = float(value9)
    loanNo = value1
    
    reportDate = (datetime.datetime.strptime(value5,'%Y%m%d')+datetime.timedelta(days=1)).strftime('%Y%m%d')
    reportDate = getDate(reportDate)
    loanPath = writePath+reportDate+"loan"
    if not os.path.exists(loanPath):
        os.makedirs(loanPath)
    if not os.path.exists(loanPath+"/"+loanPayTxtName):
        loanPayFile = open(loanPath+"/"+loanPayTxtName,"a+",encoding='GBK')
        loanPayFile.write(loanPayTxtTitle)
    else:
        loanPayFile = open(loanPath+"/"+loanPayTxtName,"a+",encoding='GBK')

    loanPayFile.write(value1+","+value2+","+value3+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+"\n")
    loanPayFile.close()

if loanNo in dueBillCountDict:
    if dueBillCountDict[loanNo] <= repayAmount:
        loanPayDict[loanNo] = reportDate

for key in loanPayDict:
    if key in loanConStatusDict:
        loanPath = writePath+loanPayDict[key]+"loan"
        if not os.path.exists(loanPath+"/"+loanConTxtName):
            loanConFile = open(loanPath+"/"+loanConTxtName,"a+",encoding='GBK')
            loanConFile.write(loanConTxtTitle)
        else:
            loanConFile = open(loanPath+"/"+loanConTxtName,"a+",encoding='GBK')
        loanConFile.write(loanConStatusDict[key])
        loanConFile.close()

        if key in guarcontDict:
            if not os.path.exists(loanPath+"/"+guarrelaTxtName):
                guarrelaFile = open(loanPath+"/"+guarrelaTxtName,"a+",encoding='GBK')
                guarrelaFile.write(guarrelaTxtTitle)
            else:
                guarrelaFile = open(loanPath+"/"+guarrelaTxtName,"a+",encoding='GBK')
            guarrelaFile.write(guarrelaStatusDict[key])
            guarrelaFile.close()

            guaranteNoList = guarcontDict[key].split(",")
            for i in range(len(guaranteNoList)):
                if guaranteNoList[i] in guaranteeDict:
                    if not os.path.exists(loanPath+"/"+guaranteeTxtName):
                        guaranteeFile = open(loanPath+"/"+guaranteeTxtName,"a+",encoding='GBK')
                        guaranteeFile.write(guaranteeTxtTitle)
                    else:
                        guaranteeFile = open(loanPath+"/"+guaranteeTxtName,"a+",encoding='GBK')
                    guaranteeFile.write(guaranteeDict[guaranteNoList[i]])
                    guaranteeFile.close()

                if guaranteNoList[i] in guarentDict:
                    if not os.path.exists(loanPath+"/"+guarentTxtName):
                        guarentFile = open(loanPath+"/"+guarentTxtName,"a+",encoding='GBK')
                        guarentFile.write(guarentTxtTitle)
                    else:
                        guarentFile = open(loanPath+"/"+guarentTxtName,"a+",encoding='GBK')
                    guarentFile.write(guarentDict[guaranteNoList[i]])
                    guarentFile.close()

                if guaranteNoList[i] in guarantee32Dict:
                    if not os.path.exists(loanPath+"/"+guarantee32TxtName):
                        guarantee32File = open(loanPath+"/"+guarantee32TxtName,"a+",encoding='GBK')
                        guarantee32File.write(guarantee32TxtTitle)
                    else:
                        guarantee32File = open(loanPath+"/"+guarantee32TxtName,"a+",encoding='GBK')
                    guarantee32File.write(guarantee32Dict[guaranteNoList[i]])
                    guarantee32File.close()

                if guaranteNoList[i] in guarent32Dict:
                    if not os.path.exists(loanPath+"/"+guarent32TxtName):
                        guarent32File = open(loanPath+"/"+guarent32TxtName,"a+",encoding='GBK')
                        guarent32File.write(guarent32TxtTitle)
                    else:
                        guarent32File = open(loanPath+"/"+guarent32TxtName,"a+",encoding='GBK')
                    guarent32File.write(guarent32Dict[guaranteNoList[i]])
                    guarent32File.close()


captown = pd.read_excel(filepath,sheet_name=[19,19])
captownTxtName = "EXPORT07CAPTOWNINFO.txt"
captownTxtTitle = "LNCARDNO,DEPTCODE,BORRNM,REPYEAR,REPTP,REPTPSUB,AUDNM,AUDMANNM,AUDTM,"
captownTxtTitle = captownTxtTitle + "AMT9100,AMT9101,AMT9102,AMT9103,AMT9104,AMT9105,AMT9106,AMT9107,AMT9108,AMT9109,"
captownTxtTitle = captownTxtTitle + "AMT9110,AMT9111,AMT9112,AMT9113,AMT9114,AMT9115,AMT9116,AMT9117,AMT9118,AMT9119,"
captownTxtTitle = captownTxtTitle + "AMT9120,AMT9121,AMT9122,AMT9123,AMT9124,AMT9125,AMT9126,AMT9127,AMT9128,AMT9129,"
captownTxtTitle = captownTxtTitle + "AMT9130,AMT9131,AMT9132,AMT9133,AMT9134,AMT9135,AMT9136,AMT9137,AMT9138,AMT9139,"
captownTxtTitle = captownTxtTitle + "AMT9140,AMT9141,AMT9142,AMT9143,AMT9144,AMT9145,AMT9146,AMT9147,AMT9148,AMT9149,"
captownTxtTitle = captownTxtTitle + "AMT9150,AMT9151,AMT9152,AMT9153,AMT9154,AMT9155,AMT9156,AMT9157,AMT9158,AMT9159\n"
captownExcel = {}
for k,v in captown.items():
    captownExcel = v.to_dict()
for i in range(len(captownExcel['LNCARDNO'])):
    value1 = str(captownExcel['LNCARDNO'][i])
    value2 = str(captownExcel['DEPTCODE'][i])
    # value3 = str(captownExcel['BUSSDT'][i])
    value4 = str(captownExcel['BORRNM'][i])
    value5 = str(captownExcel['REPYEAR'][i])
    value6 = str(captownExcel['REPTP'][i])
    value7 = str(captownExcel['REPTPSUB'][i])
    value8 = getValue(str(captownExcel['AUDNM'][i]))
    value9 = getValue(str(captownExcel['AUDMANNM'][i]))
    value10 = getValue(str(captownExcel['AUDTM'][i]))
    value11 = getValue(str(captownExcel['AMT9100'][i]))
    value12 = getValue(str(captownExcel['AMT9101'][i]))
    value13 = getValue(str(captownExcel['AMT9102'][i]))
    value14 = getValue(str(captownExcel['AMT9103'][i]))
    value15 = getValue(str(captownExcel['AMT9104'][i]))
    value16 = getValue(str(captownExcel['AMT9105'][i]))
    value17 = getValue(str(captownExcel['AMT9106'][i]))
    value18 = getValue(str(captownExcel['AMT9107'][i]))
    value19 = getValue(str(captownExcel['AMT9108'][i]))
    value20 = getValue(str(captownExcel['AMT9109'][i]))
    value21 = getValue(str(captownExcel['AMT9110'][i]))
    value22 = getValue(str(captownExcel['AMT9111'][i]))
    value23 = getValue(str(captownExcel['AMT9112'][i]))
    value24 = getValue(str(captownExcel['AMT9113'][i]))
    value25 = getValue(str(captownExcel['AMT9114'][i]))
    value26 = getValue(str(captownExcel['AMT9115'][i]))
    value27 = getValue(str(captownExcel['AMT9116'][i]))
    value28 = getValue(str(captownExcel['AMT9117'][i]))
    value29 = getValue(str(captownExcel['AMT9118'][i]))
    value30 = getValue(str(captownExcel['AMT9119'][i]))
    value31 = getValue(str(captownExcel['AMT9120'][i]))
    value32 = getValue(str(captownExcel['AMT9121'][i]))
    value33 = getValue(str(captownExcel['AMT9122'][i]))
    value34 = getValue(str(captownExcel['AMT9123'][i]))
    value35 = getValue(str(captownExcel['AMT9124'][i]))
    value36 = getValue(str(captownExcel['AMT9125'][i]))
    value37 = getValue(str(captownExcel['AMT9126'][i]))
    value38 = getValue(str(captownExcel['AMT9127'][i]))
    value39 = getValue(str(captownExcel['AMT9128'][i]))
    value40 = getValue(str(captownExcel['AMT9129'][i]))
    value41 = getValue(str(captownExcel['AMT9130'][i]))
    value42 = getValue(str(captownExcel['AMT9131'][i]))
    value43 = getValue(str(captownExcel['AMT9132'][i]))
    value44 = getValue(str(captownExcel['AMT9133'][i]))
    value45 = getValue(str(captownExcel['AMT9134'][i]))
    value46 = getValue(str(captownExcel['AMT9135'][i]))
    value47 = getValue(str(captownExcel['AMT9136'][i]))
    value48 = getValue(str(captownExcel['AMT9137'][i]))
    value49 = getValue(str(captownExcel['AMT9138'][i]))
    value50 = getValue(str(captownExcel['AMT9139'][i]))
    value51 = getValue(str(captownExcel['AMT9140'][i]))
    value52 = getValue(str(captownExcel['AMT9141'][i]))
    value53 = getValue(str(captownExcel['AMT9142'][i]))
    value54 = getValue(str(captownExcel['AMT9143'][i]))
    value55 = getValue(str(captownExcel['AMT9144'][i]))
    value56 = getValue(str(captownExcel['AMT9145'][i]))
    value57 = getValue(str(captownExcel['AMT9146'][i]))
    value58 = getValue(str(captownExcel['AMT9147'][i]))
    value59 = getValue(str(captownExcel['AMT9148'][i]))
    value60 = getValue(str(captownExcel['AMT9149'][i]))
    value61 = getValue(str(captownExcel['AMT9150'][i]))
    value62 = getValue(str(captownExcel['AMT9151'][i]))
    value63 = getValue(str(captownExcel['AMT9152'][i]))
    value64 = getValue(str(captownExcel['AMT9153'][i]))
    value65 = getValue(str(captownExcel['AMT9154'][i]))
    value66 = getValue(str(captownExcel['AMT9155'][i]))
    value67 = getValue(str(captownExcel['AMT9156'][i]))
    value68 = getValue(str(captownExcel['AMT9157'][i]))
    value69 = getValue(str(captownExcel['AMT9158'][i]))
    value70 = getValue(str(captownExcel['AMT9159'][i]))
    
    basePath = writePath+"base"
    if not os.path.exists(basePath):
        os.makedirs(basePath)
    if not os.path.exists(basePath+"/"+captownTxtName):
        captownFile = open(basePath+"/"+captownTxtName,"a+",encoding='GBK')
        captownFile.write(captownTxtTitle)
    else:
        captownFile = open(basePath+"/"+captownTxtName,"a+",encoding='GBK')
    captownFile.write(value1+","+value2+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+","+value10+",")
    captownFile.write(value11+","+value12+","+value13+","+value14+","+value15+","+value16+","+value17+","+value18+","+value19+","+value20+",")
    captownFile.write(value21+","+value22+","+value23+","+value24+","+value25+","+value26+","+value27+","+value28+","+value29+","+value30+",")
    captownFile.write(value31+","+value32+","+value33+","+value34+","+value35+","+value36+","+value37+","+value38+","+value39+","+value40+",")
    captownFile.write(value41+","+value42+","+value43+","+value44+","+value45+","+value46+","+value47+","+value48+","+value49+","+value50+",")
    captownFile.write(value51+","+value52+","+value53+","+value54+","+value55+","+value56+","+value57+","+value58+","+value59+","+value60+",")
    captownFile.write(value61+","+value62+","+value63+","+value64+","+value65+","+value66+","+value67+","+value68+","+value69+","+value70+"\n")


rushflux = pd.read_excel(filepath,sheet_name=[20,20])
rushfluxTxtName = "EXPORT07RUSHFLUXINFO.txt"
rushfluxTxtTitle = "LNCARDNO,DEPTCODE,BORRNM,REPYEAR,REPTP,REPTPSUB,AUDNM,AUDMANNM,AUDTM,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9199,AMT9200,AMT9201,AMT9202,AMT9203,AMT9204,AMT9205,AMT9206,AMT9207,AMT9208,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9209,AMT9210,AMT9211,AMT9212,AMT9213,AMT9214,AMT9215,AMT9216,AMT9217,AMT9218,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9219,AMT9220,AMT9221,AMT9222,AMT9223,AMT9224,AMT9225,AMT9226,AMT9227,AMT9228,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9229,AMT9230,AMT9231,AMT9232,AMT9233,AMT9234,AMT9235,AMT9236,AMT9237,AMT9238,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9239,AMT9240,AMT9241,AMT9242,AMT9243,AMT9244,AMT9245,AMT9246,AMT9247,AMT9248,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9249,AMT9250,AMT9251,AMT9252,AMT9253,AMT9254,AMT9255,AMT9256,AMT9257,AMT9258,"
rushfluxTxtTitle = rushfluxTxtTitle + "AMT9259,AMT9260,AMT9261\n"
rushfluxExcel = {}
for k,v in rushflux.items():
    rushfluxExcel = v.to_dict()
for i in range(len(rushfluxExcel['LNCARDNO'])):
    value1 = getValue(str(rushfluxExcel['LNCARDNO'][i]))
    value2 = getValue(str(rushfluxExcel['DEPTCODE'][i]))
    # value3 = getValue(str(rushfluxExcel['BUSSDT'][i]))
    value4 = getValue(str(rushfluxExcel['BORRNM'][i]))
    value5 = getValue(str(rushfluxExcel['REPYEAR'][i]))
    value6 = getValue(str(rushfluxExcel['REPTP'][i]))
    value7 = getValue(str(rushfluxExcel['REPTPSUB'][i]))
    value8 = getValue(str(rushfluxExcel['AUDNM'][i]))
    value9 = getValue(str(rushfluxExcel['AUDMANNM'][i]))
    value10 = getValue(str(rushfluxExcel['AUDTM'][i]))

    value11 = getValue(str(rushfluxExcel['AMT9199'][i]))
    value12 = getValue(str(rushfluxExcel['AMT9200'][i]))
    value13 = getValue(str(rushfluxExcel['AMT9201'][i]))
    value14 = getValue(str(rushfluxExcel['AMT9202'][i]))
    value15 = getValue(str(rushfluxExcel['AMT9203'][i]))
    value16 = getValue(str(rushfluxExcel['AMT9204'][i]))
    value17 = getValue(str(rushfluxExcel['AMT9205'][i]))
    value18 = getValue(str(rushfluxExcel['AMT9206'][i]))
    value19 = getValue(str(rushfluxExcel['AMT9207'][i]))
    value20 = getValue(str(rushfluxExcel['AMT9208'][i]))
          
    value21 = getValue(str(rushfluxExcel['AMT9209'][i]))                                       
    value22 = getValue(str(rushfluxExcel['AMT9210'][i]))
    value23 = getValue(str(rushfluxExcel['AMT9211'][i]))
    value24 = getValue(str(rushfluxExcel['AMT9212'][i]))
    value25 = getValue(str(rushfluxExcel['AMT9213'][i]))
    value26 = getValue(str(rushfluxExcel['AMT9214'][i]))
    value27 = getValue(str(rushfluxExcel['AMT9215'][i]))
    value28 = getValue(str(rushfluxExcel['AMT9216'][i]))
    value29 = getValue(str(rushfluxExcel['AMT9217'][i]))
    value30 = getValue(str(rushfluxExcel['AMT9218'][i]))
          
    value31 = getValue(str(rushfluxExcel['AMT9219'][i]))                                       
    value32 = getValue(str(rushfluxExcel['AMT9220'][i]))
    value33 = getValue(str(rushfluxExcel['AMT9221'][i]))
    value34 = getValue(str(rushfluxExcel['AMT9222'][i]))
    value35 = getValue(str(rushfluxExcel['AMT9223'][i]))
    value36 = getValue(str(rushfluxExcel['AMT9224'][i]))
    value37 = getValue(str(rushfluxExcel['AMT9225'][i]))
    value38 = getValue(str(rushfluxExcel['AMT9226'][i]))
    value39 = getValue(str(rushfluxExcel['AMT9227'][i]))
    value40 = getValue(str(rushfluxExcel['AMT9228'][i]))
          
    value41 = getValue(str(rushfluxExcel['AMT9229'][i]))                                       
    value42 = getValue(str(rushfluxExcel['AMT9230'][i]))
    value43 = getValue(str(rushfluxExcel['AMT9231'][i]))
    value44 = getValue(str(rushfluxExcel['AMT9232'][i]))
    value45 = getValue(str(rushfluxExcel['AMT9233'][i]))
    value46 = getValue(str(rushfluxExcel['AMT9234'][i]))
    value47 = getValue(str(rushfluxExcel['AMT9235'][i]))
    value48 = getValue(str(rushfluxExcel['AMT9236'][i]))
    value49 = getValue(str(rushfluxExcel['AMT9237'][i]))
    value50 = getValue(str(rushfluxExcel['AMT9238'][i]))
          
    value51 = getValue(str(rushfluxExcel['AMT9239'][i]))                                       
    value52 = getValue(str(rushfluxExcel['AMT9240'][i]))
    value53 = getValue(str(rushfluxExcel['AMT9241'][i]))
    value54 = getValue(str(rushfluxExcel['AMT9242'][i]))
    value55 = getValue(str(rushfluxExcel['AMT9243'][i]))
    value56 = getValue(str(rushfluxExcel['AMT9244'][i]))
    value57 = getValue(str(rushfluxExcel['AMT9245'][i]))
    value58 = getValue(str(rushfluxExcel['AMT9246'][i]))
    value59 = getValue(str(rushfluxExcel['AMT9247'][i]))
    value60 = getValue(str(rushfluxExcel['AMT9248'][i]))
          
    value61 = getValue(str(rushfluxExcel['AMT9249'][i]))                                       
    value62 = getValue(str(rushfluxExcel['AMT9250'][i]))
    value63 = getValue(str(rushfluxExcel['AMT9251'][i]))
    value64 = getValue(str(rushfluxExcel['AMT9252'][i]))
    value65 = getValue(str(rushfluxExcel['AMT9253'][i]))
    value66 = getValue(str(rushfluxExcel['AMT9254'][i]))
    value67 = getValue(str(rushfluxExcel['AMT9255'][i]))
    value68 = getValue(str(rushfluxExcel['AMT9256'][i]))
    value69 = getValue(str(rushfluxExcel['AMT9257'][i]))
    value70 = getValue(str(rushfluxExcel['AMT9258'][i]))

    value71 = getValue(str(rushfluxExcel['AMT9259'][i]))
    value72 = getValue(str(rushfluxExcel['AMT9260'][i]))
    value73 = getValue(str(rushfluxExcel['AMT9261'][i]))

    basePath = writePath+"base"
    if not os.path.exists(basePath):
        os.makedirs(basePath)
    if not os.path.exists(basePath+"/"+rushfluxTxtName):
        rushfluxFile = open(basePath+"/"+rushfluxTxtName,"a+",encoding='GBK')
        rushfluxFile.write(rushfluxTxtTitle)
    else:
        rushfluxFile = open(basePath+"/"+rushfluxTxtName,"a+",encoding='GBK')

    rushfluxFile.write(value1+","+value2+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+","+value10+",")
    rushfluxFile.write(value11+","+value12+","+value13+","+value14+","+value15+","+value16+","+value17+","+value18+","+value19+","+value20+",")
    rushfluxFile.write(value21+","+value22+","+value23+","+value24+","+value25+","+value26+","+value27+","+value28+","+value29+","+value30+",")
    rushfluxFile.write(value31+","+value32+","+value33+","+value34+","+value35+","+value36+","+value37+","+value38+","+value39+","+value40+",")
    rushfluxFile.write(value41+","+value42+","+value43+","+value44+","+value45+","+value46+","+value47+","+value48+","+value49+","+value50+",")
    rushfluxFile.write(value51+","+value52+","+value53+","+value54+","+value55+","+value56+","+value57+","+value58+","+value59+","+value60+",")
    rushfluxFile.write(value61+","+value62+","+value63+","+value64+","+value65+","+value66+","+value67+","+value68+","+value69+","+value70+",")
    rushfluxFile.write(value71+","+value72+","+value73+"\n")


profass = pd.read_excel(filepath,sheet_name=[21,21])
profassTxtName = "EXPORT07PROFASSINFO.txt"
profassTxtTitle = "LNCARDNO,DEPTCODE,BORRNM,REPYEAR,REPTP,REPTPSUB,AUDNM,AUDMANNM,AUDTM,"
profassTxtTitle = profassTxtTitle + "AMT9170,AMT9171,AMT9172,AMT9173,AMT9174,AMT9175,AMT9176,AMT9177,AMT9178,AMT9179,"
profassTxtTitle = profassTxtTitle + "AMT9180,AMT9181,AMT9182,AMT9183,AMT9184,AMT9185,AMT9186,AMT9187,AMT9188\n"
profassExcel = {}
for k,v in profass.items():
    profassExcel = v.to_dict()
for i in range(len(profassExcel['LNCARDNO'])):
    value1 = getValue(str(profassExcel['LNCARDNO'][i]))
    value2 = getValue(str(profassExcel['DEPTCODE'][i]))
    # value3 = getValue(str(profassExcel['BUSSDT'][i]))
    value4 = getValue(str(profassExcel['BORRNM'][i]))
    value5 = getValue(str(profassExcel['REPYEAR'][i]))
    value6 = getValue(str(profassExcel['REPTP'][i]))
    value7 = getValue(str(profassExcel['REPTPSUB'][i]))
    value8 = getValue(str(profassExcel['AUDNM'][i]))
    value9 = getValue(str(profassExcel['AUDMANNM'][i]))
    value10 = getValue(str(profassExcel['AUDTM'][i]))

    value11 = getValue(str(profassExcel['AMT9170'][i]))
    value12 = getValue(str(profassExcel['AMT9171'][i]))
    value13 = getValue(str(profassExcel['AMT9172'][i]))
    value14 = getValue(str(profassExcel['AMT9173'][i]))
    value15 = getValue(str(profassExcel['AMT9174'][i]))
    value16 = getValue(str(profassExcel['AMT9175'][i]))
    value17 = getValue(str(profassExcel['AMT9176'][i]))
    value18 = getValue(str(profassExcel['AMT9177'][i]))
    value19 = getValue(str(profassExcel['AMT9178'][i]))
    value20 = getValue(str(profassExcel['AMT9179'][i]))

    value21 = getValue(str(profassExcel['AMT9180'][i]))
    value22 = getValue(str(profassExcel['AMT9181'][i]))
    value23 = getValue(str(profassExcel['AMT9182'][i]))
    value24 = getValue(str(profassExcel['AMT9183'][i]))
    value25 = getValue(str(profassExcel['AMT9184'][i]))
    value26 = getValue(str(profassExcel['AMT9185'][i]))
    value27 = getValue(str(profassExcel['AMT9186'][i]))
    value28 = getValue(str(profassExcel['AMT9187'][i]))
    value29 = getValue(str(profassExcel['AMT9188'][i]))

    basePath = writePath+"base"
    if not os.path.exists(basePath):
        os.makedirs(basePath)
    if not os.path.exists(basePath+"/"+profassTxtName):
        profassFile = open(basePath+"/"+profassTxtName,"a+",encoding='GBK')
        profassFile.write(profassTxtTitle)
    else:
        profassFile = open(basePath+"/"+profassTxtName,"a+",encoding='GBK')

    profassFile.write(value1+","+value2+","+value4+","+value5+","+value6+","+value7+","+value8+","+value9+","+value10+",")
    profassFile.write(value11+","+value12+","+value13+","+value14+","+value15+","+value16+","+value17+","+value18+","+value19+","+value20+",")
    profassFile.write(value21+","+value22+","+value23+","+value24+","+value25+","+value26+","+value27+","+value28+","+value29+"\n")