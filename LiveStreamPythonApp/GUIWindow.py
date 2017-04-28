from PyQt5 import QtWidgets
from ApplicationThread import ApplicationThread
import mainwindow
import sys

class GUIWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    """Creates the main window for the GUI"""
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.startApplication)

    def stopApplication(self):
        self.appThread.pre_stop()
        self.appThread.terminate()
        print("Application Stopped ...")

    def startApplication(self):
        product = self.productInput.text()
        frequency = self.frequencyInput.text()
        horizon = self.horizonInput.text()
        
        print("Application Started ...")
        self.appThread = ApplicationThread()
        self.appThread.start()
        self.stopButton.setEnabled(True)
        self.stopButton.clicked.connect(self.stopApplication)
        self.startButton.setEnabled(False)
        

    


