
from tkinter import *
from tkinter import messagebox
import csv


def display_data():
    with open("student_data.csv","r") as f1:
        csvReader=csv.reader(f1)
        next(csvReader)
        for x in csvReader:
            print(x)
    

def save_data():
    

    if fname.get()=="" or lname.get()=="" or sclass.get()=="" or division.get()=="" or rnumber.get()=="" or idnumber.get()=="" or  english.get()=="" or urdu.get()=="" or maths.get()=="" or science.get()=="":
        messagebox.showerror("Alert!","All Fields must be filled!")
    else:
        with open("student_data.csv", "a", newline="") as f1:
            csvWriter = csv.writer(f1)
            csvWriter.writerow([
                fname.get(), lname.get(), sclass.get(), division.get(),
                rnumber.get(), idnumber.get(), english.get(), urdu.get(),
                maths.get(), science.get()
            ])
        messagebox.showinfo("Success!","Data Stored!")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        


table = Tk()
table.title("Student Information System")
table.resizable(False, False)
table.configure(bg="#EAF2F8")

fname = StringVar()
lname = StringVar()
sclass = StringVar()
division = StringVar()
rnumber = StringVar()
idnumber = StringVar()
english = StringVar()
urdu = StringVar()
maths = StringVar()
science = StringVar()

bg_color = "#EAF2F8"
header_color = "#1F4E78"
label_color = "#163A5F"
entry_bg = "#FFFFFF"
button_color = "#2874A6"
button_hover = "#1B4F72"



header = Label(
    table,
    text="STUDENT INFORMATION FORM",
    font=("Calibri", 24, "bold"),
    bg=header_color,
    fg="white",
    padx=25,
    pady=18
)
header.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="ew",
    padx=10,
    pady=(10, 20)
)



def create_label(text, row, column):
    label = Label(
        table,
        text=text,
        font=("Calibri", 15, "bold"),
        bg=bg_color,
        fg=label_color
    )
    label.grid(
        row=row,
        column=column,
        padx=15,
        pady=10,
        sticky="w"
    )
    return label



def create_entry(variable, row, column):
    entry = Entry(
        table,
        font=("Calibri", 15),
        textvariable=variable,
        bg=entry_bg,
        fg="#17202A",
        relief="solid",
        bd=1,
        width=18
    )
    entry.grid(
        row=row,
        column=column,
        padx=15,
        pady=10,
        ipady=6
    )
    return entry


create_label("First Name", 1, 0)
e1 = create_entry(fname, 1, 1)

create_label("Last Name", 1, 2)
e2 = create_entry(lname, 1, 3)

create_label("Class", 2, 0)
e3 = create_entry(sclass, 2, 1)

create_label("Class Division", 2, 2)
e4 = create_entry(division, 2, 3)

create_label("Roll Number", 3, 0)
e11 = create_entry(rnumber, 3, 1)

create_label("Student ID Number", 3, 2)
e10 = create_entry(idnumber, 3, 3)

marks_title = Label(
    table,
    text="SUBJECT MARKS",
    font=("Calibri", 18, "bold"),
    bg="#D6EAF8",
    fg=header_color,
    padx=15,
    pady=8
)
marks_title.grid(
    row=4,
    column=0,
    columnspan=4,
    sticky="ew",
    padx=10,
    pady=(15, 5)
)

create_label("English Marks", 5, 0)
e5 = create_entry(english, 5, 1)

create_label("Urdu Marks", 5, 2)
e6 = create_entry(urdu, 5, 3)

create_label("Maths Marks", 6, 0)
e7 = create_entry(maths, 6, 1)

create_label("Science Marks", 6, 2)
e8 = create_entry(science, 6, 3)

