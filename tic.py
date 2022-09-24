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


def main():
   pass

print("Welcome to Tic Tac Toe!")    


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


currentPlayer = "X"
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
        board[inp-1] = currentPlayer
    else:
         print("spot taken.")



# check for win or tie
def checkHorizontle(board):
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


#Switch players for now
def switchPlayer():
    global currentPlayer
if  currentPlayer == 'X':
    currentPlayer = 'O'
else:
     currentPlayer = 'X'


def com(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#Allows board to print out
while gameRunning:
    printBoard(board)
    playerInput(board)
