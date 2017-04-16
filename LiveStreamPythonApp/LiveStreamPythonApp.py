from GDAXAPIClient import GDAXAPIClient
from DataSetRoutine import DataSetRoutine
from ComputationRoutine import ComputationRoutine
from GlobalRoutine import GlobalRoutine
import time

GDAXClient = GDAXAPIClient() #Creates the link to the public API
datasetRoutine = DataSetRoutine(GDAXClient, 1, "BTC-USD", False, 5)
computationRoutine = ComputationRoutine(datasetRoutine, "algo")
globalRoutine = GlobalRoutine(datasetRoutine, computationRoutine)

globalRoutine.run()
#datasetRoutine.launch()
