from tkinter import *


def add():

    a = int(num1.get())
    b = int(num2.get())

    ab = (a + b)

    w1 = Tk()
    w1.geometry("800x600")
    w1.title("Result for Addition")
    w1.resizable(FALSE, FALSE)
    w1.configure(bg="#F4F8FB")

    m1 = Label(
        w1,
        text="THE ADDITION OF THE FOLLOWING IS =",
        font=("Calibri", 25, "bold"),
        bg="#F4F8FB",
        fg="#2C3E50"
    )
    m1.grid(row=0, column=0, padx=30, pady=250)

    m2 = Label(
        w1,
        text=ab,
        font=("Calibri", 30, "bold"),
        bg="#F4F8FB",
        fg="#2196F3"
    )
    m2.grid(row=0, column=1, padx=20)

    w1.mainloop()

def sub():

    a = int(num1.get())
    b = int(num2.get())

    ab = (a - b)

    w1 = Tk()
    w1.geometry("800x600")
    w1.title("Result for Subtraction")
    w1.resizable(FALSE, FALSE)
    w1.configure(bg="#FFF8F0")

    m1 = Label(
        w1,
        text="THE SUBTRACTION OF THE FOLLOWING IS =",
        font=("Calibri", 25, "bold"),
        bg="#FFF8F0",
        fg="#5D4037"
    )
    m1.grid(row=0, column=0, padx=30, pady=250)

    m2 = Label(
        w1,
        text=ab,
        font=("Calibri", 30, "bold"),
        bg="#FFF8F0",
        fg="#FF9800"
    )
    m2.grid(row=0, column=1, padx=20)

    w1.mainloop()

def mul():

    a = int(num1.get())
    b = int(num2.get())

    ab = (a * b)

    w1 = Tk()
    w1.geometry("1000x1000")
    w1.title("Result for Multiplication")
    w1.resizable(FALSE, FALSE)
    w1.configure(bg="#FAF5FC")

    m1 = Label(
        w1,
        text="THE MULTIPLICATION OF THE FOLLOWING IS =",
        font=("Calibri", 25, "bold"),
        bg="#FAF5FC",
        fg="#4A235A"
    )
    m1.grid(row=0, column=0, padx=30, pady=250)

    m2 = Label(
        w1,
        text=ab,
        font=("Calibri", 30, "bold"),
        bg="#FAF5FC",
        fg="#9C27B0"
    )
    m2.grid(row=0, column=1, padx=20)

    w1.mainloop()


c = Tk()
c.geometry("800x600")
c.title("Calculator")
c.resizable(FALSE, FALSE)
c.configure(bg="#F4F7FA")


num1 = StringVar()
num2 = StringVar()


title = Label(
    c,
    text="SIMPLE CALCULATOR",
    font=("Calibri", 32, "bold"),
    bg="#F4F7FA",
    fg="#263238"
)
title.grid(row=0, column=0, columnspan=2, pady=(50, 40))


l1 = Label(
    c,
    text="Enter the first number",
    font=("Calibri", 18, "bold"),
    bg="#F4F7FA",
    fg="#455A64"
)
l1.grid(row=1, column=0, padx=30, pady=15)


e1 = Entry(
    c,
    font=("Calibri", 18, "bold"),
    textvariable=num1,
    width=20,
    bg="#FFFFFF",
    fg="#263238",
    relief="solid",
    bd=1
)
e1.grid(row=1, column=1, padx=30, pady=15, ipady=8)


l2 = Label(
    c,
    text="Enter the second number",
    font=("Calibri", 18, "bold"),
    bg="#F4F7FA",
    fg="#455A64"
)
l2.grid(row=2, column=0, padx=30, pady=15)


e2 = Entry(
    c,
    font=("Calibri", 18, "bold"),
    textvariable=num2,
    width=20,
    bg="#FFFFFF",
    fg="#263238",
    relief="solid",
    bd=1
)
e2.grid(row=2, column=1, padx=30, pady=15, ipady=8)


b1 = Button(
    c,
    text="ADD",
    font=("Calibri", 18, "bold"),
    command=add,
    bg="#4CAF50",
    fg="white",
    activebackground="#388E3C",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=10
)
b1.grid(row=3, column=0, padx=20, pady=40)


b2 = Button(
    c,
    text="SUBTRACT",
    font=("Calibri", 18, "bold"),
    command=sub,
    bg="#FF9800",
    fg="white",
    activebackground="#F57C00",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=10
)
b2.grid(row=3, column=1, padx=20, pady=40)


b3 = Button(
    c,
    text="MULTIPLY",
    font=("Calibri", 18, "bold"),
    command=mul,
    bg="#9C27B0",
    fg="white",
    activebackground="#7B1FA2",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=30,
    pady=10
)
b3.grid(row=4, column=0, columnspan=2, pady=10)


c.mainloop()


'''from tkinter import *
def add():
    a=int(num1.get())
    b=int(num2.get())
    ab=(a+b)
    w1=Tk()
    w1.geometry("800x600")
    w1.title("Result for addition")
    w1.resizable(FALSE,FALSE)
    m1=Label(w1,text="THE ADDITION OF THE FOLLOWING IS=",font=("Calibri",25,"bold"))
    m1.grid(row=0,column=0)
    m2=Label(w1,text=ab,font=("Calibri",25,"bold"))
    m2.grid(row=0,column=1)
    w1.mainloop()
def sub():
    a=int(num1.get())
    b=int(num2.get())
    ab=(a-b)
    w1=Tk()
    w1.geometry("800x600")
    w1.title("Result for subraction")
    w1.resizable(FALSE,FALSE)
    m1=Label(w1,text="THE SUBTRACTION OF THE FOLLOWING IS=",font=("Calibri",25,"bold"))
    m1.grid(row=0,column=0)
    m2=Label(w1,text=ab,font=("Calibri",25,"bold"))
    m2.grid(row=0,column=1)
    w1.mainloop()
def mul():
    a=int(num1.get())
    b=int(num2.get())
    ab=(a*b)
    w1=Tk()
    w1.geometry("800x600")
    w1.title("Result for multiplication")
    w1.resizable(FALSE,FALSE)
    m1=Label(w1,text="THE MULTIPLICATION OF THE FOLLOWING IS=",font=("Calibri",25,"bold"))
    m1.grid(row=0,column=0)
    m2=Label(w1,text=ab,font=("Calibri",25,"bold"))
    m2.grid(row=0,column=1)
    w1.mainloop()
c=Tk()
c.geometry("800x600")
c.title("calculator for addition")
c.resizable(FALSE,FALSE)

num1=StringVar()
num2=StringVar()

l1=Label(c,text="enter the first number",font=("Calibri",18,"bold"))
l1.grid(row=0,column=0)
e1=Entry(c,font=("Calibri",18,"bold"),textvariable=num1)
e1.grid(row=0,column=1)

l2=Label(c,text="enter the second number",font=("Calibri",18,"bold"))
l2.grid(row=1,column=0)
e2=Entry(c,font=("Calibri",18,"bold"),textvariable=num2)
e2.grid(row=1,column=1)

b1=Button(c,text="Click to Add",font=("Calibri",25,"bold"),command=add)
b1.grid(row=2,column=0)

b2=Button(c,text="Click to Subtract",font=("Calibri",25,"bold"),command=sub)
b2.grid(row=2,column=1)

b3=Button(c,text="Click to Multiply",font=("Calibri",25,"bold"),command=mul)
b3.grid(row=3,column=0)

c.mainloop()'''