#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
def querySql(report_date,line_type):
    
    conn = pymysql.connect(host='172.17.33.65', port=3306, user='root', passwd='root', db='jrpt_supervise_report_dev', charset='utf8')
    cursor = conn.cursor()

    sql = "select 'wrong' as type,name,cert_no,account,date_opened,date_closed,credit_limit,share_account,max_debt,billing_date,recent_pay_date,recent_pay_amount,scheduled_amount,actual_pay_amount,balance,\n"
    sql = sql + "curtermspast_due,amountpast_due,amountpast_due0,amountpast_due30,amountpast_due60,amountpast_due90,termspastdue,max_termspast_due,class5_stat,account_stat,pay_stat24_month \n"
    sql = sql + "from rh_trade_info_wrong \n"
    sql = sql + "where report_date = '" + report_date + "' and line_type = '" + line_type + "' \n"
    sql = sql + "union all \n"
    sql = sql + "select 'right' as type,name,cert_no,account,date_opened,date_closed,credit_limit,share_account,max_debt,billing_date,recent_pay_date,recent_pay_amount,scheduled_amount,actual_pay_amount,balance,\n"
    sql = sql + "curtermspast_due,amountpast_due,amountpast_due0,amountpast_due30,amountpast_due60,amountpast_due90,termspastdue,max_termspast_due,class5_stat,account_stat,pay_stat24_month \n"
    sql = sql + "from rh_trade_info_right \n"
    sql = sql + "where report_date = '" + report_date + "' and line_type = '" + line_type + "' \n"
    sql = sql + "order by cert_no,billing_date,type"

    sqlList = cursor.execute(sql)    
    sqlResult = cursor.fetchmany(sqlList)

    hisList = []
    hisCertNo = ""
    resultTxt = open("D:/project/python/mysql/"+report_date+"_"+line_type+".txt","a",encoding='GBK')
    writeData = ""
    for result in sqlResult:
        if hisCertNo == "":
            hisCertNo = result[2]
            hisList.append(result)
        else:
            if hisCertNo == result[2]:
                hisList.append(result)
            else:
                writeData = writeData + judgeNew(hisList)
                hisList = []
                hisCertNo = result[2]
                hisList.append(result)
    writeData = writeData + judgeNew(hisList)
    cursor.close()
    conn.commit()
    conn.close()
    resultTxt.write(writeData)

def judge(hisList):
    result = ""
    if len(hisList) == 1:
        result = dealResult(hisList[0],"1")
        
    if len(hisList) == 2:
        if hisList[0][0] == hisList[1][0]:
            result = dealResult(hisList[0],"2")
            result = result + dealResult(hisList[1],"2")
        else:
            if hisList[0][3] != hisList[1][3] or hisList[0][9] != hisList[1][9] or hisList[0][4] != hisList[1][4]:
                result = dealResult(hisList[0],"dif")
                result = result + dealResult(hisList[1],"dif")
    if len(hisList) == 3:
        result = dealResult(hisList[0],"3")
        result = result + dealResult(hisList[1],"3")
        result = result + dealResult(hisList[2],"3")
    if len(hisList) == 4:
        if hisList[0][0] == hisList[1][0]:
            result = dealResult(hisList[0],"2")
            result = result + dealResult(hisList[1],"2")
        else:
            if hisList[0][3] != hisList[1][3] or hisList[0][9] != hisList[1][9] or hisList[0][4] != hisList[1][4]:
                result = dealResult(hisList[0],"dif")
                result = result + dealResult(hisList[1],"dif")

        if hisList[2][0] == hisList[3][0]:
            result = dealResult(hisList[2],"2")
            result = result + dealResult(hisList[3],"2")
        else:
            if hisList[0][3] != hisList[1][3] or hisList[0][9] != hisList[1][9] or hisList[0][4] != hisList[1][4]:
                result = dealResult(hisList[2],"dif")
                result = result + dealResult(hisList[3],"dif")
    return result

def judgeNew(hisList):
    result = ""
    if len(hisList) == 1:
        if hisList[0][0] == "wrong":
            result = dealResult(hisList[0],"1")
        
    if len(hisList) == 2:
        if hisList[0][9][0:6] != hisList[1][9][0:6]:
            result = dealResult(hisList[0],"2")
            result = result + dealResult(hisList[1],"2")
    if len(hisList) == 3:
        if hisList[0][9][0:6] != hisList[1][9][0:6] or hisList[1][9][0:6] != hisList[2][9][0:6] or hisList[2][9][0:6] != hisList[0][9][0:6]:
            result = dealResult(hisList[0],"3")
            result = result + dealResult(hisList[1],"3")
            result = result + dealResult(hisList[2],"3")
    if len(hisList) == 4:
        result = dealResult(hisList[0],"4")
        result = result + dealResult(hisList[1],"4")
        result = result + dealResult(hisList[2],"4")
        result = result + dealResult(hisList[3],"4")
    return result



def dealResult(writeData,type):
    return str(writeData).replace("(","").replace(")","").replace("'","").replace(" ","")+","+type+"\n"

if __name__=="__main__":
    listDate = ['20190922','20191001']
    listType = ['0','4']
    for reportDate in listDate:
        for lineType in listType:
            querySql(reportDate,lineType)