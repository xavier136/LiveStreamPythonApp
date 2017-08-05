import numpy as np
import time 
import csv

class TradingRoutine(object):
    """Routine that manages all the trading execution and order management"""

    def __init__(self, computationRoutine, GDAXClient, authentificated, holding_time, order_size):
        self.computationRoutine = computationRoutine
        self.GDAXClient = GDAXClient
        self.authentificated = authentificated
        self.holding_time = holding_time
        self.order_size = order_size
        self.myfile = None
        self.first = False
        self.wr = None #writter for the data file
        self.create_save_file()

    #creates the file where to save the data
    def create_save_file(self):
        self.myfile = open("Positions/"+str(int(time.time()))+".csv", 'w')
        self.wr = csv.writer(self.myfile, quoting = csv.QUOTE_NONE, lineterminator = '\n')
        self.first = True #create a variable to indicate i need the to save the column names
    
    #saves the dataset into a file
    def save_decision(self, prediction, order_type, mid):
        if self.first:
            self.wr.writerow(['Market Long proba (%)', 'Market Short proba (%)', 'Order Type', 'Market Mid'])
            self.first = False #no need for the columns names after the first iteration
        self.wr.writerow([prediction[0][0], prediction[0][1], order_type, mid])

    #getter for the myfile 
    def get_myfile(self): 
        return self.myfile

    #stops the routine and close the file
    def _stop(self, file):
        if file is not None:
            file.close()

    #executed everytime a prediction is sent through
    def onPredictionChange(self):
        prediction = self.computationRoutine.prediction
        order_type = self.selectOrder(prediction)
        print(prediction[0])
        print(order_type)
        self.save_decision(prediction, order_type, self.computationRoutine.current_mid)
        if self.authentificated:
            self.passOrdersPrediction(order_type)
            

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



