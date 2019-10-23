import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root,
	show = '*')
entry1.pack()

entry2 = tkinter.Entry(root,
	show = '#',
	width = 50)
entry2.pack()

entry3 = tkinter.Entry(root,
	bg = 'red',
	fg = 'blue')
entry3.pack()

entry4 = tkinter.Entry(root,
	selectbackground = 'red',
	selectforeground = 'gray')
entry4.pack()

entry5 = tkinter.Entry(root,state = tkinter.DISABLED)
entry5.pack()

edit1 = tkinter.Text(root,selectbackground='red',selectforeground='gray')
edit1.pack()

root.mainloop()
