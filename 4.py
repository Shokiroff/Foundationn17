import os
import sys
from PyQt5 import QtGui, QtWidgets, QtCore

class Calculator:
    def __init__(self):
        self.app = None
        self.widget = None
        self.txtbox = None

    def info(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.wiget = QtWidgets.QWidget()
        self.wiget.setGeometry(1400, 100, 500,500)
        self.wiget.setMinimumSize(500, 430)
        self.wiget.setMaximumSize(500, 430)
        

        ##

        self.txtbox = QtWidgets.QLineEdit(self.wiget)
        self.txtbox.setText("0")
        self.txtbox.setGeometry(0, 0,500,80)
        self.txtbox.setFont(QtGui.QFont("Consolas",20))
        self.txtbox.setStyleSheet("""border-width: 3 px;
                        border-style: solid;
                        border-color: rgb(131,137,150);
                        background-color: rgb(131,137,150);""")
                            
        self.txtbox.setAlignment(QtCore.Qt.AlignRight)

        ##

        self.btn_ON = QtWidgets.QPushButton("ON", self.wiget)
        self.btn_ON.setFont(QtGui.QFont("Consalas", 20))
        self.btn_ON.setGeometry(0, 80, 250, 60)
        self.btn_ON.setStyleSheet("""background-color: rgb(80,200,120);
                        border-width: 3px;
                        border-color:  rgb(80,200,120);""")
        
        ##

        self.btn_C = QtWidgets.QPushButton("C", self.wiget)
        self.btn_C.setFont(QtGui.QFont("Consalas", 20))
        self.btn_C.setGeometry(0, 80, 250, 60)
        self.btn_C.move(250, 80)
        self.btn_C.setStyleSheet("""background-color: rgb(80,200,120);
                        border-width: 3px;
                        border-color:  rgb(80,200,120);""")

        ##

        self.btn_1 = QtWidgets.QPushButton("1", self.wiget)
        self.btn_1.setFont(QtGui.QFont("Consalas", 20))
        self.btn_1.setGeometry(0, 140, 167, 70)
        self.btn_1.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 2px;""")
        
        self.btn_2 = QtWidgets.QPushButton("2", self.wiget)
        self.btn_2.setFont(QtGui.QFont("Consalas", 20))
        self.btn_2.setGeometry(0, 140, 167, 70)
        self.btn_2.move(167,140)
        self.btn_2.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 2px;""")
        
        self.btn_3 = QtWidgets.QPushButton("3", self.wiget)
        self.btn_3.setFont(QtGui.QFont("Consalas", 20))
        self.btn_3.setGeometry(0, 140, 166, 70)
        self.btn_3.move(334,140)
        self.btn_3.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 2px;""")
        
        self.btn_4 = QtWidgets.QPushButton("4", self.wiget)
        self.btn_4.setFont(QtGui.QFont("Consalas", 20))
        self.btn_4.setGeometry(0, 210, 167, 70)
        self.btn_4.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 2px;""")
        
        self.btn_5 = QtWidgets.QPushButton("5", self.wiget)
        self.btn_5.setFont(QtGui.QFont("Consalas", 20))
        self.btn_5.setGeometry(0, 210, 167, 70)
        self.btn_5.move(167,210)
        self.btn_5.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 2px;""")
        
        self.btn_6 = QtWidgets.QPushButton("6", self.wiget)
        self.btn_6.setFont(QtGui.QFont("Consalas", 20))
        self.btn_6.setGeometry(0, 210, 166, 70)
        self.btn_6.move(334,210)
        self.btn_6.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 2px;""")
        
        self.btn_7 = QtWidgets.QPushButton("7", self.wiget)
        self.btn_7.setFont(QtGui.QFont("Consalas", 20))
        self.btn_7.setGeometry(0, 280, 167, 70)
        self.btn_7.setStyleSheet("""background-color: rgb(240,156,104);
                      border-width: 2px;""")
        
        self.btn_8 = QtWidgets.QPushButton("8", self.wiget)
        self.btn_8.setFont(QtGui.QFont("Consalas", 20))
        self.btn_8.setGeometry(0, 280, 167, 70)
        self.btn_8.move(167,280)
        self.btn_8.setStyleSheet("""background-color: rgb(240,156,104);
                       border-width: 2px;""")
        
        self.btn_9 = QtWidgets.QPushButton("9", self.wiget)
        self.btn_9.setFont(QtGui.QFont("Consalas", 20))
        self.btn_9.setGeometry(0, 280, 166, 70)
        self.btn_9.move(334,280)
        self.btn_9.setStyleSheet("""background-color: rgb(240,156,104);
                       border-width: 2px;""")
        
        self.btn_0 = QtWidgets.QPushButton("0", self.wiget)
        self.btn_0.setFont(QtGui.QFont("Consalas", 20))
        self.btn_0.setGeometry(0, 350, 250, 80)
        self.btn_0.setStyleSheet("""background-color: rgb(240,156,104);
                        border-width: 3px;""")

        self.btn_10 = QtWidgets.QPushButton("=", self.wiget)
        self.btn_10.setFont(QtGui.QFont("Consalas", 20))
        self.btn_10.setGeometry(0, 350, 250, 80)
        self.btn_10.move(250, 350)
        self.btn_10.setStyleSheet("""background-color: rgb(188,30,240);
                        border-width: 3px;""")

        ##

        self.wiget.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    cal = Calculator()
    cal.info()