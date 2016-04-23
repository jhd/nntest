import itertools
import math

class Sigmoid():
    weights = []
    bias = []
    
    def __init__(self, startWeights=None, startBias=None):
        self.weights = startWeights
        self.bias = startBias

    def eval(self, inputs):
        if len(inputs) != len(self.weights):

            return float("inf")
        

        total = -1 * self.bias
        #1 / (1 + math.exp(-x))  Sigmoid function
        for (weight, input) in itertools.izip(self.weights, inputs):
            total += weight * input
        
        output = 1 / (1 + math.exp(-total))

        print self, " ", inputs, " : ", output

        return  output

    def printS(self):

        print self, " ", self.weights, self.bias
