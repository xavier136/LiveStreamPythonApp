import numpy as np
import time 
import datetime
import csv
from Portfolio import Portfolio

class TradingRoutine(object):
    """Routine that manages all the trading execution and order management"""

    def __init__(self, computationRoutine, GDAXClient, authentificated, max_ccy_holding, order_size, product):
        self.computationRoutine = computationRoutine
        self.GDAXClient = GDAXClient
        self.authentificated = authentificated
        self.max_ccy_holding = max_ccy_holding
        self.order_size = order_size
        self.myfile = None
        self.first = False
        self.wr = None #writter for the data file
        self.create_save_file()
        self.product = product

        if authentificated:
            self.portfolio = Portfolio(float(self.GDAXClient.get_position()['accounts']['USD']['balance']),float(self.GDAXClient.get_position()['accounts']['BTC']['balance']), self.max_ccy_holding)
        else:
            self.portfolio = Portfolio(100000, 0, self.max_ccy_holding)

    #creates the file where to save the data
    def create_save_file(self):
        self.myfile = open("Positions/"+str(int(time.time()))+".csv", 'w')
        self.wr = csv.writer(self.myfile, quoting = csv.QUOTE_NONE, lineterminator = '\n')
        self.first = True #create a variable to indicate i need the to save the column names
    
    #saves the dataset into a file
    def save_decision(self, prediction, order_type, mid, portfolio):
        if self.first:
            self.wr.writerow(['Timestamp', 'Market Long proba (%)', 'Market Short proba (%)', 'Order Type', 'Market Mid', 'Holding', 'Holding Value'])
            self.first = False #no need for the columns names after the first iteration
        if self.authentificated:
            self.wr.writerow([datetime.datetime.now(), prediction[0][0], prediction[0][1], order_type, mid, float(self.GDAXClient.get_position()['accounts']['BTC']['balance']), float(self.GDAXClient.get_position()['accounts']['BTC']['balance']) * mid])
        else:
            self.wr.writerow([datetime.datetime.now(), prediction[0][0], prediction[0][1], order_type, mid, portfolio.get_crypto(), portfolio.get_portfolio_value(mid)])

    #getter for the myfile 
    def get_myfile(self): 
        return self.myfile

    #stops the routine and close the file
    def _stop(self, file):
        if file is not None:
            file.close()

    def printLive(self, prediction, order_type):
        if order_type == 1:
            order = 'Short'
        elif order_type == 0:
            order = 'Long'
        else:
            order = 'None'
        print('#'*60)
        print('Current mid: ' + str(self.computationRoutine.current_mid))
        print('Predictions: Win Long (' + str(prediction[0][0]) + ') - Win Short (' + str(prediction[0][1]) + ')')
        print('Order Passed: ' + order)
        if self.authentificated:
            print('CryptoCurrency Holding: ' + self.GDAXClient.get_position()['accounts']['BTC']['balance'])
            print('Portfolio Value: ' + str(float(self.GDAXClient.get_position()['accounts']['BTC']['balance']) * self.computationRoutine.current_mid))

        else:
            print('CryptoCurrency Holding: ' + str(self.portfolio.get_crypto()))
            print('Portfolio Value: ' + str(self.portfolio.get_portfolio_value(self.computationRoutine.current_mid)))

    #executed everytime a prediction is sent through
    def onPredictionChange(self):
        prediction = self.computationRoutine.prediction
        order_type = self.selectOrder(prediction)
        if self.authentificated:
            self.passOrdersPrediction(order_type)
        else:
            if order_type == 0:
                self.portfolio.buy_crypto(self.order_size, self.computationRoutine.current_mid, 0)
            elif order_type == 1:
                self.portfolio.sell_crypto(2 * self.order_size, self.computationRoutine.current_mid, 0)
        self.save_decision(prediction, order_type, self.computationRoutine.current_mid, self.portfolio)
        self.printLive(prediction, order_type)


    #select the order type according to the probability of having a positive return
    def selectOrder(self, prediction):
        #select the highest probability and only if it's > 50% for selling 
        choice = np.argmax(prediction[0])
        if (choice == 0 and prediction[0][choice] > 0.5) or (choice == 1 and prediction[0][choice] > 0.5):
            return choice
        else:
            return -1

    #Pass the orders to the market once a prediction has been made
    def passOrdersPrediction(self, choice):
        if (choice == 0):
            #pass a buy market order
            self.GDAXClient.buy(product_id = self.product, size= self.order_size, type = 'market')
        elif (choice == 1):
            #pass a market sell order 
            self.GDAXClient.sell(product_id = self.product, size= self.order_size, type = 'market')
        else:
            pass



