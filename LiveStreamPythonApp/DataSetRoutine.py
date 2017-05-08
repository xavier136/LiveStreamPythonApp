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
        self.batch = pd.DataFrame()
        self.stop = False
        self.batchsize = batchsize
        self.stopping_time = stopping_time
        self.myfile = None
        self.first = False
        self.wr = None #writter for the data file
        self.observers = [] #observers to act on change of the dataset

    #registers new observers to the dataset class
    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    #unregisters new observers from the dataset class
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    #triggers the oberservers when the dataset changes
    def update(self, *args, **kwargs):
        self.create_dataset()
        self.save_dataset()
        threads = []
        for observer in self.observers:
            t = Thread(target = observer.onDataSetChange(), args = (args, kwargs,))
            threads.append(t)
            t.start

    #setter for the stop attribute
    def set_stop(self, x):
        self.stop = x

    #creates the dataset to be used for the prediction
    def create_dataset(self):
        order_book = self.webclient.getProductOrderBook(level = 2, product = self.product) #gets the order book (top 50 bid-asks)
        bids = pd.DataFrame(order_book['bids'])#puts all the bids into a dataframe
        bids.columns = ['price', 'size', 'num orders']#rename the columns
        asks = pd.DataFrame(order_book['asks'])#puts all the asks into a dataframe
        asks.columns = ['price', 'size', 'num orders']#rename the columns
        self.dataset = self.batch.iloc[0, :].to_frame().transpose() #creates a dataframe with only the first line of the batch dataframe
        self.dataset.loc[0, 'bid'] = bids.loc[0, 'price'] #gets the latest bid
        self.dataset.loc[0, 'ask'] = asks.loc[0, 'price'] #gets the latest ask
        self.dataset['spread'] = float(self.dataset.loc[0, 'ask']) - float(self.dataset.loc[0, 'bid']) #adds a spread column and its value
        self.dataset['smartPrice'] = (float(asks.loc[0, 'price']) * float(asks.loc[0, 'size']) + float(bids.loc[0, 'price']) * float(bids.loc[0, 'size'])) / (float(asks.loc[0, 'size']) + float(bids.loc[0, 'size'])) #smart price average of the bid ask weighted by their volumes
        self.dataset['volumeImbalance'] = pd.to_numeric(asks['size']).sum() - pd.to_numeric(bids['size']).sum() #difference in volumes between the bids and asks
        self.dataset['volumePerOrderImbalance'] = (pd.to_numeric(asks['size']).sum()/ pd.to_numeric(asks['num orders']).sum()) - (pd.to_numeric(bids['size']).sum() / pd.to_numeric(bids['num orders']).sum()) #volume weihgted by the number of orders 
    
    #creates the file where to save the data
    def create_save_file(self):
        if self.save: #creates file where the data are going to be stored
            self.myfile = open("Data/"+str(int(time.time()))+".csv", 'w')
            self.wr = csv.writer(self.myfile, quoting = csv.QUOTE_NONE, lineterminator = '\n')
            self.first = True #create a variable to indicate i need the to save the column names
            print("--file created--")
    
    #saves the dataset into a file
    def save_dataset(self):
        if self.save:#writes the data in the file
                if self.first:
                    self.wr.writerow(self.dataset.columns)
                    self.wr.writerow(self.dataset.iloc[0, :].tolist())
                    self.first = False #no need for the columns names after the first iteration
                    print("-- first line added--")
                else:
                    self.wr.writerow(self.dataset.iloc[0, :].tolist())
                    print("--line added--")
        
    #getter for the dataset
    def get_dataset(self):
        return self.dataset
    
    #getter for the myfile 
    def get_myfile(self): 
        return self.myfile
    
    #stops the routine and close the file
    def _stop(self, file):
        self.stop = True
        if file is not None:
            file.close()
        print("-- Disconnected --")
     
    #launches the dataset routine
    def launch(self):
        minutes = 0 #counts the number of minutes to put in a batch
        self.create_save_file() #create the save file
        
        while not self.stop:
            msg = self.webclient.getProductTicker(product = self.product)
            
            self.batch = self.batch.append(pd.DataFrame(msg, index = [0]), ignore_index = True) #gets the latest values from the API and appends them to the batch        

            if minutes == self.batchsize: #size of the batch
                self.update()
            elif minutes > self.batchsize:
                self.batch.drop(self.batch.index[0], inplace = True)#deletes the first element of the batch (the oldest) to enable the rolling window
                self.batch.reset_index(drop = True, inplace = True)# resets the indices
                self.update()

            
            time.sleep(self.frequency)#pauses the process for a given amount of time
            
            if minutes == self.stopping_time: #number of ticks to download
                self._stop(self.myfile)

            minutes += 1

            
        

    

