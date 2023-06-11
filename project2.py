import png
from pyqrcode import QRCode
import pyqrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def hello():
    print(uservalue.get())
    print(passvalue.get())
QRroot=Tk()

QRroot.geometry("733x430")
QRroot.minsize(250,250)
QRroot.maxsize(700,700)

# bb=Label(QRroot,text="A binary module that contains the low-level interface \nto Tcl/Tk. It is automatically imported by the main \ntkinter module, and should never be used directly by application programmers. \nIt is usually a shared library (or DLL), but might in some cases be statically lin\nked with the Python interpreter.",bg="blue",fg="white",font=("poppins",12,"bold"),relief=SUNKEN)
# bb.pack(fill="x")

# photo=PhotoImage(file="myqr.png")


# jpgphoto=Image.open("myqr.png")
# photo=ImageTk.PhotoImage(jpgphoto)

# plab=Label(QRroot,image=photo)
# plab.pack()

s=Label(QRroot,text="Username")
b=Label(QRroot,text="Password")

s.grid()
b.grid(row=1)
#Entries
uservalue= StringVar()
passvalue= StringVar()

userentry= Entry(QRroot, textvariable=uservalue)
passentry= Entry(QRroot, textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

butt=Button(QRroot,text="Submit",command=hello)
butt.grid()
QRroot.mainloop()






# s=input("Enter the link:")

# url=pyqrcode.create(s)
# url.svg("myqr.svg",scale=8)
# url.png("myqr.png",scale=8)