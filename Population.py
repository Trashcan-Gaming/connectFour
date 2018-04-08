from Chromosone import Chromosone as c
import numpy as np
import operator
import random as r
import math

class Population:
    def __init__(self, pop):
        self.populationSize = pop
        self.chromosones = []
        self.mutationRate = 2
        self.mutationWeight = 0.4
        self.curChromosone = 0
        self.hallOfFameSize = 4

        for i in range(self.populationSize):
            self.chromosones.append(c(True))

    def comp(greater_than):
        def compare(x, y):
            if greater_than(x.getFitness(), y.getFitness()):
                return 1
            elif greater_than(y.getFitness, x.getFitness):
                return -1
            else:
                return 0

        return compare

    def train(self):
        sorted_chromosomes = sorted(self.chromosones, key=operator.attrgetter('fitness'))
        nextGen = []

        for i in range(self.hallOfFameSize):
            nextGen.append(sorted_chromosomes.pop())

        for i in range(int(self.populationSize-self.hallOfFameSize)):
            for j in range(math.ceil((self.populationSize-self.hallOfFameSize)/2)):
                crossoverChromosone = self.crossover(nextGen[j%self.hallOfFameSize],
                                                nextGen[i%self.hallOfFameSize])
                mutateChromosone = self.mutate(crossoverChromosone)
                nextGen.append(mutateChromosone)

        self.chromosones = nextGen

    def crossover(self, c1, c2):
        output = c(True)
        outputIHWeights = np.zeros((c.noInputs,c.noHidden))
        outputHOWeights = np.zeros((c.noHidden,c.noOutput))

        #crossover weights for input to hidden
        for i in range(c.noInputs):
            for j in range(c.noHidden):
                if (r.randint(0,4) % 2 == 0 ):
                    outputIHWeights[i][j] = c1.IHWeights[i][j]
                else:
                    outputIHWeights[i][j] = c2.IHWeights[i][j]

            # crossover weights for hidden to output
            for i in range(c.noHidden):
                for j in range(c.noOutput):
                    if (r.randint(0, 4) % 2 == 0):
                        outputHOWeights[i][j] = c1.HOWeights[i][j]
                    else:
                        outputHOWeights[i][j] = c2.HOWeights[i][j]


        output.setIHWeights(outputIHWeights)
        output.setHOWeights(outputHOWeights)

        return output

    def mutate(self, cChromosone):
        mutateWeight = 0.0

        for i in range(c.noInputs):
            for j in range(c.noHidden):
                if(r.randint(0, self.populationSize)% self.mutationRate == 0):
                    if(r.randint(1,4) % 2 == 0):
                        mutateWeight = cChromosone.IHWeights[i][j]+ r.random() * r.randint(0,self.mutationRate)
                    else:
                        mutateWeight = cChromosone.IHWeights[i][j] + r.random() * r.randint(0,self.mutationRate)

                cChromosone.IHWeights[i][j] = mutateWeight

        for i in range(c.noHidden):
            for j in range(c.noOutput):
                if (r.randint(0, self.populationSize) % self.mutationRate == 0):
                    if (r.randint(1, 4) % 2 == 0):
                        mutateWeight = cChromosone.HOWeights[i][j] + r.random() * r.randint(0, self.mutationRate)
                    else:
                        mutateWeight = cChromosone.HOWeights[i][j] + r.random() * r.randint(0, self.mutationRate)

                cChromosone.HOWeights[i][j] = mutateWeight

        return cChromosone

    def incrementCurChromosone(self):
        if(self.curChromosone < self.populationSize-2):
            self.curChromosone = self.curChromosone+1
        else:
            self.curChromosone=0

    def getCurChromosone(self):
        return self.chromosones[self.curChromosone]

    #implement save here