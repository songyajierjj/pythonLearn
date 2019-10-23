import queue
import random
q = queue.PriorityQueue()
class Node:
	def __init__(self,x):#构造函数
		self.x = x
	# def __lt__(self,other):#内置函数
	# 	return other.x > self.x
	# def __str__(self):
	# 	reutrn "{}".format(self.x)

a = [0]*10
for i in range(10):
	a[i] = int(random.uniform(0,10))
for i in a:
	print(i,end=' ')
	q.put(i)
print("--------------")
while q.qsize():
	print(q.get(),end=' ')