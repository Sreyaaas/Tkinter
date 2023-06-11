from tkinter import *

def size():
    # print(f"{hei.get(),wid.get()}")
    X=hei.get()
    Y=wid.get()
    root.geometry(f"{X}x{Y}")

root=Tk()
# root.geometry(f"{X,x,Y}")

Height=StringVar
Width=StringVar

hei=Entry(root,text="Height",textvariable=Height)
wid=Entry(root,textvariable=Width)

Button(root,text="submit",command=size).pack()
hei.pack()
wid.pack()

root.mainloop()