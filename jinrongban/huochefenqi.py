#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import datetime
import os
import os.path
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='GBK')

writePath = "D:/千方/金融办监管/货车分期/卡车分期2019年5月.txt"

readPath = "D:/千方/金融办监管/货车分期/2019年5月小贷贷款发放与回收系统上报/1网签.xlsx"
read = pd.read_excel(readPath,sheet_name=[0,0])
excel = {}
for k,v in read.items():
    excel = v.to_dict()
for i in range(len(excel['合同编号'])):
    contractNo = str(excel['合同编号'][i])
    customerName = str(excel['借款人名称'][i])
    certificateNo = str(excel['借款人证件号码'][i])
    contractAmount = str(excel['合同金额'][i])
    contractAmount = contractAmount.replace(",","")
    intRate = str(excel['月利率(‰)'][i])
    contractSignDate = str(excel['合同签订日期'][i])

    writeFile = open(writePath,"a+",encoding='GBK')
    sql = "insert into report_net_sign_batch (product_type,contractNo,loanCate,customerType,customerName,"
    sql = sql + "certificateType,certificateNo,confee,contractAmount,intRate,contractSignDate)"
    sql = sql + " values(5,'"+contractNo+"','530001','480001','"+customerName+"','150001','"+certificateNo+"',0.0,"+contractAmount+","+intRate+",'"+contractSignDate+"');\n"
    writeFile.write(sql)
    writeFile.close()

readPath = "D:/千方/金融办监管/货车分期/2019年5月小贷贷款发放与回收系统上报/2授信额度.xlsx"
read = pd.read_excel(readPath,sheet_name=[0,0])
excel = {}
for k,v in read.items():
    excel = v.to_dict()
for i in range(len(excel['额度协议编号'])):
    contractNo = str(excel['额度协议编号'][i])
    customerName = str(excel['借款人名称'][i])
    certificateNo = str(excel['借款人证件号码'][i])
    contractSignDate = str(excel['额度协议签订日期'][i])
    contractBeginDate = str(excel['额度协议起期'][i])
    contractEndDate = str(excel['额度协议止期'][i])
    contractAmount = str(excel['额度协议金额'][i])
    contractAmount = contractAmount.replace(",","")
    value1 = str(excel['担保方式'][i])
    if value1 == "信用":
        guarType = "240001"
    if value1 == "抵押":
        guarType = "240002"
    if value1 == "质押":
        guarType = "240003"
    if value1 == "保证":
        guarType = "240004"

    writeFile = open(writePath,"a+",encoding='GBK')
    sql = "insert into report_credit_lines (product_type,reportType,contractNo,contractName,customerType,customerName,"
    sql = sql + "certificateType,certificateNo,contractSignDate,contractBeginDate,contractEndDate,contractAmount,ccy,"
    sql = sql + "usedAmount,remainAmount,guarType,isCircle,contractStatus,relationManager)"
    sql = sql + " values(5,'100001','"+contractNo+"','货车分期用户协议','480001','"+customerName+"','150001','"+certificateNo+"',"
    sql = sql + "'"+contractSignDate+"','"+contractBeginDate+"','"+contractEndDate+"',"+contractAmount+",'730001',"
    sql = sql + contractAmount+",0.0,'"+guarType+"','740001','490001','千方小贷');\n"
    writeFile.write(sql)
    writeFile.close()

readPath = "D:/千方/金融办监管/货车分期/2019年5月小贷贷款发放与回收系统上报/3贷款合同.xlsx"
read = pd.read_excel(readPath,sheet_name=[0,0])
excel = {}
for k,v in read.items():
    excel = v.to_dict()
