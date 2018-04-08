import numpy as np
import sys
import math
import pygame

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
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if (board[r][c+3] == player and board[r + 1][c + 2] == player and board[r + 2][c + 1] == player and board[r + 3][c] == player):
                return True

def checkDraw(board):
    return board.all()

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE,  SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()

# Game related variables
ROW_COUNT = 6
COLUMN_COUNT = 7
turn = 0
player1 = 0
player2 = 1
board = create_board()
game_over = False

# Colours for pygame.draw
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialise game
pygame.init()



# Draw board
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)

#Initialise placer
posx = width/2
speed = 100

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and posx >50:
                posx -= speed
                if turn == player1:
                    pygame.draw.circle(screen, RED, (int(posx), int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (int(posx), int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()

            if event.key == pygame.K_d and posx <width - 50:
                posx += speed
                if turn == player1:
                    pygame.draw.circle(screen, RED, (int(posx), int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (int(posx), int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Get player 1 input
                if turn == player1:
                    #posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if isValidLocation(board, col):
                        makeMove(board, col, turn)

                    if checkWin(board, 1):
                        pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                        pygame.display.update()
                        label = myfont.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

                    printBoard(board)
                    draw_board(board)
                    turn = player2

            # Get player 2 input
                else:
                    #posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if isValidLocation(board, col):
                        makeMove(board, col, turn)

                    if checkWin(board, 2):
                        pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                        pygame.display.update()
                        label = myfont.render("Player 2 wins!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

                    if checkDraw(board):
                        pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                        pygame.display.update()
                        label = myfont.render("It's a draw", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

                    printBoard(board)
                    draw_board(board)
                    turn = player1

            if game_over:
                pygame.time.wait(3000)
