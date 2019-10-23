# -*- coding: utf-8 -*-
import math
import functools
import types
from collections import Iterator
from collections import Iterable
from functools import reduce


def my_abs(x):
#校验是整数或者小数才能做运算否则抛出异常
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(1))

#返回多个值其实返回的是一个tuple
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = x - step * math.sin(angle)
	return nx,ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

def cals(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print(cals(1,2,3))
sum = [2,3,4]
print(cals(*sum))
print("可变参数")
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('Bob',35,city='BeiJing')
person('Adam',45,gender='M',job='Enginerr')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

print("可变关键字参数")
#限制关键字参数只能传入city,job
def person1(name, age, *, city, job):
    print(name, age, city, job)

person1('Jack', 24, city='Beijing', job='Engineer')
#person1('Jack', 24, city1='Beijing', job='Engineer')传入city1就报错

#定义一个默认值可以不传city
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

print("递归")
def face(n):
	if n==1:
		return 1
	return n * face(n-1)
print(face(5))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print("切片")
l = list(range(100))
#取前10个元素
print(l[0:10])
print(l[:10])
#取后10个
print(l[-10:])
#前11-20个
print(l[10:20])
#前10个每两个取一个
print(l[:10:2])
#所有数每5个取一个
print(l[::5])
#原样复制
print(l[:])
print(l[::])
print("迭代")
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,":",v)
#判断是否可以迭代
print("str迭代:",isinstance('abc', Iterable))
print("list迭代:",isinstance([1,2,3], Iterable))
print("int迭代:",isinstance(123, Iterable))
#下标循环enumerate
for i,value in enumerate(['A', 'B', 'C']):
	print(i,value)
print("列表生成式")
print("生成1到10的list,list(range(1,11))")
print(list(range(1,11)))
print("生成1*1到10*10的list,[x*x for x in range(1,11)]")
print([x*x for x in range(1,11)])
#取偶数的平方
print([x*x for x in range(1,11) if x%2 == 0])
#使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
#导入OS模块
import os
#列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])
#列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
#list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) ]
print(L2)
print("生成器generator")
g = (x * x for x in range(5))
for n in g:
	print(n)
#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(5)
#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib1(6)
print("用for得不到fib1的返回值NONE")
for n in f:
	print(n)
g = fib1(6)
print("捕捉StopIteration得到返回值")
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
#杨辉三角
def triangles(max):
	a = 1
	b = 1
	c = 0
	l = []
	temp = []
	while a <= max:
		if a == 1:
			l = [1]
		elif a == 2:
			l = [1,1]		
		else:
			b = a
			l = [1]
			c = 0
			while b > 2:
				l.append(temp[c:c+1][0]+temp[c+1:c+2][0])
				c += 1
				b -= 1
			l.append(1)
		yield l
		temp = l
		a += 1
for t in triangles(10):
	print(t)
#迭代器
#Iterable可迭代的Iterator迭代器
#isinstance('abc', Iterable)true
#isinstance('abc', Iterator)False
#只有生成的generator是迭代器
#转换器iter
print(isinstance(iter([]), Iterator))
#为什么list、dict、str等数据类型不是Iterator？
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
#直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
#只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

#函数式编程
#函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，
#就可以把复杂任务分解成简单的任务，
#这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
#对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，
#比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言

#高阶函数
#abs(-10)是函数调用abs是函数本身
print(abs(-10))
#函数本身也可以赋值给变量
f = abs
print(f(-10))
def add(x,y,f):
	return f(x)+f(y)
print(add(-5,-1,abs))

#map/reduce
#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x*x
r = map(f,list(range(1,10)))
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))
#str转换为int的函数：
#x=1,y=3,13,x=13y=5,135,x=135,y=7,1357,x=1357,y=9,13579
def fn(x,y):
	return x*10+y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))
