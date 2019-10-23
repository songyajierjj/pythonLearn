from tkinter import *
from PIL import  ImageTk 
from PIL import Image
import os,shutil,sys
import tkinter.font as tkFont 
from tkinter import ttk
from tkinter.filedialog import askdirectory,askopenfilename
import tkinter.messagebox
import time,datetime
import threading
import imagehash_retrieval as imagehash_retrieval
#期望图像显示的大小  
w_box = 250
h_box = 160
w_box1 = 250
h_box1 = 160



#四个hash加密算法
import imagehash
path_img = ''
path_folder = ''

def clicked1():

    print(path_img)
    hash_res = imagehash_retrieval.imagehash_retrieval(var1, var2,'ahash',thred=0)
    print(hash_res)
    
    
def clicked2():

    hash_res = imagehash_retrieval.imagehash_retrieval(var1, var2,'dhash',thred=0)
    print(hash_res)
        
    
    
def clicked3():

    hash_res = imagehash_retrieval.imagehash_retrieval(var1, var2,'phash',thred=0)
    print(hash_res)
    
    
    
def clicked4():

    hash_res = imagehash_retrieval.imagehash_retrieval(var1, var2,'whash',thred=0)
    print(hash_res)
    
#将结果保存至文件夹泽
def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print ("copy %s -> %s"%( srcfile,dstfile))
def save():
    for item in tree.get_children():  
        item_text = tree.item(item,"values")  
        fileB=os.path.join(item_text[1],item_text[2]+item_text[3])#被复制
        file2B=os.path.join(var2.get(),"泽",'find_'+item_text[2]+item_text[3])#复制去的文件
        mycopyfile(fileB,file2B)

#函数声明
def resize(w, h, w_box, h_box, pil_image):  #图片缩放
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
  f2 = 1.0*h_box/h  
  factor = min([f1, f2])  
  width = int(w*factor)  
  height = int(h*factor)  
  return pil_image.resize((width, height), Image.ANTIALIAS)



def selectPath1():#图片选择
    path_img = askopenfilename()
    print(path_img)
    var1.set(path_img)
    
    
def selectPath():#路径选择
    path_folder = askdirectory()
    print(path_folder)
    print(var2)
    var2.set(path_folder)
  



def Init_dog():#图像显示初始化
    global label1,label2,image4,image5
    image4 = Image.open('img1.jpg')  #打开img1的图像
    w, h = image4.size              #获取原比例    
    #w和h分开会报错“TypeError: unsupported operand type(s) for /: 'float' and 'tuple'”
    


    pil_image_resized = resize(w, h, w_box, h_box, image4)#改成合适比例函数
    image4 = ImageTk.PhotoImage(pil_image_resized)         #转成XX对象   
    label1.configure(image = image4)
    #label2.configure(image = image4)
    
    image5 = Image.open('img1.jpg')  #打开(因为image4全局后，这里引用上面就用不了了)
    pil_image_resized = resize(w, h, w_box1, h_box1, image5)    #改成合适比例函数
    image5 = ImageTk.PhotoImage(pil_image_resized)              #转成XX对象   




#鼠标点击列表的监听
from PIL import Image
import pytesseract

def treeviewClick2(event):#右击打开目录
    print ('右击')
    for item in tree.selection():
        item_text = tree.item(item,"values")
        os.system("start explorer "+str(item_text[1]))

def treeviewClick1(event):#双击打开选定的图片
    print ('双击')
    for item in tree.selection():
        item_text = tree.item(item,"values")
        os.startfile(item_text[1]+'\\'+item_text[2]+item_text[3])     

def treeviewClick(event):#单击展示选定的图片
    print ('单击')
    for item in tree.selection():
        item_text = tree.item(item,"values")
        showPic2(item_text[1]+'\\'+item_text[2]+item_text[3])#调用展示图片函数
    
#点击列表调用的函数
def showPic3(path):
    global image13
    image1 = Image.open(path)           #打开
    w, h = image1.size                  #获取原比例
    image1_resized = resize(w, h, w_box1, h_box1, image1)#改成合适比例函数
    image13= ImageTk.PhotoImage(image1_resized)         #转成XX对象

#鼠标单击的调用
def showPic2(path):
    global label2,image12
    image1 = Image.open(path)           #打开
    w, h = image1.size                  #获取原比例
    image1_resized = resize(w, h, w_box, h_box, image1)#改成合适比例函数
    image12= ImageTk.PhotoImage(image1_resized)         #转成XX对象
    label2.configure(image = image12)
    
