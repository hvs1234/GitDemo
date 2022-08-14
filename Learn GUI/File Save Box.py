from distutils.util import execute
import opcode
from operator import mod
from tkinter import *
from tkinter  import filedialog
root = Tk()
root.geometry('700x500+340+80')
root.title('File Save Box')
root.resizable(False,False)
def f1():
    filedialog.asksaveasfile(mode='w',defaultextension=(".txt",".py",".c",".cpp"))
b1 = Button(root,text="File Dialog",command=f1); b1.pack(pady=10)
root.mainloop()