#合并为一个函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
   	return name.lower()[0:1].upper()+name.lower()[1:]
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	def fx(x,y):
		return x * y
	return reduce(fx,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#字符串'123.456'转换成浮点数123.456
#先将字符串用小数点分成两个数组，分别算出值，
#用整数部分的值加上小数部分除以10的数组长度的幂次
def str2float(s):
	def char2num(a):
		return int(a)
	def fa(x,y):
		return x*10 + y
	point = True
	s1 = []
	s2 = []
	for n in s:
		if point and n != ".":
			s1.append(n)
		elif point and n == ".":
			point = False
		else:
			s2.append(n)
	return reduce(fa, map(char2num, s1))+reduce(fa, map(char2num, s2))/pow(10,len(s2))
print('str2float(\'123.456\') =', str2float('123.456'))
print("")
print("filter()函数")
#filter()也接收一个函数和一个序列。
#和map()不同的是，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素
#在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

#求素数
#构造一个三开始的奇数序列的生成器
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
#定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0
#生成器
def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
	if n < 20:
		print(n)
	else:
		break 
#取回数
def is_palindrome(n):
	s1 = str(n)
	s2 = ""
	for a in s1:
		s2 = a + s2 
	if s1 == s2:
		return n
	else:
		return False
output = filter(is_palindrome, range(100, 200))
print(list(output))
print("")
print("sorted函数")
#排序
print(sorted([36, 5, -12, 9, -21]))
#自定义排序
print(sorted([36, 5, -12, 9, -21], key=abs))
#字符串排序默认安装ASCII排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[:1]
def by_score(t):
    return t[-1:]
L2 = sorted(L, key=by_name)
L3 = sorted(L,key=by_score,reverse=True)
print(L2)
print(L3)
print("")
print("返回函数")
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1,3,5,7,9)
print(f())
#即使传入参数相同返回的也是不同的函数
f1 = lazy_sum(1,3,5,7,9)
print(f==f1)
#返回的函数并没有立刻执行，而是直到调用了才执行
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
def count1():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))#f(i)立刻被执行，因此i的当前值被传入f()
	return fs
f1,f2,f3 = count1()
print(f1(),f2(),f3())
print("")
print("装饰器decorator")
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def now():
	print('2015-3-25')
now()
print("now.name:",now.__name__)

