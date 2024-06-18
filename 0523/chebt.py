from tkinter import *
from tkinter import messagebox

wd = Tk()

def myF():
    if chk.get() == 0:
        messagebox.showinfo("", "checkbutton on")
    else:
        messagebox.showinfo("", "checkbutton off")

chk = IntVar()

cb = Checkbutton(wd, text= "click", variable= chk, command= myF)

cb.pack()

wd.mainloop()