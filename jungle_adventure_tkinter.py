
import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# JUNGLE ADVENTURE - THE LOST FOREST
# ==========================================

root = tk.Tk()
root.title("JUNGLE ADVENTURE - THE LOST FOREST")
root.geometry("900x650")
root.resizable(False, False)
root.configure(bg="#102A1C")

BG = "#102A1C"
CARD = "#1B4332"
GREEN = "#2D6A4F"
GOLD = "#FFD166"
WHITE = "#FFFFFF"
RED = "#E63946"

health = 100
score = 0
inventory = []

# ==========================================
# FUNCTIONS
# ==========================================

def update_stats():
    health_label.config(text=f"❤️ Health: {health}")
    score_label.config(text=f"⭐ Score: {score}")
    inventory_label.config(
        text="🎒 Inventory: " +
        (", ".join(inventory) if inventory else "Empty")
    )


def clear_buttons():
    for widget in choice_frame.winfo_children():
        widget.destroy()


def show_story(title, story, choices):
    clear_buttons()

    title_label.config(text=title)
    story_label.config(text=story)

    for text, function in choices:
        btn = tk.Button(
            choice_frame,
            text=text,
            font=("Arial", 12, "bold"),
            bg=GREEN,
            fg=WHITE,
            activebackground=GOLD,
            activeforeground="black",
            width=35,
            height=2,
            cursor="hand2",
            relief="raised",
            bd=3,
            command=function
        )
        btn.pack(pady=6)


def game_over(reason):
    show_story(
        "GAME OVER 💀",
        reason + "\n\nYour jungle adventure has ended!",
        [("🔄 PLAY AGAIN", restart_game)]
    )


def victory(reason):
    global score

    score += 100
    update_stats()

    show_story(
        "YOU ESCAPED! 🏆",
        reason + "\n\nCongratulations! You survived "
        "the Lost Forest!\n\n"
        f"FINAL SCORE: {score}",
        [("🔄 PLAY AGAIN", restart_game)]
    )


def damage(amount):
    global health
    health -= amount

    if health <= 0:
        health = 0
        update_stats()
        game_over("You ran out of health!")
        return True

    update_stats()
    return False


def add_score(amount):
    global score
    score += amount
    update_stats()


def add_item(item):
    if item not in inventory:
        inventory.append(item)
    update_stats()


# ==========================================
# STORY
# ==========================================

def start_game():
    global health, score, inventory

    health = 100
    score = 0
    inventory = []

    update_stats()

    show_story(
        "🌴 THE LOST FOREST 🌴",

        "You and your friends went on a jungle "
        "adventure during your holidays.\n\n"
        "Everything was going perfectly until "
        "a terrible storm appeared!\n\n"
        "You got separated from your friends "
        "and lost your way.\n\n"
        "Your phone has no network connection.\n"
        "You must find a way out before sunset!\n\n"
        "Suddenly, you notice TWO paths ahead.",

        [
            ("🌿 Take the LEFT path", left_path),
            ("🌳 Take the RIGHT path", right_path)
        ]
    )


# ==========================================
# LEFT PATH
# ==========================================

def left_path():

    add_score(10)

    show_story(
        "🐍 THE GIANT SNAKE",

        "You walk through thick bushes.\n\n"
        "Suddenly, a giant snake appears "
        "near a tree!\n\n"
        "You stop immediately.\n"
        "The snake notices your movement.\n\n"
        "You spot a narrow trail nearby.",

        [
            ("🚶 Slowly move away", snake_escape),
            ("🌿 Hide behind a tree", snake_hide),
            ("🏃 Run towards the trail", snake_run)
        ]
    )


def snake_escape():

    add_score(20)

    show_story(
        "SAFE ESCAPE",

        "You slowly move away without disturbing "
        "the snake.\n\n"
        "After a few minutes, you reach "
        "an open area.\n\n"
        "There are two mysterious gates!",

        [
            ("🚪 Enter Gate ONE", deadly_gate),
            ("🚪 Enter Gate TWO", safe_gate)
        ]
    )


def snake_hide():

    add_score(15)

    show_story(
        "HIDDEN IN THE BUSHES",

        "You hide behind a large tree.\n\n"
        "After some time, the snake disappears "
        "into the forest.\n\n"
        "You notice a small wooden box "
        "near the tree!",

        [
            ("📦 Open the box", treasure_box),
            ("🚶 Continue walking", river_path)
        ]
    )


