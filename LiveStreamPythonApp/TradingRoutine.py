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
        self.passOrders(1)
    
    #select the order type according to the probability of having a positive return
    def selectOrder(self, prediction):
        choice = np.argmax(prediction[0])
        if (prediction[0][choice] > 0):
            return choice
        else:
            return -1

    #Pass the orders to the market
    def passOrders(self, choice):
        if (choice == 0):
            pass
        elif (choice == 1):
            self.GDAXClient.buy({"product_id": "BTC-USD", "price" : 2690, "size" : self.order_size})
        elif (choice == 2):
            pass
        else:
            pass
       



