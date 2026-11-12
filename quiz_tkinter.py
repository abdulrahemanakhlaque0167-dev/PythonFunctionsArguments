
from tkinter import *
from tkinter import messagebox
import random

# ==========================================
# COLOUR THEME
# ==========================================

BG = "#172554"
CARD = "#1E3A5F"
WHITE = "#FFFFFF"
PURPLE = "#9333EA"
BLUE = "#2563EB"
GREEN = "#059669"
ORANGE = "#EA580C"
YELLOW = "#FACC15"
ENTRY_BG = "#DBEAFE"

# ==========================================
# EASY QUESTION BANK
# ==========================================

easy = [
    ("What is the capital of India?", ["delhi"]),
    ("Which planet is known as the Red Planet?", ["mars"]),
    ("How many days are there in a week?", ["7", "seven"]),
    ("What is 5 + 5?", ["10", "ten"]),
    ("Which language are we using to make this game?", ["python"]),
    ("How many months are there in a year?", ["12", "twelve"]),
    ("Which animal is known as the King of the Jungle?", ["lion"]),
    ("What is the opposite of hot?", ["cold"]),
    ("How many legs does a spider have?", ["8", "eight"]),
    ("Which is the largest land animal?", ["elephant"]),
    ("Which colour is made by mixing red and white?", ["pink"]),
    ("How many sides does a triangle have?", ["3", "three"]),
    ("Which is the national bird of India?", ["peacock"]),
    ("Which star gives us light during the day?", ["sun"]),
    ("What is the freezing point of water in Celsius?", ["0", "zero"])
]

# ==========================================
# MEDIUM QUESTION BANK
# ==========================================

medium = [
    ("Which is the largest ocean on Earth?", ["pacific ocean", "pacific"]),
    ("What is the square root of 144?", ["12", "twelve"]),
    ("Which animal is known as the Ship of the Desert?", ["camel"]),
    ("How many bones does an adult human usually have?", ["206"]),
    ("Which planet has the most famous ring system?", ["saturn"]),
    ("What is the chemical symbol of gold?", ["au"]),
    ("Which is the smallest continent?", ["australia"]),
    ("Who wrote Romeo and Juliet?", ["william shakespeare", "shakespeare"]),
    ("What is the largest organ of the human body?", ["skin"]),
    ("How many players are there in a cricket team?", ["11", "eleven"]),
    ("Which gas do plants absorb from the atmosphere?", ["carbon dioxide"]),
    ("What is the capital of Japan?", ["tokyo"]),
    ("Which instrument is used to measure temperature?", ["thermometer"]),
    ("How many degrees are there in a right angle?", ["90", "ninety"]),
    ("Which country is famous for the Eiffel Tower?", ["france"])
]

# ==========================================
# HARD QUESTION BANK
# ==========================================

hard = [
    ("If you have 3 apples and take away 2, how many apples do you have?", ["2", "two"]),
    ("Which country gifted the Statue of Liberty to the United States?", ["france"]),
    ("What is the only even prime number?", ["2", "two"]),
    ("A train travels 60 km in 1 hour. How far will it travel in 2 hours and 30 minutes?", ["150", "150 km"]),
    ("Which is the smallest country in the world by area?", ["vatican city"]),
    ("What is the Roman numeral for 50?", ["l"]),
    ("Which element has the chemical symbol Na?", ["sodium"]),
    ("How many sides does a dodecagon have?", ["12", "twelve"]),
    ("Which scientist developed the theory of relativity?", ["albert einstein", "einstein"]),
    ("What is the hardest natural substance on Earth?", ["diamond"]),
    ("Which blood cells help the body fight infections?", ["white blood cells"]),
    ("What is the value of pi rounded to two decimal places?", ["3.14"]),
    ("Which is the deepest ocean trench in the world?", ["mariana trench"]),
    ("What is the smallest prime number greater than 20?", ["23", "twenty three"]),
    ("Which planet takes the longest time to orbit the Sun?", ["neptune"])
]

# ==========================================
# MAIN WINDOW
# ==========================================

root = Tk()
root.geometry("1000x700")
root.title("Quiz Application")
root.resizable(False, False)
root.configure(bg=BG)

# ==========================================
# MAIN SCREEN
# ==========================================

home = Frame(root, bg=BG)
home.pack(fill="both", expand=True)

def show_home():

    quiz_frame.pack_forget()
    home.pack(fill="both", expand=True)

