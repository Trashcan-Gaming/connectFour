import numpy as np
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def print_board(board):
	print(np.flip(board, 0))

def checkInput(selection):
    for i in selection:
        if i != 'd' and i != 'a':
            print("please input d for right and a for left")
            return False
    return True

def checkInputLength(selection):
    x = inputToNumber(selection)
    if (x<0 or x>ROW_COUNT):
        print("d = +1 right, a = -1 left")
        return False
    return True


def inputToNumber(selection):
    result = 0;
    for i in selection:
        if i == 'a':
            result = result-1
        if i == 'd':
            result = result+1
    return result;

def getInput(turn):
    print("right is +1, left is -1, you start at 0")
    inputValid = False

    while not inputValid:
        selection = input("Player " + str(turn + 1) + " make your input 0-" + str(COLUMN_COUNT-1) + ":")
        if checkInput(selection) == False:
            continue
        elif checkInputLength(selection) == False:
            continue
        inputValid = True
    result = inputToNumber(selection)

    return result

def isValidLocation(board, col):
    return board[ROW_COUNT-1][col] == 0

def dropPiece(board, row, col, turn):
    board[row][col] = turn+1;

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col]== 0:
            return r

def makeMove(board, col, turn):
    row = getNextOpenRow(board,col)
    dropPiece(board, row, col, turn)

def printBoard(board):
    print(np.flip(board,0))

def checkWin(board, turn):
    player = turn

    # Check for horizontal wins
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if (board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player):
                return True

    # Check for vertical wins
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if (board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player):
                return True

    # Positive slope diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if (board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player):
                return True

    # Negative slope diagonals
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if (board[r][c] == player and board[r - 1][c + 1] == player and board[r - 2][c + 2] == player and
                        board[r - 3][c + 3] == player):
                return True


turn = 0
player1 = 0
player2 = 1
board = create_board()
game_over = False

while not game_over:
    #Get player 1 input
    if turn == player1:
        col = getInput(turn)

        if isValidLocation(board, col):
            makeMove(board, col, turn)

        if checkWin(board, 1):
            print("You win!!!")
            game_over = True

        printBoard(board)
        turn = player2
        
    #Get player 2 input
    else:
        col = getInput(turn)

        if isValidLocation(board, col):
            makeMove(board, col, turn)

        if checkWin(board, 2):
            print("You win!!!")
            game_over = True

        printBoard(board)
        turn = player1
