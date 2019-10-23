from tkinter import *
from PIL import  ImageTk 
from PIL import Image
import os
import tkinter.font as tkFont 
from tkinter import ttk
from tkinter.filedialog import askdirectory,askopenfilename
import time
import datetime

Const_Image_Format = [".jpg",".png"]#筛选格式，局部要求的话单加

#时间转换为人话
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

#打印属性
def treePrint(tree,a,b,c,d,e,f,g,h):
    w1, h1 = f.size                                         #h不要和h1重名！！
    tree.insert('', END, values=[str(a),str(b),str(c),str(d),
                                 str(round(e/1024,2)),
                                 str(w1)+'*'+str(h1),
                                 str(TimeStampToTime(g)),
                                 str(h)])

#显示进度
def process(label,a,b):
    label.config(text=str(a)+"/"+str(b))



#都返回的是升函数，尽量是与相似度正相关的百分比
#遍历，条件（格式），算法比较，条件（相似度），输出

#图片-dHash算法（单层文件夹）
import _dhash
def startSearch01(var1,var2,var3,tree,x,root1):
    count1=0;path=var2.get();im1=Image.open(var1.get())

    #Const_Image_Format = [".jpg",".jpeg",".bmp",".png"]
    for filename in os.listdir(path):
            if os.path.splitext(filename)[1] in Const_Image_Format :#筛选格式

                im2=Image.open(os.path.join(path,filename))
                j=100-2.38*_dhash.classfiy_dHash(im1,im2,size=(7,6))

                count1+=1;x.set('处理了'+str(count1)+'张');root1.update()#显示处理过程

                if j>=int(var3.get()):                              #条件筛选

                    treePrint(tree,                                 #调用打印函数
                              round(j,2),
                              os.path.join(path),
                              os.path.splitext(filename)[0],
                              os.path.splitext(filename)[1],
                              os.path.getsize(os.path.join(path,filename)),
                              im2,
                              os.path.getctime(os.path.join(path,filename)),
                              ""
                               )

#图片-dHash算法(多层文件夹)
import _dhash
def startSearch0(var1,var2,var3,tree,x,root1):#所有子文件夹
    count1=0;path= var2.get();im1=Image.open(var1.get())

    #Const_Image_Format = [".jpg",".jpeg",".bmp",".png"]
    for (root, dirs, files) in os.walk(path):  
        for filename in files:
            if os.path.splitext(filename)[1] in Const_Image_Format :#筛选格式

                sizePingheng=51#现在只改这个就好了
                pingheng=100/(sizePingheng-1)**2
                im2=Image.open(os.path.join(root,filename))
                j=pingheng*((sizePingheng-1)**2-_dhash.classfiy_dHash(im1,im2,size=(sizePingheng,sizePingheng-1)))

                count1+=1;x.set('已处理'+str(count1)+'张');root1.update()#显示处理过程

                if j>=int(var3.get()):                              #条件筛选

                    treePrint(tree,                                 #调用打印函数
                              round(j,2),
                              os.path.join(root),
                              os.path.splitext(filename)[0],
                              os.path.splitext(filename)[1],
                              os.path.getsize(os.path.join(root,filename)),
                              im2,
                              os.path.getctime(os.path.join(root,filename)),
                              ""
                               )


