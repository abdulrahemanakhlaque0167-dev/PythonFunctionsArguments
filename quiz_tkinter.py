
from tkinter import *
from tkinter import messagebox

# ================= COLORS =================

BG = "#172554"
CARD = "#1E3A5F"
WHITE = "#FFFFFF"
PURPLE = "#9333EA"
BLUE = "#2563EB"
GREEN = "#059669"
ORANGE = "#EA580C"
YELLOW = "#FACC15"
ENTRY_BG = "#DBEAFE"

e=["What is the capital of India?",
   "Which planet is known as the Red Planet?",
   "How many days are there in a week?",
   "What is 5 + 5?",
   "Which language are we using to make this game?"
]

m=["Which is the largest ocean on Earth?",
   "What is the square root of 144?",
   "Which animal is known as the 'Ship of the Desert?'",
   "How many bones does an adult human usually have?",
   "Which planet has the most famous ring system?"
]

d=["If you have 3 apples and take away 2, how many apples do you have?",
   "Which country gifted the Statue of Liberty to the United States?",
   "What is the only even prime number?",
   "A train travels 60 km in 1 hour. How far will it travel in 2 hours and 30 minutes?",
   "Which is the smallest country in the world by area?"
]


def easy():
    messagebox.showinfo("Easy Level", "Welcome to the Easy Level!")
    x.destroy()
    y=Tk()
    y.geometry("1000x600")
    y.title("Easy Level")
    y.resizable(FALSE,FALSE)
    y.configure(bg=BG)

    def check():
        score=0
        if first.get().lower()=="delhi":
            score+=1
        if second.get().lower()=="mars":
            score+=1
        if third.get()=="7":
            score+=1
        if fourth.get()=="10":
            score+=1
        if fifth.get().lower()=="python":
            score+=1

        messagebox.showinfo("Score", f"Your Score is: {score}/5")

    first=StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    fifth=StringVar()

    l1=Label(y,text=e[0],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l1.grid(row=0,column=0)
    e1=Entry(y,font=("Arial",18),textvariable=first,bg=ENTRY_BG,fg=BG)
    e1.grid(row=0,column=1)

    l2=Label(y,text=e[1],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l2.grid(row=1,column=0)
    e2=Entry(y,font=("Arial",18),textvariable=second,bg=ENTRY_BG,fg=BG)
    e2.grid(row=1,column=1)

    l3=Label(y,text=e[2],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l3.grid(row=2,column=0)
    e3=Entry(y,font=("Arial",18),textvariable=third,bg=ENTRY_BG,fg=BG)
    e3.grid(row=2,column=1)

    l4=Label(y,text=e[3],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l4.grid(row=3,column=0)
    e4=Entry(y,font=("Arial",18),textvariable=fourth,bg=ENTRY_BG,fg=BG)
    e4.grid(row=3,column=1)

    l5=Label(y,text=e[4],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l5.grid(row=4,column=0)
    e5=Entry(y,font=("Arial",18),textvariable=fifth,bg=ENTRY_BG,fg=BG)
    e5.grid(row=4,column=1)

    b1=Button(y,text="SUBMIT THE ANSWERS",font=("Arial",16,"bold"),pady=15,bg=GREEN,fg=WHITE,activebackground="#047857",command=check)
    b1.grid(row=5,column=0)

    b2=Button(y,text="CLICK TO EXIT",font=("Arial",16,"bold"),pady=15,bg=ORANGE,fg=WHITE,activebackground="#C2410C",command=y.destroy)
    b2.grid(row=5,column=1)

    y.mainloop()


def medium():
    messagebox.showinfo("Medium Level", "Welcome to the Medium Level!")
    x.destroy()
    z=Tk()
    z.geometry("1000x600")
    z.title("Medium Level")
    z.resizable(FALSE,FALSE)
    z.configure(bg=BG)

    def check():
        score=0
        if first.get().lower()=="pacific ocean":
            score+=1
        if second.get()=="12":
            score+=1
        if third.get().lower()=="camel":
            score+=1
        if fourth.get()=="206":
            score+=1
        if fifth.get().lower()=="saturn":
            score+=1

        messagebox.showinfo("Score", f"Your Score is: {score}/5")

    first=StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    fifth=StringVar()

    l1=Label(z,text=m[0],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l1.grid(row=0,column=0)
    e1=Entry(z,font=("Arial",18),textvariable=first,bg=ENTRY_BG,fg=BG)
    e1.grid(row=0,column=1)

    l2=Label(z,text=m[1],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l2.grid(row=1,column=0)
    e2=Entry(z,font=("Arial",18),textvariable=second,bg=ENTRY_BG,fg=BG)
    e2.grid(row=1,column=1)

    l3=Label(z,text=m[2],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l3.grid(row=2,column=0)
    e3=Entry(z,font=("Arial",18),textvariable=third,bg=ENTRY_BG,fg=BG)
    e3.grid(row=2,column=1)

    l4=Label(z,text=m[3],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l4.grid(row=3,column=0)
    e4=Entry(z,font=("Arial",18),textvariable=fourth,bg=ENTRY_BG,fg=BG)
    e4.grid(row=3,column=1)

    l5=Label(z,text=m[4],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l5.grid(row=4,column=0)
    e5=Entry(z,font=("Arial",18),textvariable=fifth,bg=ENTRY_BG,fg=BG)
    e5.grid(row=4,column=1)

    b1=Button(z,text="SUBMIT THE ANSWERS",font=("Arial",16,"bold"),pady=15,bg=GREEN,fg=WHITE,activebackground="#047857",command=check)
    b1.grid(row=5,column=0)

    b2=Button(z,text="CLICK TO EXIT",font=("Arial",16,"bold"),pady=15,bg=ORANGE,fg=WHITE,activebackground="#C2410C",command=z.destroy)
    b2.grid(row=5,column=1)

    z.mainloop()


def hard():
    messagebox.showinfo("Hard Level", "Welcome to the Hard Level!")
    x.destroy()
    w=Tk()
    w.geometry("1000x600")
    w.title("Hard Level")
    w.resizable(FALSE,FALSE)
    w.configure(bg=BG)

    def check():
        score=0
        if first.get().lower()=="2":
            score+=1
        if second.get().lower()=="france":
            score+=1
        if third.get().lower()=="2":
            score+=1
        if fourth.get().lower()=="150":
            score+=1
        if fifth.get().lower()=="vatican city":
            score+=1

        messagebox.showinfo("Score", f"Your Score is: {score}/5")

    first=StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    fifth=StringVar()

    l1=Label(w,text=d[0],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE,wraplength=600)
    l1.grid(row=0,column=0)
    e1=Entry(w,font=("Arial",18),textvariable=first,bg=ENTRY_BG,fg=BG)
    e1.grid(row=0,column=1)

    l2=Label(w,text=d[1],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l2.grid(row=1,column=0)
    e2=Entry(w,font=("Arial",18),textvariable=second,bg=ENTRY_BG,fg=BG)
    e2.grid(row=1,column=1)

    l3=Label(w,text=d[2],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l3.grid(row=2,column=0)
    e3=Entry(w,font=("Arial",18),textvariable=third,bg=ENTRY_BG,fg=BG)
    e3.grid(row=2,column=1)

    l4=Label(w,text=d[3],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE,wraplength=600)
    l4.grid(row=3,column=0)
    e4=Entry(w,font=("Arial",18),textvariable=fourth,bg=ENTRY_BG,fg=BG)
    e4.grid(row=3,column=1)

    l5=Label(w,text=d[4],font=("Arial",16,"bold"),pady=20,bg=BG,fg=WHITE)
    l5.grid(row=4,column=0)
    e5=Entry(w,font=("Arial",18),textvariable=fifth,bg=ENTRY_BG,fg=BG)
    e5.grid(row=4,column=1)

    b1=Button(w,text="SUBMIT THE ANSWERS",font=("Arial",16,"bold"),pady=15,bg=GREEN,fg=WHITE,activebackground="#045778",command=check)
    b1.grid(row=5,column=0)

    b2=Button(w,text="CLICK TO EXIT",font=("Arial",16,"bold"),pady=15,bg=ORANGE,fg=WHITE,activebackground="#C2410C",command=w.destroy)
    b2.grid(row=5,column=1)

    w.mainloop()


# ================= MAIN WINDOW =================

x=Tk()
x.geometry("800x600")
x.title("Quiz Application")
x.resizable(FALSE,FALSE)
x.configure(bg=BG)

l1=Label(
    x,
    text="WELCOME TO THE QUIZ!\nPLEASE SELECT YOUR LEVEL",
    font=("Arial",20,"bold"),
    pady=30,
    bg=BG,
    fg=YELLOW
)
l1.grid(row=0,column=0,padx=100)

b1=Button(
    x,
    text="CLICK FOR EASY LEVEL",
    font=("Arial",16,"bold"),
    pady=20,
    bg=BLUE,
    fg=WHITE,
    width=25,
    activebackground="#05B8FF",
    command=easy
)
b1.grid(row=1,column=0,pady=15)

b2=Button(
    x,
    text="CLICK FOR MEDIUM LEVEL",
    font=("Arial",16,"bold"),
    pady=20,
    bg=BLUE,
    fg=WHITE,
    width=25,
    activebackground="#1D4ED8",
    command=medium
)
b2.grid(row=2,column=0,pady=15)

b3=Button(
    x,
    text="CLICK FOR HARD LEVEL",
    font=("Arial",16,"bold"),
    pady=20,
    bg=BLUE,
    fg=WHITE,
    width=25,
    activebackground="#006EFF",
    command=hard
)
b3.grid(row=3,column=0,pady=15)

Label(
    x,
    text="TEST YOUR KNOWLEDGE!",
    font=("Arial",14,"bold"),
    bg=BG,
    fg=ORANGE
).grid(row=4,column=0,pady=25)

x.mainloop()





'''
from tkinter import *
from tkinter import messagebox

e=["What is the capital of India?",
   "Which planet is known as the Red Planet?",
   "How many days are there in a week?",
   "What is 5 + 5?",
   "Which language are we using to make this game?"
]

m=["Which is the largest ocean on Earth?","What is the square root of 144?","Which animal is known as the 'Ship of the Desert?'","How many bones does an adult human usually have?","Which planet has the most famous ring system?"]

d=["If you have 3 apples and take away 2, how many apples do you have?","Which country gifted the Statue of Liberty to the United States?","What is the only even prime number?","A train travels 60 km in 1 hour. How far will it travel in 2 hours and 30 minutes?","Which is the smallest country in the world by area?"]


def easy():
    messagebox.showinfo("Easy Level", "Welcome to the Easy Level!")
    x.destroy()
    y=Tk()
    y.geometry("1000x600")
    y.title("Easy Level")
    y.resizable(FALSE,FALSE)

    def check():
        score=0
        if first.get().lower()=="delhi":
            score+=1
        if second.get().lower()=="mars":
            score+=1
        if third.get()=="7":
            score+=1
        if fourth.get()=="10":
            score+=1
        if fifth.get().lower()=="python":
            score+=1

        messagebox.showinfo("Score", f"Your Score is: {score}/5")
    first=StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    fifth=StringVar()

    l1=Label(y,text=e[0],font=("Arial",20),pady=20)
    l1.grid(row=0,column=0)
    e1=Entry(y,font=("Arial",20),textvariable=first)
    e1.grid(row=0,column=1)

    l2=Label(y,text=e[1],font=("Arial",20),pady=20)
    l2.grid(row=1,column=0)
    e2=Entry(y,font=("Arial",20),textvariable=second)
    e2.grid(row=1,column=1)

    l3=Label(y,text=e[2],font=("Arial",20),pady=20)
    l3.grid(row=2,column=0)
    e3=Entry(y,font=("Arial",20),textvariable=third)
    e3.grid(row=2,column=1)

    l4=Label(y,text=e[3],font=("Arial",20),pady=20)
    l4.grid(row=3,column=0)
    e4=Entry(y,font=("Arial",20),textvariable=fourth)
    e4.grid(row=3,column=1)

    l5=Label(y,text=e[4],font=("Arial",20),pady=20)
    l5.grid(row=4,column=0)
    e5=Entry(y,font=("Arial",20),textvariable=fifth)
    e5.grid(row=4,column=1)

    b1=Button(y,text="SUBMIT THE ANSWERS",font=("Arial",20),pady=20,command=check)
    b1.grid(row=5,column=0)

    b2=Button(y,text="CLICK TO EXIT",font=("Arial",20),pady=20,command=y.destroy)
    b2.grid(row=5,column=1)

    y.mainloop()

def medium():
    messagebox.showinfo("Medium Level", "Welcome to the Medium Level!")
    x.destroy()
    z=Tk()
    z.geometry("1000x600")
    z.title("Medium Level")
    z.resizable(FALSE,FALSE)

    def check():
        score=0
        if first.get().lower()=="pacific ocean":
            score+=1
        if second.get()=="12":
            score+=1
        if third.get().lower()=="camel":
            score+=1
        if fourth.get()=="206":
            score+=1
        if fifth.get().lower()=="saturn":
            score+=1

        messagebox.showinfo("Score", f"Your Score is: {score}/5")
    first=StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    fifth=StringVar()

    l1=Label(z,text=m[0],font=("Arial",20),pady=20)
    l1.grid(row=0,column=0)
    e1=Entry(z,font=("Arial",20),textvariable=first)
    e1.grid(row=0,column=1)

    l2=Label(z,text=m[1],font=("Arial",20),pady=20)
    l2.grid(row=1,column=0)
    e2=Entry(z,font=("Arial",20),textvariable=second)
    e2.grid(row=1,column=1)

    l3=Label(z,text=m[2],font=("Arial",20),pady=20)
    l3.grid(row=2,column=0)
    e3=Entry(z,font=("Arial",20),textvariable=third)
    e3.grid(row=2,column=1)

    l4=Label(z,text=m[3],font=("Arial",20),pady=20)
    l4.grid(row=3,column=0)
    e4=Entry(z,font=("Arial",20),textvariable=fourth)
    e4.grid(row=3,column=1)

    l5=Label(z,text=m[4],font=("Arial",20),pady=20)
    l5.grid(row=4,column=0)
    e5=Entry(z,font=("Arial",20),textvariable=fifth)
    e5.grid(row=4,column=1)

    b1=Button(z,text="SUBMIT THE ANSWERS",font=("Arial",20),pady=20,command=check)
    b1.grid(row=5,column=0)

    b2=Button(z,text="CLICK TO EXIT",font=("Arial",20),pady=20,command=z.destroy)
    b2.grid(row=5,column=1)

def hard():
    messagebox.showinfo("Hard Level", "Welcome to the Hard Level!")
    x.destroy()
    w=Tk()
    w.geometry("1000x600")
    w.title("Hard Level")
    w.resizable(FALSE,FALSE)

    def check():
        score=0
        if first.get().lower()=="42":
            score+=1
        if second.get().lower()=="france":
            score+=1
        if third.get().lower()=="2":
            score+=1
        if fourth.get().lower()=="150":
            score+=1
        if fifth.get().lower()=="vatican city":
            score+=1

        messagebox.showinfo("Score", f"Your Score is: {score}/5")
    first=StringVar()
    second=StringVar()
    third=StringVar()
    fourth=StringVar()
    fifth=StringVar()

    l1=Label(w,text=d[0],font=("Arial",20),pady=20)
    l1.grid(row=0,column=0)
    e1=Entry(w,font=("Arial",20),textvariable=first)
    e1.grid(row=0,column=1)

    l2=Label(w,text=d[1],font=("Arial",20),pady=20)
    l2.grid(row=1,column=0)
    e2=Entry(w,font=("Arial",20),textvariable=second)
    e2.grid(row=1,column=1)

    l3=Label(w,text=d[2],font=("Arial",20),pady=20)
    l3.grid(row=2,column=0)
    e3=Entry(w,font=("Arial",20),textvariable=third)
    e3.grid(row=2,column=1)

    l4=Label(w,text=d[3],font=("Arial",20),pady=20)
    l4.grid(row=3,column=0)
    e4=Entry(w,font=("Arial",20),textvariable=fourth)
    e4.grid(row=3,column=1)

    l5=Label(w,text=d[4],font=("Arial",20),pady=20)
    l5.grid(row=4,column=0)
    e5=Entry(w,font=("Arial",20),textvariable=fifth)
    e5.grid(row=4,column=1)

    b1=Button(w,text="SUBMIT THE ANSWERS",font=("Arial",20),pady=20,command=check)
    b1.grid(row=5,column=0)

    b2=Button(w,text="CLICK TO EXIT",font=("Arial",20),pady=20,command=w.destroy)
    b2.grid(row=5,column=1)

x=Tk()
x.geometry("800x600")
x.title("Quiz Application")
x.resizable(FALSE,FALSE)

l1=Label(x,text="WELCOME TO THE QUIZ, PLEASE SELECT YOUR LEVEL",font=("Arial",15),pady=20)
l1.grid(row=0,column=0)

b1=Button(x,text="CLICK FOR EASY LEVEL",font=("Arial",15),pady=20,command=easy)
b1.grid(row=1,column=0)

b2=Button(x,text="CLICK FOR MEDIUM LEVEL",font=("Arial",15),pady=20,command=medium)
b2.grid(row=2,column=0)

b3=Button(x,text="CLICK FOR HARD LEVEL",font=("Arial",15),pady=20)
b3.grid(row=3,column=0)

x.mainloop()
'''