l9 = Button(
    table,
    text="  STORE DATA  ",
    padx=25,
    pady=10,
    font=("Calibri", 17, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=save_data
)

l9.grid(
    row=7,
    column=0,
    columnspan=2,
    padx=10,
    pady=(20, 20)
)

l10 = Button(
    table,
    text="  DISPLAY DATA  ",
    padx=25,
    pady=10,
    font=("Calibri", 17, "bold"),
    bg=button_color,
    fg="white",
    activebackground=button_hover,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=display_data
)

l10.grid(
    row=7,
    column=2,
    columnspan=2,
    padx=10,
    pady=(20, 20)
)


footer = Label(
    table,
    text="Student Information Management System",
    font=("Calibri", 10, "italic"),
    bg=bg_color,
    fg="#5D6D7E"
)
footer.grid(
    row=8,
    column=0,
    columnspan=4,
    pady=(0, 10)
)

table.mainloop()
'''
from tkinter import *
import csv

with open("student_data.csv","w",newline="") as f1:
    csvWriter=csv.writer(f1)
    csvWriter.writerow(["fname","lname","class","division","roll","id","english","urdu","maths","science"])
    f1.close()


def save_data():
    print("Button is Clicked!")
    print(fname.get())
    print(lname.get())
    print(sclass.get())
    print(division.get())
    print(rnumber.get())
    print(idnumber.get())
    print(english.get())
    print(urdu.get())
    print(maths.get())
    print(science.get())
    with open("student_data.csv","a",newline="") as f1:
        csvWriter=csv.writer(f1)
        csvWriter.writerow([fname.get(),lname.get(),sclass.get(),division.get(),rnumber.get(),idnumber.get(),english.get(),urdu.get(),maths.get(),science.get()])

table=Tk()
table.title("student information storing file")
table.resizable(False,False)
fname=StringVar()
lname=StringVar()
sclass=StringVar()
division=StringVar()
rnumber=StringVar()
idnumber=StringVar()
english=StringVar()
urdu=StringVar()
maths=StringVar()
science=StringVar()
l1=Label(table,text="Enter the first name",font=("calibri",18,"bold"),padx=10,pady=10)
l1.grid(row=0,column=0,padx=10,pady=10)
e1=Entry(table,font=("calibri",18,"bold"),textvariable=fname)
e1.grid(row=0,column=1,padx=10,pady=10)
l2=Label(table,text="Enter the last name",font=("calibri",18,"bold"),padx=10,pady=10)
l2.grid(row=0,column=2,padx=10,pady=10)
e2=Entry(table,font=("calibri",18,"bold"),textvariable=lname)
e2.grid(row=0,column=3,padx=10,pady=10)
l3=Label(table,text="Enter the class",font=("calibri",18,"bold"),padx=10,pady=10)
l3.grid(row=1,column=0,padx=10,pady=10)
e3=Entry(table,font=("calibri",18,"bold"),textvariable=sclass)
e3.grid(row=1,column=1,padx=10,pady=10)
l4=Label(table,text="Enter the class division",font=("calibri",18,"bold"),padx=10,pady=10)
l4.grid(row=1,column=2,padx=10,pady=10)
e4=Entry(table,font=("calibri",18,"bold"),textvariable=division)
e4.grid(row=1,column=3,padx=10,pady=10)
l11=Label(table,text="Enter the roll number",font=("calibri",18,"bold"),padx=10,pady=10)
l11.grid(row=2,column=0,padx=10,pady=10)
e11=Entry(table,font=("calibri",18,"bold"),textvariable=rnumber)
e11.grid(row=2,column=1,padx=10,pady=10)
l10=Label(table,text="Enter the student id number",font=("calibri",18,"bold"),padx=10,pady=10)
l10.grid(row=2,column=2,padx=10,pady=10)
e10=Entry(table,font=("calibri",18,"bold"),textvariable=idnumber)
e10.grid(row=2,column=3,padx=10,pady=10)
l5=Label(table,text="Enter the marks of english",font=("calibri",18,"bold"),padx=10,pady=10)
l5.grid(row=3,column=0,padx=10,pady=10)
e5=Entry(table,font=("calibri",18,"bold"),textvariable=english)
e5.grid(row=3,column=1,padx=10,pady=10)
l6=Label(table,text="Enter the marks of urdu",font=("calibri",18,"bold"),padx=10,pady=10)
l6.grid(row=3,column=2,padx=10,pady=10)
e6=Entry(table,font=("calibri",18,"bold"),textvariable=urdu)
e6.grid(row=3,column=3,padx=10,pady=10)
l7=Label(table,text="Enter the marks of maths",font=("calibri",18,"bold"),padx=10,pady=10)
l7.grid(row=4,column=0,padx=10,pady=10)
e7=Entry(table,font=("calibri",18,"bold"),textvariable=maths)
e7.grid(row=4,column=1,padx=10,pady=10)
l8=Label(table,text="Enter the marks of science",font=("calibri",18,"bold"),padx=10,pady=10)
l8.grid(row=4,column=2,padx=10,pady=10)
e8=Entry(table,font=("calibri",18,"bold"),textvariable=science)
e8.grid(row=4,column=3,padx=10,pady=10)
l9=Button(table,text="Store Data",padx=20,font=("calibri",22,"bold"),command=save_data)
l9.grid(row=5,column=1,padx=10,pady=10)
table.mainloop()
'''
'''
with open("student_data.csv", "w", newline="") as f1:
    csvWriter = csv.writer(f1)
    csvWriter.writerow([
        "fname", "lname", "class", "division", "roll", "id",
        "english", "urdu", "maths", "science"
    ])
    f1.close()
'''
'''
    print(fname.get())
    print(lname.get())
    print(sclass.get())
    print(division.get())
    print(rnumber.get())
    print(idnumber.get())
    print(english.get())
    print(urdu.get())
    print(maths.get())
    print(science.get())
    '''