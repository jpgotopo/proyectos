import sys
from PyQt5 import  uic
from PyQt5.QtCore import QAbstractTableModel, QVariant,  Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                                        QDialog, QTableView, QVBoxLayout)
from PyQt5.QtGui import QFont
import numpy as np

letters = {'p':0, 'b':1, 'k':2, 'g':3, 't':4, 'd':5, 'ʈ':6, 'ɖ':7, 'c':8, 'ɟ':9, 'q':10, 'G':11, 'ʡ':12, 'ʔ':13, 'm':14, 'ɱ':15, 'n':16, 'ɳ':17, 'ŋ':18, 'ɲ':19, 'N':20, 'ɸ':21, 'β':22, 'f':23, 'v':24, 'θ':25, 'ð':26, 's':27, 'z': 28, 'ʃ':29, 'ʒ':30, 'ʂ':31, 'ʐ':32, 'ç':33, 'ʝ':34, 'x':35, 'ɣ':36, 'χ':37, 'ħ':38, 'ʕ':39, 'ʜ':40, 'ʢ':41, 'h':42, 'ɦ':43, 'ʧ':44, 'ʦ':45, 'ʤ':46, 'ʣ':47, 'j':48, 'w':49, 'ɰ':50, 'V':51, 'ʁ':52, 'R':53, 'ɹ':54, 'ɻ':55, 'B':56, 'ⱱ':57, 'ɾ':58, 'ɽ':59, 'r':60, 'ɬ':61, 'ɮ':62, 'l':63, 'ɭ':64, 'L':65, 'ʎ':66, 'ɺ':67}
features = {0:'sonoro', 1:'sonorante', 2:'obstruyente', 3:'consonantal', 4:'plosiva',
5:'continuante', 6:'nasal', 7:'labial', 8:'redondo', 9:'coronal',
10:'estridente', 11:'anterior', 12:'distribuido', 13:'lateral', 14:'dorsal',
15:'alto', 16:'posterior', 17:'bajo', 18:'Silabico', 19:'Retraido', 20: 'Soltar Det/Afr', 21: 'Glot Constricta', 22: 'Glot Ext (Asp)'}
#{'p':0, 'b':1, 'k':2, 'g':3, 't':4, 'd':5, 'ʈ':6, 'ɖ':7, 'c':8, 'ɟ':9, 'q':10, 'G':11, 'ʡ':12, 'ʔ':13, 'm':14, 'ɱ':15, 'n':16, 'ɳ':17, 'ŋ':18, 'ɲ':19, 'N':20, 'ɸ':21, 'β':22, 'f':23, 'v':24, 'θ':25, 'ð':26, 's':27, 'z': 28, 'ʃ':29, 'ʒ':30, 'ʂ':31, 'ʐ':32, 'ç':33, 'ʝ':34, 'x':35, 'ɣ':36, 'χ':37, 'ħ':38, 'ʕ':39, 'ʜ':40, 'ʢ':41, 'h':42, 'ɦ':43, 'ʧ':44, 'ʦ':45, 'ʤ':46, 'dz':47, 'j':48, 'w':49, 'ɰ':50, 'V':51, ʁ':52, 'R':53, 'ɹ':54, 'ɻ':55, 'B':56, 'ⱱ':57, 'ɾ':58, 'ɽ':59, 'r':60, 'ɬ':61, 'ɮ':62, 'l':63, 'ɭ':64, 'L':65, 'ʎ':66, 'ɺ':67}

values = {0:'-', 1:'+'}

matriz=[[0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1], #sonoro
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1], #sonorante
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0], #obstruyente
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #consonantal
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #plosiva
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1], #continuante
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #nasal
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0], #labial
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1], #redondo
        [0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1], #coronal
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #estridente
        [1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1], #anterior
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], #distribuido
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1], #lateral
        [0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0], #dorsal
        [0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0], #alto
        [0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0], #posterior
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #bajo
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #silabico
        [0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0], #retraido
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Soltar Det/Afr
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Glot Constricta
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] #Glot Ext (Asp)

t_matrix = np.transpose(matriz)

class MainWindow(QMainWindow):
    """docstring for ClassName"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.lista = set()
        self.initUI()

    def initUI(self):
        uic.loadUi('phoneanalyzergui.ui', self)
  

        self.buttonGroup.buttonToggled.connect(self.onClicked)
        self.comparar_btn.clicked.connect(self.comparar)
        self.limpiar_btn.clicked.connect(self.limpiar)
        self.show()

    def onClicked(self, button,  checked):
        if checked:
            self.lista.add(button.text().replace("&", ""))
        else:
            self.lista.discard(button.text().replace("&", ""))

    def comparar(self):
        t_selected_matrix = np.transpose([t_matrix[letters[elemento]] for elemento in self.lista])
        common_features = [[features[i],list[0]] for i, list in enumerate(t_selected_matrix)
                             if all(x == list[0] for x in list)]

        rows = [(feature,  values[value]) for feature,  value in common_features]
        self._create_table(rows)

    def _create_table(self,  data):
        if data:
            dialog = Resultados(data)
            dialog.exec_()

    def limpiar(self):
        for button in self.buttonGroup.buttons():
            button.setChecked(False)

class Resultados(QDialog):
    """docstring for ClassName"""
    def __init__(self,  data):
        super(Resultados, self).__init__()
        self.data = data
        print(self.data)
        self.initUI()

    def initUI(self):
        table = self.create_table() 
        layout = QVBoxLayout()
        layout.addWidget(table) 
        self.setLayout(layout)
        
         
  
    def create_table(self):
        table_view = QTableView()
        header = ['Rasgos', 'Valor']
        table_model = MyTableModel(self.data, header, self) 
        table_view.setModel(table_model)
        
        table_view.setMinimumSize(400, 300)
        table_view.setShowGrid(False)
        table_view.setFont(QFont("Courier New", 12))
        vheader = table_view.verticalHeader()
        vheader.setVisible(False)
        hheader = table_view.horizontalHeader()
        hheader.setStretchLastSection(True)
        table_view.resizeColumnsToContents()
        
        for row in range(len(self.data)):
            table_view.setRowHeight(row, 20)
            
        return table_view

class MyTableModel(QAbstractTableModel): 
    def __init__(self, data, header, parent=None, *args): 
        QAbstractTableModel.__init__(self, parent, *args) 
        self.rows_data = data
        self.header_data = header
 
    def rowCount(self, parent): 
        return len(self.rows_data) 
 
    def columnCount(self, parent): 
        return len(self.rows_data[0]) 
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        return QVariant(self.rows_data[index.row()][index.column()]) 

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header_data[col])
        return QVariant()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())