def snake_run():

    if damage(15):
        return

    show_story(
        "THE NARROW TRAIL",

        "You rush towards the narrow trail.\n\n"
        "You manage to leave the snake behind, "
        "but you accidentally drop your water bottle.\n\n"
        "You find a river nearby.",

        [
            ("🌊 Cross the river", river_path),
            ("🌲 Follow the river", river_follow)
        ]
    )


# ==========================================
# RIGHT PATH
# ==========================================

def right_path():

    add_score(10)

    show_story(
        "🦁 THE SLEEPING LION",

        "You walk quietly through the forest.\n\n"
        "Suddenly, you see a lion sleeping "
        "under a giant tree!\n\n"
        "You also notice a small cave nearby.\n\n"
        "What will you do?",

        [
            ("🤫 Slowly walk away", lion_escape),
            ("🕳️ Explore the cave", cave_path),
            ("🌳 Climb a nearby tree", climb_tree)
        ]
    )


def lion_escape():

    add_score(20)

    show_story(
        "THE FOREST TRAIL",

        "You quietly move away from the area.\n\n"
        "After walking for a while, you discover "
        "an old wooden bridge.\n\n"
        "There is a river below it.",

        [
            ("🌉 Cross the bridge", bridge_path),
            ("🌲 Find another route", temple_path)
        ]
    )


def cave_path():

    show_story(
        "🕳️ THE MYSTERIOUS CAVE",

        "You enter the dark cave.\n\n"
        "You hear strange sounds coming "
        "from deep inside.\n\n"
        "There are two tunnels.\n\n"
        "One has a strange blue light.\n"
        "The other has a warm golden light.",

        [
            ("🔵 Enter blue tunnel", blue_tunnel),
            ("🟡 Enter golden tunnel", golden_tunnel),
            ("🚶 Leave the cave", lion_escape)
        ]
    )


def climb_tree():

    add_score(15)

    show_story(
        "🌳 THE VIEW FROM ABOVE",

        "You carefully climb a tall tree.\n\n"
        "From above, you can see the entire forest!\n\n"
        "You notice an ancient temple "
        "in the distance.\n\n"
        "You also spot a river.",

        [
            ("🏛️ Go towards the temple", temple_path),
            ("🌊 Go towards the river", river_path)
        ]
    )


# ==========================================
# TREASURE AND CAVE
# ==========================================

def treasure_box():

    add_item("Golden Key")
    add_score(30)

    show_story(
        "💰 HIDDEN TREASURE",

        "You open the old wooden box.\n\n"
        "WOW! There is a GOLDEN KEY inside!\n\n"
        "You put it safely in your backpack.\n\n"
        "Maybe it will unlock something important!",

        [
            ("🌊 Continue to the river", river_path),
            ("🏛️ Search for an ancient temple", temple_path)
        ]
    )


def blue_tunnel():

    show_story(
        "🔵 THE BLUE TUNNEL",

        "You enter the blue tunnel.\n\n"
        "The walls are glowing with strange blue stones.\n\n"
        "At the end, you discover a beautiful "
        "underground lake.\n\n"
        "A small boat is waiting there!",

        [
            ("🚣 Take the boat", boat_path),
            ("↩️ Return to the cave", cave_path)
        ]
    )


def golden_tunnel():

    add_score(25)

    show_story(
        "🟡 THE GOLDEN TUNNEL",

        "You walk through the golden tunnel.\n\n"
        "You discover an old treasure chamber!\n\n"
        "There is a mysterious golden key "
        "on a table.",

        [
            ("🔑 Take the golden key", get_key),
            ("🚶 Leave the chamber", temple_path)
        ]
    )


def get_key():

    add_item("Golden Key")
    add_score(30)

    show_story(
        "KEY COLLECTED!",

        "You picked up the golden key.\n\n"
        "There might be a locked door "
        "somewhere in this jungle.",

        [
            ("🏛️ Visit the ancient temple", temple_path),
            ("🌊 Go to the river", river_path)
        ]
    )


# ==========================================
# RIVER AND BRIDGE
# ==========================================

