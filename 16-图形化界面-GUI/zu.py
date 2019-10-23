import tkinter #导入tkinter模块
root = tkinter.Tk() #生成一个主窗口对象
#实例化标签label组件
label = tkinter.Label(root,text="Python,tkinter")
label.pack() #将标签（label)添加到窗口中
button1 = tkinter.Button(root,text="按钮1")
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(root,text="按钮2")
button2.pack(side=tkinter.RIGHT)

root.mainloop()