import pandas as pd
import pymysql
import json


conn = pymysql.connect(host='192.168.105.172', port=3306, user='root', passwd='Edc3!Qaz1Wsx2', db='report', charset='utf8')
cursor = conn.cursor()

sql = "truncate qf_loan;"
cursor.execute(sql)
sql = "truncate qf_payment;"
cursor.execute(sql)


filepath = "D:/千方/风控平台/人行征信/个人征信报送/报送源数据/按揭贷/按揭贷台账20190430.xlsx"

taizhangData = pd.read_excel(filepath,sheet_name=[0,0])
taizhangDict = {}
for k,v in taizhangData.items():
    taizhangDict = v.to_dict()

for i in range(len(taizhangDict['序号'])):
    value1 = str(taizhangDict['序号'][i])
    value2 = str(taizhangDict['客户编号'][i])
    value3 = str(taizhangDict['客户名称'][i])
    value4 = str(taizhangDict['授信对象'][i])
    value5 = str(taizhangDict['客户证件号码\n（社会统一信用代码、组织机构代码、身份证号）'][i])

    value6 = str(taizhangDict['所属区域'][i])
    value7 = str(taizhangDict['所属区县\n（区域为重庆时选择）'][i])
    if value7 == "nan":
        value7 = ""
    value8 = str(taizhangDict['所属客户经理'][i])
    value9 = str(taizhangDict['审查时间'][i])
    if value9 == "nan":
        value9 = ""
    if value9 == "NaT":
        value9 = ""
    value10 = str(taizhangDict['审查人'][i])

    value11 = str(taizhangDict['审批时间'][i])
    if value11 == "nan":
        value11 = ""
    if value11 == "NaT":
        value11 = ""
    value12 = str(taizhangDict['审批人'][i])
    if value12 == "nan":
        value12 = ""
    value13 = str(taizhangDict['自营or委托'][i])
    value14 = str(taizhangDict['合同编号'][i])
    value15 = str(taizhangDict['贷款编号'][i])

    value16 = str(taizhangDict['贷款用途'][i])
    value17 = str(taizhangDict['贷款用途产业划分'][i])
    value18 = str(taizhangDict['贷款用途：经营or消费'][i])
    value19 = str(taizhangDict['个人&企业&其他组织'][i])
    value20 = str(taizhangDict['个人：是否农户'][i])

    value21 = str(taizhangDict['企业：农村or城市'][i])
    value22 = str(taizhangDict['其他组织：农村or城市'][i])
    value23 = str(taizhangDict['所属行业'][i])
    value24 = str(taizhangDict['规模'][i])
    value25 = str(taizhangDict['贷款金额\n（元）'][i])

    value26 = str(taizhangDict['期限'][i])
    value27 = str(taizhangDict['期限分类'][i])
    value28 = str(taizhangDict['合同签订时间'][i])
    value29 = str(taizhangDict['贷款发放日'][i])
    value30 = str(taizhangDict['展期日期'][i])
    if value30 == "nan":
        value30 = "2000-01-01 00:00:00"
    if value30 == "NaT":
        value30 = "2000-01-01 00:00:00"

    value31 = str(taizhangDict['贷款到期日'][i])
    value32 = str(taizhangDict['还本付息方式'][i])
    value33 = str(taizhangDict['还本付息方式说明'][i])
    value34 = str(taizhangDict['贷款服务费率\n（%）'][i])
    value35 = str(taizhangDict['贷款利率\n（年化，%）'][i])

    value36 = str(taizhangDict['信用形式'][i])
    value37 = str(taizhangDict['备注'][i]).replace("\n","")
    value38 = str(taizhangDict['是否逾期'][i])
    value39 = str(taizhangDict['贷款五级分类'][i])
    value40 = str(taizhangDict['已偿还贷款金额'][i])

    value41 = str(taizhangDict['当月贷款余额'][i])
    value42 = str(taizhangDict['是否结清'][i])
    value43 = str(taizhangDict['加权利率过渡值'][i])

    sql = "insert into qf_loan (seq_no,origin_customer_no,customer_name,credit_customer,customer_cert_no,city,area,client_manager,check_time,check_user,\n"
    sql = sql + "approval_time,approve_user,applier_type,contract_no,loan_no,loan_usage,loan_usage_industry,loan_usage_target,loaner_type,personal_is_farmer,\n"
    sql = sql + "biz_is_countryside,org_is_countryside,industry,loan_scale,loan_amount,loan_period,loan_period_type,contract_sign_date,loan_date,extend_date,\n"
    sql = sql + "loan_due_date,payment_mthod_monitor,payment_mthod_actual,fee,interest,credit_type,description,is_overdue,loan_level,paid_amount,\n"
    sql = sql + "loan_balance,is_writeoff,weight_rate) values("

    sql = sql + "\""+value1+"\",\""+value2+"\",\""+value3+"\",\""+value4+"\",\""+value5+"\",\""+value6+"\",\""+value7+"\",\""+value8+"\",\""+value9+"\",\""+value10+"\",\n"
    sql = sql + "\""+value11+"\",\""+value12+"\",\""+value13+"\",\""+value14+"\",\""+value15+"\",\""+value16+"\",\""+value17+"\",\""+value18+"\",\""+value19+"\",\""+value20+"\",\n"
    sql = sql + "\""+value21+"\",\""+value22+"\",\""+value23+"\",\""+value24+"\",\""+value25+"\",\""+value26+"\",\""+value27+"\",\""+value28+"\",\""+value29+"\",\""+value30+"\",\n"
    sql = sql + "\""+value31+"\",\""+value32+"\",\""+value33+"\",\""+value34+"\",\""+value35+"\",\""+value36+"\",\""+value37+"\",\""+value38+"\",\""+value39+"\",\""+value40+"\",\n"
    sql = sql + "\""+value41+"\",\""+value42+"\",\""+value43+"\")"

    
    # print(sql)
    cursor.execute(sql)

