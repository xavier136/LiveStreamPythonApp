import numpy as np
import pandas as pd
#from threading import Thread

class ComputationRoutine(object):
    """Routine that performs the ML predictions"""

    def __init__(self, dataSetRoutine, algo):
        self.dataSetRoutine = dataSetRoutine
        self.algo = algo
        self.model = algo.buildModel() #builds the NN to use for the prediction
        self.observers = [] #observers to act on change of the dataset
        self.previous_mid = None #previous mid, needed for the reward function
        self.previous_prediction = None #previous prediction, needed for the reward function
        self.previous_dataset = None
        self.current_mid = None

    #register observers to this class
    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    #unregisters new observers from the dataset class
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    #triggers the oberservers when the dataset changes
    def update(self, *args, **kwargs):
        #threads = []
        for observer in self.observers:
        #    t = Thread(target = observer.onPredictionChange(), args = (args, kwargs,))
        #    threads.append(t)
        #    t.start
            observer.onPredictionChange()
    
    #dynamically choses the learning rate
    def computeLearningRate(self, probas, prediction):
        learning_rate = 0
        for i in range(len(prediction)):
            learning_rate +=  abs(probas[i] - prediction[0][i]) / (10 * len(prediction))
        return learning_rate

    def updateNN(self, learning_rate, probas, previous_data):
        self.algo.recompileModel(self.model, learning_rate)
        self.model.train_on_batch(np.array(previous_data), np.array(probas).reshape((1, 2)))

    #every time a new batch of data is sent we run the algo and get a prediction
    # we also check if the previous prediction was accurate and update the algo accordingly
    def onDataSetChange(self):
        full_dataset = self.dataSetRoutine.get_dataset()
        self.current_mid = (float(full_dataset[['ask']].iloc[0, 0]) + float(full_dataset[['bid']].iloc[0, 0])) / 2
        X_dataset = np.array(full_dataset[['ask', 'bid', 'price', 'size', 'volume', 'spread', 'smartPrice', 'volumeImbalance', 'volumePerOrderImbalance']])
        self.prediction = self.model.predict(np.array(X_dataset))
        if self.previous_mid and not (self.previous_prediction is None):
            if self.previous_mid > self.current_mid:
                actual_prob = [0, 1]
            elif self.previous_mid < self.current_mid:
                actual_prob = [1, 0]  
            else:
                actual_prob = [0, 0]          
            learning_rate = self.computeLearningRate(actual_prob, self.previous_prediction)
            print('learning rate :' + str(learning_rate))
            print(self.current_mid)
            self.updateNN(learning_rate, actual_prob, self.previous_dataset)
        self.update()


        self.previous_prediction = self.prediction
        self.previous_mid = self.current_mid
        self.previous_dataset = X_dataset

