import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# Snake body
segments = []

# Score
score = 0
high_score = 0

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0",
                    align="center",
                    font=("Arial", 18, "normal"))


# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    elif head.direction == "down":
        head.sety(y - 20)

    elif head.direction == "left":
        head.setx(x - 20)

    elif head.direction == "right":
        head.setx(x + 20)


# Keyboard controls
screen.listen()

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")


# Main game loop
while True:

    screen.update()

    # Wall collision
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):

        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0

        score_display.clear()
        score_display.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    # Food collision
    if head.distance(food) < 20:

        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()

        segments.append(new_segment)

        score += 1

        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0

            score_display.clear()
            score_display.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Arial", 18, "normal")
            )

    time.sleep(0.1)

screen.mainloop()


'''
import random

# ==========================================
#          TIC-TAC-TOE GAME
# ==========================================

board = [" " for i in range(9)]

print("================================")
print("       TIC-TAC-TOE GAME")
print("================================")

print("1. Single Player")
print("2. Two Players")

mode = input("Choose mode (1 or 2): ")

# ------------------------------------------
# DISPLAY BOARD
# ------------------------------------------

def show_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# ------------------------------------------
# CHECK WIN
# ------------------------------------------

def check_win(player):

    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:

        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):

            return True

    return False


# ------------------------------------------
# CHECK DRAW
# ------------------------------------------

def board_full():

    for space in board:

        if space == " ":
            return False

    return True


# ------------------------------------------
# COMPUTER MOVE
# ------------------------------------------

def computer_move():

    empty_spaces = []

    for i in range(9):

        if board[i] == " ":
            empty_spaces.append(i)

    if empty_spaces:

        move = random.choice(empty_spaces)

        board[move] = "O"

        print("Computer chose position", move + 1)


# ------------------------------------------
# SINGLE PLAYER
# ------------------------------------------

if mode == "1":

    print("\nYou are X")
    print("Computer is O")

    while True:

        # Player turn
        show_board()

        print("Your turn!")

        try:
            position = int(input("Choose a position (1-9): "))
            position = position - 1

            if position < 0 or position > 8:
                print("Choose a number from 1 to 9!")
                continue

            if board[position] != " ":
                print("That position is already taken!")
                continue

            board[position] = "X"

        except ValueError:
            print("Please enter a number!")
            continue

        # Player wins
        if check_win("X"):

            show_board()
            print("🎉 YOU WIN!")
            break

        # Draw
        if board_full():

            show_board()
            print("🤝 IT'S A DRAW!")
            break

        # Computer turn
        computer_move()

        # Computer wins
        if check_win("O"):

            show_board()
            print("💻 COMPUTER WINS!")
            break

        # Draw
        if board_full():

            show_board()
            print("🤝 IT'S A DRAW!")
            break


# ------------------------------------------
# TWO PLAYER
# ------------------------------------------

elif mode == "2":

    print("\nPlayer 1 = X")
    print("Player 2 = O")

    current_player = "X"

    while True:

        show_board()

        print("Player", current_player, "turn")

        try:
            position = int(input("Choose a position (1-9): "))
            position = position - 1

            if position < 0 or position > 8:
                print("Choose a number from 1 to 9!")
                continue

            if board[position] != " ":
                print("That position is already taken!")
                continue

            board[position] = current_player

        except ValueError:
            print("Please enter a number!")
            continue

        # Check winner
        if check_win(current_player):

            show_board()
            print("🎉 Player", current_player, "WINS!")
            break

        # Check draw
        if board_full():

            show_board()
            print("🤝 IT'S A DRAW!")
            break

        # Change player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

else:

    print("Invalid choice!")
'''

