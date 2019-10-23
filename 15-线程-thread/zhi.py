import threading
def zhiyun(x,y):
	for i in range(x,y):
		print(str(i*i)+";")

ta = threading.Thread(target=zhiyun,args=(1,6))
tb = threading.Thread(target=zhiyun,args=(16,21))
ta.start()
tb.start()