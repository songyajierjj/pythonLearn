import pymysql


#源文件的路径
sgData = open("D:/千方/好运条/白名单用户统计/山高.txt",encoding='GBK')
writePath = "D:/千方/好运条/白名单用户统计/山高Detail.txt"
writeSgFile = open(writePath,"a+",encoding='GBK')

cgData = open("D:/千方/好运条/白名单用户统计/重高.txt",encoding='GBK')
writePath = "D:/千方/好运条/白名单用户统计/重高Detail.txt"
writeCgFile = open(writePath,"a+",encoding='GBK')


conndb = pymysql.connect(host='ladybird.awservice.net', port=3306, user='awchain', passwd='rd@awchain423%', db='awchaindb', charset='utf8')
cursordb = conndb.cursor()

conndc = pymysql.connect(host='ladybird.awservice.net', port=3306, user='awchain', passwd='rd@awchain423%', db='dc', charset='utf8')
cursordc = conndc.cursor()

for line in cgData:
    lineList = line.split(",")
    sql = "select id from cus_customer where personal_id = '" + lineList[1] + "'"
    cursordb.execute(sql)
    results = cursordb.fetchall()
    customer_id = 0
    for row in results:
        customer_id = row[0]

    sql = "SELECT bank_name,IFNULL(branch_name,''),account_no from cus_customer_account where customer_id = " + str(customer_id) + " ORDER BY create_time desc"
    cursordb.execute(sql)
    results = cursordb.fetchall()
    bank_name = ""
    branch_name = ""
    account_no = ""
    for row in results:
        bank_name = row[0]
        branch_name = row[1]
        account_no = row[2]
        break

    sql = "SELECT id from crt_creditline_product_apply where customer_id = " + str(customer_id)
    cursordb.execute(sql)
    results = cursordb.fetchall()
    product_id = 0
    for row in results:
        product_id = row[0]

    sql = "SELECT form_id from udf_form_mapping where object_name = 'crt_creditline_product_apply' and object_id = " + str(product_id)
    cursordc.execute(sql)
    results = cursordc.fetchall()
    form_id = 0
    for row in results:
        form_id = row[0]

    sql = "SELECT ifnull(attribute_value,'') from udf_form_attribute where attribute_key = 'sxsq_address' and form_id = " + str(form_id)
    cursordc.execute(sql)
    results = cursordc.fetchall()
    address = ""
    for row in results:
        address = row[0]

    conndb.commit()
    conndc.commit()

    writeCgFile.write(lineList[0]+","+lineList[1]+","+lineList[2]+","+bank_name+","+branch_name+","+account_no+","+address+"\n")
    

cursordb.close()
cursordc.close()
conndb.close()
conndc.close()
writeCgFile.close()