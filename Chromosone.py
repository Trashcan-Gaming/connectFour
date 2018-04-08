import numpy as np
import random as r



class Chromosone:
    noInputs = 85
    noHidden = 20
    noOutput = 6

    def __init__(self):
        self.fitness = 0
        self.IHWeights = np.zeros((self.noInputs, self.noHidden))
        self.HOWeights = np.zeros((self.noHidden,self.noOutput))

    def __init__(self, firstRun):
        if firstRun:
            self.fitness = 0
            self.IHWeights = np.zeros((self.noInputs, self.noHidden))
            self.HOWeights = np.zeros((self.noHidden, self.noOutput))

            for i in range(self.noInputs):
                for j in range(self.noHidden):
                    self.IHWeights[i][j] = self.random()

            for i in range(self.noHidden):
                for j in range(self.noOutput):
                    self.IHWeights[i][j] = self.random()

    def getFitness(self):
        return self.fitness

    def getBoardUtility(self, board, player):
        p = player +1
        twoInARow = 0
        threeInARow = 0
        rowCount = 1
        columnCount = 1
        prevPos = (-1,-1)

        # Check for horizontal wins
        for c in range(np.size(board, axis=1)):
            for r in range(np.size(board, axis=0)):
                if board[r][c] == p and prevPos != (-1,-1):
                    if board[prevPos[0]][prevPos[1]] == p:
                        rowCount = rowCount + 1
                        prevPos = (r,c)
                    else:
                        if rowCount == 2:
                            twoInARow = twoInARow + 1
                        elif rowCount == 3:
                            threeInARow = threeInARow + 1
                        rowCount = 1
                        prevPos = (r, c)
                else:
                    if rowCount == 2:
                        twoInARow = twoInARow + 1
                    elif rowCount == 3:
                        threeInARow = threeInARow + 1
                    rowCount = 1
                    prevPos = (r,c)

            prevPos = (-1, -1)
            # Check for Vertical wins
            for r in range(np.size(board, axis=0)):
                for c in range(np.size(board, axis=1)):
                    if board[r][c] == p and prevPos != (-1, -1):
                        if board[prevPos[0]][prevPos[1]] == p:
                            columnCount = columnCount + 1
                            prevPos = (r, c)
                        else:
                            if columnCount == 2:
                                twoInARow = twoInARow + 1
                            elif columnCount == 3:
                                threeInARow = threeInARow + 1
                            columnCount = 1
                            prevPos = (r, c)
                    else:
                        if columnCount == 2:
                            twoInARow = twoInARow + 1
                        elif columnCount == 3:
                            threeInARow = threeInARow + 1
                        columnCount = 1
                        prevPos = (r, c)

                #add diagonal later
        return twoInARow * 2 + threeInARow * 6 + 1


    def setFitness(self, endGame, board, player):
        x = self.getBoardUtility(board,player)
        if endGame == 1:
            self.fitness = 2*x
        elif endGame == 0:
            self.fitness = x
        elif endGame == -1:
            self.fitness = 0.5*x
        else:
            self.fitness = 0


    def random(self):
        return r.random()*1/self.noInputs

    def getIHWeights(self):
        return self.IHWeights

    def getHOWeights(self):
        return self.HOWeights

    def setIHWeights(self, IHWeights_new):
        self.IHWeights = IHWeights_new

    def setHOWeights(self, HOWeights_new):
        self.HOWeights = HOWeights_new