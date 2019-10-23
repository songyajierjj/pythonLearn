import requests
from bs4 import BeautifulSoup
import pymysql

def wirteIn(writeData):
    conn = pymysql.connect(host='172.17.33.225', port=3306, user='root', passwd='root', db='fangzi', charset='utf8')
    cursor = conn.cursor()
    sql = "insert into house_price (province,city,area,remark,estate_name,pattern,bulit_area,orientation,decoration_style,elevator,\n"
    sql = sql + "floor,location,follow_number,visit_number,public_time,total_price,single_price,create_time) values \n"
    for i in range(len(writeData)):
        if i < len(writeData)-1:
            sql = sql + "("+writeData[i]+"),\n"
        else:
            sql = sql + "(" + writeData[i] + ");"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def getUrl(url,headers,area,writeData):
    res = requests.get(url, headers=headers, timeout=30)
    if res.status_code == 200:
        bsObj = BeautifulSoup(res.text, "html.parser")
        item = bsObj.select("div[class='info clear']")
        for i in range(len(item)):
            hourseObj = BeautifulSoup(str(item[i]), "html.parser")
            title = hourseObj.select(".title")[0].text
            address = hourseObj.select(".address")[0].text
            flood = hourseObj.select(".flood")[0].text
            followInfo = hourseObj.select(".followInfo")[0].text
            totalPrice = hourseObj.select(".totalPrice")[0].text
            unitPrice = hourseObj.select(".unitPrice")[0].text
            addressList = address.split("|")
            j = 0
            estateName = addressList[j].replace(" ","")
            j = j + 1
            if addressList[j].find("室") > - 1:
                patten = addressList[j].replace(" ", "")
            else :
                j = j + 1
                patten = addressList[j].replace(" ", "")
            j = j + 1
            builtArea = addressList[j].replace("平米","").replace(" ","")
            j = j + 1
            orientation = addressList[j].replace(" ","")
            j = j + 1
            decorationStyle = addressList[j].replace(" ","")
            j = j + 1
            elevator = ""
            if len(addressList) >= j+1:
                elevator = addressList[j].replace(" ","")
            floodList = flood.split("-")
            floor = floodList[0].replace(" ","")
            location = floodList[1].replace(" ","")
            followInfoList = followInfo.split("/")
            followNumber = "0"
            visitNumber = "0"
            publicTime = ""
            if len(followInfoList) >= 3:
                followNumber = followInfoList[0].replace(" ","").replace("人关注","")
                visitNumber = followInfoList[1].replace(" ","").replace("次带看","").replace("共","")
                publicTime = followInfoList[2].replace(" ","")
            single = unitPrice.replace("单价","").replace("元/平米","")
            data = "'天津','天津','"+area+"','"+title+"','"+estateName+"','"+patten+"','"+builtArea+"','"+orientation+"','"+decorationStyle
            data = data + "','"+elevator+"','"+floor+"','"+location+"',"+followNumber+","+visitNumber+",'"+publicTime+"',"+totalPrice.replace("万","")+","+single+",now()"
            writeData.append(data)
        return True
    else:
        return False
if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
    baseUrl = "https://tj.lianjia.com/ershoufang/"
    areaList = ["heping","nankai","hexi","hebei","hedong","hongqiao","xiqing","beichen","dongli","baodi"]
    # areaList = ["nankai"]
    writeData = []
    for i in range(len(areaList)):
        result = True
        for j in range(1,100):
            if result:
                if j == 1:
                    result = getUrl(baseUrl + areaList[i] + "/l2l3a3a4a5p3p4p5/", headers,areaList[i],writeData)
                else:
                    result = getUrl(baseUrl + areaList[i] + "/pg"+str(j)+"l2l3a3a4a5p3p4p5/", headers,areaList[i],writeData)
            else :
                break
    for i in range(0,len(writeData),100):
        wirteIn(writeData[i:i+100])
