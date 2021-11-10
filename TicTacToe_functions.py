from IPython.display import clear_output
import random



def display_board(board):
    clear_output() #Clearing the output every time the function is called
    print("                 ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("-----|-----|-----")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("-----|-----|-----")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print("                 ")


def player_input():
    markers = ["X", "O"]
    marker = "wrong"

    while marker not in markers:
        marker = input("Would you like to X or O ?").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[int(position)] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # horizontal middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # vertical left
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # vertical middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # vertical right
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))    # diagonal


def choose_first():
    #randomly deciding wich player goes first
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    #this will be used inside another function
    return board[int(position)] == " "

def player_choice(board):
    position = "0"
    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while position not in positions or space_check(board, position) == False:
        position = input("Where would you like to place your mark next?")

    return position


def full_board_check(board):
    #Checking if there's any space on the board
    if " " in board:
        return False
    else:
        return True


def replay():
    choice = "wrong"
    choices = ["YES", "NO"]
    while choice not in choices:
        choice = input("Would you like to play again?").upper()

    if choice == "YES":
        return True
    else:
        return False













