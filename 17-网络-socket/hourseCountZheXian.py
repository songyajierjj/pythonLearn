#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   # 雅黑字体


conn = pymysql.connect(host='172.17.33.225', port=3306, user='root', passwd='root', db='fangzi', charset='utf8')
areaList = ["郑州","天津","北京","重庆","广州","深圳","武汉","长沙","石家庄","上海","西安","杭州"]
colorList = ["b-.","b-.v","b:1","b-s","b-.p","b:*","g-.","g-.v","g:1","g-s","g-.p","g:*",]
i = 0
for city in areaList:
    sql = "SELECT DATE_FORMAT(create_time,'%Y-%m-%d') as date,city,count as number from second_house_count where city = '"+city+"'"
    data = pd.read_sql(sql,con = conn)
    x = list(data.date)
    y = list(data.number)
    plt.plot(x,y,colorList[i], linewidth=1,label=city)
    i = i + 1
plt.xlabel("Day")
plt.ylabel("Count")
plt.title("二手房数量")
plt.legend()
plt.show()
conn.close()