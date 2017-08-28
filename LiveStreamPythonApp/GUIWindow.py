from PyQt5 import QtWidgets, QtGui
from ApplicationThread import ApplicationThread
import fullapplayout
import sys

class FullAppLayout(QtWidgets.QStackedWidget, fullapplayout.Ui_StackedWidget):
   """ Creates the main window for the GUI"""
   
   def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # Creates the GUI from the mainwindow.py file
        self.setCurrentWidget(self.WelcomePage)
        self.simulationModeButton.clicked.connect(self.launchSimulation)
        self.sandBoxModeButton.clicked.connect(self.launchSandBox)
        self.authentificatedModeButton.clicked.connect(self.launchAuth)
        self.connectButton.clicked.connect(self.connecFunc)
        self.startButton.clicked.connect(self.startApplication)
        self.stopButton.clicked.connect(self.stopApplication)
        
        #initialization of the auth parameters
        self.apiKey = None
        self.apiSecret = None
        self.password = None

   #launches the Simulation Mode
   def launchSimulation(self):
        self.auth = False
        self.url = 'https://api.gdax.com'
        self.setCurrentWidget(self.AlgoPage)

   #launches the sandBox Mode
   def launchSandBox(self):
        self.auth = True
        self.url = 'https://api-public.sandbox.gdax.com'
        self.setCurrentWidget(self.AuthPage)

   #launches the authentificated mode
   def launchAuth(self):
        self.auth = True
        self.url = 'https://api.gdax.com'
        self.setCurrentWidget(self.AuthPage)

   #launches the algo
   def connecFunc(self):
        self.apiKey = self.aPIKeyLineEdit.text() #gets the API Key
        self.apiSecret = self.aPISecretLineEdit.text() #gets the API Secret
        self.password = self.passwordLineEdit.text() #gets the password
        self.setCurrentWidget(self.AlgoPage)

   #stops the application
   def stopApplication(self):
       self.appThread.pre_stop() #prepare the thread to properly stop
       report = self.appThread.generateReport() #generates the end of session report
       self.startDate.setText(report.start_date)
       self.endDate.setText(report.end_date)
       self.stratReturn.setText(str(report.strat_return) + '%')
       self.stratVol.setText(str(report.strat_vol) + '%')
       self.stratMaxDrawDown.setText(str(report.drawdown) + '%')
       self.cumulReturn.setScene(report.cumulRet)
       self.positionEvolution.setScene(report.posEvol)
       self.setCurrentWidget(self.ResultPage) #dispalys the report page
       self.appThread.terminate() #terminates the thread
       print("Application Stopped ...")

    #starts the application
   def startApplication(self):
       product = self.fontComboBox.currentText() #gets the product code from the GUI
       frequency = self.tradeFrequencyInSecondsSpinBox.value() #gets the frequency from the GUI
       maxHolding = self.maxHoldingUnitOfCryptoCurrencyDoubleSpinBox.value() #gets the horizon from the GUI
       tradeSize = self.volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox.value()
       save_data = self.saveDataCheckBox.isChecked() #check if the data need to be saved or not
       layers = self.LayerNumber.value() #gets the number of layers for the NN
       neurons = self.LayerNumber_2.value() #gets the number of neurons per layer for the NN
       
        
       print("Application Started ...")
       self.appThread = ApplicationThread(product, frequency, maxHolding, tradeSize, save_data, self.auth, self.url, self.apiKey, self.apiSecret, self.password, layers, neurons) #creates a Thread for the application
       self.appThread.start() #starts the application and runs the thread
       self.stopButton.setEnabled(True) #enables stop button
       self.startButton.setEnabled(False) #disables the start button to prevent running the application multiple times in parallel
 
       

