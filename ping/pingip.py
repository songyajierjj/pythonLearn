#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import subprocess
import re
# import schedule
import time
# import os


writePath = "D:/python/"

def job():
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nowDate=datetime.datetime.now().strftime('%Y-%m-%d')
    writeFile = open(writePath+nowDate+".txt","a+",encoding='GBK')
    # p = os.system("ping -n 1 -w 1 192.168.10.160")
    # writeFile.write(nowTime+","+str(p)+"\n")
    p = subprocess.Popen(["ping.exe", '9.16.15.119'],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True) 
    out = p.stdout.read()
    writeFile.write(nowTime+","+out.decode("GBK")+"\n")

    writeFile.close()
job()
# schedule.every(1).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(30)
