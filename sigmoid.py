import itertools
import math

class Sigmoid():
    weights = []
    bias = []
    weighedInput = None
    activation = None
    activationPrime = None
    error = None
    
    def __init__(self, startWeights=None, startBias=None):
        self.weights = startWeights
        self.bias = startBias
    
    def sig(self, x):

        return 1 / (1 + math.exp(-1 * x ))


    def eval(self, inputs):
        if len(inputs) != len(self.weights):

            return float("inf")
        

        total = self.bias
        #1 / (1 + math.exp(-x))  Sigmoid function
        for (weight, input) in itertools.izip(self.weights, inputs):
            total += weight * input
        
        output = self.sig(total)

        print self, " ", inputs, " : ", output
        
        self.weighedInput = total
        self.activation = output
        self.activationPrime = output*(1-output)

        return  output

    def printS(self):

        print self, " ", self.weights, self.bias
