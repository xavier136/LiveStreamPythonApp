import csv
import numpy
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets, QtGui
import datetime
from matplotlib.ticker import NullFormatter, MultipleLocator, FormatStrFormatter
from matplotlib.dates import DateFormatter, MinuteLocator
import matplotlib.ticker as ticker


class Report(object):
    """class that generates the report and the associated metrics"""

    def __init__(self, trading_file):
        self.trading_file = trading_file
        self.strat_return = 0
        self.strat_vol = 0
        self.drawdown = 0
        self.start_date = None
        self.end_date = None
        self.posGraph = None
        self.cumul_ret = None
        self.cumulRet = None
        self.posEvol = None

    def read_file(self):
        self.dates = []
        self.market_mids = []
        self.holdings = []
        self.values = []

        with open(self.trading_file, 'r') as f:
            file_reader = csv.reader(f)
            for line in file_reader:
                try:
                    self.market_mids.append(float(line[4]))
                    self.holdings.append(float(line[5]))
                    self.values.append(float(line[6]))
                    self.dates.append(line[0])

                except Exception:
                    pass
        self.start_date = self.dates[0]
        self.end_date = self.dates[-1]

    def compute_return(self):
        self.strat_return = round(((self.values[-1] / self.values[0]) - 1) * 100, 5)

    def compute_volatility(self):
        self.strat_vol = round(numpy.std(self.values) * 100, 3)
    
    def compute_maxDD(self):
        self.cumul_ret = [x / self.values[0] for x in self.values]
        if  self.strat_vol == 0:
            self.drawdown = 0
        else:
            i = numpy.argmax(numpy.maximum.accumulate(self.cumul_ret) - self.cumul_ret)
            if i == 0:
                self.drawdown =0
            else:
                j = numpy.argmax(self.cumul_ret[:i])
                self.drawdown = round((self.cumul_ret[j] - self.cumul_ret[i]) * 100, 3)

    def cumul_graph(self):
        scene = QtWidgets.QGraphicsScene()
        dates = [datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') for x in self.dates]
        plt.plot(dates, self.cumul_ret)
        plt.gca().yaxis.set_minor_formatter(NullFormatter())
        plt.gca().yaxis.set_major_locator( MultipleLocator(base=0.0001) )
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
        plt.gca().xaxis.set_minor_formatter(NullFormatter())
        plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
        plt.gca().xaxis.set_major_locator( MinuteLocator(interval = 15) )
        plt.savefig('Graphs/cumulGraph.png')
        pic = QtGui.QPixmap("Graphs/cumulGraph.png").scaled(400, 300)
        scene.addItem(QtWidgets.QGraphicsPixmapItem(pic)) 
        self.cumulRet = scene

    def pos_graph(self):
        scene = QtWidgets.QGraphicsScene()
        dates = [datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') for x in self.dates]
        plt.plot(dates, self.holdings)
        plt.gca().yaxis.set_minor_formatter(NullFormatter())
        plt.gca().yaxis.set_major_locator( MultipleLocator(base=0.1) )
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
        plt.gca().xaxis.set_minor_formatter(NullFormatter())
        plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
        plt.gca().xaxis.set_major_locator( MinuteLocator(interval = 15) )
        plt.twinx()
        plt.plot(dates, self.market_mids)
        plt.gca().yaxis.set_major_locator( MultipleLocator(base=10) )
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
        plt.savefig('Graphs/posGraph.png')
        pic = QtGui.QPixmap("Graphs/posGraph.png").scaled(400, 300)
        scene.addItem(QtWidgets.QGraphicsPixmapItem(pic)) 
        self.posEvol = scene

        
                

            
