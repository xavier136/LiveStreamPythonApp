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
        # self.passOrdersPrediction(0)
    
    #select the order type according to the probability of having a positive return
    def selectOrder(self, prediction):
        #select the highest probability and only if it's > 50%
        choice = np.argmax(prediction[0])
        if (prediction[0][choice] > 0):
            return choice
        else:
            return -1

    #Pass the orders to the market once a prediction has been made
    def passOrdersPrediction(self, choice):
        #get the bid ask
        bid = self.GDAXClient.getProductOrderBook(level = 1)["bids"][0][0]
        ask = self.GDAXClient.getProductOrderBook(level = 1)["asks"][0][0]
    

        if (choice == 0):
            #pass a buy market order
            self.GDAXClient.buy({"product_id": self.GDAXClient.productId, "type" : "market", "size" : self.order_size})
        elif (choice == 1):
            #pass a buy limit order at the best ask
            self.GDAXClient.buy({"product_id": self.GDAXClient.productId, "price" : bid, "size" : self.order_size})
        elif (choice == 2):
            #pass a market sell order 
            self.GDAXClient.sell({"product_id": self.GDAXClient.productId, "type" : "market", "size" : self.order_size})
        elif (choice == 3):
            #pass a limit sell order at the best bid
            self.GDAXClient.sell({"product_id": self.GDAXClient.productId, "price" : ask, "size" : self.order_size})
        else:
            pass
    #Pass the opposite side order once an order issued from the prediction is filled
    def passOrderFill(self, id):
        pass


