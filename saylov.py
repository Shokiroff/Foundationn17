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
        self.setMinimumSize(1920,1200)
        self.setMaximumSize(1920,1200)
        self.tb=QTableWidget(self)
        self.setFont(QFont("Consolas",22))
        self.tb.setRowCount(3)
        self.tb.setColumnCount(6)
        self.tb.setGeometry(50,100,1700,600)
        self.con=mysql.connector.connect(user='root',password='root',
                                         host='localhost',database='saylov')
        self.baza_show()

        self.btn=QPushButton("Refresh",self)
        self.btn.setGeometry(700,735,250,50)
        self.btn.setFont(QFont("Calibri",18))
        self.btn.setStyleSheet("""border-color: rgb(0,255,0);
                              color: rgb(0,255,0);
                              border-radius: 25;
                              border-style: solid;
                              background-color: rgb(0,0,0);
                              border-width: 3px;""")
        self.btn.clicked.connect(self.baza_show) 


        self.lb=QLabel("\t\t****UPDATE DATABASE****",self)
        self.lb.setGeometry(200,510,1000,50)
        self.lb.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.lb1=QLabel("Tanlang",self)
        self.lb1.setGeometry(100,570,200,50)
        self.lb1.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.cmb=QComboBox(self)
        self.cmb.setGeometry(320,570,350,50)
        self.cmb.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        self.cmb.addItems(["id","shaxar","uchaska_raqami", "saylovchilar_soni", "uchaska_adresi","tel_raqam"])


        self.lb5=QLabel("Tanlang",self)
        self.lb5.setGeometry(700,570,200,50)
        self.lb5.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.cmb_1=QComboBox(self)
        self.cmb_1.setGeometry(905,570,350,50)
        self.cmb_1.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        self.cmb_1.addItems(["shaxar","uchaska_raqami", "saylovchilar_soni", "uchaska_adresi","tel_raqam"])
        
        
        self.lb2=QLabel("Eski qiymat:",self)
        self.lb2.setGeometry(100,625,270,50)
        self.lb2.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.txt1=QLineEdit(self)
        self.txt1.setGeometry(380,625,300,50)
        self.txt1.setStyleSheet("""border-color: rgb(0,255,255);
                              color: rgb(149,69,53);
                              border-width: 4px;
                              border-style: solid;
                              border-radius: 15;""")
        
        self.lb3=QLabel("Yangi qiymat:",self)
        self.lb3.setGeometry(700,625,280,50)
        self.lb3.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        
        self.txt2=QLineEdit(self)
        self.txt2.setGeometry(990,625,300,50)
        self.txt2.setStyleSheet("""border-color: rgb(0,255,255);
                              color: rgb(0,128,128);
                              border-width: 4px;
                              border-style: solid;
                              border-radius: 15;""")
        
        
        self.btn1=QPushButton("Update",self)
        self.btn1.setGeometry(430,735,250,50)
        self.btn1.setFont(QFont("Calibri",22))
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
        self.tb.setHorizontalHeaderLabels(["id","shaxar","uchaska_raqami", "saylovchilar_soni", "uchaska_adresi","tel_raqam"])
        head=self.tb.horizontalHeader()
        for x in range(6):
            head.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        
        self.kur=self.con.cursor()
        self.kur.execute("SELECT * from saylovv")
        res=self.kur.fetchall()
        n=len(res)
        self.tb.setRowCount(n)
        self.tb.setVerticalHeaderLabels(["","","","","","","",""])
        sch=0
        for x in res:
            self.tb.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.tb.setItem(sch,1,QTableWidgetItem(x[1]))
            self.tb.setItem(sch,2,QTableWidgetItem(str(x[2])))
            self.tb.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.tb.setItem(sch,4,QTableWidgetItem(x[4]))
            self.tb.setItem(sch,5,QTableWidgetItem(str(x[5])))
            sch+=1       


    def baza_update(self):
        self.kur=self.con.cursor()
        sql=f"""Update saylovv set {self.cmb_1.currentText()} = '{self.txt2.text()}' where {self.cmb.currentText()} = '{self.txt1.text()}'"""
        self.kur.execute(sql)
        self.con.commit()




app=QApplication(sys.argv)
ilova=baza_pyqt5()
ilova.show()
sys.exit(app.exec_())