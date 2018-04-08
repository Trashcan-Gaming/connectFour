from ConnectFourTraining import ConnectFourTraining as CT
from NeuralNetwork import NeuralNetwork as NN
from Population import Population
import numpy as np

pop1 = Population(20)
pop2 = Population(20)

curChromosone1 = 0
curChromosone2 = 0
iterationCounter = 0

while True:
    curChromosone1 = pop1.chromosones[pop1.curChromosone]
    curChromosone2 = pop2.chromosones[pop2.curChromosone]
    NN1 = NN()
    NN2 = NN()

    game = CT()
    game_over = False
    score1=0
    score2=0

    while not game_over:
        if(iterationCounter % 20 == 0):
            print(score1)
            print(score2)
            game.print_board(game.board)


        NN1.setWeightsOfNN(curChromosone1.IHWeights, curChromosone1.HOWeights)
        NN2.setWeightsOfNN(curChromosone2.IHWeights, curChromosone2.HOWeights)

        inputs1 = game.getGameState(game.board, game.turn, 0)
        inputs2 = game.getGameState(game.board, game.turn, 1)

        move1 = NN1.getNextMove(inputs1, game.board)
        move2 = NN2.getNextMove(inputs2, game.board)

        #move
        # Get player 1 input
        if game.turn == 0:
            col = move1
            if game.isValidLocation(game.board, col):
                game.makeMove(game.board, col, game.turn)
            else:
                game.makeMove(game.board, col, game.turn)

            if game.checkWin(game.board, 1):
                score1 = score1+1
                game.endGame = 1
                game_over = True
            elif game.checkDraw(game.board):
                game.endGame = 0
                game_over = True

            game.turn = 1

        # Get player 2 input
        else:
            col = move2
            if game.isValidLocation(game.board, col):
                game.makeMove(game.board, col, game.turn)

            if game.checkWin(game.board, 2):
                score2 = score2 +1
                game.endGame = 2
                game_over = True
            elif game.checkDraw(game.board):
                game.endGame = 0
                game_over = True

            game.turn = 0


    #set fitness endGame, board, player
    if game.endGame == 1:
        curChromosone1.setFitness(1, game.board, 0)
        curChromosone2.setFitness(-1, game.board, 1)
    elif game.endGame == 2:
        curChromosone1.setFitness(-1, game.board, 0)
        curChromosone2.setFitness(1,  game.board, 1)
    elif game.endGame == 0:
        curChromosone1.setFitness(0, game.board, 0)
        curChromosone2.setFitness(0, game.board, 1)

    iterationCounter = iterationCounter +1

    if(iterationCounter % pop1.populationSize == 0):
        pop1.train()
    if(iterationCounter % pop2.populationSize == 0):
        pop2.train()

    pop1.incrementCurChromosone()
    pop2.incrementCurChromosone()

    game = CT()
