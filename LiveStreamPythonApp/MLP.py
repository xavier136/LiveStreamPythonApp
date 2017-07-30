from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

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
        
        #input layer
        model.add(Dense(self.neurons, kernel_initializer = self.kernel_initializer, bias_initializer = self.bias_initializer, input_shape = self.input_shape)) #adds first layer
        model.add(Activation(self.activation))
        
        #hidden layers
        for i in range(self.hidden_layers):#creates all the hidden layers 
            model.add(Dense(self.neurons, kernel_initializer = self.kernel_initializer, bias_initializer = self.bias_initializer))
            model.add(Activation(self.activation))
        
        #output layers
        model.add(Dense(2, kernel_initializer = self.kernel_initializer, bias_initializer = self.bias_initializer)) #creates the last layer and outputs 2 elements : probability of winning with a market order, buy/sell
        model.add(Activation(self.activation))

        model.compile(optimizer='rmsprop', loss='mse')#compiles the model
        return model

    #Recompiles the model with a new learning rate
    def recompileModel(self, model, learning_rate):
        backprop = RMSprop(lr=learning_rate, rho=0.9, epsilon=1e-08, decay=0.0)
        model.compile(optimizer=backprop, loss='mse')#compiles the model





