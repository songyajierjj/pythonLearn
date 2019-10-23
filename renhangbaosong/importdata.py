import pymysql


path = "D:/千方/人行征信/个人征信报送/报送源数据/20180802/"

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='awchaindb_mirror', charset='utf8')
cursor = conn.cursor()
sql = ""
sql = "truncate table axs_customize_template;\n"
sql = sql + "truncate table cus_customer;\n"
sql = sql + "truncate table lns_loan;\n"
sql = sql + "truncate table lns_loan_detail_period;\n"
sql = sql + "truncate table lns_loan_product_base_rule;\n"
sql = sql + "truncate table usr_user;\n"
sql = sql + "truncate table lns_repayment_detail;\n"
sql = sql + "truncate table lns_repayment_order;\n"
sql = sql + "truncate table pro_product_sign_rule;"
cursor.execute(sql)

data = open(path+"axs_customize_template.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"cus_customer.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"lns_loan.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"lns_loan_detail_period.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"lns_loan_product_base_rule.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i)

data = open(path+"usr_user.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"lns_repayment_detail.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"lns_repayment_order.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

data = open(path+"pro_product_sign_rule.sql",encoding='utf8')
for i in data.readlines():
    cursor.execute(i) 

conn.commit()
cursor.close()
conn.close()