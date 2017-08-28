# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullapplayout.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.setWindowModality(QtCore.Qt.NonModal)
        StackedWidget.resize(800, 600)
        StackedWidget.setMinimumSize(QtCore.QSize(800, 600))
        StackedWidget.setMaximumSize(QtCore.QSize(800, 600))
        StackedWidget.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(Images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.WelcomePage = QtWidgets.QWidget()
        self.WelcomePage.setMinimumSize(QtCore.QSize(800, 600))
        self.WelcomePage.setMaximumSize(QtCore.QSize(800, 600))
        self.WelcomePage.setObjectName("WelcomePage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WelcomePage)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.WelcomePage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.WelcomePage)
        self.label_4.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.WelcomePage)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.simulationModeButton = QtWidgets.QPushButton(self.WelcomePage)
        self.simulationModeButton.setObjectName("simulationModeButton")
        self.gridLayout.addWidget(self.simulationModeButton, 8, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.WelcomePage)
        self.label_3.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)
        self.sandBoxModeButton = QtWidgets.QPushButton(self.WelcomePage)
        self.sandBoxModeButton.setObjectName("sandBoxModeButton")
        self.gridLayout.addWidget(self.sandBoxModeButton, 13, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.WelcomePage)
        self.label_6.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 16, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.WelcomePage)
        self.label_7.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 15, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 14, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.WelcomePage)
        self.label_5.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 1, 1, 1)
        self.authentificatedModeButton = QtWidgets.QPushButton(self.WelcomePage)
        self.authentificatedModeButton.setObjectName("authentificatedModeButton")
        self.gridLayout.addWidget(self.authentificatedModeButton, 17, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 18, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        StackedWidget.addWidget(self.WelcomePage)
        self.AuthPage = QtWidgets.QWidget()
        self.AuthPage.setMinimumSize(QtCore.QSize(800, 600))
        self.AuthPage.setMaximumSize(QtCore.QSize(800, 600))
        self.AuthPage.setObjectName("AuthPage")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.AuthPage)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.AuthPage)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.AuthPage)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem12, 2, 1, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.AuthPage)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout_2.addWidget(self.connectButton, 8, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.aPIKeyLabel = QtWidgets.QLabel(self.AuthPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.aPIKeyLabel.setFont(font)
        self.aPIKeyLabel.setObjectName("aPIKeyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.aPIKeyLabel)
        self.aPIKeyLineEdit = QtWidgets.QLineEdit(self.AuthPage)
        self.aPIKeyLineEdit.setObjectName("aPIKeyLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aPIKeyLineEdit)
        self.aPISecretLabel = QtWidgets.QLabel(self.AuthPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.aPISecretLabel.setFont(font)
        self.aPISecretLabel.setObjectName("aPISecretLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.aPISecretLabel)
        self.aPISecretLineEdit = QtWidgets.QLineEdit(self.AuthPage)
        self.aPISecretLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.aPISecretLineEdit.setObjectName("aPISecretLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.aPISecretLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.AuthPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.AuthPage)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 6, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem13, 4, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem14, 7, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 9, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        StackedWidget.addWidget(self.AuthPage)
        self.AlgoPage = QtWidgets.QWidget()
        self.AlgoPage.setMinimumSize(QtCore.QSize(800, 600))
        self.AlgoPage.setMaximumSize(QtCore.QSize(800, 600))
        self.AlgoPage.setObjectName("AlgoPage")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.AlgoPage)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_16 = QtWidgets.QLabel(self.AlgoPage)
        self.label_16.setEnabled(True)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 8, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem16, 9, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem17, 16, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem18, 2, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 1, 2, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.cryptoCurrencyLabel = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cryptoCurrencyLabel.setFont(font)
        self.cryptoCurrencyLabel.setObjectName("cryptoCurrencyLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cryptoCurrencyLabel)
        self.fontComboBox = QtWidgets.QFontComboBox(self.AlgoPage)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.maxHoldingUnitOfCryptoCurrencyLabel = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maxHoldingUnitOfCryptoCurrencyLabel.setFont(font)
        self.maxHoldingUnitOfCryptoCurrencyLabel.setObjectName("maxHoldingUnitOfCryptoCurrencyLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxHoldingUnitOfCryptoCurrencyLabel)
        self.maxHoldingUnitOfCryptoCurrencyDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.AlgoPage)
        self.maxHoldingUnitOfCryptoCurrencyDoubleSpinBox.setMinimum(0.01)
        self.maxHoldingUnitOfCryptoCurrencyDoubleSpinBox.setSingleStep(0.01)
        self.maxHoldingUnitOfCryptoCurrencyDoubleSpinBox.setObjectName("maxHoldingUnitOfCryptoCurrencyDoubleSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxHoldingUnitOfCryptoCurrencyDoubleSpinBox)
        self.volumePerTradeUnitOfCryptoCurrencyLabel = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.volumePerTradeUnitOfCryptoCurrencyLabel.setFont(font)
        self.volumePerTradeUnitOfCryptoCurrencyLabel.setObjectName("volumePerTradeUnitOfCryptoCurrencyLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.volumePerTradeUnitOfCryptoCurrencyLabel)
        self.volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.AlgoPage)
        self.volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox.setMinimum(0.01)
        self.volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox.setSingleStep(0.01)
        self.volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox.setObjectName("volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.volumePerTradeUnitOfCryptoCurrencyDoubleSpinBox)
        self.tradeFrequencyInSecondsLabel = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tradeFrequencyInSecondsLabel.setFont(font)
        self.tradeFrequencyInSecondsLabel.setObjectName("tradeFrequencyInSecondsLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tradeFrequencyInSecondsLabel)
        self.tradeFrequencyInSecondsSpinBox = QtWidgets.QSpinBox(self.AlgoPage)
        self.tradeFrequencyInSecondsSpinBox.setMinimum(1)
        self.tradeFrequencyInSecondsSpinBox.setObjectName("tradeFrequencyInSecondsSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tradeFrequencyInSecondsSpinBox)
        self.saveDataLabel = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveDataLabel.setFont(font)
        self.saveDataLabel.setObjectName("saveDataLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.saveDataLabel)
        self.saveDataCheckBox = QtWidgets.QCheckBox(self.AlgoPage)
        self.saveDataCheckBox.setObjectName("saveDataCheckBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.saveDataCheckBox)
        self.gridLayout_3.addLayout(self.formLayout_2, 6, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem20, 4, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.AlgoPage)
        self.startButton.setObjectName("startButton")
        self.gridLayout_3.addWidget(self.startButton, 14, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.AlgoPage)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem22, 7, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem23, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.AlgoPage)
        self.label_11.setEnabled(True)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.AlgoPage)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_3.addWidget(self.stopButton, 15, 1, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_4.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setObjectName("formLayout_4")
        self.cryptoCurrencyLabel_2 = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cryptoCurrencyLabel_2.setFont(font)
        self.cryptoCurrencyLabel_2.setObjectName("cryptoCurrencyLabel_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cryptoCurrencyLabel_2)
        self.LayerNumber = QtWidgets.QSpinBox(self.AlgoPage)
        self.LayerNumber.setMinimum(1)
        self.LayerNumber.setObjectName("LayerNumber")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LayerNumber)
        self.maxHoldingUnitOfCryptoCurrencyLabel_2 = QtWidgets.QLabel(self.AlgoPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maxHoldingUnitOfCryptoCurrencyLabel_2.setFont(font)
        self.maxHoldingUnitOfCryptoCurrencyLabel_2.setObjectName("maxHoldingUnitOfCryptoCurrencyLabel_2")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxHoldingUnitOfCryptoCurrencyLabel_2)
        self.LayerNumber_2 = QtWidgets.QSpinBox(self.AlgoPage)
        self.LayerNumber_2.setMinimum(1)
        self.LayerNumber_2.setProperty("value", 10)
        self.LayerNumber_2.setObjectName("LayerNumber_2")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LayerNumber_2)
        self.gridLayout_3.addLayout(self.formLayout_4, 10, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem24, 13, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_3)
        StackedWidget.addWidget(self.AlgoPage)
        self.ResultPage = QtWidgets.QWidget()
        self.ResultPage.setMinimumSize(QtCore.QSize(800, 600))
        self.ResultPage.setMaximumSize(QtCore.QSize(800, 600))
        self.ResultPage.setObjectName("ResultPage")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ResultPage)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_13 = QtWidgets.QLabel(self.ResultPage)
        self.label_13.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.ResultPage)
        self.label_14.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cumulReturn = QtWidgets.QGraphicsView(self.ResultPage)
        self.cumulReturn.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cumulReturn.setObjectName("cumulReturn")
        self.horizontalLayout_2.addWidget(self.cumulReturn)
        self.positionEvolution = QtWidgets.QGraphicsView(self.ResultPage)
        self.positionEvolution.setObjectName("positionEvolution")
        self.horizontalLayout_2.addWidget(self.positionEvolution)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem25, 3, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(50, -1, 50, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_17 = QtWidgets.QLabel(self.ResultPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setWordWrap(False)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.startDate = QtWidgets.QLabel(self.ResultPage)
        self.startDate.setText("")
        self.startDate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.startDate.setObjectName("startDate")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startDate)
        self.label_18 = QtWidgets.QLabel(self.ResultPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.endDate = QtWidgets.QLabel(self.ResultPage)
        self.endDate.setText("")
        self.endDate.setObjectName("endDate")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endDate)
        self.label_20 = QtWidgets.QLabel(self.ResultPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.stratReturn = QtWidgets.QLabel(self.ResultPage)
        self.stratReturn.setText("")
        self.stratReturn.setObjectName("stratReturn")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stratReturn)
        self.label_22 = QtWidgets.QLabel(self.ResultPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.stratVol = QtWidgets.QLabel(self.ResultPage)
        self.stratVol.setText("")
        self.stratVol.setObjectName("stratVol")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.stratVol)
        self.label_24 = QtWidgets.QLabel(self.ResultPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.stratMaxDrawDown = QtWidgets.QLabel(self.ResultPage)
        self.stratMaxDrawDown.setText("")
        self.stratMaxDrawDown.setObjectName("stratMaxDrawDown")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stratMaxDrawDown)
        self.gridLayout_4.addLayout(self.formLayout_3, 8, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.ResultPage)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_12.setFont(font)
        self.label_12.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem26, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.ResultPage)
        self.label_15.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 7, 0, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem27, 6, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_4)
        StackedWidget.addWidget(self.ResultPage)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "CryptoTrader"))
        self.label_2.setText(_translate("StackedWidget", "Please Select a Mode to run the software:"))
        self.label_4.setText(_translate("StackedWidget", "This mode enables you to run your strategy in a non authentificated environment. Therefore no trading is required nevertheless the environment isn\'t fully realistic as it assumes trading at mid price and doesn\'t account for market impact. (Good for testing new strategies ideas)"))
        self.label.setText(_translate("StackedWidget", "Crypto Currencies Algorithmic Trader"))
        self.simulationModeButton.setText(_translate("StackedWidget", "Simulation Mode"))
        self.label_3.setText(_translate("StackedWidget", "- Simulation Mode: "))
        self.sandBoxModeButton.setText(_translate("StackedWidget", "SandBox Mode"))
        self.label_6.setText(_translate("StackedWidget", "This mode enables you to run your strategy using your real GDAX Trading account. This mode should be used only once your strategy has been proof tested through the two other modes (Trading Involves risks, invest only what you are willing to lose)"))
        self.label_7.setText(_translate("StackedWidget", "- Authentificated  Mode: "))
        self.label_5.setText(_translate("StackedWidget", "- Authentificated SandBox Mode: "))
        self.authentificatedModeButton.setText(_translate("StackedWidget", "Authentificated Mode"))
        self.label_8.setText(_translate("StackedWidget", "Authentification"))
        self.label_9.setText(_translate("StackedWidget", "Please enter your GDAX Details:"))
        self.connectButton.setText(_translate("StackedWidget", "Connect"))
        self.aPIKeyLabel.setText(_translate("StackedWidget", "API Key:"))
        self.aPISecretLabel.setText(_translate("StackedWidget", "API Secret:"))
        self.passwordLabel.setText(_translate("StackedWidget", "Password:"))
        self.label_16.setText(_translate("StackedWidget", "Please enter the Neural Network\'s parameters:"))
        self.cryptoCurrencyLabel.setText(_translate("StackedWidget", "Crypto Currency"))
        self.fontComboBox.setCurrentText(_translate("StackedWidget", "BTC-USD"))
        self.maxHoldingUnitOfCryptoCurrencyLabel.setText(_translate("StackedWidget", "Max Holding (unit of crypto currency)"))
        self.volumePerTradeUnitOfCryptoCurrencyLabel.setText(_translate("StackedWidget", "Volume per Trade (unit of crypto currency)"))
        self.tradeFrequencyInSecondsLabel.setText(_translate("StackedWidget", "Trade Frequency (in seconds)"))
        self.saveDataLabel.setText(_translate("StackedWidget", "SaveData"))
        self.startButton.setText(_translate("StackedWidget", "Start"))
        self.label_10.setText(_translate("StackedWidget", "Algorithm Setting Menu"))
        self.label_11.setText(_translate("StackedWidget", "Please detail your strategy\'s parameters:"))
        self.stopButton.setText(_translate("StackedWidget", "Stop"))
        self.cryptoCurrencyLabel_2.setText(_translate("StackedWidget", "Number of Layers"))
        self.maxHoldingUnitOfCryptoCurrencyLabel_2.setText(_translate("StackedWidget", "Number of Neurons per Layer"))
        self.label_13.setText(_translate("StackedWidget", "- Cumulative Return Index"))
        self.label_14.setText(_translate("StackedWidget", "- Crypto Currency Holdings in units"))
        self.label_17.setText(_translate("StackedWidget", "Start: "))
        self.label_18.setText(_translate("StackedWidget", "End: "))
        self.label_20.setText(_translate("StackedWidget", "Return: "))
        self.label_22.setText(_translate("StackedWidget", "Volatility: "))
        self.label_24.setText(_translate("StackedWidget", "Max Drawdown: "))
        self.label_12.setText(_translate("StackedWidget", "Report"))
        self.label_15.setText(_translate("StackedWidget", "- Strategy\'s Details"))

