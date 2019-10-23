import pymysql


#源文件的路径
readData = open("D:/千方/好运条/白名单用户统计/山东白名单.txt",encoding='GBK')

writePath = "D:/千方/好运条/白名单用户统计/sd.txt"
writeFile = open(writePath,"a+",encoding='GBK')

conn = pymysql.connect(host='ladybird.awservice.net', port=3306, user='awchain', passwd='rd@awchain423%', db='awchaindb_mirror', charset='utf8')
cursor = conn.cursor()

for line in readData:
    lineList = line.split(",")
    sql = "SELECT id from cus_customer where personal_id = '" + lineList[0] + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    customer_id = 0
    for row in results:
    	customer_id = row[0]
    sql = "SELECT login_name from usr_user where customer_id = " + str(customer_id)
    cursor.execute(sql)
    results = cursor.fetchall()
    login_name = ""
    for row in results:
    	login_name = row[0]
    writeFile.write(lineList[0]+","+lineList[1]+","+login_name+"\n")
conn.commit()
cursor.close()
conn.close()
writeFile.close()