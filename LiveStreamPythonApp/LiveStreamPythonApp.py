from GDAXAPIClient import GDAXAPIClient
from DataSetRoutine import DataSetRoutine
import time

GDAXClient = GDAXAPIClient() #Creates the link to the public API
datasetRoutine = DataSetRoutine(GDAXClient, 10, "BTC-USD", False)

datasetRoutine.launch()
