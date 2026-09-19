from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Simple GUI Application")
root.resizable(False,False)

l1=Label(root,text="Enter your name:",font=("Calibri",18,"bold"))
l1.grid(row=0,column=0)
e1=Entry(root,font=("Calibri",14,"bold"))
e1.grid(row=0,column=1)

l2=Label(root,text="Enter your email:",font=("Calibri",18,"bold"))
l2.grid(row=1,column=0)
e2=Entry(root,font=("Calibri",14,"bold"))
e2.grid(row=1,column=1)

b1=Button(root,text="Submit",padx=20,font=("Arial",16,"bold"))
b1.grid(row=2,column=1,pady=10)

root.mainloop()