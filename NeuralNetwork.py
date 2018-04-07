from Chromosone import Chromosone as c
from StoredNetClass import StoredNetClass as snc
import numpy as np
import random as r
import math

class NeuralNetwork:


    def __init__(self):
        self.IHWeights = np.zeros(c.noInputs,c.noHidden)
        self.HOWeights = np.zeros(c.noHidden,c.noInputs)

    def setWeightsOfNN(self, inputIHWeights, inputHOWeights):
        self.IHWeights = inputIHWeights
        self.HOWeights = inputHOWeights

    def getNextMove(self, inputs):
        highestActual = 0
        toOutput = 0

        for i in range(c.noOutput):
            actual = self.calculateHiddenAndOutput(inputs).storedOutputNets[i]
            if(actual> highestActual):
                highestActual = actual
                toOutput = i

        return toOutput

    def setWeightsOfNN(self):
        #Give initial weights of NN

        for i in range(c.noInputs):
            for j in range(c.noHidden):
                self.IHWeights[i][j] = self.randomDouble()

        for i in range(c.noHidden):
            for j in range(c.noOutput):
                self.HOWeights[i][j] = self.randomDouble()

    def calculateHiddenAndOuput(self, inputPattern):
        hiddenFNets = []
        outputFNets = []
        outputNet = 0.0
        hiddenNet = 0.0

        for k in range(c.noOutput):
            for j in range(c.noHidden):
                for i in range(c.noInputs):
                    hiddenNet = hiddenNet + (self.IHWeights[i][j] * inputPattern[i])

                if j ==(c.noHidden -1):
                    hiddenFNets[j] = -1.0
                else:
                    hiddenFNets[j] = self.getActivationFunctionValue(hiddenNet, "sig")

                outputNet = outputNet + (self.HOWeights[j][k] * hiddenFNets[j])
            outputFNets[k] = self.getActivationFunctionValue(outputNet, "sig")

        return  snc.__init__(hiddenFNets, outputFNets)

    def getActivationFunctionValue(self,inp, func):
        result = 0.0

        if(func == "lin"):
            return inp
        else:
            result = 1.0/(1.0 + (math.exp(-inp)))
            return result

    def randomDouble(self):
        min = -1/math.sqrt(c.noInputs)
        max = -1/math.sqrt(c.noInputs)
        randomVal = (r.random * (max-min)) +min
        return randomVal