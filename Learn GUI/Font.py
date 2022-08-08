from tkinter import *
from tkinter.font import Font
root = Tk()
root.geometry('700x500+300+80')
root.title('Learn GUI')
root.resizable(False,False)
l1 = Label(root,text="Learn GUI",
        font=Font(family="Times New Roman",size=30,weight="bold",slant="italic",underline=1)).place(x=250,y=40)
root.mainloop()
