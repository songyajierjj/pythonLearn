import threading
class myThread(threading.Thread):
	def __init__ (self,mynum):
		super().__init__()
		self.mynum = mynum
	def run(self):
		for i in range(self.mynum,self.mynum+5):
			print(str(i*i))

ma = myThread(1)
mb = myThread(16)
ma.start()
mb.start()