from keras.models import Sequential
from keras.layers import Dense, Activation

class MLP(object):
    """Builds the Multilayers Perceptron"""
    
    def __init__(self, hidden_layers, neurons, activation, kernel_initializer, bias_initializer, input_shape):
        self.hidden_layers = hidden_layers
        self.neurons = neurons
        self.activation = activation
        self.kernel_initializer = kernel_initializer
        self.bias_initializer = bias_initializer
        self.input_shape = input_shape

    #Builds a standards Sequential Neural Network
    def buildModel(self):
        model = Sequential()
        model.add(Dense(self.neurons, kernel_initializer = self.kernel_initializer, bias_initializer = self.bias_initializer, input_shape = self.input_shape)) #adds first layer
        model.add(Activation(self.activation))
        
        for i in range(self.hidden_layers):#creates all the hidden layers 
            model.add(Dense(self.neurons, kernel_initializer = self.kernel_initializer, bias_initializer = self.bias_initializer))
            model.add(Activation(self.activation))

        model.add(Dense(2, kernel_initializer = self.kernel_initializer, bias_initializer = self.bias_initializer)) #creates the last layer and outputs 2 elements : probability of winning with a market order, probability of winning with a limit order
        model.add(Activation(self.activation))

        model.compile(optimizer='rmsprop', loss='mse')#compiles the model
        return model





