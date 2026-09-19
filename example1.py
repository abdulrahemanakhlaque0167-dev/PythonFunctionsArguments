
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