for i in range(len(excel['合同编号'])):
    contractNo = str(excel['合同编号'][i])
    customerName = str(excel['借款人名称'][i])
    certificateNo = str(excel['借款人证件号码'][i])
    contractSignDate = str(excel['合同签订日期'][i])
    contractBeginDate = str(excel['合同有效起始日期'][i])
    contractEndDate = str(excel['合同有效结束日期'][i])
    contractAmount = str(excel['合同金额'][i])
    contractAmount = contractAmount.replace(",","")
    value1 = str(excel['担保方式'][i])
    if value1 == "信用":
        guarType = "240001"
    if value1 == "抵押":
        guarType = "240002"
    if value1 == "质押":
        guarType = "240003"
    if value1 == "保证":
        guarType = "240004"

    intRate = str(excel['月利率(‰)'][i])
    priPltyRate = str(excel['逾期月利率(‰)'][i])

    writeFile = open(writePath,"a+",encoding='GBK')
    sql = "insert into report_loan_contract (product_type,reportType,contractNo,loanCate,contractName,customerType,customerName,"
    sql = sql + "certificateType,certificateNo,loanObject,loanObjectSize,contractSignDate,contractBeginDate,contractEndDate,"
    sql = sql + "contractAmount,outstanding,guarType,ccy,isRealQuotaLoan,intRate,priPltyRate,contractStatus,disputeScheme)"
    sql = sql + " values(5,'100001','"+contractNo+"','530001','货车分期用户协议','480001','"+customerName+"',"
    sql = sql + "'150001','"+certificateNo+"','410001','280003','"+contractSignDate+"','"+contractBeginDate+"','"+contractEndDate+"',"
    sql = sql + contractAmount+",0.0,'"+guarType+"','730001','740002',"+intRate+","+priPltyRate+",'490001','400001');\n"
    writeFile.write(sql)
    writeFile.close()

readPath = "D:/千方/金融办监管/货车分期/2019年5月小贷贷款发放与回收系统上报/4贷款发放.xlsx"
read = pd.read_excel(readPath,sheet_name=[0,0])
excel = {}
for k,v in read.items():
    excel = v.to_dict()
for i in range(len(excel['合同编号'])):
    contractNo = str(excel['合同编号'][i])
    customerName = str(excel['借款人名称'][i])
    certificateNo = str(excel['借款人证件号码'][i])
    ddAmt = str(excel['发放金额'][i])
    ddAmt = ddAmt.replace(",","")
    signDate = str(excel['签约日期'][i])
    ddDate = str(excel['发放日期'][i])
    matureDate = str(excel['到期日期'][i])
    value1 = str(excel['担保方式'][i])
    if value1 == "信用":
        guarType = "240001"
    if value1 == "抵押":
        guarType = "240002"
    if value1 == "质押":
        guarType = "240003"
    if value1 == "保证":
        guarType = "240004"

    intRate = str(excel['月利率(‰)'][i])
    priPltyRate = str(excel['逾期月利率(‰)'][i])
    value2 = str(excel['贷款期限'][i])
    if value2 == "1年以上":
    	term = "250005"
    if value2 == "半年以上":
    	term = "250004"
    if value2 == "1～3个月":
        term = "250002"

    writeFile = open(writePath,"a+",encoding='GBK')
    sql = "insert into report_loan_grant (product_type,reportType,contractNo,dueBillNo,customerType,customerName,"
    sql = sql + "certificateType,certificateNo,ddAmt,loanCate,intRate,priPltyRate,rateType,"
    sql = sql + "signDate,ddDate,matureDate,zone,guarType,term,purpose,"
    sql = sql + "loanObject,loanObjectSize,rateCalcMode,repayMode,industry,riskLevel,issueStatus)"
    sql = sql + " values(5,'100001','"+contractNo+"','"+contractNo+"','480001','"+customerName+"',"
    sql = sql + "'150001','"+certificateNo+"',"+ddAmt+",'530001',"+intRate+","+priPltyRate+",'520001',"
    sql = sql + "'"+signDate+"','"+ddDate+"','"+matureDate+"','230044','"+guarType+"','"+term+"','260001',"
    sql = sql + "'410001','280006','270002','430004','290006','510001','540002');\n"
    writeFile.write(sql)
    writeFile.close()

