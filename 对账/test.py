import pandas as pd
import numpy as np
import json
import pymysql

# readData1 = open("D:/千方/互联网金融/121EXPORTTRADEINFO1.txt")
# readData2 = open("D:/千方/互联网金融/121EXPORTTRADEINFO2.txt")

# writeFile1 = open("D:/千方/互联网金融/result1.txt","a+",encoding='GBK')
# writeFile2 = open("D:/千方/互联网金融/result2.txt","a+",encoding='GBK')

# writeData = ""
# for i in readData1.readlines():
#     dataList = i.split(",")
#     if len(dataList) > 2:
#         name = dataList[0]
#         name = name[0:1]+"英雄"
#         cardNo = dataList[2]
#         cardNo = cardNo[0:6]+"19890121"+cardNo[-4:]
#         writeData = i.replace(dataList[2],cardNo)
#         writeData = writeData.replace(dataList[0],name)
#         writeFile1.write(writeData)
# writeFile1.close()

# for i in readData2.readlines():
#     dataList = i.split(",")
#     if len(dataList) > 2:
#         name = dataList[0]
#         name = name[0:1]+"耀明"
#         cardNo = dataList[2]
#         cardNo = cardNo[0:6]+"19890121"+cardNo[-4:]
#         writeData = i.replace(dataList[2],cardNo)
#         writeData = writeData.replace(dataList[0],name)
#         writeFile2.write(writeData)
# writeFile2.close()



# readData = open("D:/千方/人行征信/历史错误数据处理/上报无最终结果.txt")
# resultFile = open("D:/千方/人行征信/历史错误数据处理/1.txt","a+",encoding='GBK')

# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='lmk_credit', charset='utf8')
# cursor = conn.cursor()

# for i in readData.readlines():
#     sql = "SELECT create_time,pay_status from tb_transaction where order_no = \"" + i.replace("\n","") + "\""
    
#     result = cursor.execute(sql) 

#     info = cursor.fetchmany(result)
#     for j in info:
#         resultFile.write(i.replace("\n","")+","+str(j[0])+","+str(j[1])+"\n")
    
    
# conn.commit()
# cursor.close()
# conn.close()

a = 200030
b = 100

print(type(round(a/b)))

