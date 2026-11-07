
from tkinter import *
from tkinter import messagebox
import random

# ================= COLORS =================

BG = "#0F172A"
CARD = "#1E293B"
WHITE = "#FFFFFF"
GREEN = "#22C55E"
BLUE = "#2563EB"
RED = "#EF4444"
YELLOW = "#FACC15"
ENTRY_BG = "#334155"

# ================= GAME VARIABLES =================

score = 0
saves = 0
shots = 0
max_shots = 5

# ================= FUNCTIONS =================

def update_score():
    score_label.config(text=f"GOALS: {score}")
    save_label.config(text=f"SAVES: {saves}")
    shot_label.config(text=f"SHOTS: {shots}/{max_shots}")


def shoot(direction):

    global score, saves, shots

    if shots >= max_shots:
        messagebox.showinfo("GAME OVER", "You have completed all 5 shots!")
        return

    goalkeeper = random.choice(["LEFT", "CENTRE", "RIGHT"])

    shots += 1

    result_label.config(
        text=f"GOALKEEPER DIVED: {goalkeeper}",
        fg=YELLOW
    )

    if direction == goalkeeper:

        saves += 1

        result_label.config(
            text="SAVED! THE GOALKEEPER STOPPED IT!",
            fg=RED
        )

    else:

        score += 1

        result_label.config(
            text="GOOOOOAL! AMAZING SHOT!",
            fg=GREEN
        )

    update_score()

    if shots == max_shots:

        if score > saves:
            messagebox.showinfo(
                "WINNER!",
                f"CONGRATULATIONS!\n\nGoals: {score}\nSaves: {saves}"
            )

        elif score == saves:
            messagebox.showinfo(
                "DRAW!",
                f"Well played!\n\nGoals: {score}\nSaves: {saves}"
            )

        else:
            messagebox.showinfo(
                "GAME OVER",
                f"Better luck next time!\n\nGoals: {score}\nSaves: {saves}"
            )


def reset_game():

    global score, saves, shots

    score = 0
    saves = 0
    shots = 0

    result_label.config(
        text="CHOOSE YOUR SHOOTING DIRECTION!",
        fg=WHITE
    )

    update_score()


# ================= MAIN WINDOW =================

x = Tk()

x.title("FOOTBALL PENALTY SHOOTOUT")
x.geometry("1000x650")
x.resizable(False, False)
x.configure(bg=BG)

# ================= TITLE =================

title = Label(
    x,
    text="⚽ FOOTBALL PENALTY SHOOTOUT ⚽",
    font=("Arial", 28, "bold"),
    bg=BG,
    fg=GREEN
)

title.pack(pady=25)

subtitle = Label(
    x,
    text="CAN YOU SCORE 5 GOALS?",
    font=("Arial", 15, "bold"),
    bg=BG,
    fg=YELLOW
)

subtitle.pack(pady=5)

# ================= SCOREBOARD =================

score_frame = Frame(x, bg=CARD, padx=30, pady=20)
score_frame.pack(pady=20)

score_label = Label(
    score_frame,
    text="GOALS: 0",
    font=("Arial", 19, "bold"),
    bg=CARD,
    fg=GREEN,
    width=15
)

score_label.grid(row=0, column=0, padx=10)

save_label = Label(
    score_frame,
    text="SAVES: 0",
    font=("Arial", 19, "bold"),
    bg=CARD,
    fg=RED,
    width=15
)

save_label.grid(row=0, column=1, padx=10)

shot_label = Label(
    score_frame,
    text="SHOTS: 0/5",
    font=("Arial", 19, "bold"),
    bg=CARD,
    fg=YELLOW,
    width=15
)

shot_label.grid(row=0, column=2, padx=10)

# ================= RESULT =================

result_label = Label(
    x,
    text="CHOOSE YOUR SHOOTING DIRECTION!",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg=WHITE
)

result_label.pack(pady=25)

# ================= SHOOTING BUTTONS =================

button_frame = Frame(x, bg=BG)
button_frame.pack(pady=20)

left_button = Button(
    button_frame,
    text="⬅ LEFT",
    font=("Arial", 18, "bold"),
    bg=BLUE,
    fg=WHITE,
    width=12,
    height=2,
    command=lambda: shoot("LEFT")
)

left_button.grid(row=0, column=0, padx=15)

centre_button = Button(
    button_frame,
    text="⬆ CENTRE",
    font=("Arial", 18, "bold"),
    bg=GREEN,
    fg=WHITE,
    width=12,
    height=2,
    command=lambda: shoot("CENTRE")
)

centre_button.grid(row=0, column=1, padx=15)

right_button = Button(
    button_frame,
    text="RIGHT ➡",
    font=("Arial", 18, "bold"),
    bg=BLUE,
    fg=WHITE,
    width=12,
    height=2,
    command=lambda: shoot("RIGHT")
)

right_button.grid(row=0, column=2, padx=15)

# ================= RESET BUTTON =================

reset_button = Button(
    x,
    text="🔄 PLAY AGAIN",
    font=("Arial", 17, "bold"),
    bg=YELLOW,
    fg=BG,
    width=18,
    command=reset_game
)

reset_button.pack(pady=30)

# ================= FOOTER =================

footer = Label(
    x,
    text="GOOD LUCK, CHAMPION! ⚽",
    font=("Arial", 13, "italic"),
    bg=BG,
    fg=WHITE
)

footer.pack(pady=5)

x.mainloop()
