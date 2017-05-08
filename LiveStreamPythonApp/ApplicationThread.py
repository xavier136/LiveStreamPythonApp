from PyQt5.QtCore import QThread
from GDAXAPIClient import GDAXAPIClient
from DataSetRoutine import DataSetRoutine
from ComputationRoutine import ComputationRoutine
from GlobalRoutine import GlobalRoutine

class ApplicationThread(QThread):
    """Thread running the Application. It enables to have the GUI and the applicaton
    running in parallel."""
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()
    
    #runs the algorithm
    def run(self):
        self.GDAXClient = GDAXAPIClient(api_url = "https://api.gdax.com") #Creates the link to the GDAX public API, use the URL to determine if using the sandbox or real market data
        self.datasetRoutine = DataSetRoutine(self.GDAXClient, 1, "BTC-USD", False, 5, 60) #routine that builds the dataset/treats the raw data obtained from the API
        self.computationRoutine = ComputationRoutine(self.datasetRoutine, "algo")#Routine that performs the prediction/computation on the dataset
        self.globalRoutine = GlobalRoutine(self.datasetRoutine, self.computationRoutine)# Global routine that aggregates all the routines together
        self.globalRoutine.run()#Run the global routine and therefore the whole application
    
    #stops the algorithm properly, closes all opened files. This is required before dropping the Thread
    def pre_stop(self):
        self.datasetRoutine._stop(self.datasetRoutine.get_myfile())



