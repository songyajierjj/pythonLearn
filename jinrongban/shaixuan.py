import os
import os.path
import datetime

month = "6"

#源文件的路径
readData = open("D:/新建文本文档.txt",encoding='GBK')

writePath1 = "D:/1.txt"
writeFile1 = open(writePath1,"a+",encoding='GBK')

writePath2 = "D:/2.txt"
writeFile2 = open(writePath2,"a+",encoding='GBK')

amount = 0.0
a = {}
b = {}

for line in readData:
    line = line.replace("\n","")
    lineList = line.split(",")

    if lineList[0] != "":
        
        if lineList[0] in a:
            print(lineList[0]+","+lineList[1])
        else:
            a[lineList[0]] = lineList[0]+"_"+lineList[1]
    if lineList[2] != "":
        if lineList[2] in b:
            print(lineList[2]+","+lineList[3])
        else:
            b[lineList[2]] = lineList[2]+"_"+lineList[3]

readData = open("D:/新建文本文档.txt",encoding='GBK')
for line in readData:
    line = line.replace("\n","")
    lineList = line.split(",")
    if (lineList[2]) in a:
        continue
    else:
        writeFile1.write(lineList[2]+","+lineList[3]+"\n")

readData = open("D:/新建文本文档.txt",encoding='GBK')
for line in readData:
    line = line.replace("\n","")
    lineList = line.split(",")
    if (lineList[0]) in b:
        continue
    else:
        writeFile2.write(lineList[0]+","+lineList[1]+"\n")

print(len(b))
print(len(a))

