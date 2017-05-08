from PyQt5 import QtWidgets
from ApplicationThread import ApplicationThread
import mainwindow
import sys

class GUIWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    """Creates the main window for the GUI"""
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)#Creates the GUI from the mainwindow.py file
        self.startButton.clicked.connect(self.startApplication)#associates the function startApplication to the start button

    #stops the application
    def stopApplication(self):
        self.appThread.pre_stop() #prepare the thread to properly stop
        self.appThread.terminate() #terminates the thread
        self.startButton.setEnabled(True) #makes the start button clickable again
        print("Application Stopped ...")

    #starts the application
    def startApplication(self):
        product = self.productInput.currentText() #gets the product code from the GUI
        frequency = self.frequencyInput.value() #gets the frequency from the GUI
        horizon = self.horizonInput.value() #gets the horizon from the GUI
        save_data = self.dataInput.isChecked() #check if the data need to be saved or not
        
        print("Application Started ...")
        self.appThread = ApplicationThread(product, frequency, horizon, save_data) #creates a Thread for the application
        self.appThread.start() #starts the application and runs the thread
        self.stopButton.setEnabled(True) #enables stop button
        self.stopButton.clicked.connect(self.stopApplication) #associates the function stop application with the stop button
        self.startButton.setEnabled(False) #disables the start button to prevent running the application multiple times in parallel
        

    


