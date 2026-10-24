
from tkinter import *
import random
from tkinter import messagebox


l = random.randint(1, 100)

def noguess():
    try:
        g = int(guess.get())

        if g < 1 or g > 100:
            messagebox.showwarning(
                "Invalid Guess",
                "Please enter a number between 1 and 100!"
            )
            e1.delete(0, END)
            return

        if g == l:
            messagebox.showinfo(
                "Congratulations!",
                "🎉 You Won!\n\nYou guessed the correct number!"
            )
            w.destroy() 
        elif g >= l:
            messagebox.showinfo(
                "Go Lower",
                "Your guess is High!\n\nTry a smaller number."
            )

        elif g <= l:
            messagebox.showinfo(
                "Go Higher",
                "Your guess is Low!\n\nTry a bigger number."
            )

        e1.delete(0, END)
        e1.focus_set()

    except ValueError:
        messagebox.showwarning(
            "Invalid Input",
            "Please enter a valid number!"
        )
        e1.delete(0, END)
        e1.focus_set()



w = Tk()
w.geometry("800x600")
w.title("NUMBER GUESSING GAME")
w.resizable(FALSE, FALSE)
w.configure(bg="#EAF4F8")

guess = StringVar()

header = Frame(w, bg="#123B5D", height=130)
header.pack(fill=X)

title = Label(
    header,
    text="🎯 NUMBER GUESSING GAME",
    font=("Calibri", 30, "bold"),
    bg="#123B5D",
    fg="white"
)
title.pack(pady=(22, 5))

subtitle = Label(
    header,
    text="Guess the secret number between 1 and 100!",
    font=("Calibri", 15),
    bg="#123B5D",
    fg="#D6EAF8"
)
subtitle.pack()

card = Frame(
    w,
    bg="white",
    highlightbackground="#C5DCE8",
    highlightthickness=2
)
card.pack(padx=80, pady=45, fill=BOTH, expand=True)

instruction = Label(
    card,
    text="ENTER YOUR GUESS",
    font=("Calibri", 22, "bold"),
    bg="white",
    fg="#123B5D"
)
instruction.pack(pady=(35, 15))

e1 = Entry(
    card,
    font=("Calibri", 24, "bold"),
    textvariable=guess,
    justify="center",
    width=12,
    bd=0,
    relief=FLAT,
    bg="#F0F7FA",
    fg="#123B5D",
    highlightthickness=2,
    highlightbackground="#B7D7E8",
    highlightcolor="#167D9A"
)
e1.pack(ipady=10, pady=10)
e1.focus_set()

def on_enter(event):
    b1.config(bg="#0B5D73")

def on_leave(event):
    b1.config(bg="#167D9A")


b1 = Button(
    card,
    text="CHECK MY GUESS",
    font=("Calibri", 18, "bold"),
    bg="#167D9A",
    fg="white",
    activebackground="#0B5D73",
    activeforeground="white",
    command=noguess,
    cursor="hand2",
    bd=0,
    relief=FLAT,
    padx=25,
    pady=12
)
b1.pack(pady=25)

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)


w.bind("<Return>", lambda event: noguess())


footer = Label(
    w,
    text="💡 Keep trying until you find the secret number!",
    font=("Calibri", 13, "italic"),
    bg="#EAF4F8",
    fg="#456B80"
)
footer.pack(pady=(0, 15))

w.mainloop()


'''from tkinter import *
import random
from tkinter import messagebox
l=random.randint(1,100)
def noguess():
    g=int(guess.get())
    if g==l:
        messagebox.showinfo(
            "Congratulations!",
            "You Won!"
        )

    elif g>=l:
        messagebox.showinfo(
            "Go Lower",
            "Your guess is High!"            
        )
    elif g<=l:
        messagebox.showinfo(
            "Go Higher",
            "Your guess is Low!"          
        )
    e1.delete(0, END)
w=Tk()
w.geometry("800x600")
w.title("NUMBER GUESSING GAME")
w.resizable(FALSE,FALSE)
guess=StringVar()
l1=Label(w,text="ENTER YOUR GUESS=",font=("Calibri",25,"bold"))
l1.grid(row=0,column=0,padx=20,pady=20)
e1=Entry(w,font=("calibri",25,"bold"),textvariable=guess)
e1.grid(row=0,column=1,padx=20,pady=20)
b1=Button(w,text="CLICK FOR GUESS",font=("Calibri",25,"bold"),command=noguess)
b1.grid(row=1,column=0,padx=20,pady=20)
w.mainloop()'''