from  tkinter import *

wd = Tk()

def myF():
    if var.get() == 1:
        lb1.configure(text="python")
    elif var.get() == 2:
        lb1.configure(text = "C++")
    else:
        lb1.configure(text = "java")

var = IntVar()
rb1= Radiobutton(wd, text="python", variable= var, value=1, command= myF)
rb2= Radiobutton(wd, text="C++", variable= var, value=2, command= myF)
rb3= Radiobutton(wd, text="java", variable= var, value=3, command= myF)

lb1 = Label(wd, text="select leg : ", fg = "green")

rb1.pack()
rb2.pack()
rb3.pack()
lb1.pack()

wd.mainloop()