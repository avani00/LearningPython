import random
from IPython.display import clear_output

#Functions
def display_board(board):
    clear_output()
    print("     |     |")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  ")
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  ")
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  ")
    print("     |     |")
    
def player_input():
    while True:
        marker = input("Player 1. Do you want 'X' or 'O'? Enter 'X' or 'O': ")
        if marker == 'X' or marker == 'O':
            break
    return marker

def choose_first():
    num = random.randint(1,2)
    if num == 1:
        return "Player 1 goes first"
    else:
        return "Player 2 goes first"
    
def place_marker(board, marker, position):
    board[position] = marker
    
def space_check(board, position):
    return board[position] in ["1","2","3","4","5","6","7","8","9"]
    
def player_choice(board, player):
    position = input(f"{player} what position do you want to play? (pick a number between 1 and 9): ")
    while True:
        if position in ["1","2","3","4","5","6","7","8","9"]:
            while space_check(board, int(position)) == False:
                position = input("That position is taken. Pick again. (pick a number between 1 and 9): ")
            return int(position)
        else:
            position = input(f"Not Valid. {player} what position do you want to play? (pick a number between 1 and 9): ")
        
    
def win_check(board, mark):
    if board[1] == board [2] == board [3] == mark:
        return True
    elif board[4] == board [5] == board [6] == mark:
        return True
    elif board[7] == board [8] == board [9] == mark:
        return True
    elif board[1] == board[4] == board [7] == mark:
        return True
    elif board[2] == board [5] == board [8] == mark:
        return True
    elif board[3] == board [6] == board [9] == mark:
        return True
    elif board[1] == board [5] == board [9] == mark:
        return True
    elif board[3] == board [5] == board [7] == mark:
        return True
    else:
        return False

def replay():
    playagain = input("Do you want to play again? (Type 'Yes' or 'No'): ")
    return playagain.lower() == "yes"

def full_board_check(board):
    for value in board:
        if value in ["1","2","3","4","5","6","7","8","9"]:
            return False
    return True

print('Welcome to Tic Tac Toe!')
while True:
    #Set the game up here
    #Make Board
    board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    display_board(board)
    #Choose the marker
    player1_marker = player_input()
    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
    #Choose who goes first
    first_player = choose_first()
    print(first_player)
    while True:
        if first_player == "Player 1 goes first":
            #Player 1 Turn
            #Get spot 
            player1_position = player_choice(board, "Player 1")
            #Place the marker
            place_marker(board, player1_marker, player1_position)
            #Show Board
            display_board(board)
            #Check for Win
            if win_check(board, player1_marker) == True:
                print("Player 1 won!")
                break
            if full_board_check(board) == True:
                print("BOARD'S FULL! IT'S A TIE!")
                break
            first_player = "Player 2 goes first"
        else:
            #Player2's turn.
            #Get spot 
            player2_position = player_choice(board, "Player 2")
            #Place the marker
            place_marker(board, player2_marker, player2_position)
            #Show Board
            display_board(board)
            #Check for Win
            if win_check(board, player2_marker) == True:
                print("Player 2 won!")
                break
            if full_board_check(board) == True:
                print("BOARD'S FULL! IT'S A TIE!")
                break
            first_player = "Player 1 goes first"
    if not replay():
        break