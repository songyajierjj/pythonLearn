data = open("D:/project/python/renhangchaxun/message.log",encoding='GBK')
for line in data:
	responseDict = eval(line)
	print(bytes(responseDict['xml'],encoding="GBK").decode())