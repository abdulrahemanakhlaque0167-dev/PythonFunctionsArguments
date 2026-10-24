from tkinter import *
from tkinter import messagebox
import random


# ============================================================
# MASTER RIDDLE DATA - 40 RIDDLES
# ============================================================

all_riddles = [
    ("I say meow and like to chase mice. What am I?", "cat"),
    ("I come out in the day and give you light. What am I?", "sun"),
    ("I say woof and love to wag my tail. What am I?", "dog"),
    ("I am yellow and monkeys love to eat me. What am I?", "banana"),
    ("I am white outside and yellow inside. What am I?", "egg"),
    ("I am often red, round, and you can eat me. What am I?", "apple"),
    ("I am very big and have a long trunk. What am I?", "elephant"),
    ("I shine in the night sky. What am I?", "moon"),
    ("I have four wheels and take you places. What am I?", "car"),
    ("I live in water and can swim. What am I?", "fish"),

    ("I have hands but cannot clap. What am I?", "clock"),
    ("I have keys but open no locks. What am I?", "piano"),
    ("I have a face and two hands but no arms. What am I?", "clock"),
    ("I have many teeth but cannot bite. What am I?", "comb"),
    ("I get wetter as I dry. What am I?", "towel"),
    ("I have a neck but no head. What am I?", "bottle"),
    ("I have one eye but cannot see. What am I?", "needle"),
    ("I fly without wings and cry without eyes. What am I?", "cloud"),
    ("I have pages but I am not a website. What am I?", "book"),
    ("I have legs but cannot walk. What am I?", "table"),

    ("I am full of holes but can hold water. What am I?", "sponge"),
    ("I have a tail and fly in the sky on a windy day. What am I?", "kite"),
    ("I fall from the sky and help plants grow. What am I?", "rain"),
    ("I am cold, white, and fall in winter. What am I?", "snow"),
    ("I have a shell and move very slowly. What am I?", "turtle"),
    ("I make honey and buzz around flowers. What am I?", "bee"),
    ("I have black and white stripes. What am I?", "zebra"),
    ("I hop and carry my baby in a pouch. What am I?", "kangaroo"),
    ("I change from a caterpillar into a beautiful insect. What am I?", "butterfly"),
    ("I have eight legs and spin webs. What am I?", "spider"),

    ("I have a trunk and branches but no arms. What am I?", "tree"),
    ("I have cities but no houses and rivers but no water. What am I?", "map"),
    ("The more you take, the more you leave behind. What are they?", "footsteps"),
    ("I have a ring but no finger. What am I?", "telephone"),
    ("I can be cracked, made, told, and played. What am I?", "joke"),
    ("I have a head and a tail but no body. What am I?", "coin"),
    ("I go up but never come down. What am I?", "age"),
    ("I have four legs and a back but no body. What am I?", "chair"),
    ("I light up a room but take up no space. What am I?", "light"),
    ("I am always in front of you but cannot be seen. What am I?", "future")
]

# Active game variables
riddles = []
current = 0
score = 0


# ============================================================
# COLORS
# ============================================================

BG = "#EAF4FB"
DARK_BLUE = "#123B5D"
BLUE = "#167D9A"
HOVER_BLUE = "#0B5D73"
WHITE = "#FFFFFF"
GREEN = "#198754"
RED = "#D9485F"
TEXT = "#243746"


# ============================================================
# FUNCTIONS
# ============================================================

def init_game():
    global riddles, current, score
    current = 0
    score = 0
    # Pick 10 random unique riddles from the 40 available
    riddles = random.sample(all_riddles, 10)


def show_riddle():
    question, answer = riddles[current]

    question_label.config(text=question)
    counter_label.config(
        text=f"RIDDLE {current + 1} OF {len(riddles)}"
    )
    score_label.config(text=f"⭐ Score: {score}")

    guess.set("")
    entry.config(state=NORMAL)
    entry.focus_set()

    check_button.config(state=NORMAL)
    next_button.config(state=DISABLED)

    feedback_label.config(
        text="Think carefully and enter your answer!",
        fg=TEXT
    )


