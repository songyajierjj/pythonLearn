import tkinter
root = tkinter.Tk()
menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu,tearoff=0)
submenu.add_command(label='打开')
submenu.add_command(label='保存')
submenu.add_command(label='关闭')
menu.add_cascade(label='文件',menu=submenu)

submenu = tkinter.Menu(menu,tearoff=0)
submenu.add_command(label='复制')
submenu.add_command(label='粘贴')
submenu.add_separator()
submenu.add_command(label='剪切')
menu.add_cascade(label='编辑',menu=submenu)

submenu = tkinter.Menu(menu,tearoff=0)
submenu.add_command(label='关于')

menu.add_cascade(label='帮助',menu=submenu)
root.config(menu=menu)

root.mainloop()