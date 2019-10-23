import pymysql

path = "D:/千方/好运条/用户信息/白名单用户统计/重高Finally.txt"

conn = pymysql.connect(host='172.17.4.63', port=3306, user='root', passwd='root', db='awchaindb', charset='utf8')
cursor = conn.cursor()


data = open(path,encoding='GBK')
for line in data.readlines():
	lineList = line.split(",")
	sql = "SELECT period_begin_date,period_due_date,payment_date \n"
	sql = sql + "from lns_loan_detail_period a \n"
	sql = sql + "LEFT JOIN lns_loan b on b.id = a.loan_id \n"
	sql = sql + "LEFT JOIN cus_customer c on c.id = b.loaner_id \n"
	sql = sql + "where period_begin_date is not null and period_due_date is not null and payment_date is null \n"
	sql = sql + " and c.personal_id = '" + lineList[1] + "' "
	result = cursor.execute(sql)  
	info = cursor.fetchmany(result)
	if len(info) > 0:
		print(line)