def check_answer():
    global score

    if current >= len(riddles):
        return

    user_answer = guess.get().strip().lower()
    correct_answer = riddles[current][1].lower()

    if not user_answer:
        messagebox.showwarning(
            "Empty Guess",
            "Please enter your answer first!"
        )
        entry.focus_set()
        return

    if user_answer == correct_answer:
        score += 1

        feedback_label.config(
            text="🎉 Correct! Excellent work!",
            fg=GREEN
        )

        score_label.config(text=f"⭐ Score: {score}")

        entry.config(state=DISABLED)
        check_button.config(state=DISABLED)
        next_button.config(state=NORMAL)
        next_button.focus_set()

    else:
        feedback_label.config(
            text="❌ Not quite! Try another answer.",
            fg=RED
        )

        entry.delete(0, END)
        entry.focus_set()


def next_riddle():
    global current

    if current >= len(riddles):
        return

    current += 1

    if current < len(riddles):
        show_riddle()
    else:
        finish_game()


def finish_game():
    question_label.config(
        text="🏆 AMAZING! YOU COMPLETED ALL 10 RIDDLES!"
    )

    counter_label.config(text="GAME COMPLETED")
    score_label.config(
        text=f"⭐ Final Score: {score}/{len(riddles)}"
    )

    feedback_label.config(
        text="You are a Riddle Master! 🎉",
        fg=GREEN
    )

    entry.config(state=DISABLED)
    check_button.config(state=DISABLED)
    next_button.config(state=DISABLED)
    restart_button.grid()

    messagebox.showinfo(
        "Game Completed!",
        f"Congratulations!\n\n"
        f"Your final score is {score}/{len(riddles)}.\n\n"
        f"Thanks for playing!"
    )


def restart_game():
    init_game()
    restart_button.grid_remove()
    show_riddle()


# ============================================================
# MAIN WINDOW
# ============================================================

r = Tk()
r.title("Riddle Master - Guessing Game")
r.geometry("1000x650")
r.resizable(False, False)
r.configure(bg=BG)


# ============================================================
# HEADER
# ============================================================

header = Frame(r, bg=DARK_BLUE, height=120)
header.pack(fill=X)
header.pack_propagate(False)

title_label = Label(
    header,
    text="🧩 RIDDLE MASTER",
    font=("Calibri", 32, "bold"),
    bg=DARK_BLUE,
    fg=WHITE
)
title_label.pack(pady=(15, 0))

subtitle = Label(
    header,
    text="Think smart • Guess correctly • Have fun!",
    font=("Calibri", 14),
    bg=DARK_BLUE,
    fg="#D6EAF8"
)
subtitle.pack(pady=3)


# ============================================================
# SCORE AND COUNTER
# ============================================================

info_frame = Frame(r, bg=BG)
info_frame.pack(fill=X, padx=45, pady=20)

counter_label = Label(
    info_frame,
    text="RIDDLE 1 OF 10",
    font=("Calibri", 15, "bold"),
    bg=BG,
    fg=BLUE
)
counter_label.pack(side=LEFT)

score_label = Label(
    info_frame,
    text="⭐ Score: 0",
    font=("Calibri", 15, "bold"),
    bg=BG,
    fg=DARK_BLUE
)
score_label.pack(side=RIGHT)


# ============================================================
# RIDDLE CARD
# ============================================================

card = Frame(
    r,
    bg=WHITE,
    highlightbackground="#C7DFEC",
    highlightthickness=2
)
card.pack(fill=X, padx=45, pady=5)

Label(
    card,
    text="YOUR CHALLENGE",
    font=("Calibri", 13, "bold"),
    bg=WHITE,
    fg=BLUE
).pack(pady=(25, 10))

question_label = Label(
    card,
    text="",
    font=("Calibri", 22, "bold"),
    bg=WHITE,
    fg=DARK_BLUE,
    wraplength=820,
    justify=CENTER,
    padx=25,
    pady=20
)
question_label.pack(fill=X)


# ============================================================
# ANSWER INPUT
# ============================================================

