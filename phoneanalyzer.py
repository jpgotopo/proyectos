#import random
#import sys
#import os

#fono =[["-", "-", "-", "-"], ["-", "+", "+", "-"], ["-", "+", "+", "-"], ["-", "+", "+", "-"]]
#print(fono[2][2])

#for i = 0 in range(0,4)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
form_class = uic.loadUiType("FeatureAnalyzer.ui")[0]
#Clase Heredada de QMainWindow (Constructor de Ventana)
class MainWindow(QtWidgets.QMainWindow, form_class):
    """Metodo constructor de la clase"""
    def __init__(self,parent=None):
        #iniciar el objeto QMainWindow
        QtWidgets.QMainWindow.__init__(self, parent);
        self.setupUi(self)
        #super(MainWindow,self).__init__(*args)
        #loadUi('FeatureAnalyzer.ui',self)
        self.setWindowTitle('Analizador de Rasgos')

#Instancia para iniciar una aplicacion
app = QtWidgets.QApplication(sys.argv)
widget = MainWindow(None)
#widget.MyWindowClass(None)
widget.show()
app.exec_()
