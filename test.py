# -*- coding: UTF-8 -*-
 
#数字
var1 = 1
var2 = 2
print(var1)
print(var2)
print("")

#字符串
a,b,c = 1,2,"jonh"
print(a)
print(b)
print(c)
a = b = c = 1
print(a,b,c)
print("")

s = "ilovepython"
print(s,s[1:5],s[0],s[2:],s * 2,s + "TEST")
print("")

#列表
list = [ 'list', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)              # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个的元素 
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表
print("")

#元组（元组不允许更新）
tuple = ( 'tuple', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)
print("")

#字典
dict = {}
dict['one'] = "This is a dictionary"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 3: 'sales'}
 
print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值
print("")

#type()函数返回变量的类型
n=1
print(type(n))
n="sfasf"
print(type(n))
n=[2,2]
print(type(n))
n=(12,2)
print(type(n))
n={1:"132","sdf":"121"}
print(type(n))
print("")

#isinstance(a,int)