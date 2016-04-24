import itertools

class Layer():

    def __init__(self, neurons):

        self.neurons = neurons
        self.error = None

    def eval(self, inputs):

        outputs = []

        for neuron in self.neurons:

            outputs.append(neuron.eval(inputs))

        #print self, " ", inputs, " : ", outputs

        return outputs
    
    def printS(self):
        
        print self, "[ "

        for neuron in self.neurons:

            neuron.printS()

        print " ]"
