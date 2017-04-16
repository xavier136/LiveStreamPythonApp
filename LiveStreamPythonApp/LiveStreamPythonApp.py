from GDAXAPIClient import GDAXAPIClient
from DataSetRoutine import DataSetRoutine
from GlobalRoutine import GlobalRoutine
import time

GDAXClient = GDAXAPIClient() #Creates the link to the public API
datasetRoutine = DataSetRoutine(GDAXClient, 1, "BTC-USD", True)
globalRoutine = GlobalRoutine(datasetRoutine)

#globalRoutine.run()
datasetRoutine.launch()
