from PyQt5.QtCore import QThread
from DataSetRoutine import DataSetRoutine
from ComputationRoutine import ComputationRoutine
from GlobalRoutine import GlobalRoutine
from TradingRoutine import TradingRoutine
from Report import Report
from MLP import MLP
import gdax as GDAX

class ApplicationThread(QThread):
    """Thread running the Application. It enables to have the GUI and the applicaton
    running in parallel."""
    
    def __init__(self, product, frequency, maxHolding, tradeSize, save, auth, url, api_key, api_secret, password, layers, neurons):
        QThread.__init__(self)
        self.product = product
        self.maxHolding = maxHolding
        self.tradeSize = tradeSize
        self.frequency = frequency
        self.save = save
        self.api_key = api_key
        self.api_secret = api_secret
        self.password = password
        self.authentificated = auth
        self.url = url
        self.layers = layers
        self.neurons = neurons

    def __del__(self):
        self.wait()
    
    #runs the algorithm
    def run(self):
        self.MLP = MLP(self.layers, self.neurons, 'sigmoid', 'random_uniform', 'zeros', (9,))#creates the MLP used for the learning
        if self.authentificated:
            self.GDAXClient = GDAX.AuthenticatedClient(self.api_key, self.api_secret, self.password, api_url = self.url) #Creates the link to the GDAX private authentificated API, use the URL to determine if using the sandbox or real market data
        else:
            self.GDAXClient = GDAX.PublicClient(api_url = self.url) #Creates the link to the GDAX public API, use the URL to determine if using the sandbox or real market data
        self.datasetRoutine = DataSetRoutine(self.GDAXClient, self.frequency , self.product, self.save) #routine that builds the dataset/treats the raw data obtained from the API
        self.computationRoutine = ComputationRoutine(self.datasetRoutine, self.MLP)#Routine that performs the prediction/computation on the dataset
        self.tradingRoutine = TradingRoutine(self.computationRoutine, self.GDAXClient, self.authentificated, self.maxHolding, self.tradeSize, self.product)#Routine that performs all the trading aspect of the application
        self.globalRoutine = GlobalRoutine(self.datasetRoutine, self.computationRoutine, self.tradingRoutine)# Global routine that aggregates all the routines together
        self.globalRoutine.run()#Run the global routine and therefore the whole application

    #stops the algorithm properly, closes all opened files. This is required before dropping the Thread
    def pre_stop(self):
        self.datasetRoutine._stop(self.datasetRoutine.get_myfile())
        self.tradingRoutine._stop(self.tradingRoutine.get_myfile())
        if self.authentificated:
            self.GDAXClient.cancel_all(product = self.product)
    
    #generates the report to display
    def generateReport(self):
        report = Report(self.tradingRoutine.file_name)
        report.read_file()
        report.compute_return()
        report.compute_volatility()
        report.compute_maxDD()
        report.cumul_graph()
        report.pos_graph()
        return report

