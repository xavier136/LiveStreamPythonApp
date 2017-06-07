from PyQt5.QtCore import QThread
from GDAXAPIClient import GDAXAPIClient
from DataSetRoutine import DataSetRoutine
from ComputationRoutine import ComputationRoutine
from GlobalRoutine import GlobalRoutine
from TradingRoutine import TradingRoutine
from MLP import MLP
import GDAX 

class ApplicationThread(QThread):
    """Thread running the Application. It enables to have the GUI and the applicaton
    running in parallel."""
    
    def __init__(self, product, frequency, horizon, save):
        QThread.__init__(self)
        self.product = product
        self.horizon = horizon
        self.frequency = frequency
        self.save = save

    def __del__(self):
        self.wait()
    
    #runs the algorithm
    def run(self):
        self.MLP = MLP(10, 60, 'sigmoid', 'random_uniform', 'zeros', (9,))#creates the MLP used for the learning
        self.GDAXClient = GDAX.PublicClient(api_url = "https://api.gdax.com") #Creates the link to the GDAX public API, use the URL to determine if using the sandbox or real market data
        #self.GDAXClient = GDAX.AuthenticatedClient("731e94e021484683fd45915b36cfe17b", "y7YtPzLyRA9JXATjIG7RVGixOMzTPEiAXN7kpwj+NJPumhI5kbVrPbdcQkgdzUdzwemNR/2TYWttP7ZuMlx5Pw==", "3972brnquio", api_url = "https://api.gdax.com") #Creates the link to the GDAX private authentificated API, use the URL to determine if using the sandbox or real market data
        self.datasetRoutine = DataSetRoutine(self.GDAXClient, self.frequency , self.product, self.save, self.horizon) #routine that builds the dataset/treats the raw data obtained from the API
        self.computationRoutine = ComputationRoutine(self.datasetRoutine, self.MLP)#Routine that performs the prediction/computation on the dataset
        self.tradingRoutine = TradingRoutine(self.computationRoutine, self.GDAXClient)#Routine that performs all the trading aspect of the application
        self.globalRoutine = GlobalRoutine(self.datasetRoutine, self.computationRoutine, self.tradingRoutine)# Global routine that aggregates all the routines together
        self.globalRoutine.run()#Run the global routine and therefore the whole application
    #stops the algorithm properly, closes all opened files. This is required before dropping the Thread
    def pre_stop(self):
        self.datasetRoutine._stop(self.datasetRoutine.get_myfile())


