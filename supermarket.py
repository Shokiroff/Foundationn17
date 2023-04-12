import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class supermarket(QWidget):
 
    
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1700,900)
        self.setMinimumSize(1700,900)
        self.move(150,100)
        self.setWindowIcon(QIcon("D:\\python\\amaliyot\\10.04.2023\\13"))
        self.setWindowTitle("KORZINKA")

        self.sb=QLabel(self)
        self.sb.setGeometry(200,50,250,60)
        self.sb.setFont(QFont("Calibri",18))
        self.sb.setText("Sabzavotlar: ")
        self.sb.setStyleSheet("color: rgb(139,0,0);")


        self.kartoshka=QCheckBox("Kartoshka",self)
        self.kartoshka.setGeometry(200,100,250,50)
        self.kartoshka.setFont(QFont("Calibri",16))
        self.kartoshka.setStyleSheet("color: rgb(218,165,32);")

        self.kartoshka_narx1=QLabel(self)
        self.kartoshka_narx1.setGeometry(350,100,100,50)
        self.kartoshka_narx1.setText("4.900")
        self.kartoshka_narx1.setFont(QFont("Calibri",16))
        self.kartoshka_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.txt=QLineEdit(self)
        self.txt.setFont(QFont("Calibri",18))
        self.txt.setGeometry(450,100,50,50)
        self.txt.setStyleSheet("color: rgb(218,165,32);")

        self.kg1=QLabel(self)
        self.kg1.setGeometry(510,100,50,50)
        self.kg1.setText("Kg")
        self.kg1.setFont(QFont("Calibri",16))
        self.kg1.setStyleSheet("color: rgb(218,165,32);")


        self.sabzi=QCheckBox("Sabzi",self)
        self.sabzi.setGeometry(200,150,250,50)
        self.sabzi.setFont(QFont("Calibri",16))
        self.sabzi.setStyleSheet("color: rgb(218,165,32);")

        self.sabsi_narx=QLabel(self)
        self.sabsi_narx.setGeometry(350,150,100,50)
        self.sabsi_narx.setText("7.900")
        self.sabsi_narx.setFont(QFont("Calibri",16))
        self.sabsi_narx.setStyleSheet("color: rgb(218,165,32);")

        self.txt1=QLineEdit(self)
        self.txt1.setFont(QFont("Calibri",18))
        self.txt1.setGeometry(450,150,50,50)
        self.txt1.setStyleSheet("color: rgb(218,165,32);")

        self.kg2=QLabel(self)
        self.kg2.setGeometry(510,150,50,50)
        self.kg2.setText("Kg")
        self.kg2.setFont(QFont("Calibri",16))
        self.kg2.setStyleSheet("color: rgb(218,165,32);")

        self.karam=QCheckBox("Karam",self)
        self.karam.setGeometry(200,200,250,50)
        self.karam.setFont(QFont("Calibri",16))
        self.karam.setStyleSheet("color: rgb(218,165,32);")

        self.karam_narx1=QLabel(self)
        self.karam_narx1.setGeometry(350,200,100,50)
        self.karam_narx1.setText("3.900")
        self.karam_narx1.setFont(QFont("Calibri",16))
        self.karam_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.txt2=QLineEdit(self)
        self.txt2.setFont(QFont("Calibri",18))
        self.txt2.setGeometry(450,200,50,50)
        self.txt2.setStyleSheet("color: rgb(218,165,32);")

        self.kg3=QLabel(self)
        self.kg3.setGeometry(510,200,50,50)
        self.kg3.setText("Kg")
        self.kg3.setFont(QFont("Calibri",16))
        self.kg3.setStyleSheet("color: rgb(218,165,32);")

        self.kabachki=QCheckBox("Kabachki",self)
        self.kabachki.setGeometry(200,250,250,50)
        self.kabachki.setFont(QFont("Calibri",16))
        self.kabachki.setStyleSheet("color: rgb(218,165,32);")

        self.kabachki_narx1=QLabel(self)
        self.kabachki_narx1.setGeometry(350,250,100,50)
        self.kabachki_narx1.setText("6.900")
        self.kabachki_narx1.setFont(QFont("Calibri",16))
        self.kabachki_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.txt3=QLineEdit(self)
        self.txt3.setFont(QFont("Calibri",18))
        self.txt3.setGeometry(450,250,50,50)
        self.txt3.setStyleSheet("color: rgb(218,165,32);")

        self.kg4=QLabel(self)
        self.kg4.setGeometry(510,250,50,50)
        self.kg4.setText("Kg")
        self.kg4.setFont(QFont("Calibri",16))
        self.kg4.setStyleSheet("color: rgb(218,165,32);")

        self.baqlajon=QCheckBox("Baqlajon",self)
        self.baqlajon.setGeometry(200,300,250,50)
        self.baqlajon.setFont(QFont("Calibri",16))
        self.baqlajon.setStyleSheet("color: rgb(218,165,32);")

        self.baqlajopn_narx1=QLabel(self)
        self.baqlajopn_narx1.setGeometry(350,300,100,50)
        self.baqlajopn_narx1.setText("5.900")
        self.baqlajopn_narx1.setFont(QFont("Calibri",16))
        self.baqlajopn_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.txt4=QLineEdit(self)
        self.txt4.setFont(QFont("Calibri",18))
        self.txt4.setGeometry(450,300,50,50)
        self.txt4.setStyleSheet("color: rgb(218,165,32);")

        self.kg5=QLabel(self)
        self.kg5.setGeometry(510,300,50,50)
        self.kg5.setText("Kg")
        self.kg5.setFont(QFont("Calibri",16))
        self.kg5.setStyleSheet("color: rgb(218,165,32);")

        ###

        self.meva=QLabel(self)
        self.meva.setGeometry(700,50,250,60)
        self.meva.setFont(QFont("Calibri",18))
        self.meva.setText("Meva: ")
        self.meva.setStyleSheet("color: rgb(139,0,0);")

        self.olma=QCheckBox("Olma ",self)
        self.olma.setGeometry(700,100,250,50)
        self.olma.setFont(QFont("Calibri",16))
        self.olma.setStyleSheet("color: rgb(218,165,32);")

        self.olma_narxi=QLabel(self)
        self.olma_narxi.setGeometry(850,100,100,50)
        self.olma_narxi.setText("12.000")
        self.olma_narxi.setFont(QFont("Calibri",16))
        self.olma_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.txt5=QLineEdit(self)
        self.txt5.setFont(QFont("Calibri",18))
        self.txt5.setGeometry(950,100,50,50)
        self.txt5.setStyleSheet("color: rgb(218,165,32);")

        self.kg6=QLabel(self)
        self.kg6.setGeometry(1000,100,50,50)
        self.kg6.setText("Kg")
        self.kg6.setFont(QFont("Calibri",16))
        self.kg6.setStyleSheet("color: rgb(218,165,32);")


        self.banan=QCheckBox("Banan ",self)
        self.banan.setGeometry(700,150,250,50)
        self.banan.setFont(QFont("Calibri",16))
        self.banan.setStyleSheet("color: rgb(218,165,32);")

        self.banan_narxi=QLabel(self)
        self.banan_narxi.setGeometry(850,150,100,50)
        self.banan_narxi.setText("21.000")
        self.banan_narxi.setFont(QFont("Calibri",16))
        self.banan_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.txt6=QLineEdit(self)
        self.txt6.setFont(QFont("Calibri",18))
        self.txt6.setGeometry(950,150,50,50)
        self.txt6.setStyleSheet("color: rgb(218,165,32);")

        self.kg7=QLabel(self)
        self.kg7.setGeometry(1000,150,50,50)
        self.kg7.setText("Kg")
        self.kg7.setFont(QFont("Calibri",16))
        self.kg7.setStyleSheet("color: rgb(218,165,32);")


        

        self.anor=QCheckBox("Anor ",self)
        self.anor.setGeometry(700,200,250,50)
        self.anor.setFont(QFont("Calibri",16))
        self.anor.setStyleSheet("color: rgb(218,165,32);")

        self.anor_narxi=QLabel(self)
        self.anor_narxi.setGeometry(850,200,100,50)
        self.anor_narxi.setText("18.000")
        self.anor_narxi.setFont(QFont("Calibri",16))
        self.anor_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.txt7=QLineEdit(self)
        self.txt7.setFont(QFont("Calibri",18))
        self.txt7.setGeometry(950,200,50,50)
        self.txt7.setStyleSheet("color: rgb(218,165,32);")

        self.kg8=QLabel(self)
        self.kg8.setGeometry(1000,200,50,50)
        self.kg8.setText("Kg")
        self.kg8.setFont(QFont("Calibri",16))
        self.kg8.setStyleSheet("color: rgb(218,165,32);")

        self.apelsen=QCheckBox("Apelsen ",self)
        self.apelsen.setGeometry(700,250,250,50)
        self.apelsen.setFont(QFont("Calibri",16))
        self.apelsen.setStyleSheet("color: rgb(218,165,32);")

        self.apelsen_narxi=QLabel(self)
        self.apelsen_narxi.setGeometry(850,250,100,50)
        self.apelsen_narxi.setText("28.000")
        self.apelsen_narxi.setFont(QFont("Calibri",16))
        self.apelsen_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.txt8=QLineEdit(self)
        self.txt8.setFont(QFont("Calibri",18))
        self.txt8.setGeometry(950,250,50,50)
        self.txt8.setStyleSheet("color: rgb(218,165,32);")

        self.kg9=QLabel(self)
        self.kg9.setGeometry(1000,250,50,50)
        self.kg9.setText("Kg")
        self.kg9.setFont(QFont("Calibri",16))
        self.kg9.setStyleSheet("color: rgb(218,165,32);")

        self.ananas=QCheckBox("Ananas ",self)
        self.ananas.setGeometry(700,300,250,50)
        self.ananas.setFont(QFont("Calibri",16))
        self.ananas.setStyleSheet("color: rgb(218,165,32);")

        self.ananas_narxi=QLabel(self)
        self.ananas_narxi.setGeometry(850,300,100,50)
        self.ananas_narxi.setText("33.000")
        self.ananas_narxi.setFont(QFont("Calibri",16))
        self.ananas_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.txt9=QLineEdit(self)
        self.txt9.setFont(QFont("Calibri",18))
        self.txt9.setGeometry(950,300,50,50)
        self.txt9.setStyleSheet("color: rgb(218,165,32);")

        self.kg10=QLabel(self)
        self.kg10.setGeometry(1000,300,50,50)
        self.kg10.setText("Kg")
        self.kg10.setFont(QFont("Calibri",16))
        self.kg10.setStyleSheet("color: rgb(218,165,32);")


        self.meva=QLabel(self)
        self.meva.setGeometry(1200,50,250,60)
        self.meva.setFont(QFont("Calibri",18))
        self.meva.setText("Ichmliklar: ")
        self.meva.setStyleSheet("color: rgb(139,0,0);")

        self.coal=QCheckBox("Cocacola",self)
        self.coal.setGeometry(1200,100,250,50)
        self.coal.setFont(QFont("Calibri",16))
        self.coal.setStyleSheet("color: rgb(218,165,32);")

        self.coal_narxi=QLabel(self)
        self.coal_narxi.setGeometry(1350,100,100,50)
        self.coal_narxi.setText("11.000")
        self.coal_narxi.setFont(QFont("Calibri",16))
        self.coal_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.coal1=QLineEdit(self)
        self.coal1.setFont(QFont("Calibri",18))
        self.coal1.setGeometry(1450,100,50,50)
        self.coal1.setStyleSheet("color: rgb(218,165,32);")

        self.sok=QCheckBox("Sok",self)
        self.sok.setGeometry(1200,150,250,50)
        self.sok.setFont(QFont("Calibri",16))
        self.sok.setStyleSheet("color: rgb(218,165,32);")

        self.sok_narxi=QLabel(self)
        self.sok_narxi.setGeometry(1350,150,100,50)
        self.sok_narxi.setText("14.000")
        self.sok_narxi.setFont(QFont("Calibri",16))
        self.sok_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.sok1=QLineEdit(self)
        self.sok1.setFont(QFont("Calibri",18))
        self.sok1.setGeometry(1450,150,50,50)
        self.sok1.setStyleSheet("color: rgb(218,165,32);")

        self.suv=QCheckBox("Oddiy suv",self)
        self.suv.setGeometry(1200,200,250,50)
        self.suv.setFont(QFont("Calibri",16))
        self.suv.setStyleSheet("color: rgb(218,165,32);")

        self.suv_narxi=QLabel(self)
        self.suv_narxi.setGeometry(1350,200,100,50)
        self.suv_narxi.setText("4.000")
        self.suv_narxi.setFont(QFont("Calibri",16))
        self.suv_narxi.setStyleSheet("color: rgb(218,165,32);")

        self.suv1=QLineEdit(self)
        self.suv1.setFont(QFont("Calibri",18))
        self.suv1.setGeometry(1450,200,50,50)
        self.suv1.setStyleSheet("color: rgb(218,165,32);")


        self.konde=QLabel(self)
        self.konde.setGeometry(200,350,250,60)
        self.konde.setFont(QFont("Calibri",18))
        self.konde.setText("Konditer:")
        self.konde.setStyleSheet("color: rgb(139,0,0);")

        self.ritter=QCheckBox("Ritter Sport",self)
        self.ritter.setGeometry(200,400,250,50)
        self.ritter.setFont(QFont("Calibri",16))
        self.ritter.setStyleSheet("color: rgb(218,165,32);")

        self.ritter_narx1=QLabel(self)
        self.ritter_narx1.setGeometry(350,400,100,50)
        self.ritter_narx1.setText("30.000")
        self.ritter_narx1.setFont(QFont("Calibri",16))
        self.ritter_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.rit=QLineEdit(self)
        self.rit.setFont(QFont("Calibri",18))
        self.rit.setGeometry(450,400,50,50)
        self.rit.setStyleSheet("color: rgb(218,165,32);")

        self.kg13=QLabel(self)
        self.kg13.setGeometry(510,400,50,50)
        self.kg13.setText("Kg")
        self.kg13.setFont(QFont("Calibri",16))
        self.kg13.setStyleSheet("color: rgb(218,165,32);")

        self.choka=QCheckBox("Alpengold",self)
        self.choka.setGeometry(200,450,250,50)
        self.choka.setFont(QFont("Calibri",16))
        self.choka.setStyleSheet("color: rgb(218,165,32);")

        self.choka_narx1=QLabel(self)
        self.choka_narx1.setGeometry(350,450,100,50)
        self.choka_narx1.setText("10.000")
        self.choka_narx1.setFont(QFont("Calibri",16))
        self.choka_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.alpin=QLineEdit(self)
        self.alpin.setFont(QFont("Calibri",18))
        self.alpin.setGeometry(450,450,50,50)
        self.alpin.setStyleSheet("color: rgb(218,165,32);")

        self.kg14=QLabel(self)
        self.kg14.setGeometry(510,450,50,50)
        self.kg14.setText("Kg")
        self.kg14.setFont(QFont("Calibri",16))
        self.kg14.setStyleSheet("color: rgb(218,165,32);")

        self.ot=QCheckBox("Otlami",self)
        self.ot.setGeometry(200,500,250,50)
        self.ot.setFont(QFont("Calibri",16))
        self.ot.setStyleSheet("color: rgb(218,165,32);")

        self.ot_narx1=QLabel(self)
        self.ot_narx1.setGeometry(350,500,100,50)
        self.ot_narx1.setText("119.000")
        self.ot_narx1.setFont(QFont("Calibri",16))
        self.ot_narx1.setStyleSheet("color: rgb(218,165,32);")

        self.ot1=QLineEdit(self)
        self.ot1.setFont(QFont("Calibri",18))
        self.ot1.setGeometry(450,500,50,50)
        self.ot1.setStyleSheet("color: rgb(218,165,32);")

        self.kg15=QLabel(self)
        self.kg15.setGeometry(510,500,50,50)
        self.kg15.setText("Kg")
        self.kg15.setFont(QFont("Calibri",16))
        self.kg15.setStyleSheet("color: rgb(218,165,32);")


        self.but=QPushButton("Hisobni to'lash",self)
        self.but.resize(250,50)
        self.but.move(1400,800)
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
        self.but1.move(1400,700)
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

        self.but1=QPushButton("UZKART",self)
        self.but1.resize(250,50)
        self.but1.move(1200,600)
        self.but1.setFont(QFont("Consolas",18))
        self.but1.setStyleSheet("""
                                color: rgb(255,255,102);   
                                border-color: rgb(178,236,93);
                                border-radius: 15px;
                                border-width: 3px;
                                border-style: outset;
                                background-color: rgb(50,205,50);
                                """)
        self.but1.clicked.connect(self.uzkart)

        self.but1=QPushButton("HUMO",self)
        self.but1.resize(250,50)
        self.but1.move(1200,500)
        self.but1.setFont(QFont("Consolas",18))
        self.but1.setStyleSheet("""
                                color: rgb(255,255,102);   
                                border-color: rgb(178,236,93);
                                border-radius: 15px;
                                border-width: 3px;
                                border-style: outset;
                                background-color: rgb(50,205,50);
                                """)
        self.but1.clicked.connect(self.humo)

    def uzkart (self):
        g=open("Chek.txt","at+")
        g.write(f"Tulov:\n")
        g.write(f"Terminal....................{self.uzkart}")
    
    def humo(self):
        q=open("Chek.txt","at+")
        q.write(f"Tulov:\n")
        q.write(f"Terminal....................{self.humo}")

    def hisob(self):
        sch=0
        f=open("Chek.txt","wt+")
        f.write("\n             KORZINKA.UZ\n             SUPERMARKET\n")
        

        if self.kartoshka.isChecked(): 
            sch+=1
            ka_n=float(self.txt.text()) * float(self.kartoshka_narx1.text())
            f.write(f"{self.kartoshka.text()}\n{self.kartoshka_narx1.text()}*{self.txt.text()}....................{ka_n}\n")
        else:
            ka_n=0
        if self.sabzi.isChecked():
            sch+=1
            sb=float(self.txt1.text()) * float(self.sabsi_narx.text())
            f.write(f"{self.sabzi.text()}\n{self.sabsi_narx.text()}*{self.txt1.text()}....................{sb}\n")
        else:
            sb=0
        if self.karam.isChecked():
            sch+=1
            km=float(self.txt2.text()) * float(self.karam_narx1.text())
            f.write(f"{self.karam.text()}\n{self.karam_narx1.text()}*{self.txt2.text()}....................{km}\n")
        else:
            km=0
        if self.kabachki.isChecked(): 
            sch+=1
            kb=float(self.txt3.text()) * float(self.kabachki_narx1.text())
            f.write(f"{self.kabachki.text()}\n{self.kabachki_narx1.text()}*{self.txt3.text()}....................{kb}\n")
        else:
            kb=0
        if self.baqlajon.isChecked():
            sch+=1
            bp=float(self.txt4.text()) * float(self.baqlajopn_narx1.text())
            f.write(f"{self.baqlajon.text()}\n{self.baqlajopn_narx1.text()}*{self.txt2.text()}....................{bp}\n")
        else:
            bp=0
        
        # Mevalar

        if self.olma.isChecked():
            sch+=1
            ol=float(self.txt5.text()) * float(self.olma_narxi.text())
            f.write(f"{self.olma.text()}\n{self.olma_narxi.text()}*{self.txt5.text()}....................{ol}\n")
        else:
            ol=0
        if self.banan.isChecked():
            sch+=1
            bn=float(self.txt6.text()) * float(self.banan_narxi.text())
            f.write(f"{self.banan.text()}\n{self.banan_narxi.text()}*{self.txt6.text()}....................{bn}\n")
        else: 
            bn=0
        if self.anor.isChecked():
            sch+=1
            an=float(self.txt7.text()) * float(self.anor_narxi.text())
            f.write(f"{self.anor.text()}\n{self.anor_narxi.text()}*{self.txt7.text()}....................{an}\n")
        else:
            an=0
        if self.apelsen.isChecked():
            sch+=1
            ap=float(self.txt8.text()) * float(self.apelsen_narxi.text())
            f.write(f"{self.apelsen.text()}\n{self.apelsen_narxi.text()}*{self.txt7.text()}....................{ap}\n")
        else:
            ap=0
        if self.ananas.isChecked():
            sch+=1
            an=float(self.txt9.text()) * float(self.ananas_narxi.text())
            f.write(f"{self.ananas.text()}\n{self.ananas_narxi.text()}*{self.txt9.text()}....................{an}\n")
        else:
            an=0

        if self.coal.isChecked():
            sch+=1
            ca=float(self.coal1.text())*float(self.coal_narxi.text())
            f.write(f"{self.coal.text()}\n{self.coal_narxi.text()}*{self.coal1.text()}....................{ca}\n")
        else: ca=0
        if self.sok.isChecked():
            sch+=1
            sa=float(self.sok1.text())*float(self.sok_narxi.text())
            f.write(f"{self.sok.text()}\n{self.sok_narxi.text()}*{self.sok1.text()}....................{sa}\n")
        else: sa=0
        if self.suv.isChecked():
            sch+=1
            su=float(self.suv1.text())*float(self.suv_narxi.text())
            f.write(f"{self.suv.text()}\n{self.suv_narxi.text()}*{self.suv1.text()}....................{su}\n")
        else: su=0
        if self.ritter.isChecked():
            sch+=1
            rs=float(self.rit.text())*float(self.ritter_narx1.text())
            f.write(f"{self.ritter.text()}\n{self.ritter_narx1.text()}*{self.rit.text()}....................{rs}\n")
        else: rs=0 
        if self.choka.isChecked():
            sch+=1
            apl=float(self.alpin.text())*float(self.choka_narx1.text())
            f.write(f"{self.choka.text()}\n{self.choka_narx1.text()}*{self.alpin.text()}....................{apl}\n")
        else: apl=0   
        if self.ot.isChecked():
            sch+=1
            to=float(self.ot1.text())*float(self.ot_narx1.text())
            f.write(f"{self.ot.text()}\n{self.ot_narx1.text()}*{self.ot1.text()}....................{to}\n")
        else: to=0
        f.write(f"\nSiz {sch} ta maxsulot sotib oldingiz:\n")
        

        f.write(f"Jami summa....................{ka_n+sb+km+kb+bp+ol+bn+an+ap+an+ca+sa+su+rs+apl+to}00 so'm \n")
        f.write(f"\n\nBiz bilan bulganingizgan xursandmiz!")

               



    def chek(self):
        os.system("D:\\python\\amaliyot\\10.04.2023\\chek.txt")    
        
        self.nike=QLabel()
        self.nike_rasm=QPixmap("D:\\Rasmlar\\134")
        nk=self.nike_rasm.scaled(100,600,Qt.KeepAspectRatio)
        self.nike.setPixmap(nk)
        gr=QGridLayout()
        gr.addWidget(self.nike,1,1)
if __name__=="__main__":
    app=QApplication(sys.argv)
    projekt=supermarket()
  
    projekt.show()
    sys.exit(app.exec_())


