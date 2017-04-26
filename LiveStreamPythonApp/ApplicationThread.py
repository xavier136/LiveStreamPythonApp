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

    def run(self):
        GDAXClient = GDAXAPIClient() #Creates the link to the public API
        datasetRoutine = DataSetRoutine(GDAXClient, 1, "BTC-USD", False, 5, 60)
        computationRoutine = ComputationRoutine(datasetRoutine, "algo")
        globalRoutine = GlobalRoutine(datasetRoutine, computationRoutine)
        globalRoutine.run()



