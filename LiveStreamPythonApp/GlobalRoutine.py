from threading import Thread


class GlobalRoutine(object):
    """Combines all the operations : - dataset
                                     - prediction
                                     - Trading"""
    def __init__(self, dataSetRoutine, *args):
        self.dataSetRoutine = dataSetRoutine
        self.computationRoutines = args

    def run(self):
        for routine in self.computationRoutines:
           self.dataSetRoutine.register(routine)

        data_thread = Thread(target = self.dataSetRoutine.launch(), args = ())
        data_thread.start()
        
 


