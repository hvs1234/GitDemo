from tkinter import *
root = Tk()
root.geometry('700x500+300+80')
root.title('Learn GUI')
root.resizable(False,False)

def f1():
    pass
def f2():
    l1 = Label(root,text="Have a good day!").pack(pady=5)
main_menu = Menu(root)
root.config(menu = main_menu)
file = Menu(main_menu)
main_menu.add_cascade(label="File",menu=file)
file.add_command(label="New ...",command=f1)
file.add_separator()
file.add_command(label="Exit",command=root.quit)
Edit = Menu(main_menu)
main_menu.add_cascade(label="Exit",menu=Edit)
Edit.add_command(label="Print",command=f2)
Edit.add_separator()
a = Edit.add_command(label="Delete")
root.mainloop()
