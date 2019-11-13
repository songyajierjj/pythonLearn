import requests
import json
import logging

def main():
    try:
        file = open("D:/logs/queryrh/message.log", encoding="utf-8", mode="a")
        logging.basicConfig(stream=file,
                        level=logging.DEBUG,
                        format='time:%(asctime)s,message:%(message)s')
        # readData = json.loads(open("D:/logs/queryrh/renghang.txt").read())
        userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        contentType = "application/x-www-form-urlencoded"
        origin = "http://9.16.15.119"
        referer = "http://9.16.15.119/shcreditunion/logon.do?isDissentLogin=null"
        postUrl = "http://9.16.15.119/shcreditunion/logon.do?isDissentLogin=null"
        # postData = json.loads(readData['postData'])
        header = {
            "Content-Type": contentType,
            "Origin": origin,
            "Referer": referer,
            'User-Agent': userAgent
        }

        response = requests.post(postUrl, data=postData, headers=header)

        # 无论是否登录成功，状态码一般都是 statusCode = 200
        logging.info(f"statusCode = {response.status_code}")
        logging.info(f"text = {response.text}")
    except Exception as e:
        logging.info(e)

if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    main()
