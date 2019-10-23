#coding=utf-8
from pymongo import MongoClient
import json


#建立MongoDB数据库连接
#client = MongoClient()
#client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('172.17.4.60', 27017)


#连接所需数据库,cms为数据库名
db=client.cms

#连接所用集合，也就是我们通常所说的表，mobilearea为表名
collection=db.mobilearea

#接下里就可以用collection来完成对数据库表的一些操作

#查找集合中所有数据
#for item in collection.find():
#    print item

#查找集合中单条数据
#print(collection.find_one())

#向集合中插入数据

fmobile = open("D:/千方/CMS+决策引擎/手机号归属地.txt",encoding='utf-8')
mobilelist = []
for i in fmobile.readlines():
	mobilelist = i.split("@")
	if(len(mobilelist) == 7):
		collection.insert({'id':mobilelist[0],'mobile':mobilelist[1],'province':mobilelist[2],'city':mobilelist[3],'crop':mobilelist[4],'areacode':mobilelist[5],'postcode':mobilelist[6].replace("\n","")})

#更新集合中的数据,第一个大括号里为更新条件，第二个大括号为更新之后的内容
#collection.update({Name:'Tom'},{Name:'Tom',age:18})

#删除集合collection中的所有数据
#collection.remove()

#删除集合collection
#collection.drop()