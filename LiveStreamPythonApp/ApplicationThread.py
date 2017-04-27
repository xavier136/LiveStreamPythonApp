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
    
    #run the algorithm
    def run(self):
        self.GDAXClient = GDAXAPIClient() #Creates the link to the public API
        self.datasetRoutine = DataSetRoutine(self.GDAXClient, 1, "BTC-USD", True, 5, 60)
        self.computationRoutine = ComputationRoutine(self.datasetRoutine, "algo")
        self.globalRoutine = GlobalRoutine(self.datasetRoutine, self.computationRoutine)
        self.globalRoutine.run()
    
    #stops the algorithm properly, closes all opened files. This is required before dropping the Thread
    def pre_stop(self):
        self.datasetRoutine._stop(self.datasetRoutine.get_myfile())



