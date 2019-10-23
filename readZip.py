import os  
import os.path  
import datetime
import pymysql
import gzip
import zipfile

path = "D:/千方/人行征信/全量数据/"

date = datetime.datetime.strptime("20170418","%Y%m%d")

futureday = datetime.timedelta(days=1)


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='lmk_credit', charset='utf8')
cursor = conn.cursor()

b = '0'
for i in range(348):
    strDate = (date+futureday).strftime('%Y%m%d')
    newPath = path + strDate + ".zip";
    if os.path.exists(newPath):
        azip = zipfile.ZipFile(newPath)
        a = azip.read(strDate + '/EXPORTTRADEINFO.txt').decode('GBK')
        lineList = a.split("\n")
        for j in range(len(lineList)):
            if j == 0:
                continue
            else:
                b = str(int(b) + 1)
                valueList = lineList[j].replace("\r","").split(",")
                sql = "insert into credit_report values( " + b + ","
                if len(valueList) == 39:
                    for k in range(len(valueList)):
                        if k != 38:
                            sql += "\'"+valueList[k]+"\',"
                        else:
                            sql += "\'" + valueList[k] + "\',\'"+strDate+"\')"
                elif len(valueList) == 40:
                    for k in range(len(valueList)):
                        if k == 0 :
                            continue
                        elif k == 1:
                            sql += "\'"+valueList[0]+"."+valueList[1]+"\',"
                        elif k != 39:
                            sql += "\'"+valueList[k]+"\',"
                        else:
                            sql += "\'"+valueList[k]+"\',\'"+strDate+"\')"
                if len(valueList) == 39 or len(valueList) == 40:
                    print(sql)
                    cursor.execute(sql)	
    date = datetime.datetime.strptime(strDate,"%Y%m%d")
conn.commit()
cursor.close()
conn.close()
