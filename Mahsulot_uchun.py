from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import sys
import mysql.connector
os.system("cls")
class baza_pyqt5(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(1020,900)
        self.setMaximumSize(1020,900)
        self.tb=QTableWidget(self)
        self.setFont(QFont("Consolas",22))
        self.tb.setRowCount(3)
        self.tb.setColumnCount(4)
        self.tb.setGeometry(50,50,700,300)
        self.con=mysql.connector.connect(user='root',password='root',
                                          host='localhost',database='bozor')
        self.baza_show()
        
        self.btn=QPushButton("Refresh",self)
        self.btn.setGeometry(800,175,200,50)
        self.btn.setFont(QFont("Calibri",18))
        self.btn.setStyleSheet("""border-color: rgb(0,255,0);
                              color: rgb(0,255,0);
                              border-radius: 25;
                              border-style: solid;
                              background-color: rgb(0,0,0);
                              border-width: 3px;""")
        self.btn.clicked.connect(self.baza_show)
        
        
    #     #malumotni o'zgaritish
        
        self.lb=QLabel("\t\t****UPDATE DATABASE****",self)
        self.lb.setGeometry(100,400,600,50)
        self.lb.setFont(QFont("Consolas",20))
        self.lb.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.lb1=QLabel("Tanlang",self)
        self.lb1.setGeometry(40,450,200,50)
        self.lb1.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.cmb=QComboBox(self)
        self.cmb.setGeometry(220,450,250,50)
        self.cmb.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        self.cmb.addItems(["name","price","country"])
        

        
        self.lb2=QLabel("Kiriting:",self)
        self.lb2.setFont(QFont("Consolas",15))
        self.lb2.setGeometry(40,500,270,50)
        self.lb2.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.txt1=QLineEdit(self)
        self.txt1.setGeometry(220,500,300,50)
        self.txt1.setStyleSheet("""border-color: rgb(0,255,255);
                              color: rgb(149,69,53);
                              border-width: 4px;
                              border-style: solid;
                              border-radius: 15;""")
        
        self.cmb1=QComboBox(self)
        self.cmb1.setGeometry(600,450,250,50)
        self.cmb1.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        self.cmb1.addItems(["name","price","country"])
        
        self.lb3=QLabel("Qiymat:",self)
        self.lb3.setGeometry(40,570,270,50)
        self.lb3.setFont(QFont("Consolas",15))
        self.lb3.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.txt2=QLineEdit(self)
        self.txt2.setGeometry(600,500,300,50)
        self.txt2.setStyleSheet("""border-color: rgb(0,255,255);
                              color: rgb(0,128,128);
                              border-width: 4px;
                              border-style: solid;
                              border-radius: 15;""")
        
        
        self.btn1=QPushButton("Update",self)
        self.btn1.setGeometry(300,630,250,50)
        self.btn1.setFont(QFont("Calibri",18))
        self.btn1.setStyleSheet("""border-color: rgb(0,255,0);
                              color: rgb(0,255,0);
                              border-radius: 25;
                              border-style: solid;
                              background-color: rgb(0,0,0);
                              border-width: 3px;""")
        self.btn1.clicked.connect(self.baza_update)
        
    def baza_show(self):
        self.tb.setFont(QFont("Consolas",22))
        self.tb.setStyleSheet("""border-color: rgb(0,0,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;
                              background-color: rgb(192,192,192);""")
        self.tb.setHorizontalHeaderLabels(["ID", "Nomi", "Davlat", "Narxi"])
        head=self.tb.horizontalHeader()
        for x in range(4):
            head.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        
        self.kur=self.con.cursor()
        self.kur.execute("SELECT * from mahsulot")
        res=self.kur.fetchall()
        n=len(res)
        self.tb.setRowCount(n)
        self.tb.setVerticalHeaderLabels(["","","","","","","",""])
        sch=0
        for x in res:
            self.tb.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.tb.setItem(sch,1,QTableWidgetItem(x[1]))
            self.tb.setItem(sch,2,QTableWidgetItem(x[2]))
            self.tb.setItem(sch,3,QTableWidgetItem(str(x[3])))
            sch+=1
            
            
    def baza_update(self):
        
        tanlash=self.cmb.currentText()
        tanlash2=self.cmb1.currentText()
        eski=self.txt1.text()
        yangi=self.txt2.text()
        self.kur=self.con.cursor()
        self.kur.execute(f"UPDATE mahsulot SET {tanlash2} = '{yangi}' where {tanlash}='{eski}'")
        self.con.commit()

    
            
            
            
        

app=QApplication(sys.argv)
ilova=baza_pyqt5()
ilova.show()
sys.exit(app.exec_())