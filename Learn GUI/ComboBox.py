from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
root.title('ComboBox')
root.geometry('700x500+300+80')
root.resizable(False,False)
root.configure(bg='sky blue')
def f1():
    a = cb1.get()
    if(a=="C++"):
        root1 = Tk()
        root1.title("C++")
        root1.resizable(False,False)
        root1.configure(bg='sky blue'); root1.geometry("300x300+160+60")
        root1.mainloop()
v = ["C++","Java","Python","C#","C","Javascript"]
cb1 = Combobox(root,values=v,height=4,width=15)
cb1.set('Select')
cb1.place(x=320,y=20)
b1 = Button(root,text='Click',command=f1).place(x=480,y=20)
root.mainloop()
