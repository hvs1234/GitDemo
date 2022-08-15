from distutils.util import execute
import opcode
from operator import mod
from tkinter import *
from tkinter  import filedialog
root = Tk()
root.geometry('700x500+340+80')
root.title('Shortcut Keys')
global l1
l1 = Label(root,text="Click clt-d to close and clt-s to save the file box"); l1.pack(pady=20)
root.resizable(False,False)
def d1(event): root.destroy()
def f1(event):
    filedialog.asksaveasfile(mode='w',defaultextension=(".txt",".py",".c",".cpp"))
root.bind('<Control-d>',d1); root.bind('<Control-s>',f1)
root.mainloop()
