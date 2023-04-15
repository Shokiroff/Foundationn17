import os 
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system("cls")

class ilova(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMaximumSize(840,500)
        self.setMinimumSize(840,500)
        
        self.tana1=QPushButton("",self)
        self.tana1.setFont(QFont("Calibri",18))
        self.tana1.move(30,40)
        self.tana1.resize(500,70)
        self.tana1.clicked.connect(self.rangni_tanla1)
        
        
        
        self.tana2=QPushButton("",self)
        self.tana2.setFont(QFont("Calibri",18))
        self.tana2.move(30,108)
        self.tana2.resize(500,70)
        self.tana2.clicked.connect(self.rangni_tanla2)
        
        
        self.tana3=QPushButton("",self)
        self.tana3.setFont(QFont("Calibri",18))
        self.tana3.move(30,177)
        self.tana3.resize(500,70)
        self.tana3.clicked.connect(self.rangni_tanla3)
                
        self.btn1=QPushButton("Click",self)
        self.btn1.setFont(QFont("Calibri",18))
        self.btn1.setStyleSheet("""
                        border-width: 3px;
                        border-radius: 15px;
                        border-color: rgb(0,255,0);
                        color: rgb(0,128,128);
                        background-color: rgb(0,0,0);
                        border-style: solid;
                               """)
        self.btn1.move(500,300)
        self.btn1.resize(200,50)
        self.btn1.clicked.connect(self.show_message)
    
    def rangni_tanla1(self):
        self.color1=QColorDialog().getColor()
        if self.color1.isValid():
            print(self.color1.name())
            self.tana1.setStyleSheet(f"background-color: {self.color1.name()}")
            
    def rangni_tanla2(self):
        self.color2=QColorDialog().getColor()
        if self.color2.isValid():
            print(self.color2.name())
            self.tana2.setStyleSheet(f"background-color: {self.color2.name()}")
    def rangni_tanla3(self):
        self.color3=QColorDialog().getColor()
        if self.color3.isValid():
            print(self.color3.name())
            self.tana3.setStyleSheet(f"background-color: {self.color3.name()}")
            
            
    def show_name(self):
        if   self.color1.name()=="#0000ff" and self.color2.name()=="#ffffff" and self.color3.name()=="#00ff00":
            return "Uzbekistan"
        if   self.color1.name()=="#000000" and self.color2.name()=="#ff0000" and self.color3.name()=="#ffff00":
            return "Germany"
        if   self.color1.name()=="#ffffff" and self.color2.name()=="#0000ff" and self.color3.name()=="#ff0000":
            return "Russia"
        if   self.color1.name()=="#00007f" and self.color2.name()=="#000000" and self.color3.name()=="#ffffff":
            return "Estonia"
        if   self.color1.name()=="#ff0000" and self.color2.name()=="#ffffff" and self.color3.name()=="#00007f":
            return "Croatia"
        else:
            return "Men bunday davlatni bilmayman"
    def show_message(self):
        xabar = QMessageBox(self)
        xabar.setFont(QFont("Times New Roman", 15))
        xabar.setText(self.show_name())
        xabar.setWindowTitle("Davlat nomi")
        xabar.setIcon(QMessageBox.Information)
        xabar.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        xabar.exec_()
    
    
    
    
   
        
app=QApplication(sys.argv)
project=ilova()
project.show()
sys.exit(app.exec_())       