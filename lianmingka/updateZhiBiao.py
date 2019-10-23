#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import json
import os  
import os.path  
import gzip
import datetime
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
        writeFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" 开始执行\n")
        readData = json.loads(open("e:/python/engine.txt").read())
        localIp = readData['localIp']
        localName = readData['localName']
        localPassword = readData['localPassword']
        localDbName = readData['localDbName']
        engineIp = readData['engineIp']
        engineName = readData['engineName']
        enginePassword = readData['enginePassword']
        engineDbName = readData['engineDbName']

        
        localConn = pymysql.connect(host=localIp, port=3306, user=localName, passwd=localPassword, db=localDbName, charset='utf8')
        localCursor = localConn.cursor()
        localSql = "select USER_id, ifnull(credit_used,0), ifnull(credit,0), first_tran_time, ifnull(money_all,0), ifnull(count_all,0), ifnull(money_normal,0), \n";
        localSql = localSql + "ifnull(count_normal,0), ifnull(money_overdue,0),ifnull(count_overdue,0), ifnull(money_overdue_repay,0), ifnull(count_overdue_repay,0), \n";
        localSql = localSql + "ifnull(money_not_due,0),ifnull(count_not_due,0),ifnull(max_duedays,0),ifnull(history_max_duedays,0),ifnull(days_last,0),ifnull(month_max_duedays,0) \n"
        localSql = localSql + " from credit_behaviour";

        localResult = localCursor.execute(localSql)    
        localList = localCursor.fetchmany(localResult)
        localDict = {}
        for localInfo in localList:
            localDict[localInfo[0]] = localInfo
        localCursor.close()
        localConn.close()

        writeFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" 获取本地数据结束\n")

        engineConn = pymysql.connect(host=engineIp, port=3306, user=engineName, passwd=enginePassword, db=engineDbName, charset='utf8')
        engineCursor = engineConn.cursor()
        engineSql = "select USER_id from credit_behaviour";
        engineResult = engineCursor.execute(engineSql);
        engineList = engineCursor.fetchmany(engineResult)
        engineDict = {}
        for engineInfo in engineList:
            engineDict[engineInfo[0]] = engineInfo[0]

        writeFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" 获取决策数据结束\n")

        insert = 0
        update = 0
        for key in localDict:
            localInfo = localDict[key]
            sql = ""
            if localInfo[3] == None:
                first_tran_time = "null"
            else:
                first_tran_time = "'"+str(localInfo[3])+"'"
            if key in engineDict:
                sql = sql + "update credit_behaviour set "
                sql = sql + "credit_used = " + str(localInfo[1])+",credit = " + str(localInfo[2]) + ",first_tran_time = " + first_tran_time + ",money_all = " + str(localInfo[4]) + ",count_all = " + str(localInfo[5])+","
                sql = sql + "money_normal = " + str(localInfo[6])+",count_normal = " + str(localInfo[7]) + ",money_overdue = " + str(localInfo[8]) + ",count_overdue = " + str(localInfo[9]) + ",money_overdue_repay = " + str(localInfo[10])+","
                sql = sql + "count_overdue_repay = " + str(localInfo[11])+",money_not_due = " + str(localInfo[12]) + ",count_not_due = " + str(localInfo[13]) + ",max_duedays = " + str(localInfo[14]) + ",history_max_duedays = " + str(localInfo[15])+","
                sql = sql + "days_last = " + str(localInfo[16])+",month_max_duedays = " + str(localInfo[17]) + " where user_id = '" +key+"';\n"
                insert = insert +1
            else:
                sql = sql + "insert into credit_behaviour values ("
                sql = sql + "'"+localInfo[0]+"',"+str(localInfo[1])+","+str(localInfo[2])+","+first_tran_time+","+str(localInfo[4])+","+str(localInfo[5])+","+str(localInfo[6])+","+str(localInfo[7])+","+str(localInfo[8])+","+str(localInfo[9])+","
                sql = sql + str(localInfo[10])+","+str(localInfo[11])+","+str(localInfo[12])+","+str(localInfo[13])+","+str(localInfo[14])+","+str(localInfo[15])+","+str(localInfo[16])+","+str(localInfo[17])+");\n"
                update = update + 1
            try:
                engineCursor.execute(sql)
            except  Exception as e:
                writeFile.write(sql+"\n")
                writeFile.write(e.message+"\n")

        engineConn.commit()
        engineCursor.close()
        engineConn.close()
        writeFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" 执行成功，插入"+str(insert)+"条,更新"+str(update)+"条\n\n")
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
        msg=MIMEText('风控决策指标库更新'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'自动任务执行失败,'+message,'plain','utf-8')
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