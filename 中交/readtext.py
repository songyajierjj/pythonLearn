

data = open("d:/新建文本文档.txt",encoding='UTF-8')
writeFile = open("d:/1.txt","a+",encoding='GBK')

for i in data.readlines():
    i = i.replace("\n","");
    writeData = "update "