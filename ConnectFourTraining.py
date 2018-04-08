

import numpy as np
import sys
import math

# Game related variables
ROW_COUNT = 6
COLUMN_COUNT = 7
turn = 0
player1 = 0
player2 = 1


class ConnectFourTraining:

    def __init__(self):
        self.board = self.create_board()
        self.game_over = False
        self.turn = 0
        self.endGame = 0

    def setBoard(self,board):
        self.board = board

    def create_board(self):
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def print_board(self,board):
        print(np.flip(board, 0))

    def checkInput(self,selection):
        for i in selection:
            if i != 'd' and i != 'a':
                print("please input d for right and a for left")
                return False
        return True


    def isValidLocation(self,board, col):
        return board[ROW_COUNT - 1][col] == 0

    def dropPiece(self,board, row, col, turn):
        board[row][col] = turn + 1;

    def getNextOpenRow(self,board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def makeMove(self, board, col, turn):
        row = self.getNextOpenRow(board, col)
        self.dropPiece(board, row, col, turn)

    def printBoard(self, board):
        print(np.flip(board, 0))

    def checkWin(self,board, turn):
        player = turn

    def checkDraw(self,board):
        return self.board.all()


    def checkWin(self, board, turn):
        player = turn

        # Check for horizontal wins
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if (board[r][c] == player and board[r][c + 1] == player and board[r][c + 2] == player and board[r][
                        c + 3] == player):
                    return True

        # Check for vertical wins
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if (board[r][c] == player and board[r + 1][c] == player and board[r + 2][c] == player and board[r + 3][
                    c] == player):
                    return True

        # Positive slope diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (board[r][c] == player and board[r + 1][c + 1] == player and board[r + 2][c + 2] == player and
                            board[r + 3][c + 3] == player):
                    return True

        # Negative slope diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (board[r][c + 3] == player and board[r + 1][c + 2] == player and board[r + 2][c + 1] == player and
                            board[r + 3][c] == player):
                    return True

    def getGameState(self, board, turn, player):
        output = []

        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                if board[r][c] == 1:
                    output.append(1)
                else:
                    output.append(0)
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                if board[r][c] == 2:
                    output.append(1)
                else:
                    output.append(0)

        if turn == player:
            output.append(1)
        else:
            output.append(0)

        return output

    def playGame(self):
       while not game_over:

                # Get player 1 input
                if turn == player1:
                    col = self.getInputFromNN(self.getGameState(self.board, self.turn, player1))
                    if self.isValidLocation(self.board, col):
                        self.makeMove(self.board, col, turn)

                    if self.checkWin(self.board, 1):
                        print("Player 1 wins")
                        game_over = True

                    turn = player2

                # Get player 2 input
                else:
                    col = self.getInputFromNN(self.getGameState(self.board, self.turn, player2))
                    if self.isValidLocation(self.board, col):
                        self.makeMove(self.board, col, turn)

                    if self.checkWin(self.board, 2):
                        print("Player 2 wins")
                        game_over = True
                    self.printBoard(self.board)

                    turn = player1

