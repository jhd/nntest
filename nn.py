from sigmoid import Sigmoid
from connection import Connection
from layer import Layer
from inputNeuron import InputNeuron

import itertools
import numpy
import matplotlib.pyplot as pyplot

class NeuralNetwork():

    def __init__(self, layers=None):
        
        self.network = []

        if layers == None:

            return

        for layer in layers:

            self.network.append(layer)

    def randomLayersInit(self, layers, startInputs):
        #layers format: [number of input neurons, number of sigs for this layer...]

        if len(layers) <= 2:

            return

        self.network = []
        
        inputs = []
        for input in range(0, layers[0]):
            
            inputs.append(InputNeuron(startInputs[input]))

        self.network.append(Layer(inputs))

        for layerLength in layers[1:]:

            neurons = []

            for neuron in range(0, layerLength):

                neurons.append(Sigmoid([numpy.random.uniform(0, 1) for startWeight in range(0, len(self.network[len(self.network)-1].neurons))], numpy.random.uniform(0, 1)))

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

    def outputError(self, targets): 

        eta = 0.5

        for output, target in itertools.izip(self.network[len(self.network)-1].neurons, targets):
            
            output.error = (output.sig(output.weighedInput) - target)*output.activationPrime

            #print (output.sig(output.weighedInput) - target)*output.activationPrime
            
        for weightIndex in range(0, len(output.weights)):

                output.weights[weightIndex] -=  eta * self.network[len(self.network)-2].neurons[weightIndex].activation * output.error
        
        output.bias -= eta * output.error

        return (output.sig(output.weighedInput) - target)*output.activationPrime

    def fillbackError(self):
        
        eta = 0.5

        for layerIndex in range (len(self.network)-2, 0, -1):

            layer = self.network[layerIndex]

            for neuronIndex in range(0, len(layer.neurons)):
                
                prevError = 0

                for prevNeuron in self.network[layerIndex+1].neurons:
                    
                    prevError += prevNeuron.error * prevNeuron.weights[neuronIndex]

                layer.neurons[neuronIndex].error = prevError*layer.neurons[neuronIndex].activationPrime

                layer.neurons[neuronIndex].bias -= eta * layer.neurons[neuronIndex].error

                for weightIndex in range(0, len(layer.neurons[neuronIndex].weights)):

                    layer.neurons[neuronIndex].weights[weightIndex] -=  eta * self.network[layerIndex-1].neurons[weightIndex].activation * layer.neurons[neuronIndex].error

                #print "Layer: ", layerIndex, " Sig: ", neuronIndex, " Error: ", layer.neurons[neuronIndex].error

"""
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
"""

"""
nnRand = NeuralNetwork()
nnRand.randomLayersInit([1, 1, 1], [0.2])
#nnRand.printS()
print nnRand.eval([0.5])
nnRand.outputError([0.2])
nnRand.fillbackError()
#nnRand.printS()
print nnRand.eval([0.5])
nnRand.outputError([0.2])
#nnRand.printS()
"""

nn = NeuralNetwork()
nn.randomLayersInit([2, 20, 1], [0.5, 0.2])
target = 0.8
outputs = []
for i in range(0, 500):
    #nn.printS()
    output = nn.eval([0.5, 0.2])
    outputs.append(output)
    print "Iter: ", i, " Output: ", output
    nn.outputError([0.2])
    nn.fillbackError()

pyplot.plot(range(0, 500), outputs)
pyplot.axis([0, 500, 0, 1])
pyplot.show()
