from threading import Thread


class GlobalRoutine(object):
    """Combines all the operations : - dataset
                                     - prediction
                                     - Trading"""
    def __init__(self, dataSetRoutine):
        self.dataSetRoutine = dataSetRoutine

    def run(self):
        #data_thread = Thread(target = self.dataSetRoutine.launch(), args = ())
        #data_thread.start()
        #data_thread.join()
        self.dataSetRoutine.launch()