Label(
    r,
    text="Enter your answer below",
    font=("Calibri", 16, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=(22, 8))

guess = StringVar()

entry = Entry(
    r,
    textvariable=guess,
    font=("Calibri", 20),
    justify=CENTER,
    width=25,
    relief=FLAT,
    bd=0,
    bg=WHITE,
    fg=TEXT,
    highlightthickness=2,
    highlightbackground="#B5D3E2",
    highlightcolor=BLUE
)
entry.pack(ipady=10, pady=5)


# ============================================================
# FEEDBACK
# ============================================================

feedback_label = Label(
    r,
    text="Think carefully and enter your answer!",
    font=("Calibri", 14, "bold"),
    bg=BG,
    fg=TEXT
)
feedback_label.pack(pady=10)


# ============================================================
# BUTTONS
# ============================================================

button_frame = Frame(r, bg=BG)
button_frame.pack(pady=8)


check_button = Button(
    button_frame,
    text="✓  CHECK ANSWER",
    font=("Calibri", 14, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=HOVER_BLUE,
    activeforeground=WHITE,
    relief=FLAT,
    cursor="hand2",
    padx=20,
    pady=12,
    command=check_answer
)
check_button.grid(row=0, column=0, padx=10)


next_button = Button(
    button_frame,
    text="NEXT RIDDLE  ➜",
    font=("Calibri", 14, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#146C43",
    activeforeground=WHITE,
    relief=FLAT,
    cursor="hand2",
    padx=20,
    pady=12,
    state=DISABLED,
    command=next_riddle
)
next_button.grid(row=0, column=1, padx=10)


restart_button = Button(
    button_frame,
    text="↻  PLAY AGAIN",
    font=("Calibri", 13, "bold"),
    bg=DARK_BLUE,
    fg=WHITE,
    activebackground=HOVER_BLUE,
    activeforeground=WHITE,
    relief=FLAT,
    cursor="hand2",
    padx=20,
    pady=10,
    command=restart_game
)
# Place restart button below check/next buttons and hide it initially
restart_button.grid(row=1, column=0, columnspan=2, pady=10)
restart_button.grid_remove()


# Press Enter to check the answer
r.bind("<Return>", lambda event: check_answer())


# ============================================================
# START GAME
# ============================================================

init_game()
show_riddle()

r.mainloop()

'''from tkinter import *
from tkinter import messagebox
import random

ans=["cat","sun","dog","banana","egg","apple","elephant","moon","car","fish"]
l=random.choice(ans)
if l=="cat":
    x=("I say “meow” and I like to chase mice. What am I?")
elif l=="sun":
    x=("I come out in the day and give you light. What am I?")
elif l=="dog":
    x=("I say “woof” and I love to wag my tail. What am I?")
elif l=="banana":
    x=("I am yellow and monkeys love to eat me. What am I?")
elif l=="egg":
    x=("I am white outside and yellow inside. You can eat me for breakfast. What am I?")
elif l=="apple":
    x=("I am red, round, and you can eat me. What am I?")
elif l=="elephant":
    x=("I am very big and have a long trunk. What am I?")
elif l=="moon":
    x=("I come out at night and shine in the sky. What am I?")
elif l=="car":
    x=("I have four wheels and take you from one place to another. What am I?")
elif l=="fish":
    x=("I live in water and I can swim. What am I?")
else:
    print()

def button():
    y=(guess.get())
    if y==l:
        messagebox.showinfo("You Won","Congratulations! You Won")
        r.destroy()
    else:
        messagebox.showerror("wrong","your guess is wrong")
        e1.delete(0,END)
        

r=Tk()
r.geometry("1350x600")
r.resizable(FALSE,FALSE)
r.title("Riddle Guessing Game")

guess=StringVar()

l1=Label(r,text=x,font=("calibri",25,"bold"),padx=20,pady=20)
l1.grid(row=0,column=0)
l2=Label(r,text="Enter your guess",font=("calibri",25,"bold"),padx=20,pady=20)
l2.grid(row=1,column=0)

e1=Entry(r,font=("Calibri",25,"bold"),textvariable=guess)
e1.grid(row=1,column=1)

b1=Button(r,text="press to guess",font=("Calibri",25,"bold"),command=button)
b1.grid(row=2,column=0,padx=20,pady=20)
r.mainloop()'''