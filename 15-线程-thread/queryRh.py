#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
from urllib import parse,request
import time
import json

import http.client
import logging

# logger = logging.getLogger()  # 实例化一个logger对象
# logger.setLevel(logging.INFO)  # 设置初始显示级别

# # 创建一个文件句柄
# file_handle = logging.FileHandler("D:/logs/queryrh/message.log", encoding="UTF-8")
# # 创建一个流句柄
# stream_handle = logging.StreamHandler()

# # 创建一个输出格式
# fmt = logging.Formatter(f"{'*'*28}\n"
#                         "> %(asctime)s\n"
#                         "> %(levelname)s - "
#                         "%(filename)s - "
#                         "[line:%(lineno)d]\n"
#                         f"{'-'*40}\n"
#                         "  %(message)s\n"
#                         f"{'-'*40}\n\n",
#                         datefmt="%a, %d %b %Y %H:%M:%S"
#                         )

# file_handle.setFormatter(fmt)  # 文件句柄设置格式
# # stream_handle.setFormatter(fmt)  # 流句柄设置格式

# logger.addHandler(file_handle)  # logger对象绑定文件句柄

file = open("D:/logs/queryrh/message.log", encoding="utf-8", mode="a")
logging.basicConfig(stream=file,
    level=logging.DEBUG,
    format='time:%(asctime)s,message:%(message)s')

readData = json.loads(open("D:/logs/queryrh/renghang.txt").read())
ip = readData['ip']
port = readData['port']
url = readData['url']


def main():
	try:
	    readData = json.loads(open("D:/logs/queryrh/renghang.txt").read())
	    ip = readData['ip']
	    port = readData['port']
	    url = readData['url']
	    connection = http.client.HTTPConnection(ip,port)
	    connection.request('GET', url)
	    response = connection.getresponse()
	    resultData = response.read().decode()
	    
	    logging.info(resultData)
	except Exception as e:
		logging.info(e)


if __name__ == "__main__":
    main()