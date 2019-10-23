import tkinter
root = tkinter.Tk()
button1 = tkinter.Button(root,
	anchor = tkinter.E,
	text = 'Button1',
	width = 30,
	height = 7)
button1.pack()

button2 = tkinter.Button(root,
	text = "Button2",
	bg = 'blue')
button2.pack()

button3 = tkinter.Button(root,
	text = "Button3",
	width = 12,
	height = 1)
button3.pack()

button4 = tkinter.Button(root,
	text = 'Button4',
	width = 40,
	height = 7,
	state = tkinter.DISABLED)
button4.pack()

root.mainloop()