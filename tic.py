'''
Tic-Tac-Toe:
Author: Brittany Ridley
'''

#The program must have a comment with assignment and author names. Done
#The program must have at least one if/then block.
#The program must have at least one while loop.
#The program must have more than one function.
#The program must have a function called main.

import random

#If I write pass the def main allows my code to run. 
def main():
    pass

print("Welcome to Tic Tac Toe!")    


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

Player = "X"
winner = None 
gameRunning = True

     
#Print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input 
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = Player
    else:
         print("spot taken.")


def place_marker(board, marker, position):
    board[position] = marker



# win or tie
def checkHor(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def IfWin(board):
    global gameRunning
    if checkHor(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

def IfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


#next players for now
def nextPlayer():
    global Player
    if Player == "X":
        Player = "O"
    else:
        Player= "X"

def game(board):
    while Player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            nextPlayer()



#Allows board to print out
while gameRunning:
    printBoard(board)
    playerInput(board)
    IfWin(board)
    IfTie(board)
    nextPlayer()
    game(board)
    IfWin(board)
    IfTie(board)
 

    

if __name__ == "__main__":
    main()