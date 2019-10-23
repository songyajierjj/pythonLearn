import requests
from bs4 import BeautifulSoup
import pymysql

writePath = "D:/download/result.txt"
writeFile = open(writePath,"a+",encoding='GBK')


def wirteIn(writeData):
    conn = pymysql.connect(host='172.17.33.225', port=3306, user='root', passwd='root', db='fangzi', charset='utf8')
    cursor = conn.cursor()
    sql = "insert into second_house_count (count,city,create_time) values \n"
    for i in range(len(writeData)):
        if i < len(writeData)-1:
            sql = sql + "("+writeData[i]+"),\n"
        else:
            sql = sql + "(" + writeData[i] + ");"
    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def getUrl(url,headers,writeData):
    res = requests.get(url, headers=headers, timeout=30)
    result = ""
    if res.status_code == 200:
        bsObj = BeautifulSoup(res.text, "html.parser")
        item = bsObj.select("h2[class='total fl']")
        countObj = BeautifulSoup(str(item[0]), "html.parser")
        result = countObj.text.split(" ")[1].replace(" ","")+",'"+countObj.text.split(" ")[2].replace("套","").replace("二手房","").replace("在售源","").replace(" ","")+"',now()"
        writeData.append(result)

if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
    baseUrl1 = "https://"
    baseUrl2 = ".lianjia.com/ershoufang/rs/"
    areaList = ["zz","tj","bj","hf","cq","xm","gz","sz","wh","cs","sjz","hrb","su","cc","sh","cd","jn","xa","ty","hz"]
    # areaList = ["zz"]
    writeData = []
    for i in range(len(areaList)):
        getUrl(baseUrl1 + areaList[i] + baseUrl2,headers,writeData)

    wirteIn(writeData)