#显示所查找的图片
def showPic1():
    global label1,image11
    image1 = Image.open(var1.get())     #打开
    w, h = image1.size                  #获取原比例
    image1_resized = resize(w, h, w_box, h_box, image1)#改成合适比例函数
    image11= ImageTk.PhotoImage(image1_resized)         #转成XX对象
    label1.configure(image = image11)

def treeview_sort_column1(tv, col, reverse):#Treeview、列名、排列方式（桶排序）
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column1(tv, col, not reverse))

def treeview_sort_column2(tv, col, reverse):#Treeview、列名、排列方式（数字排序）
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(key=lambda t: float(t[0]), reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column2(tv, col, not reverse))

def delButton(tree):#清空tree表列
    x=tree.get_children()
    for item in x:
        tree.delete(item)

def LbClick1(event):#listbox点击
    try:
        showPic3(lb.get(lb.curselection()))
    except:
        pass

def LbClick2(event):#listbox双击
    try:
        print (lb.get(lb.curselection()))
        #读取图像  
        im=Image.open(lb.get(lb.curselection()))  
        #显示图像  
        im.show() 
    except:
        pass

def lbExecute(listT):#listbox处理
    lb.delete(0, END) #先清除
    for item in listT:#再输出
        lb.insert(END, item)    


#执行搜图
import Execute
def start():
    if var1.get()=='' or var2.get()=='' :
        tkinter.messagebox.askokcancel('error','图片以及文件夹的路径请完整填写')
        tabControl.select(0)#跳回第一个标签
        pass
    else :#路径合法，可以执行
        Init_dog()#初始化图像显示
        delButton(tree)#清空表列
        showPic1()#预览所找图
        #time_start=time.time()#time.time()为1970.1.1到当前时间的毫秒数  
        #搜图开始
        if numberChosen.current() == 0 :
            Execute.startSearch01(var1,var2,var3,tree,x,root)#单层文件夹   
        elif numberChosen.current() == 1 :
            Execute.startSearch0(var1,var2,var3,tree,x,root)#多层文件夹
        else :
            tkinter.messagebox.askokcancel('error','算法出错')

        #label3.config(text="耗时"+str(round(time_end-time_start,3))+'秒')#显示耗时 
        #自动筛选







#label=Label(root,textvariable = result, font=("黑体", 30, "bold"))
#label.grid(row=0,column=1,padx=20, pady=10,sticky=N)
#窗口开始===========================================================================
root = Tk()     # 初始框的声明
root.title('基于哈希的图像文件整理应用的设计与实现')#设置窗口标题
root.geometry('1300x650+500+200')#设置窗口的大小宽x高+偏移量
root.resizable(width=True, height=True) #宽不可变, 高可变,默认为True
root.iconbitmap('img4.ico')

#ft1 = tkFont.Font(family='Fixdsys', size=12)
#ft2 = tkFont.Font(family='Fixdsys', size=10)


#标题
label9 = Label(root, text='欢迎使用本软件')
label9.pack(side=TOP)
frm = Frame(root)
frm.pack(side=TOP,fill=BOTH)

#底部公用
frm_BB = Frame(root)
frm_BB.pack(side=BOTTOM,fill=BOTH)

#按钮（右）
frm_BBB1 = Frame(frm_BB)
frm_BBB1.pack(side=RIGHT,fill=BOTH)

#label3=Label(frm_BBB1, text='耗时')
#label3.pack(fill=BOTH)
x=StringVar()
label4=Label(frm_BBB1,textvariable = x)
label4.pack(fill=BOTH)
x.set("无任务")

#button_img_gif = PhotoImage(file='start.png')  
button_img = Button(frm_BBB1,text = '开始搜图',width=20,height=20,command=start)  
button_img.pack(side=BOTTOM) 

#框架（左）
frm_BB1 = Frame(frm_BB)
frm_BB1.pack(side=LEFT,fill=BOTH)

#left左边显示信息
frm_L = Frame(frm)
frm_L.pack(side=LEFT)


columns=("a","b","c")
tree=ttk.Treeview(frm_L,height=18,show="headings",columns=columns )#表格 
for col in columns:
    if (col=='a')or(col=='e'):#数字排序
        tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column2(tree, _col, False))#重建标题，添加控件排序方法
    else :#默认排序
        tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column1(tree, _col, False))
tree.column('a', width=100, anchor='center') 
tree.column('b', width=400, anchor='center') 
tree.column('c', width=200, anchor='center')
tree.heading('a', text='相似度')
tree.heading('b', text='路径')
tree.heading('c', text='文件名')

