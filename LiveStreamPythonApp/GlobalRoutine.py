from threading import Thread


class GlobalRoutine(object):
    """Combines all the operations : - dataset
                                     - prediction
                                     - Trading"""
    def __init__(self, dataSetRoutine, computationRoutine, tradingRoutine):
        self.dataSetRoutine = dataSetRoutine
        self.computationRoutines = computationRoutine
        self.tradingRoutine = tradingRoutine

    def run(self):
        #create an observer relationship between the computation and dataset routine
        self.dataSetRoutine.register(self.computationRoutines)
        #creates an observer relationship between the trading and computation routine
        self.computationRoutines.register(self.tradingRoutine)
        
        self.dataSetRoutine.launch()
        
 


