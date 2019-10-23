#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

data = open("D:/千方/风控平台/百融/20180808/qianfang/bairongSpecialList.json",encoding='UTF-8')
specialFile = open("D:/千方/风控平台/百融/20180808/qianfang/specialList.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["userName"]+","+readData["idEntityId"]+","+readData["phone"]+","+readData["code"]+","+readData["createTime"]
    if "sl_cell_p2p_bad" in readData:
        writeData = writeData + "," + readData["sl_cell_p2p_bad"]
    else:
        writeData = writeData + ","
    if "sl_id_p2p_bad" in readData:
        writeData = writeData + "," + readData["sl_id_p2p_bad"]
    else:
        writeData = writeData + ","
    if "sl_id_bank_bad" in readData:
        writeData = writeData + "," + readData["sl_id_bank_bad"]
    else:
        writeData = writeData + ","
    if "sl_cell_bank_bad" in readData:
        writeData = writeData + "," + readData["sl_cell_bank_bad"]
    else:
        writeData = writeData + ","
    if "sl_id_bank_fraud" in readData:
        writeData = writeData + "," + readData["sl_id_bank_fraud"]
    else:
        writeData = writeData + ","
    if "sl_cell_bank_fraud" in readData:
        writeData = writeData + "," + readData["sl_cell_bank_fraud"]
    else:
        writeData = writeData + ","
    if "sl_id_p2p_fraud" in readData:
        writeData = writeData + "," + readData["sl_id_p2p_fraud"]
    else:
        writeData = writeData + ","
    if "sl_cell_p2p_fraud" in readData:
        writeData = writeData + "," + readData["sl_cell_p2p_fraud"]
    else:
        writeData = writeData + ","
    if "sl_id_p2p_refuse" in readData:
        writeData = writeData + "," + readData["sl_id_p2p_refuse"]
    else:
        writeData = writeData + ","
    if "sl_cell_p2p_refuse" in readData:
        writeData = writeData + "," + readData["sl_cell_p2p_refuse"]
    else:
        writeData = writeData + ","
    writeData = writeData + "\n"
    specialFile.write(writeData)

specialFile.close()

data = open("D:/千方/风控平台/百融/20180808/qianfang/bairongApplyLoanStr.json",encoding='UTF-8')
applyLoanFile = open("D:/千方/风控平台/百融/20180808/qianfang/applyLoanStr.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["userName"]+","+readData["idEntityId"]+","+readData["phone"]+","+readData["code"]+","+readData["createTime"]
    if "als_m1_id_nbank_allnum" in readData:
        writeData = writeData + "," + readData["als_m1_id_nbank_allnum"]
    else:
        writeData = writeData + ","
    if "als_m1_cell_nbank_allnum" in readData:
        writeData = writeData + "," + readData["als_m1_cell_nbank_allnum"]
    else:
        writeData = writeData + ","
    writeData = writeData + "\n"
    applyLoanFile.write(writeData)

applyLoanFile.close()

data = open("D:/千方/风控平台/百融/20180808/qianfang/bairongExecution.json",encoding='UTF-8')
executionFile = open("D:/千方/风控平台/百融/20180808/qianfang/execution.txt","a+",encoding='GBK')

for i in data.readlines():
    readData = json.loads(i)
    writeData = readData["userName"]+","+readData["idEntityId"]+","+readData["phone"]+","+readData["code"]+","+readData["createTime"]
    if "flag_execution" in readData:
        writeData = writeData + "," + readData["flag_execution"]
    else:
        writeData = writeData + ","
    writeData = writeData + "\n"
    executionFile.write(writeData)

executionFile.close()