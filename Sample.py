# Calculator using Tkinder
# My first python projects

from tkinter import *

# add a Tkinder Tk window

root = Tk()

root.configure(bg="#343b3b")
root.title('Simple Calculator')
entry = Entry(root, width=50,borderwidth=1,bg="#343b3b",fg="white",textvariable=1,)
entry.grid(row=0,column=0)





root.mainloop()