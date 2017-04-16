class ComputationRoutine(object):
    """Routine that performs the ML predictions"""

    def __init__(self, dataSetRoutine, algo):
        self.dataSetRoutine = dataSetRoutine
        self.algo = algo

    def onDataSetChange(self):
        dataset = self.dataSetRoutine.get_dataset()
        print(dataset)
        


