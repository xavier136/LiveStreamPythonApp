import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from GUIWindow import GUIWindow
from PyQt5 import QtWidgets
import sys

def main():
  app = QtWidgets.QApplication(sys.argv)
  form = GUIWindow()
  form.show()
  app.exec()

if __name__ == "__main__":
   main()