readPath = "D:/千方/金融办监管/货车分期/2019年5月小贷贷款发放与回收系统上报/5还款计划.xlsx"
read = pd.read_excel(readPath,sheet_name=[0,0])
excel = {}
for k,v in read.items():
    excel = v.to_dict()
for i in range(len(excel['合同编号'])):
    contractNo = str(excel['合同编号'][i])
    counter = str(excel['还款期数'][i])
    repayDate = str(excel['应还日期'][i])
    repayPriAmt = str(excel['应还本金（元）'][i])
    repayPriAmt = repayPriAmt.replace(",","")
    repayIntAmt = str(excel['应还利息（元）'][i])
    repayIntAmt = repayIntAmt.replace(",","")
    startDate = str(excel['起息日期'][i])
    endDate = str(excel['止息日期'][i])

    writeFile = open(writePath,"a+",encoding='GBK')
    sql = "insert into report_repayment_plan (product_type,reportType,contractNo,dueBillNo,counter,"
    sql = sql + "repayDate,repayPriAmt,repayIntAmt,startDate,endDate)"
    sql = sql + " values(5,'100001','"+contractNo+"','"+contractNo+"',"+counter+","
    sql = sql + "'"+repayDate+"',"+repayPriAmt+","+repayIntAmt+",'"+startDate+"','"+endDate+"');\n"
    writeFile.write(sql)
    writeFile.close()

readPath = "D:/千方/金融办监管/货车分期/2019年5月小贷贷款发放与回收系统上报/6回收.xlsx"
read = pd.read_excel(readPath,sheet_name=[0,0])
excel = {}
for k,v in read.items():
    excel = v.to_dict()
for i in range(len(excel['合同编号'])):
    contractNo = str(excel['合同编号'][i])
    counter = str(excel['还款期数'][i])
    repayDate = str(excel['回收日期'][i])

    customerName = str(excel['借款人名称'][i])
    repayPriAmt = str(excel['收回本金'][i])
    repayPriAmt = repayPriAmt.replace(",","")
    repayIntAmt = str(excel['收回利息'][i])
    if repayIntAmt == "nan" or  repayIntAmt == "NaT":
    	repayIntAmt = "''"
    repayIntAmt = repayIntAmt.replace(",","")
    startDate = str(excel['起息日期'][i])
    endDate = str(excel['止息日期'][i])
    value1 = str(excel['回收类型'][i])
    if value1 == "逾期":
    	receiptType = "550002"
    if value1 == "正常":
    	receiptType = "550001"
    print(contractNo)
    d1 = datetime.datetime.strptime(repayDate[0:8],"%Y%m%d")
    d2 = datetime.datetime.strptime(endDate[0:8],"%Y%m%d")
    overduedays = (d1 - d2).days
    delayInterest = str(excel['逾期利息'][i])
    if delayInterest == "nan" or  delayInterest == "NaT":
    	delayInterest = "''"
    delayInterest = delayInterest.replace(",","") 

    writeFile = open(writePath,"a+",encoding='GBK')
    sql = "insert into report_loan_recovery (product_type,reportType,contractNo,dueBillNo,repayDate,counter,customerType,customerName,"
    sql = sql + "gatherMode,repayPriAmt,repayIntAmt,startDate,endDate,"
    sql = sql + "receiptType,delayDays,delayAmt,delayInterest,delayFee)"
    sql = sql + " values(5,'100001','"+contractNo+"','"+contractNo+"','"+repayDate+"',"+counter+",'480001','"+customerName+"',"
    sql = sql + "'430004',"+repayPriAmt+","+repayIntAmt+",'"+startDate+"','"+endDate+"',"
    if overduedays > 0:
        sql = sql + "'"+receiptType+"',"+str(overduedays)+","+repayPriAmt+","+delayInterest+",0.0);\n"
    else:
    	sql = sql + "'"+receiptType+"','','','','');\n"
    writeFile.write(sql)
    writeFile.close()

