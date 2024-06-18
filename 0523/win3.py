from tkinter import *
from tkinter import messagebox

def myF():
    messagebox.showinfo("this is cat")

wd=Tk()

photo=PhotoImage(file = "images/GIF/dog.gif")

bt1 = Button(wd, image= photo, command=myF)

bt1.pack()

wd.mainloop()