from tkinter import *

wd = Tk()

wd.title("window title")
wd.geometry('400x300')
wd.resizable(width= FALSE,height=FALSE)

lb1= Label(wd, text="test label")
lb2 = Label(wd, text="python", font=("굴림",30), fg="green")
lb3 = Label(wd, text= "python programing", bg="purple", width=20, height=5, anchor =S)
lb1.pack()
lb2.pack()
lb3.pack()

wd.mainloop()

