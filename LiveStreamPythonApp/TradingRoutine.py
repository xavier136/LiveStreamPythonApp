import numpy as np

class TradingRoutine(object):
    """Routine that manages all the trading execution and order management"""

    def __init__(self, computationRoutine, GDAXClient):
        self.computationRoutine = computationRoutine
        self.GDAXClient = GDAXClient

    #executed everytime a prediction is sent through
    def onPredictionChange(self):
        prediction = self.computationRoutine.prediction
        order_type = self.selectOrder(prediction)
        print(prediction[0])
        print(order_type)
    
    #select the order type according to the probability of having a positive return
    def selectOrder(self, prediction):
        choice = np.argmax(prediction[0])
        if (prediction[0][choice] > 0):
            return choice
        else:
            return -1
       



