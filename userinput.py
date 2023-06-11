from tkinter import *


def getvals():
    print(f"{NameValue.get(), GenderValue.get(), ErconValue.get(), PaymentValue.get(), foodserValue.get()}")
    with open("records.txt","a") as f:
        f.write(f"{NameValue.get(), GenderValue.get(), ErconValue.get(), PaymentValue.get(), foodserValue.get()}\n")


root=Tk()
root.geometry("350x350")
root.title("Travels")

headding=Label(root,text="Travels OP").grid(row=0,column=1)

name=Label(root,text="Name")
Phone=Label(root,text="Phone")
Gender=Label(root,text="Gender")
Ercon=Label(root,text="Emergency Contact")
Payment=Label(root,text="Payment Mode")


name.grid()
Phone.grid()
Gender.grid()
Ercon.grid()
Payment.grid()

NameValue=StringVar()
PhoneValue=StringVar()
GenderValue=StringVar()
ErconValue=StringVar()
PaymentValue=StringVar()
foodserValue=IntVar()

Nameentry=Entry(root,textvariable=NameValue)
Phoneentry=Entry(root,textvariable=PhoneValue)
Genderentry=Entry(root,textvariable=GenderValue)
Erconentry=Entry(root,textvariable=ErconValue)
Paymententry=Entry(root,textvariable=PaymentValue)

Nameentry.grid(row=1,column=1)
Phoneentry.grid(row=2,column=1)
Genderentry.grid(row=3,column=1)
Erconentry.grid(row=4,column=1)
Paymententry.grid(row=5,column=1)

foodservice=Checkbutton(text="Want food?",variable=foodserValue)
foodservice.grid(row=6,column=1)

Button(text="Submit",command=getvals).grid(row=7,column=1)

root.mainloop()