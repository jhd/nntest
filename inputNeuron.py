import itertools
import math

class InputNeuron():
    
    def __init__(self, value):

        self.value = value

    def eval(self, inputs=None):

        print "Input: ", self.value
        return self.value

    def printS(self):

        print self, "Input: ", self.value