repayPlanData = pd.read_excel(filepath,sheet_name=[1,1],skiprows=[0,1])
repayPlanDict = {}
for k,v in repayPlanData.items():
    repayPlanDict = v.to_dict()


for i in range(len(repayPlanDict['合同编号'])):
    value1 = str(repayPlanDict['合同编号'][i])
    if value1 == "nan":
        break
    value2 = str(repayPlanDict['贷款编号'][i])
    value3 = str(repayPlanDict['客户名称'][i])
    value4 = str(repayPlanDict['授信对象'][i])
    value5 = str(repayPlanDict['还款期数'][i])

    value6 = str(repayPlanDict['应还日期'][i])
    value7 = str(repayPlanDict['应还本金（元）'][i])
    value8 = str(repayPlanDict['应还利息（元）'][i])
    value9 = str(repayPlanDict['起息日期'][i])
    value10 = str(repayPlanDict['止息日期'][i])

    value11 = str(repayPlanDict['实际还款日期'][i])

    if value11 == "nan":
        value11 = "null"
    if value11 == "NaT":
        value11 = "null"
    value12 = str(repayPlanDict['实际还本'][i])
    if value12 == "nan":
        value12 = "0.00"
    if value12 == "NaT":
        value12 = "0.00"
    value13 = str(repayPlanDict['实际付息'][i])
    if value13 == "nan":
        value13 = "0.00"
    if value13 == "NaT":
        value13 = "0.00"
    value14 = str(repayPlanDict['逾期利息'][i])
    if value14 == "nan":
        value14 = "0.00"
    if value14 == "NaT":
        value14 = "0.00"
    value15 = str(repayPlanDict['贷款余额'][i])

    sql = "insert into qf_payment (contract_no,loan_no,loaner_name,payment_period,period_due_date,required_principal,\n"
    sql = sql + "required_interest,begin_date,end_date,payment_date,paid_pricipal,paid_interest,overdue_interest,loan_balance) \n"
    sql = sql + "values ("+"\""+value1+"\",\""+value2+"\",\""+value3+"\",\""+value5+"\",\""+value6+"\",\""+value7+"\",\""+value8+"\",\n"
    sql = sql + "\""+value9+"\",\""+value10+"\",\""+value11+"\",\""+value12+"\",\""+value13+"\",\""+value14+"\",\""+value15+"\")"

    cursor.execute(sql)

sql = "update qf_loan set check_time = null where check_time = null;"
cursor.execute(sql)
sql = "update qf_loan set approval_time = null where approval_time = null;"
cursor.execute(sql)
sql = "update qf_loan set contract_sign_date = null where contract_sign_date = null;"
cursor.execute(sql)
sql = "update qf_loan set loan_date = null where loan_date = null;"
cursor.execute(sql)
sql = "update qf_loan set extend_date = null where extend_date = null;"
cursor.execute(sql)
sql = "update qf_loan set loan_due_date = null where loan_due_date = null;"
cursor.execute(sql)
sql = "update qf_payment set period_due_date = null where period_due_date = null;"
cursor.execute(sql)
sql = "update qf_payment set begin_date = null where begin_date = null;"
cursor.execute(sql)
sql = "update qf_payment set end_date = null where end_date = null;"
cursor.execute(sql)
sql = "update qf_payment set payment_date = null where payment_date = null;"
cursor.execute(sql)
sql = "update qf_payment set payment_date = null where payment_date = '0000-00-00 00:00:00';"
cursor.execute(sql)


cursor.close()
conn.commit()
conn.close()