def river_path():

    show_story(
        "🌊 THE DEEP RIVER",

        "You reach a beautiful river.\n\n"
        "The water is flowing quickly.\n\n"
        "You see a wooden boat on the riverbank.\n"
        "There are also some stepping stones.\n\n"
        "How will you continue?",

        [
            ("🚣 Use the boat", boat_path),
            ("🪨 Cross using the stones", stone_path),
            ("🌲 Follow the riverbank", river_follow)
        ]
    )


def river_follow():

    show_story(
        "🌴 RIVERBANK",

        "You follow the riverbank.\n\n"
        "After walking for some time, "
        "you discover an ancient temple.\n\n"
        "Its entrance looks mysterious!",

        [
            ("🏛️ Enter the temple", temple_path),
            ("🌉 Find the wooden bridge", bridge_path)
        ]
    )


def boat_path():

    add_score(20)

    show_story(
        "🚣 THE OLD BOAT",

        "You get into the boat.\n\n"
        "You slowly travel across the river.\n\n"
        "Suddenly, you notice a small island "
        "in the middle of the river!\n\n"
        "There is a strange chest on it.",

        [
            ("🏝️ Visit the island", island_path),
            ("➡️ Continue across the river", temple_path)
        ]
    )


def stone_path():

    if damage(10):
        return

    add_score(15)

    show_story(
        "🪨 THE STEPPING STONES",

        "You carefully make your way "
        "across the stones.\n\n"
        "You reach the other side safely!\n\n"
        "There is an old temple nearby.",

        [
            ("🏛️ Explore the temple", temple_path),
            ("🌳 Explore the forest", forest_path)
        ]
    )


def bridge_path():

    add_score(15)

    show_story(
        "🌉 THE OLD BRIDGE",

        "You approach the wooden bridge.\n\n"
        "It looks old, but there is a path "
        "leading to the other side.\n\n"
        "You carefully cross it.\n\n"
        "You find an ancient temple!",

        [
            ("🏛️ Enter the temple", temple_path),
            ("🌲 Explore another trail", forest_path)
        ]
    )


# ==========================================
# ISLAND AND FOREST
# ==========================================

def island_path():

    add_score(25)

    show_story(
        "🏝️ THE MYSTERIOUS ISLAND",

        "You step onto the island.\n\n"
        "You discover a treasure chest "
        "covered in leaves.\n\n"
        "There is a strange symbol on it.\n\n"
        "You notice a keyhole!",

        [
            ("🔑 Try your golden key", open_chest),
            ("🚣 Return to the river", temple_path)
        ]
    )


def open_chest():

    if "Golden Key" in inventory:

        add_item("Ancient Treasure")
        add_score(50)

        show_story(
            "💎 ANCIENT TREASURE",

            "Your golden key fits perfectly!\n\n"
            "The chest opens.\n\n"
            "Inside, you discover an ancient "
            "treasure and a map!\n\n"
            "The map shows the way out "
            "of the jungle!",

            [
                ("🗺️ Follow the map", forest_path)
            ]
        )

    else:

        show_story(
            "🔒 LOCKED CHEST",

            "The chest is locked.\n\n"
            "You need a golden key to open it!\n\n"
            "Maybe you can find one in the cave "
            "or the wooden box.",

            [
                ("🚣 Return to the river", temple_path)
            ]
        )


def forest_path():

    add_score(20)

    show_story(
        "🌳 THE DEEP FOREST",

        "You enter a part of the jungle "
        "that looks completely different.\n\n"
        "You see colourful birds and "
        "strange plants everywhere.\n\n"
        "Suddenly, you discover a small "
        "wooden sign.\n\n"
        "It says: EXIT - 2 KM!",

        [
            ("➡️ Follow the EXIT sign", exit_path),
            ("🏛️ Explore the nearby temple", temple_path)
        ]
    )


# ==========================================
# ANCIENT TEMPLE
# ==========================================

def temple_path():

    show_story(
        "🏛️ THE ANCIENT TEMPLE",

        "You finally reach an ancient temple.\n\n"
        "Its walls are covered with mysterious "
        "symbols and paintings.\n\n"
        "At the entrance, you find a locked door.\n\n"
        "There is also a narrow opening "
        "on the side.",

        [
            ("🔑 Try the golden key", temple_door),
            ("🚪 Enter through the opening", secret_room),
            ("🌲 Leave the temple", forest_path)
        ]
    )


