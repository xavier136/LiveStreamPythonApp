import pandas as pd
import time
import csv

class DataSetRoutine(object):
    """ - Build the dataset using batch
        - save the data into excel files for backtests"""
    def __init__(self, webclient = None, frequency = 60, product = "BTC-USD", save = True):
        self.webclient = webclient
        self.frequency = frequency
        self.product = product
        self.save = save
        self.dataset = pd.DataFrame()
        self.stop = False

    def _stop(self, file):
        self.stop = True
        file.close()
        

    def launch(self):
        minutes = 0
        if self.save:
            myfile = open("Data/"+str(int(time.time()))+".csv", 'w')
            wr = csv.writer(myfile, quoting = csv.QUOTE_NONE, lineterminator = '\n')
            first = True #create a variable to indicate i need the to save the column names
            print("--file created--")
        while not self.stop:
            msg = self.webclient.getProductTicker(product = self.product)
            if self.save:
                if first:
                    wr.writerow(list(msg.keys()))
                    wr.writerow(list(msg.values()))
                    first = False #no need for the columns names after the first iteration
                    print("-- first line added--")
                else:
                    wr.writerow(list(msg.values()))
                    print("--line added--")

            time.sleep(self.frequency)

            minutes += 1

            if minutes == 3:
                self._stop(myfile)

        print("-- Disconnected --")

    

