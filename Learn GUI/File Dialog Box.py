from distutils.util import execute
import opcode
from tkinter import *
from tkinter  import filedialog
root = Tk()
root.geometry('700x500+340+80')
root.title('File Dialog Box')
root.resizable(False,False)
def f1():
    filedialog.askopenfile(initialdir='/',filetypes=(("Text files",".txt"),("All Files","*.*")))
b1 = Button(root,text="File Dialog",command=f1); b1.pack(pady=10)
root.mainloop()
