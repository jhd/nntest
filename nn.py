from sigmoid import Sigmoid
from connection import Connection
from layer import Layer
from inputNeuron import InputNeuron

import numpy

class NeuralNetwork():

    def __init__(self, layers=None):
        
        self.network = []

        if layers == None:

            return

        for layer in layers:

            self.network.append(layer)

    def randomLayersInit(self, layers):
        #layers format: [number of input neurons, number of sigs for this layer...]

        if len(layers) <= 2:

            return

        self.network = []
        
        inputs = []
        for input in range(0, layers[0]):
            
            inputs.append(InputNeuron(numpy.random.uniform(0, 1)))

        self.network.append(Layer(inputs))

        for layerLength in layers[1:]:

            neurons = []

            for neuron in range(0, layerLength):

                neurons.append(Sigmoid([numpy.random.uniform(0, 1) for startWeight in range(0, len(self.network[:1]))], numpy.random.uniform(0, 1)))

            self.network.append(Layer(neurons))

    def eval(self, startInputs):
        
        inputs = startInputs

        for layer in self.network:
            
            inputs = layer.eval(inputs)

        return inputs # "inputs" is now the output from the output layer, suitable to be the input to another NN

    def printS(self):
        
        print self, "[ "
        for layer in self.network:

            layer.printS()
        print "]"

input1 = InputNeuron(0.9)
input2 = InputNeuron(0.1)
hidden1 = Sigmoid([0.5, 0.5], 0.2)
hidden2 = Sigmoid([0.2, 0.8], 0.4)
out1 = Sigmoid([0.3, 0.8], 0.1)
out2 = Sigmoid([0.8, 0.2], 0.6)

layerIn = Layer([input1, input2])
layerHidden = Layer([hidden1, hidden2])
layerOut = Layer([out1, out2])

nn = NeuralNetwork([layerIn, layerHidden, layerOut])

#print nn.printS()
#print nn.eval([0.9, 0.1])

nnRand = NeuralNetwork()
nnRand.randomLayersInit([2, 2, 2])
print nnRand.printS()
print nnRand.eval([0.9, 0.1])
