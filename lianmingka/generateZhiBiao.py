#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import json
import os  
import os.path  
import gzip
import datetime
import timedelta
import smtplib
import socket
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='qfjr@sinoiov.com' #发件人邮箱账号
my_user='qfjr@sinoiov.com' #收件人邮箱账号

def execute():
    ret=''
    try:
        writePath = "e:/python/"+datetime.datetime.now().strftime('%Y-%m')+"_result.txt"
        writeFile = open(writePath,"a+",encoding='GBK')
        writeFile.write(str(datetime.datetime.now())+" 开始执行\n")
        readData = json.loads(open("e:/python/engine.txt").read())
        localIp = readData['localIp']
        localName = readData['localName']
        localPassword = readData['localPassword']
        localDbName = readData['localDbName']
        engineIp = readData['engineIp']
        engineName = readData['engineName']
        enginePassword = readData['enginePassword']
        engineDbName = readData['engineDbName']

        writeFile.write(str(datetime.datetime.now())+" 开始获取本地数据库连接\n")
        localConn = pymysql.connect(host=localIp, port=3306, user=localName, passwd=localPassword, db=localDbName, charset='utf8')

        localCursor = localConn.cursor()

        writeFile.write(str(datetime.datetime.now())+" 开始查询本地联名卡油卡数据\n")
        localSql = "SELECT user_id,ROUND(credit_line/100,2),ROUND((credit_line-credit_usable)/100,2) \n"
        localSql = localSql + "from tb_oil_card where card_id != '' and credit_line > 0 "
        creditResult = localCursor.execute(localSql)  
        creditList = localCursor.fetchmany(creditResult)

        localDict = {}
        for creditInfo in creditList:
            if creditInfo[0] in localDict:
                dataDict = localDict[creditInfo[0]]
                if dataDict["credit"] < creditInfo[1]:
                    dataDict["credit"] = creditInfo[1]
                if dataDict["credit_used"] < creditInfo[2]:
                    dataDict["credit_used"] = creditInfo[2]
            else:
                dataDict = {}
                dataDict["user_id"] = creditInfo[0]
                dataDict["credit"] = creditInfo[1]
                dataDict["credit_used"] = creditInfo[2]
                dataDict["first_tran_time"] = "null"
                dataDict["money_all"] = 0
                dataDict["count_all"] = 0
                dataDict["money_normal"] = 0
                dataDict["count_normal"] = 0
                dataDict["money_overdue"] = 0
                dataDict["count_overdue"] = 0
                dataDict["money_overdue_repay"] = 0
                dataDict["count_overdue_repay"] = 0
                dataDict["money_not_due"] = 0
                dataDict["count_not_due"] = 0
                dataDict["max_duedays"] = -1
                dataDict["history_max_duedays"] = -1
                dataDict["days_last"] = -1
                dataDict["month_max_duedays"] = -1
                localDict[creditInfo[0]] = dataDict

        writeFile.write(str(datetime.datetime.now())+" 获取本地联名卡油卡表数据结束\n")

        writeFile.write(str(datetime.datetime.now())+" 开始查询本地联名卡交易数据\n")
        transactionSql = "SELECT user_id,order_no,ROUND(money/100,2),DATE_FORMAT(transaction_time,'%Y-%m-%d'),DATE_FORMAT(actual_time,'%Y-%m-%d'),pay_status,DATE_FORMAT(plan_time,'%Y-%m-%d') from tb_transaction "
        transactionSql = transactionSql + " where pay_status in ('0','1','2','4','40','05','01','06','11','12','21','22','41','42') "
        transactionResult = localCursor.execute(transactionSql)
        trasactionList = localCursor.fetchmany(transactionResult)


        nowTime = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'),"%Y-%m-%d")
        threeMonthAgoTime = nowTime - datetime.timedelta(days=90)


        for transactionInfo in trasactionList:
            if transactionInfo[0] in localDict:
                dataDict = localDict[transactionInfo[0]]

                days_last = (nowTime - datetime.datetime.strptime(transactionInfo[3],"%Y-%m-%d")).days
                days_over_last = (nowTime - datetime.datetime.strptime(transactionInfo[6],"%Y-%m-%d")).days
                if dataDict["first_tran_time"] != "null":
                    if dataDict["first_tran_time"] > transactionInfo[3]:
                        dataDict["first_tran_time"] = transactionInfo[3]
                else:
                    dataDict["first_tran_time"] = transactionInfo[3]
                if dataDict["days_last"] == -1:
                    dataDict["days_last"] = days_last
                else:
                    if dataDict["days_last"] > days_last:
                        dataDict["days_last"] = days_last

                #总借款金额，总借款笔数
                dataDict["money_all"] = dataDict["money_all"] + transactionInfo[2]
                dataDict["count_all"] = dataDict["count_all"] + 1

                #正常还款金额，正常还款笔数
                if transactionInfo[5] == "0" or transactionInfo[5] == "01":
                    dataDict["money_normal"] = dataDict["money_normal"] + transactionInfo[2]
                    dataDict["count_normal"] = dataDict["count_normal"] + 1

                #逾期金额，逾期笔数，当前最大逾期天数，近三个月最大逾期天数
                if transactionInfo[5] == "2" or transactionInfo[5] == "21" or transactionInfo[5] == "22" or transactionInfo[5] == "40" or transactionInfo[5] == "42":
                    dataDict["money_overdue"] = dataDict["money_overdue"] + transactionInfo[2]
                    dataDict["count_overdue"] = dataDict["count_overdue"] + 1
                    if dataDict["max_duedays"] == -1:
                        dataDict["max_duedays"] = days_over_last
                    else:
                        if dataDict["max_duedays"] < days_over_last:
                            dataDict["max_duedays"] = days_over_last
                    if threeMonthAgoTime > datetime.datetime.strptime(transactionInfo[3],"%Y-%m-%d"):
                        if dataDict["month_max_duedays"] == -1:
                            dataDict["month_max_duedays"] = days_over_last
                        else:
                            if dataDict["month_max_duedays"] < days_over_last:
                                dataDict["month_max_duedays"] = days_over_last

                #逾期还款金额，逾期还款笔数，历史最大逾期天数，近三个月最大逾期天数
                if transactionInfo[5] == "05" or transactionInfo[5] == "06":
                    dataDict["money_overdue_repay"] = dataDict["money_overdue_repay"] + transactionInfo[2]
                    dataDict["count_overdue_repay"] = dataDict["count_overdue_repay"] + 1

                    history_last = (datetime.datetime.strptime(transactionInfo[4],"%Y-%m-%d") - datetime.datetime.strptime(transactionInfo[6],"%Y-%m-%d")).days
                    if dataDict["history_max_duedays"] == -1:
                        dataDict["history_max_duedays"] = history_last
                    else:
                        if dataDict["history_max_duedays"] < history_last:
                            dataDict["history_max_duedays"] = history_last
                    if threeMonthAgoTime > datetime.datetime.strptime(transactionInfo[3],"%Y-%m-%d"):
                        if dataDict["month_max_duedays"] == -1:
                            dataDict["month_max_duedays"] = history_last
                        else:
                            if dataDict["month_max_duedays"] < history_last:
                                dataDict["month_max_duedays"] = history_last

                #未到期总金额，未到期总笔数
                if transactionInfo[5] == "1" or transactionInfo[5] == "11":
                    dataDict["money_not_due"] = dataDict["money_not_due"] + transactionInfo[2]
                    dataDict["count_not_due"] = dataDict["count_not_due"] + 1


        writeFile.write(str(datetime.datetime.now())+" 获取本地联名卡交易表数据结束\n")

        localCursor.close()
        localConn.close()
        writeFile.write(str(datetime.datetime.now())+" 关闭本地数据库连接\n")

        writeFile.write(str(datetime.datetime.now())+" 开始获取决策数据库连接\n")

        engineConn = pymysql.connect(host=engineIp, port=3306, user=engineName, passwd=enginePassword, db=engineDbName, charset='utf8')
        engineCursor = engineConn.cursor()

        writeFile.write(str(datetime.datetime.now())+" 开始获取决策数据结束\n")
        engineSql = "select USER_id from credit_behaviour";
        engineResult = engineCursor.execute(engineSql);
        engineList = engineCursor.fetchmany(engineResult)
        engineDict = {}
        for engineInfo in engineList:
            engineDict[engineInfo[0]] = engineInfo[0]

        writeFile.write(str(datetime.datetime.now())+" 获取决策数据结束\n")

        writeFile.write(str(datetime.datetime.now())+" 开始更新决策数据\n")
        insert = 0
        update = 0
        for key in localDict:
            dataDict = localDict[key]
            if dataDict["max_duedays"] == -1:
                dataDict["max_duedays"] = 0
            if dataDict["history_max_duedays"] == -1:
                dataDict["history_max_duedays"] = 0
            if dataDict["days_last"] == -1:
                dataDict["days_last"] = 0
            if dataDict["month_max_duedays"] == -1:
                dataDict["month_max_duedays"] = 0
            if dataDict["first_tran_time"] != "null":
                dataDict["first_tran_time"] = "'"+str(dataDict["first_tran_time"])+"'"
            sql = ""
            if key in engineDict:
                sql = sql + "update credit_behaviour set "
                sql = sql + "credit_used = " + str(dataDict["credit_used"])+",credit = " + str(dataDict["credit"]) + ",first_tran_time = " + dataDict["first_tran_time"] + ",money_all = " 
                sql = sql + str(dataDict["money_all"]) + ",count_all = " + str(dataDict["count_all"])+","
                sql = sql + "money_normal = " + str(dataDict["money_normal"])+",count_normal = " + str(dataDict["count_normal"]) + ",money_overdue = " + str(dataDict["money_overdue"]) + ",count_overdue = " 
                sql = sql + str(dataDict["count_overdue"]) + ",money_overdue_repay = " + str(dataDict["money_overdue_repay"])+","
                sql = sql + "count_overdue_repay = " + str(dataDict["count_overdue_repay"])+",money_not_due = " + str(dataDict["money_not_due"]) + ",count_not_due = " 
                sql = sql + str(dataDict["count_not_due"]) + ",max_duedays = " + str(dataDict["max_duedays"]) + ",history_max_duedays = " + str(dataDict["history_max_duedays"])+","
                sql = sql + "days_last = " + str(dataDict["days_last"])+",month_max_duedays = " + str(dataDict["month_max_duedays"]) + " where user_id = '" +key+"';\n"
                update = update +1
            else:
                sql = sql + "insert into credit_behaviour values ("
                sql = sql + "'"+dataDict["user_id"]+"',"+str(dataDict["credit_used"])+","+str(dataDict["credit"])+","+dataDict["first_tran_time"]+","+str(dataDict["money_all"])+","
                sql = sql + str(dataDict["count_all"])+","+str(dataDict["money_normal"])+","+str(dataDict["count_normal"])+","+str(dataDict["money_overdue"])+","+str(dataDict["count_overdue"])+","
                sql = sql + str(dataDict["money_overdue_repay"])+","+str(dataDict["count_overdue_repay"])+","+str(dataDict["money_not_due"])+","+str(dataDict["count_not_due"])+","+str(dataDict["max_duedays"])
                sql = sql + ","+str(dataDict["history_max_duedays"])+","+str(dataDict["days_last"])+","+str(dataDict["month_max_duedays"])+");\n"
                insert = insert + 1
            try:
                engineCursor.execute(sql)
            except  Exception as e:
                writeFile.write(sql+"\n")
                writeFile.write(e.message+"\n")

        engineConn.commit()
        writeFile.write(str(datetime.datetime.now())+" 结束更新决策数据\n")
        engineCursor.close()
        engineConn.close()
        writeFile.write(str(datetime.datetime.now())+" 关闭决策数据库连接\n")

        writeFile.write(str(datetime.datetime.now())+" 执行成功，插入"+str(insert)+"条,更新"+str(update)+"条\n\n")
        writeFile.close()
    except Exception as err:
        ret = str(err)
    return ret

def mail(message):
    try:
        readData = readData = json.loads(open("e:/python/engine.txt").read())
        my_sender = readData['emailsender']
        my_user = readData['emailuser']
        emailip = readData['emailip']
        port = readData['emailport']
        password = readData['emailpassword']
        msg=MIMEText('风控决策指标库更新'+datetime.datetime.now()+'自动任务执行失败,'+message,'plain','utf-8')
        message
        msg['From']=formataddr(["千方金融",my_sender])
        msg['Subject']="风控决策指标库更新处理结果"
        socket.setdefaulttimeout(10)
        server=smtplib.SMTP_SSL(emailip,port)
        server.login(my_sender,password)
        server.sendmail(my_sender,my_user.split(','),msg.as_string())
        server.quit()
    except Exception as err:
        print(err)

ret=execute()
if ret == '':
    print("执行成功")
else:
    print("发送邮件")
    mail(ret)