tree.pack(side=LEFT,fill=BOTH)
tree.bind('<ButtonRelease-1>', treeviewClick)   #单击离开
tree.bind('<Double-1>', treeviewClick1)         #双击
tree.bind('<3>', treeviewClick2)                #右键

scrollBar = Scrollbar(frm_L)#tree滚动条
scrollBar.pack(side=RIGHT, fill=Y)
scrollBar.config(command=tree.yview)


#right右边展示图片
frm_R = Frame(frm)
frm_R.pack(fill=BOTH)

#初始化右边的两个显示图片
pil_image = Image.open('img1.jpg')  #打开
w, h = pil_image.size              #获取原比例
pil_image_resized = resize(w, h, w_box, h_box, pil_image)#改成合适比例函数
tk_image = ImageTk.PhotoImage(pil_image_resized)         #转成XX对象

Label(frm_R, text='所找图片预览').pack()
label1 = Label(frm_R,image=tk_image, width=w_box, height=h_box)
label1.pack()

Label(frm_R, text='所选图片预览').pack()
label2 = Label(frm_R,image=tk_image, width=w_box, height=h_box)
label2.pack() 



#tab
tabControl = ttk.Notebook(frm_BB1) # Create Tab Control
tab1 = Frame(tabControl) # Create a tab
tabControl.pack(expand=2, fill="both") # Pack to make visible
tabControl.add(tab1, text='基础识图') # Add the tab
tab2 = Frame(tabControl) 
tabControl.add(tab2, text='更多功能') 


#tab1 基本
frm_B0 = Frame(tab1)
frm_B0.pack()

frm_B01 = Frame(frm_B0)
frm_B01.pack(side=TOP,fill=BOTH)
Label(frm_B01, text='所寻图片的路径').pack(side=LEFT)
Button(frm_B01, text = "图片选择",command = selectPath1).pack(side=RIGHT)
var1 = StringVar()
e1 = Entry(frm_B01,width=300,textvariable = var1)
#var1.set("请在此处输入需要查询的图片的路径")
var1.set(r'C:\图片\img1.jpg')
e1.pack(side=RIGHT)

frm_B02 = Frame(frm_B0)
frm_B02.pack(side=TOP,fill=BOTH)
Label(frm_B02, text='搜索范围文件夹').pack(side=LEFT)
Button(frm_B02, text = "路径选择",command = selectPath).pack(side=RIGHT)
var2 = StringVar()
e2 = Entry(frm_B02,width=300,textvariable = var2)
#var2.set("请在此处输入需要搜索的文件夹路径")
var2.set(r'C:\图片2')
e2.pack(side=RIGHT)

var3 = StringVar()
e3 = Entry(frm_B0,width=8,textvariable=var3)
s=Scale(frm_B0,label="相似程度", from_=0,to=100,orient=HORIZONTAL,
        length=950,showvalue=0,tickinterval=5,resolution=1,
        variable=var3)
s.pack(side=LEFT,fill=BOTH)

var3.set("20")
e3.pack(side=LEFT,fill=BOTH)


#tab2 功能保存和四种算法选择
frm_B1 = Frame(tab2)
frm_B1.pack(side=TOP,fill=BOTH)



number = StringVar()
numberChosen = ttk.Combobox(frm_B1, width=16, textvariable = number,state='readonly')
numberChosen['values'] = ('特征码识图（纹理）单层','特征码识图（纹理）多层',)     # 设置下拉列表的值
numberChosen.grid(column=1, row=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)                 # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
numberChosen.grid(row=1,column=1,sticky=W)

#Button(frm_B1, text = "标签试图",bg='yellow',command =lambda : recommend2(ID=var6.get())).grid(row=3,column=2,sticky=W)
#var6 = StringVar()
#Entry(frm_B1,width=16,textvariable = var6).grid(row=3,column=2,sticky=E)
#var6.set("输入标签试试看")
label = Label(frm_B1, text='算法功能选择:')#下拉列表
label.grid(row=0,column=0)


b1=Button(frm_B1,text="average_hash",width=12,command=clicked1)
b1.grid(row=1,column=2)

b1=Button(frm_B1,text="dhash",width=12,command=clicked2)
b1.grid(row=1,column=3)

b1=Button(frm_B1,text="phash",width=12,command=clicked3)
b1.grid(row=2,column=2)

b1=Button(frm_B1,text="whash",width=12,command=clicked4)
b1.grid(row=2,column=3)

b1=Button(frm_B1, text = "保存所有结果至搜索路径下save文件夹",command = save)
b1.grid(row=4,column=0)




print(var1.get())
print(var2.get())

root.mainloop()#进入消息循环

#灰色会出毛病；opencv的人脸会出毛病