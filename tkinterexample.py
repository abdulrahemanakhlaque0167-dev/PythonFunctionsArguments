from tkinter import *
x=Tk()
x.geometry("400x400")
x.title("Simple GUI Application")
x.resizable(False,False)

l1=Label(x,text="Enter your name:",font=("Calibri",18,"bold"))
l1.grid(row=0,column=0)
e1=Entry(x,font=("Calibri",14,"bold"))
e1.grid(row=0,column=1)

l2=Label(x,text="Enter your email:",font=("Calibri",18,"bold"))
l2.grid(row=1,column=0)
e2=Entry(x,font=("Calibri",14,"bold"))
e2.grid(row=1,column=1)

b1=Button(x,text="Submit",padx=20,font=("Arial",16,"bold"))
b1.grid(row=2,column=1,pady=10)

x.mainloop()
