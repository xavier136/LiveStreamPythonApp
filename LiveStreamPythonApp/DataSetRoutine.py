import pandas as pd
import time
import csv
from threading import Thread

class DataSetRoutine(object):
    """ - Build the dataset using batch
        - save the data into excel files for backtests"""

    def __init__(self, webclient = None, frequency = 60, product = "BTC-USD", save = True, batchsize = 20, stopping_time = float("inf")):
        self.webclient = webclient
        self.frequency = frequency
        self.product = product
        self.save = save
        self.dataset = pd.DataFrame()
        self.stop = False
        self.batchsize = batchsize
        self.stopping_time = stopping_time
        self.myfile = None
        self.observers = [] #observers to act on change of the dataset

    def register(self, observer):#registers new observers to the dataset class
        if observer not in self.observers:
            self.observers.append(observer)
    
    def unregister(self, observer):#unregisters new observers from the dataset class
        if observer in self.observers:
            self.observers.remove(observer)

    def update(self, *args, **kwargs):#triggers the oberservers when the dataset changes
        threads = []
        for observer in self.observers:
            t = Thread(target = observer.onDataSetChange(), args = (args, kwargs,))
            threads.append(t)
            t.start

    def set_stop(self, x):#setter for the stop attribute
        self.stop = x

    def get_dataset(self):#getter for the dataset
        return self.dataset

    def get_myfile(self): #getter for the myfile 
        return self.myfile

    def _stop(self, file):#stops the routine and close the file
        self.stop = True
        if file is not None:
            file.close()
        print("-- Disconnected --")
        

    def launch(self):#retrieves the data and creates the datasets
        minutes = 0 #counts the number of minutes to put in a batch

        if self.save: #creates file where the data are going to be stored
            self.myfile = open("Data/"+str(int(time.time()))+".csv", 'w')
            wr = csv.writer(self.myfile, quoting = csv.QUOTE_NONE, lineterminator = '\n')
            first = True #create a variable to indicate i need the to save the column names
            print("--file created--")

        while not self.stop:
            msg = self.webclient.getProductTicker(product = self.product)
            if self.save:#writes the data in the file
                if first:
                    wr.writerow(list(msg.keys()))
                    wr.writerow(list(msg.values()))
                    first = False #no need for the columns names after the first iteration
                    print("-- first line added--")
                else:
                    wr.writerow(list(msg.values()))
                    print("--line added--")

            self.dataset = self.dataset.append([list(msg.values())], ignore_index = True)            

            if minutes == self.batchsize == 0: #size of the batch
                self.dataset.columns = list(msg.keys())
                self.update()
            elif minutes > self.batchsize:
                self.dataset.drop(self.dataset.index[0], inplace = True)
                self.update()

            
            time.sleep(self.frequency)
            
            if minutes == self.stopping_time: #number of ticks to download
                self._stop(self.myfile)

            minutes += 1

            
        

    

