import string
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
root = Tk()
root.resizable(False,False)
root.title("Dialog Box")
root.configure(bg='slate gray')
root.geometry("400x400+300+80")
def f1():
    a=simpledialog.askstring("Input String","Enter the name")
    if(a=="hvs"):
        root1 = Tk()
b = Button(root,text="Execute",command=f1); b.pack(pady=5)
root.mainloop()
