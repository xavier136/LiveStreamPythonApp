import numpy as np

class TradingRoutine(object):
    """Routine that manages all the trading execution and order management"""

    def __init__(self, computationRoutine, GDAXClient, holding_time, order_size):
        self.computationRoutine = computationRoutine
        self.GDAXClient = GDAXClient
        self.holding_time = holding_time
        self.order_size = order_size

    #executed everytime a prediction is sent through
    def onPredictionChange(self):
        prediction = self.computationRoutine.prediction
        order_type = self.selectOrder(prediction)
        print(prediction[0])
        print(order_type)
        #self.passOrdersPrediction(order_type)
            
    
    #select the order type according to the probability of having a positive return
    def selectOrder(self, prediction):
        #select the highest probability and only if it's > 50%
        choice = np.argmax(prediction[0])
        if (prediction[0][choice] > 0.5):
            return choice
        else:
            return -1

    #Pass the orders to the market once a prediction has been made
    def passOrdersPrediction(self, choice):
        if (choice == 0):
            #pass a buy market order
            self.GDAXClient.buy({"product_id": self.GDAXClient.productId, "type" : "market", "size" : self.order_size})
        elif (choice == 1):
            #pass a market sell order 
            self.GDAXClient.sell({"product_id": self.GDAXClient.productId, "type" : "market", "size" : self.order_size})
        else:
            pass



