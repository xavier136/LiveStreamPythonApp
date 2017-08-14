from PyQt5 import QtWidgets, QtGui
from ApplicationThread import ApplicationThread
import welcomewindow
import stackedwidget
import algoSetting
import sys

class WelcomeWindow(QtWidgets.QMainWindow, welcomewindow.Ui_MainWindow):
    """Creates the main window for the GUI"""
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)#Creates the GUI from the mainwindow.py file
        self.simulationModeButton.clicked.connect(self.startSimulation)#associates the function startSimulation to the start simulation button
        self.sandBoxModeButton.clicked.connect(self.startSandBox)#associates the function startSandBox to the start sandbox button
        self.authentificatedModeButton.clicked.connect(self.startAuthentificated)#associates the function startAuthentificated to the start button

    def startSimulation(self):
        pass

    def startSandBox(self):
        stack = AuthentificationWindow()
        self.centralwidget.setCurrentWidget(stack.page_2)
        print('test')

    def startAuthentificated(self):
        pass

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
        api_key = self.apiKeyInput.text() #gets the API Key
        api_secret = self.apiSecretInput.text() #gets the API Secret
        password = self.passwordInput.text() #gets the password
        
        print("Application Started ...")
        self.appThread = ApplicationThread(product, frequency, horizon, save_data, api_key, api_secret, password) #creates a Thread for the application
        self.appThread.start() #starts the application and runs the thread
        self.stopButton.setEnabled(True) #enables stop button
        self.stopButton.clicked.connect(self.stopApplication) #associates the function stop application with the stop button
        self.startButton.setEnabled(False) #disables the start button to prevent running the application multiple times in parallel
 
       
class AuthentificationWindow(QtWidgets.QStackedWidget, stackedwidget.Ui_StackedWidget):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)#Creates the GUI from the mainwindow.py file
        self.startButton.clicked.connect(self.startfunc)

    def startfunc(self):
        self.setCurrentWidget(self.page_2)

