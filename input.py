from tkinter import *

root = Tk()

def clickMe():
	mylabel = Label(root, text = "Hello there, " + e.get() + "!")
	mylabel.pack()

e = Entry(root,width = 150, fg = "black", bg = "orange")
e.pack()
e.insert(1,"Please enter your name in this box.")

myButton = Button(root,text = "Click Me!!", padx = 100, pady = 100, command = clickMe, fg = "white", bg = "red")
myButton.pack()

root.mainloop()