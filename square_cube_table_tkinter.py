
from tkinter import *
from tkinter import messagebox

# ==============================
# COLOUR THEME
# ==============================

BG = "#EAF4FF"
CARD = "#FFFFFF"
BLUE = "#60A5FA"
PURPLE = "#A78BFA"
GREEN = "#6EE7B7"
DARK = "#1E3A5F"
TEXT = "#334155"
LIGHT_BLUE = "#DBEAFE"
RED = "#EF4444"


# ==============================
# CALCULATION FUNCTION
# ==============================

def get_number():
    try:
        n = int(no.get())
        return n
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number!"
        )
        return None


# ==============================
# RESULT WINDOW
# ==============================

def result_window(title, heading, result):

    x = Toplevel(root)
    x.geometry("600x500")
    x.title(title)
    x.resizable(False, False)
    x.configure(bg=BG)

    Label(
        x,
        text=heading,
        font=("Calibri", 23, "bold"),
        bg=BG,
        fg=DARK
    ).pack(pady=30)

    Label(
        x,
        text=result,
        font=("Calibri", 23, "bold"),
        bg=CARD,
        fg="#2563EB",
        padx=30,
        pady=25,
        justify=CENTER
    ).pack(pady=20, padx=30)

    Button(
        x,
        text="CLOSE",
        font=("Calibri", 15, "bold"),
        bg=BLUE,
        fg="white",
        relief=FLAT,
        width=15,
        command=x.destroy
    ).pack(pady=20)


# ==============================
# SQUARE
# ==============================

def square():

    n = get_number()

    if n is None:
        return

    s = n * n

    result_window(
        "Square Result",
        "SQUARE OF THE NUMBER",
        f"{n} × {n} = {s}"
    )


# ==============================
# CUBE
# ==============================

def cube():

    n = get_number()

    if n is None:
        return

    s = n * n * n

    result_window(
        "Cube Result",
        "CUBE OF THE NUMBER",
        f"{n} × {n} × {n} = {s}"
    )


# ==============================
# MULTIPLICATION TABLE
# ==============================

def table():

    n = get_number()

    if n is None:
        return

    x = Toplevel(root)
    x.geometry("600x650")
    x.title("Multiplication Table")
    x.resizable(False, False)
    x.configure(bg=BG)

    Label(
        x,
        text=f"TABLE OF {n}",
        font=("Calibri", 27, "bold"),
        bg=BG,
        fg=DARK
    ).pack(pady=20)

    frame = Frame(x, bg=CARD, padx=40, pady=20)
    frame.pack(pady=10)

    for i in range(1, 11):

        Label(
            frame,
            text=f"{n} × {i} = {n * i}",
            font=("Calibri", 19, "bold"),
            bg=CARD,
            fg=TEXT,
            width=20
        ).pack(pady=3)

    Button(
        x,
        text="CLOSE",
        font=("Calibri", 15, "bold"),
        bg=GREEN,
        fg=DARK,
        relief=FLAT,
        width=15,
        command=x.destroy
    ).pack(pady=20)


# ==============================
# CLEAR FUNCTION
# ==============================

def clear():
    no.set("")


# ==============================
# CLOSE APPLICATION
# ==============================

def close_application():
    root.destroy()


# ==============================
# MAIN WINDOW
# ==============================

root = Tk()

root.geometry("900x700")
root.title("Simple Calculating GUI")
root.resizable(False, False)
root.configure(bg=BG)


# ==============================
# MAIN HEADING
# ==============================

Label(
    root,
    text="SIMPLE CALCULATING GUI",
    font=("Calibri", 30, "bold"),
    bg=BG,
    fg=DARK
).pack(pady=(20, 5))


Label(
    root,
    text="Calculate Square, Cube and Multiplication Table",
    font=("Calibri", 15),
    bg=BG,
    fg=TEXT
).pack(pady=5)


# ==============================
# MAIN CARD
# ==============================

card = Frame(
    root,
    bg=CARD,
    padx=40,
    pady=20
)

card.pack(pady=15)


Label(
    card,
    text="ENTER A NUMBER",
    font=("Calibri", 19, "bold"),
    bg=CARD,
    fg=DARK
).pack(pady=8)


# INPUT VARIABLE

no = StringVar()


# ENTRY BOX

e1 = Entry(
    card,
    font=("Calibri", 23, "bold"),
    textvariable=no,
    justify=CENTER,
    width=20,
    bg=LIGHT_BLUE,
    fg=DARK,
    relief=FLAT,
    bd=5
)

e1.pack(pady=10)


# ==============================
# CALCULATION BUTTONS
# ==============================

Button(
    card,
    text="CALCULATE SQUARE",
    font=("Calibri", 17, "bold"),
    bg=BLUE,
    fg="white",
    activebackground="#3B82F6",
    activeforeground="white",
    relief=FLAT,
    width=23,
    pady=6,
    command=square
).pack(pady=5)


Button(
    card,
    text="CALCULATE CUBE",
    font=("Calibri", 17, "bold"),
    bg=PURPLE,
    fg="white",
    activebackground="#8B5CF6",
    activeforeground="white",
    relief=FLAT,
    width=23, 
    pady=6,
    command=cube
).pack(pady=5)


Button(
    card,
    text="SHOW MULTIPLICATION TABLE",
    font=("Calibri", 17, "bold"),
    bg=GREEN,
    fg=DARK,
    activebackground="#34D399",
    activeforeground=DARK,
    relief=FLAT,
    width=25,
    pady=6,
    command=table
).pack(pady=5)


Button(
    card,
    text="CLEAR",
    font=("Calibri", 17, "bold"),
    bg="#FECACA",
    fg="#991B1B",
    activebackground="#FCA5A5",
    relief=FLAT,
    width=23,
    pady=6,
    command=clear
).pack(pady=5)


# ==============================
# CLOSE APPLICATION BUTTON
# ==============================

Button(
    root,
    text="CLOSE APPLICATION",
    font=("Calibri", 16, "bold"),
    bg="#9C4C4C",
    fg="white",
    activebackground="#702020",
    activeforeground="white",
    relief=FLAT,
    width=23,
    pady=8,
    command=close_application
).pack(pady=8)


# ==============================
# FOOTER
# ==============================

Label(
    root,
    text="Made with Python and Tkinter",
    font=("Calibri", 13, "italic"),
    bg=BG,
    fg=TEXT
).pack(pady=5)


# ==============================
# RUN APPLICATION
# ==============================

root.mainloop()
