import requests
from bs4 import BeautifulSoup


writePath = "D:/download/result.txt"
writeFile = open(writePath,"a+",encoding='GBK')


def wirteIn(data):
    readData = data.replace(" ", "").replace("/", "").replace("\r", "").rstrip().lstrip()
    dataList = readData.split("\n")
    writeData = ""
    for readline in dataList:
        if readline != "":
            writeData += readline.replace("元月","").replace("㎡","")+"&"
    writeData += "\n"
    writeFile.write(writeData)

def getUrl(url,headers):
    print(url)
    res = requests.get(url, headers=headers, timeout=30)
    print(res.status_code)
    if res.status_code == 200:
        bsObj = BeautifulSoup(res.text, "html.parser")
        priceList = bsObj.findAll("div", {"class": "content__list--item"})
        for detail in priceList:
            wirteIn(detail.get_text())

if __name__ == "__main__":
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        baseUrl = "https://bj.lianjia.com/zufang/"
        for i in range(1,101):
            print(i)
            if i == 1:
                getUrl(baseUrl, headers)
            else:
                getUrl(baseUrl+"pg"+str(i), headers)
    except Exception as e:
        print(u'获取数据失败',e)
