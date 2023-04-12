import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class restaran(QWidget):
    hisob=0
    def __init__(self):
        super().__init__()
        self.setMaximumSize(600,600)
        self.setMinimumSize(600,600)
        self.move(150,100)
        self.setWindowIcon(QIcon("D:\\python\\darslar\\membership.ico"))
        self.setWindowTitle("Ilxom")

        self.menyu=QLabel(self)
        self.menyu.setGeometry(300,0,150,50)
        self.menyu.setFont(QFont("Consolas",18))
        self.menyu.setText("MENYU")
        self.menyu.setStyleSheet("color: rgb(0,0,205);")


        self.taomlar=QComboBox(self)
        self.taomlar.addItems(["Taomlar","Osh: 23000","Kabob: 12000","Kuza shurva: 32000"])
        self.taomlar.setGeometry(0,60,260,50)
        self.taomlar.setFont(QFont("Calibri",18))
        self.taomlar.setStyleSheet("color: rgb(0,0,205)")        


        self.ichimlik=QComboBox(self)
        self.ichimlik.addItems(["Ichimliklar","Choy: 2000","Cocacola: 15000","Pepsi: 15000","Maxito: 20000","Iced tea: 20000"])
        self.ichimlik.setGeometry(270,60,260,50)
        self.ichimlik.setFont(QFont("Calibri",18))
        self.ichimlik.setStyleSheet("color: rgb(0,0,205)")  

        self.salat=QComboBox(self)
        self.salat.addItems(["Salatlar","Sezar:  15000","Baxor salati: 20000","Olvye: 15000","Suzma: 10000"])


        self.salat.setGeometry(0,120,260,50)
        self.salat.setFont(QFont("Calibri",18))
        self.salat.setStyleSheet("color: rgb(0,0,205)")  


        self.txtbox=QPushButton("Hisob",self)
        self.txtbox.setGeometry(0,180,200,80)
        self.txtbox.setFont(QFont("Consolas",16))
        self.txtbox.setStyleSheet("""
                        color: rgb(255,255,255);
                        background-color: black;
                        border-width: 3px;
                        border-style: inset;
                        border-radius: 40px;
                        border-color:  rgb(0,5,0);""")
        self.txtbox.clicked.connect(self.but_1)
    def but_1(self):
        f=open("restaran.txt","at+")
        

        restaran.hisob=self.taomlar[1]+self.salat[1]+self.ichimlik[1]
        print(restaran.hisob)
            


if __name__=="__main__":
    app=QApplication(sys.argv)
    projekt=restaran()
  
    projekt.show()
    sys.exit(app.exec_())


