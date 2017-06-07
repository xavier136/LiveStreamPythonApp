import numpy as np
from threading import Thread

class ComputationRoutine(object):
    """Routine that performs the ML predictions"""

    def __init__(self, dataSetRoutine, algo):
        self.dataSetRoutine = dataSetRoutine
        self.algo = algo
        self.model = algo.buildModel() #builds the NN to use for the prediction
        self.observers = [] #observers to act on change of the dataset

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
        threads = []
        for observer in self.observers:
            t = Thread(target = observer.onPredictionChange(), args = (args, kwargs,))
            threads.append(t)
            t.start

    #every time a new batch of data is sent we run the algo and get a prediction
    def onDataSetChange(self):
        full_dataset = self.dataSetRoutine.get_dataset()
        X_dataset = np.array(full_dataset[['ask', 'bid', 'price', 'size', 'volume', 'spread', 'smartPrice', 'volumeImbalance', 'volumePerOrderImbalance']])
        self.prediction = self.model.predict(np.array(X_dataset))
        self.update()
        


