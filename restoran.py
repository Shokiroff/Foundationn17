import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class restaran(QWidget):
    hisob1=0
    hisob2=0
    hisob3=0
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1700,900)
        self.setMinimumSize(1700,900)
        self.move(150,100)
        self.setWindowIcon(QIcon("D:\\python\\darslar\\membership.ico"))
        self.setWindowTitle("Ilxom")

        self.menyu=QLabel(self)
        self.menyu.setGeometry(850,0,150,50)
        self.menyu.setFont(QFont("Consolas",18))
        self.menyu.setText("MENYU")
        self.menyu.setStyleSheet("color: rgb(0,0,205);")

        self.taom=QLabel(self)
        self.taom.setGeometry(160,50,250,60)
        self.taom.setFont(QFont("Calibri",18))
        self.taom.setText("Birinchi taom: ")
        self.taom.setStyleSheet("color: rgb(139,0,0);")

        self.mastava=QCheckBox("Mastava ",self)
        self.mastava.setGeometry(160,100,150,50)
        self.mastava.setFont(QFont("Calibri",16))
        self.mastava.setStyleSheet("color: rgb(65,74,76);")

        self.shurva=QCheckBox("Shurva ",self)
        self.shurva.setGeometry(160,150,100,50)
        self.shurva.setFont(QFont("Calibri",16))
        self.shurva.setStyleSheet("color: rgb(65,74,76);")

        self.she=QCheckBox("She ",self)
        self.she.setGeometry(160,200,100,50)
        self.she.setFont(QFont("Calibri",16))
        self.she.setStyleSheet("color: rgb(65,74,76);")

        self.narx=QLabel(self)
        self.narx.setGeometry(300,100,100,50)
        self.narx.setFont(QFont("Calibri",18))
        self.narx.setText("20.000 ")
        self.narx.setStyleSheet("color: rgb(220,20,60);")

        self.narx1=QLabel(self)
        self.narx1.setGeometry(300,200,100,50)
        self.narx1.setFont(QFont("Calibri",18))
        self.narx1.setText("30.000 ")
        self.narx1.setStyleSheet("color: rgb(220,20,60);")       

        self.narx2=QLabel(self)
        self.narx2.setGeometry(300,150,100,50)
        self.narx2.setFont(QFont("Calibri",18))
        self.narx2.setText("25.000 ")
        self.narx2.setStyleSheet("color: rgb(220,20,60);")

        self.mas=QLabel()
        self.mas_ra=QPixmap("D:\\Rasmlar\\mastava")
        mr=self.mas_ra.scaled(100,100,Qt.KeepAspectRatio)
        self.mas.setPixmap(mr)

        self.shurvars=QLabel()
        self.shurvs_ra=QPixmap("D:\\Rasmlar\\kuza")
        mr=self.shurvs_ra.scaled(100,200,Qt.KeepAspectRatio)
        self.shurvars.setPixmap(mr)
        gr=QHBoxLayout()
        gr.addWidget(self.mas)
        gr.addWidget(self.shurvars)


        self.taom1=QLabel(self)
        self.taom1.setGeometry(500,50,250,60)
        self.taom1.setFont(QFont("Calibri",18))
        self.taom1.setText("Ikkinchi taom: ")
        self.taom1.setStyleSheet("color: rgb(139,0,0);")

        self.kuksi=QCheckBox("Kuksi mavsum",self)
        self.kuksi.setGeometry(500,100,190,50)
        self.kuksi.setFont(QFont("Calibri",16))
        self.kuksi.setStyleSheet("color: rgb(65,74,76);")

        self.osh=QCheckBox("Osh ",self)
        self.osh.setGeometry(500,150,100,50)
        self.osh.setFont(QFont("Calibri",16))
        self.osh.setStyleSheet("color: rgb(65,74,76);")

        self.jiz=QCheckBox("Jiz ",self)
        self.jiz.setGeometry(500,200,100,50)
        self.jiz.setFont(QFont("Calibri",16))
        self.jiz.setStyleSheet("color: rgb(65,74,76);")

        self.narx4=QLabel(self)
        self.narx4.setGeometry(700,100,100,50)
        self.narx4.setFont(QFont("Calibri",18))
        self.narx4.setText("80.000 ")
        self.narx4.setStyleSheet("color: rgb(220,20,60);")

        self.narx5=QLabel(self)
        self.narx5.setGeometry(700,150,100,50)
        self.narx5.setFont(QFont("Calibri",18))
        self.narx5.setText("30.000 ")
        self.narx5.setStyleSheet("color: rgb(220,20,60);")

        self.narx6=QLabel(self)
        self.narx6.setGeometry(700,200,100,50)
        self.narx6.setFont(QFont("Calibri",18))
        self.narx6.setText("75.000 ")
        self.narx6.setStyleSheet("color: rgb(220,20,60);")


        self.ichimlik=QLabel(self)
        self.ichimlik.setGeometry(900,50,250,60)
        self.ichimlik.setFont(QFont("Calibri",18))
        self.ichimlik.setText("Ichimliklar: ")
        self.ichimlik.setStyleSheet("color: rgb(139,0,0);")

        self.choy=QCheckBox("kuk choy",self)
        self.choy.setGeometry(900,100,190,50)
        self.choy.setFont(QFont("Calibri",16))
        self.choy.setStyleSheet("color: rgb(65,74,76);")

        self.koktel=QCheckBox("Limanat ",self)
        self.koktel.setGeometry(900,150,100,50)
        self.koktel.setFont(QFont("Calibri",16))
        self.koktel.setStyleSheet("color: rgb(65,74,76);")

        self.cola=QCheckBox("Cocacola ",self)
        self.cola.setGeometry(900,200,100,50)
        self.cola.setFont(QFont("Calibri",16))
        self.cola.setStyleSheet("color: rgb(65,74,76);")

        self.narx7=QLabel(self)
        self.narx7.setGeometry(1100,100,100,50)
        self.narx7.setFont(QFont("Calibri",18))
        self.narx7.setText("2000 ")
        self.narx7.setStyleSheet("color: rgb(220,20,60);")

        self.narx8=QLabel(self)
        self.narx8.setGeometry(1100,150,100,50)
        self.narx8.setFont(QFont("Calibri",18))
        self.narx8.setText("15.000 ")
        self.narx8.setStyleSheet("color: rgb(220,20,60);")       

        self.narx9=QLabel(self)
        self.narx9.setGeometry(1100,200,100,50)
        self.narx9.setFont(QFont("Calibri",18))
        self.narx9.setText("15.000 ")
        self.narx9.setStyleSheet("color: rgb(220,20,60);")


        self.but=QPushButton("Hisobni to'lash",self)
        self.but.resize(250,50)
        self.but.move(1000,540)
        self.but.setFont(QFont("Consolas",18))
        self.but.setStyleSheet("""
                                color: rgb(255,255,102);   
                                border-color: rgb(178,236,93);
                                border-radius: 15px;
                                border-width: 3px;
                                border-style: outset;
                                background-color: rgb(50,205,50);
                                """)
        self.but.clicked.connect(self.hisob)
        
        self.but1=QPushButton("Chek chiqarish",self)
        self.but1.resize(250,50)
        self.but1.move(500,540)
        self.but1.setFont(QFont("Consolas",18))
        self.but1.setStyleSheet("""
                                color: rgb(255,255,102);   
                                border-color: rgb(178,236,93);
                                border-radius: 15px;
                                border-width: 3px;
                                border-style: outset;
                                background-color: rgb(50,205,50);
                                """)
        self.but1.clicked.connect(self.chek)

    def hisob(self):
        f=open("hisob.txt","wt+")
        f.write("\n****************************************\n")
        if self.mastava.isChecked():
            f.write(f"Birinch taom: {self.mastava.text()}  Narxi: {self.narx.text()}\n ")
            restaran.hisob1+=20.000
        elif self.shurva.isChecked():
            f.write(f"Birinch taom: {self.shurva.text()}  Narxi: {self.narx1.text()}\n ")
            restaran.hisob1+=25.000
        elif self.she.isChecked():
            f.write(f"Birinch taom: {self.she.text()}  Narxi: {self.narx2.text()}\n ")
            restaran.hisob1+=25.000

        if self.osh.isChecked():
            f.write(f"ikkinchi taom: {self.osh.text()}  Narxi:  {self.narx5.text()}\n")
            restaran.hisob2+=30.000
        elif self.kuksi.isChecked():
            f.write(f"ikkinchi taom: {self.kuksi.text()}  Narxi:  {self.narx4.text()}\n")
            restaran.hisob2+=80.000
        elif self.jiz.isChecked():
            f.write(f"ikkinchi taom: {self.jiz.text()}  Narxi:  {self.narx6.text()}\n")
            restaran.hisob2+=75.000


        if self.choy.isChecked():
            f.write(f"Ichimlik: {self.choy.text()}  Narxi:  {self.narx7.text()}\n")
            restaran.hisob3+=2.000
        
        elif self.koktel.isChecked():
            f.write(f"Ichimlik: {self.koktel.text()}  Narxi:  {self.narx8.text()}\n")
            restaran.hisob3+=15.000
        if self.cola.isChecked():
            f.write(f"Ichimlik: {self.cola.text()}  Narxi:  {self.narx9.text()}\n")
            restaran.hisob3+=15.000
        f.write(f"Hisob:  {restaran.hisob1+restaran.hisob2+restaran.hisob3}00 So'm\n")
        f.write(f"Biz bilan bulganingizdan xursanmiz")

    def chek(self):
        os.system("D:\\python\\amaliyot\\10.04.2023\\hisob.txt")

if __name__=="__main__":
    app=QApplication(sys.argv)
    projekt=restaran()
  
    projekt.show()
    sys.exit(app.exec_())


