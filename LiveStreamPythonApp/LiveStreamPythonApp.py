from GDAXAPIClient import GDAXAPIClient
from DataSetRoutine import DataSetRoutine
from threading import Thread
import time

GDAXClient = GDAXAPIClient() #Creates the link to the public API
datasetRoutine = DataSetRoutine(GDAXClient, 60, "BTC-USD", True)

datasetRoutine.launch()
