from threading import Thread


class GlobalRoutine(object):
    """Combines all the operations : - dataset
                                     - prediction
                                     - Trading"""
    def __init__(self, dataSetRoutine, computationRoutine, tradingRoutine):
        self.dataSetRoutine = dataSetRoutine
        self.computationRoutines = computationRoutine
        self.tradingRoutine = tradingRoutine
        self.threads = []  #creates a list of threads

    def test(self, a):
        for i in range(1000000000):
            print(a)

    def run(self):
        #create an observer relationship between the computation and dataset routine
        self.dataSetRoutine.register(self.computationRoutines)
        #creates an observer relationship between the trading and computation routine
        self.computationRoutines.register(self.tradingRoutine) 
        #create a first thread in charge of watching the orders that get filled and take the opposite postion
        #also manage the reward function for the MLP
        t1 = Thread(target = self.test, args = ('test',))
        self.threads.append(t1)
        t1.start()       
        #create a second thread that manage the data fetching, prediction and position opening execution        
        t2 = Thread(target = self.dataSetRoutine.launch())
        self.threads.append(t2)
        t2.start()
        
        
 


