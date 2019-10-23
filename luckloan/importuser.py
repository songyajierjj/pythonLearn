import pymysql

data = open("D:/千方/好运条/白名单用户统计/重高Detail.txt",encoding='GBK')
writePath = "D:/千方/好运条/白名单用户统计/重高Finally.txt"
writeCgFile = open(writePath,"a+",encoding='GBK')

conndb = pymysql.connect(host='ladybird.awservice.net', port=3306, user='awchain', passwd='rd@awchain423%', db='awchaindb', charset='utf8')
cursordb = conndb.cursor()

for line in data:
    lineList = line.split(",")
    sql = "select id from cus_customer where personal_id = '" + lineList[1] + "'"
    cursordb.execute(sql)
    results = cursordb.fetchall()
    customer_id = 0
    for row in results:
        customer_id = row[0]

    sql = "SELECT count(0) from etc_vehicle_info where customer_id = " + str(customer_id)
    cursordb.execute(sql)
    results = cursordb.fetchall()
    vehicleCount = 0
    for row in results:
        vehicleCount = row[0]

    writeCgFile.write(line.replace("\n","")+","+str(vehicleCount)+"\n")
cursordb.close()
conndb.close()
writeCgFile.close()