def log1(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("%s %s():" %(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log1('execute')
def now1():
	print('2015-3-25')
now1()
print("now1.name:",now1.__name__)

def beforeAndAfter(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print("begin call")
		func(*args,**kw)
		print("after call")
	return wrapper
@beforeAndAfter
def test():
	print("test")
test()
print("")
print("偏函数")
print(int("12345"))
print(int('12345',base=8))
print(int('12345',16))
#普通方法
def int2(x, base=2):
	return int(x, base)
print(int2('100000'))
#偏函数
int2 = functools.partial(int,base=2)
print(int2('100000'))
#int2('10010')相当于kw = { 'base': 2 }，int('1001',**kw)
max2 = functools.partial(max, 10)
max2(5,6,7)
#相当于把10作为*args的一部分加到左边
args = (10,5,6,7)
max(args)

#pip install 模块名
print("")
#类
#__xxx表示私有属性外部不能访问__xxx__表示特殊变量可以访问
class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print("%s:%s" % (self.__name,self.__score))
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name
	def set_name(self,name):
		self.__name = name
	def get_score(self):
		return self.__score
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
bart = Student("yjsong",97)
print("bart.name:",bart.get_name());
bart.print_score()
print("bart.grade:",bart.get_grade())
print(bart._Student__name)
print("")
print("继承和多态")
class Animal(object):
	def run(self):
		print("Animal is running")
class Dog(Animal):
	def run(self):
		print("Dog is running")
	def eat(self):
		print("Eating meat")
class Cat(Animal):
	def run(self):
		print("Cat is running")
class Husky(Dog):
	def run(self):
		print("Husky is running")
dog = Dog()
dog.run()
cat = Cat()
cat.run()
animal = Animal()
print(isinstance(dog,Animal))
print(isinstance(dog,Dog))
print(isinstance(animal,Dog))
def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
print("")
print("获取对象信息")
def fm():
	pass
print(type(fm)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print(isinstance(123,int))
#dir()获得一个对象的所有属性和方法
print(dir('ABC'))
#__xxx__的属性和方法是特殊用途的在len函数内部会自动调用__len__方法，剩下的是普通属性和方法
print(len("ABC"))
print("ABC".__len__())
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
#有x属性吗
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)#设置一个属性Y
print(hasattr(obj,'y'))
print(getattr(obj,'y'))#获取属性Y
print(obj.y)#获取属性Y
print(getattr(obj,'z',404))#获取属性Z如果不存在则返回404
print(hasattr(obj,'power'))#有属性power
print(getattr(obj,'power'))#获取属性power
fn = getattr(obj,'power')#获取属性power并赋值给fn
print(fn())#访问fn
#能用obj.x就不用getattr(obj,'x')只有不确定时才使用正确用法如下
def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None
print("")
print("实例属性和类属性")
class Student1(object):
	name = 'Student'#类属性所有实例都可以访问
	def __inin__(self,age):
		self.age = age#age是实例的属性
s = Student1()#创建实例
print(s.name)#打印实例的name属性因为实例没有name属性，所以查询class的name属性
print(Student1.name)#打印类的name属性
s.name = "yjsong"#给实例绑定name属性
print(s.name)#实例和class都有name属性，但是实例的属性优先级比类的优先级高，所以会屏蔽类的属性
print(Student1.name)#类属性并未消失还存在所以是student
del s.name#删除实例的name属性
print(s.name)#则继续查询类的属性所以是student
print("")
print("面向对象高级编程")
print("使用__slots__")
class Student2(object):
	pass
s = Student2()
s.name = 'yjsong'#动态给实例绑定属性
print(s.name)
def set_age(self,age):#定义一个函数作为实例的方法
	self.age = age 
from types import MethodType
s.set_age = MethodType(set_age,s)#给实例绑定方法
s.set_age(25)
print(s.age)
#但是给实例绑定的方法另外一个实例是不可以用的，所以给类绑定方法
s2 = Student2()
def set_score(self,score):
	self.score = score
Student2.set_score = set_score
s2.set_score(100)
print("s2.score:",s2.score)
s.set_score(90)
print("s.score:",s.score)
#为了达到限制实例的属性，只允许对student添加name和age属性
#python允许在定义class的时候定义__slots__变量，来限制class添加的属性
class Student3(object):
	__slots__ = ('name','age')#用tuple定义允许绑定的属性名称
s = Student3()
s.name = 'yjsong'#绑定属性name
s.age = 26#绑定属性age
#s.score = 99 #绑定属性score
#__losts__仅对当前的类实例起作用，对子类是不起作用的
class GraduateStudent(Student3):
	pass
g = GraduateStudent()
g.score = 99
print(g.score)	
print("")
print("使用@property")
#@property的实现比较复杂，把一个getter方法变成属性，只需要加上@property就可以了，
#此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
#于是，我们就拥有一个可控的属性操作：
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student4(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError("score must be an integer!")
		if value < 0 or value > 100:
			raise ValueError("score must be 0-100！")
		self._score = value
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError("width must be an integer!")
		self._width = value
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError("height must be an integer")
		self._height = value
	@property
	def resolution(self):
		return self._width * self._height
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
print("")
print("定制类")
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
class Student5(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student5 object (name:%s)' % self.name
	__repr__ = __str__
print(Student5("yjsong"))
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self#实例本身就是迭代对象，所以返回自己
	def __next__(self):
		self.a,self.b = self.b,self.a+self.b#计算下一个值
		if self.a >= 100:#退出循环的条件
			raise StopIteration()
		return self.a
#把Fib用于for循环但不能用list的下标访问
for n in Fib():
	print(n)
#使用__getitem__可以让函数按下标访问
class Fib1(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a,b = b, a + b
		return a
f = Fib1()
print(f[10])
#此时虽然能用下标访问但是不能用切片访问因为传入的参数可能是n
class Fib2(object):
	def __getitem__(self,n):
		if isinstance(n,int):#n是索引
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):#n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
f = Fib2()
print(f[0:5])
print(f[:10])
#__getattr__在没有找到属性的情况下调用getattr还可以抛出错误
class Student6(object):
	def __init__(self):
		self.name = 'Michael'
	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student6()
print(s.score)
print(s.age())
class Chain(object):
	def __init__(self,path=''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
	def __str__(self):
		return self._path
	__repr__ = __str__
print(Chain().status.user.timeline.list)
#__call__()可以对实例进行直接调用
class Student7(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print('my name is %s ' % self.name)
s = Student7('yjsong')
s()
#枚举类
from enum import Enum,unique
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
#unique装饰器可以帮助我们检查保证没有重复值
print(Weekday.Mon)
print(Weekday['Mon'])
print(Weekday(1))
print(Weekday.Mon.value)
#错误处理
try:
	print('try:')
	r = 1/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')




