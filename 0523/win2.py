from tkinter import *

wd=Tk()

photo = PhotoImage(file='images/GIF/cat.gif')
lb = Label(wd, image=photo)

lb.pack()


wd.mainloop()