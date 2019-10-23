import threading
import time
class mt(threading.Thread):
	def run(self):
		global x
		# lock.acquire()
		for i in range(5):
			x += 10
		time.sleep(1)
		print(x)
		# lock.release()
x = 0
lock = threading.RLock()
def main():
	thrs = []
	for item in range(8):
		thrs.append(mt())
	for item in thrs:
		item.start()
if __name__ == "__main__":
	main()