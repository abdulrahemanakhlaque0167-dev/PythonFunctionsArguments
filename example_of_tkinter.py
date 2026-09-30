from tkinter import *
def button():
    print("button is clicked")
    print(name.get())
    print(age.get())
l=Tk()
l.geometry("800x600")
l.title("tkinter example")
l.resizable(FALSE,FALSE)
name=StringVar()
age=StringVar()

l1=Label(l,text="Enter your Name",font=("Calibri",18,"bold"))
l1.grid(row=0,column=0)
e1=Entry(l,font=("Calibri",18,"bold"),textvariable=name)
e1.grid(row=0,column=1,pady=10)
l2=Label(l,text="Enter your Age",font=("calibri",18,"bold"))
l2.grid(row=1,column=0)
e2=Entry(l,font=("calibri",18,"bold"),textvariable=age)
e2.grid(row=1,column=1,pady=10)

l3=Button(l,text="Click for Submit",font=("calibri",18,"bold"),padx=20,command=button)
l3.grid(row=2,column=1,pady=10)
l.mainloop()