def temple_door():

    if "Golden Key" in inventory:

        add_score(40)

        show_story(
            "🔓 THE SECRET DOOR",

            "The golden key fits into the lock!\n\n"
            "The ancient door slowly opens.\n\n"
            "You discover a secret room "
            "filled with old maps.\n\n"
            "One map shows the exit!",

            [
                ("🗺️ Follow the exit map", exit_path)
            ]
        )

    else:

        show_story(
            "🔒 LOCKED DOOR",

            "The door does not open.\n\n"
            "You need a golden key!\n\n"
            "Search the jungle for one.",

            [
                ("🌲 Explore the forest", forest_path),
                ("🕳️ Search for a cave", cave_path)
            ]
        )


def secret_room():

    if damage(10):
        return

    add_score(30)

    show_story(
        "🗝️ THE SECRET ROOM",

        "You carefully enter through the opening.\n\n"
        "Inside, you discover an old notebook.\n\n"
        "It contains directions to the "
        "nearest jungle exit!\n\n"
        "You are getting closer to freedom!",

        [
            ("📖 Follow the directions", exit_path)
        ]
    )


# ==========================================
# FINAL ESCAPE
# ==========================================

def exit_path():

    show_story(
        "🚪 THE FINAL EXIT",

        "You follow the directions.\n\n"
        "After walking for a long time, "
        "you finally see sunlight!\n\n"
        "There is a large wooden gate ahead.\n\n"
        "You can hear people talking "
        "outside the jungle.\n\n"
        "THIS IS YOUR LAST CHANCE!",

        [
            ("🚪 Open the gate", final_escape),
            ("🔍 Search the nearby area", final_search)
        ]
    )


def final_search():

    add_score(20)

    show_story(
        "🎒 ONE LAST DISCOVERY",

        "You search the nearby area.\n\n"
        "You find an old backpack "
        "with some supplies inside.\n\n"
        "You also discover a small note:\n\n"
        "'Congratulations! You found the exit.'",

        [
            ("🚪 Open the gate", final_escape)
        ]
    )


def safe_gate():

    add_score(50)

    victory(
        "You chose the correct gate!\n"
        "You followed the trail and found "
        "the jungle exit."
    )


def deadly_gate():

    game_over(
        "You entered the wrong gate "
        "and became lost in the forest."
    )


def final_escape():

    victory(
        "You opened the wooden gate "
        "and finally escaped!\n\n"
        "Your friends were waiting outside.\n"
        "You will never forget this adventure!"
    )


def restart_game():
    start_game()


# ==========================================
# GUI DESIGN
# ==========================================

header = tk.Label(
    root,
    text="🌴 JUNGLE ADVENTURE 🌴",
    font=("Arial", 27, "bold"),
    bg=BG,
    fg=GOLD
)
header.pack(pady=15)

subtitle = tk.Label(
    root,
    text="THE LOST FOREST",
    font=("Arial", 13, "bold"),
    bg=BG,
    fg="#95D5B2"
)
subtitle.pack()

stats_frame = tk.Frame(root, bg=CARD)
stats_frame.pack(fill="x", padx=25, pady=15)

health_label = tk.Label(
    stats_frame,
    text="❤️ Health: 100",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=WHITE
)
health_label.pack(side="left", padx=20, pady=12)

score_label = tk.Label(
    stats_frame,
    text="⭐ Score: 0",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=GOLD
)
score_label.pack(side="left", padx=20)

inventory_label = tk.Label(
    stats_frame,
    text="🎒 Inventory: Empty",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=WHITE
)
inventory_label.pack(side="right", padx=20)

story_frame = tk.Frame(
    root,
    bg=CARD,
    bd=3,
    relief="ridge"
)
story_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=10
)

title_label = tk.Label(
    story_frame,
    text="",
    font=("Arial", 20, "bold"),
    bg=CARD,
    fg=GOLD
)
title_label.pack(pady=20)

story_label = tk.Label(
    story_frame,
    text="",
    font=("Arial", 12),
    bg=CARD,
    fg=WHITE,
    justify="center",
    wraplength=760
)
story_label.pack(padx=25, pady=15)

choice_frame = tk.Frame(root, bg=BG)
choice_frame.pack(pady=15)

footer = tk.Label(
    root,
    text="Explore wisely. Every choice changes your adventure!",
    font=("Arial", 10, "italic"),
    bg=BG,
    fg="#95D5B2"
)
footer.pack(pady=8)

# ==========================================
# START GAME
# ==========================================

start_game()

root.mainloop()
