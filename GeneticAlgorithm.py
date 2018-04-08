import numpy as np

# We have the 7*6 inputs for the board
#MAX is the person playing
#MIN is the oppenent
#0 to 41 -[(0,0),(0,1)...(1,0),(1,1)...(7,6)] (1 for MAX's block) (0 otherwise)
#42 to 84-[(0,0),(0,1)...(1,0),(1,1)...(7,6)] (1 for MIN's block) (0 otherwise)
#85 - 1 or 0 (1 for MAX and 0 for MIN)

row = 6
column = 7
turn = 0
player1 = 0
player2 = 1

board = np.ones((row,column))