def start_quiz(level, questions):

    global selected_questions, answer_vars

    home.pack_forget()

    selected_questions = random.sample(questions, 5)

    quiz_frame.pack(fill="both", expand=True)

    # Clear previous questions
    for widget in question_area.winfo_children():
        widget.destroy()

    answer_vars = []

    heading.config(text=level.upper() + " LEVEL QUIZ")

    for i, (question, correct_answers) in enumerate(selected_questions):

        card = Frame(question_area, bg=CARD, padx=15, pady=8)
        card.pack(fill="x", padx=35, pady=6)

        Label(
            card,
            text=f"QUESTION {i+1}: {question}",
            font=("Arial", 13, "bold"),
            bg=CARD,
            fg=WHITE,
            wraplength=850,
            justify="left"
        ).pack(anchor="w", pady=5)

        var = StringVar()
        answer_vars.append(var)

        Entry(
            card,
            textvariable=var,
            font=("Arial", 14),
            bg=ENTRY_BG,
            fg=BG,
            width=45
        ).pack(anchor="w", pady=5)

    submit_btn.config(state=NORMAL)

    root.title(level + " Level Quiz")


# ==========================================
# CHECK ANSWERS
# ==========================================

def check_answers():

    score = 0
    result = ""

    for i, (question, correct_answers) in enumerate(selected_questions):

        user_answer = answer_vars[i].get().strip().lower()

        if user_answer in correct_answers:
            score += 1
            result += f"Question {i+1}: CORRECT\n"

        else:
            result += (
                f"Question {i+1}: INCORRECT\n"
                f"Correct answer: {correct_answers[0].title()}\n"
            )

    submit_btn.config(state=DISABLED)

    messagebox.showinfo(
        "QUIZ RESULT",
        f"YOUR SCORE: {score}/5\n\n"
        + result
    )

    if score == 5:
        messagebox.showinfo("Amazing!", "PERFECT SCORE! YOU ARE A CHAMPION!")

    elif score >= 3:
        messagebox.showinfo("Well Done!", "GREAT JOB! KEEP IT UP!")

    else:
        messagebox.showinfo("Keep Practicing!", "BETTER LUCK NEXT TIME!")

# ==========================================
# HOME SCREEN DESIGN
# ==========================================

Label(
    home,
    text="WELCOME TO THE QUIZ!",
    font=("Arial", 30, "bold"),
    bg=BG,
    fg=YELLOW
).pack(pady=(75, 10))

Label(
    home,
    text="PLEASE SELECT YOUR DIFFICULTY LEVEL",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg=WHITE
).pack(pady=15)

Button(
    home,
    text="CLICK FOR EASY LEVEL",
    font=("Arial", 16, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#05B8FF",
    width=28,
    pady=15,
    command=lambda: start_quiz("Easy", easy)
).pack(pady=12)

Button(
    home,
    text="CLICK FOR MEDIUM LEVEL",
    font=("Arial", 16, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#7E22CE",
    width=28,
    pady=15,
    command=lambda: start_quiz("Medium", medium)
).pack(pady=12)

Button(
    home,
    text="CLICK FOR HARD LEVEL",
    font=("Arial", 16, "bold"),
    bg=ORANGE,
    fg=WHITE,
    activebackground="#C2410C",
    width=28,
    pady=15,
    command=lambda: start_quiz("Hard", hard)
).pack(pady=12)

Label(
    home,
    text="TEST YOUR KNOWLEDGE!",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg=YELLOW
).pack(pady=35)

# ==========================================
# QUIZ SCREEN
# ==========================================

quiz_frame = Frame(root, bg=BG)

heading = Label(
    quiz_frame,
    text="QUIZ",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=YELLOW
)
heading.pack(pady=15)

Label(
    quiz_frame,
    text="Answer all 5 randomly selected questions!",
    font=("Arial", 13),
    bg=BG,
    fg=WHITE
).pack(pady=5)

question_area = Frame(quiz_frame, bg=BG)
question_area.pack(fill="both", expand=True, pady=5)

# ==========================================
# BUTTONS
# ==========================================

button_frame = Frame(quiz_frame, bg=BG)
button_frame.pack(pady=15)

submit_btn = Button(
    button_frame,
    text="SUBMIT ANSWERS",
    font=("Arial", 14, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#047857",
    width=20,
    pady=12,
    command=check_answers
)
submit_btn.grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="BACK TO HOME",
    font=("Arial", 14, "bold"),
    bg=ORANGE,
    fg=WHITE,
    activebackground="#C2410C",
    width=20,
    pady=12,
    command=show_home
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="EXIT",
    font=("Arial", 14, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#7E22CE",
    width=12,
    pady=12,
    command=root.destroy
).grid(row=0, column=2, padx=10)

# ==========================================
# START APPLICATION
# ==========================================

root.mainloop()



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