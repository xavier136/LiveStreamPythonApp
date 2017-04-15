import pandas as pd
import time
import csv

class DataSetRoutine(object):
    """ - Build the dataset using batch
        - save the data into excel files for backtests"""

    def __init__(self, webclient = None, frequency = 60, product = "BTC-USD", save = True, batchsize = 20):
        self.webclient = webclient
        self.frequency = frequency
        self.product = product
        self.save = save
        self.dataset = pd.DataFrame()
        self.stop = False
        self.batchsize = batchsize

    def _stop(self, file):
        self.stop = True
        file.close()
        

    def launch(self):
        minutes = 0 #counts the number of minutes to put in a batch
        batch = pd.DataFrame()

        if self.save: #creates file where the data are going to be stored
            myfile = open("Data/"+str(int(time.time()))+".csv", 'w')
            wr = csv.writer(myfile, quoting = csv.QUOTE_NONE, lineterminator = '\n')
            first = True #create a variable to indicate i need the to save the column names
            print("--file created--")

        while not self.stop:
            msg = self.webclient.getProductTicker(product = self.product)
            #book = self.webclient.getProductOrderBook(product = self.product)
            if self.save:#writes the data in the file
                if first:
                    wr.writerow(list(msg.keys()))
                    wr.writerow(list(msg.values()))
                    first = False #no need for the columns names after the first iteration
                    print("-- first line added--")
                else:
                    wr.writerow(list(msg.values()))
                    print("--line added--")
                if minutes == 300: #number of ticks to download
                    self._stop(myfile)

            batch = batch.append([list(msg.values())])            

            if minutes % self.batchsize == 0: #size of the batch
                batch.columns = list(msg.keys())
                self.dataset = batch
                print(self.dataset)
                batch = pd.DataFrame()

            time.sleep(self.frequency)

            minutes += 1

            

        print("-- Disconnected --")

    

