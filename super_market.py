import os 
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.chdir(r"C:\\Users\\Oybek\\python")
        
os.system("cls")
class dastur(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setMaximumSize(900,600)
        self.setMinimumSize(900,600)
        self.move(150,100)
        self.setWindowIcon(QIcon("C:\\Users\\Oybek\\Downloads\\Telegram Desktop\\Rayxon.png"))
        self.setWindowTitle("Korzinka.uz")
        
        self.menu=QLabel(self)
        self.menu.setGeometry(300,0,250,50)
        self.menu.setFont(QFont("Poppins",30))
        self.menu.setText("Supermarket ")
        self.menu.setStyleSheet("color: rgb(0,0,0)")
        
   
        self.mevalar=QLabel(self)
        self.mevalar.setGeometry(30,40,150,50)
        self.mevalar.setFont(QFont("Consolas",15))
        self.mevalar.setText("Mevalar: kg")
        self.mevalar.setStyleSheet("color: rgb(0,0,0)")
        
        self.olma=QCheckBox("Olma", self)
        self.olma.setGeometry(15,90,100,50)
        self.olma.setFont(QFont("Poppins",14))
        self.olma.setStyleSheet("color: rgb(0,0,0)")
        self.olmaga=QLabel("30.000 so'm/kg", self)
        self.olmaga.setGeometry(15,115,100,50)
        self.olmaga.setFont(QFont("Poppins",7))
        self.olmaga.setStyleSheet("color: rgb(0,0,0)")
        self.forolma=QLineEdit(self)
        self.forolma.setGeometry(140,110,40,30)
        self.forolma.setFont(QFont("Cosolas",12))
        
        self.anor=QCheckBox("Anor", self)
        self.anor.setGeometry(15,150,100,50)
        self.anor.setFont(QFont("Poppins",14))
        self.anor.setStyleSheet("color: rgb(0,0,0)")
        self.anorga=QLabel("25.000 so'm", self)
        self.anorga.setGeometry(15,175,100,50)
        self.anorga.setFont(QFont("Poppins",7))
        self.anorga.setStyleSheet("color: rgb(0,0,0)")
        self.foranor=QLineEdit(self)
        self.foranor.setGeometry(140,165,40,30)
        self.foranor.setFont(QFont("Cosolas",12))
        
        self.banan=QCheckBox("Banan", self)
        self.banan.setGeometry(15,200,250,50)
        self.banan.setFont(QFont("Poppins",14))
        self.banan.setStyleSheet("color: rgb(0,0,0)")
        self.bananga=QLabel("28.000 so'm", self)
        self.bananga.setGeometry(15,225,100,50)
        self.bananga.setFont(QFont("Poppins",7))
        self.bananga.setStyleSheet("color: rgb(0,0,0)")
        self.forbanan=QLineEdit(self)
        self.forbanan.setGeometry(140,215,40,30)
        self.forbanan.setFont(QFont("Cosolas",12))
        
        self.qulpinay=QCheckBox("Qulpinay", self)
        self.qulpinay.setGeometry(15,250,250,50)
        self.qulpinay.setFont(QFont("Poppins",14))
        self.qulpinay.setStyleSheet("color: rgb(0,0,0)")
        self.qulpinayga=QLabel("100.000 so'm", self)
        self.qulpinayga.setGeometry(15,275,100,50)
        self.qulpinayga.setFont(QFont("Poppins",7))
        self.qulpinayga.setStyleSheet("color: rgb(0,0,0)")
        self.forqulipnay=QLineEdit(self)
        self.forqulipnay.setGeometry(140,270,40,30)
        self.forqulipnay.setFont(QFont("Cosolas",12))
        
        self.gilos=QCheckBox("Gilos", self)
        self.gilos.setGeometry(15,305,250,50)
        self.gilos.setFont(QFont("Poppins",14))
        self.gilos.setStyleSheet("color: rgb(0,0,0)")
        self.gilosga=QLabel("300.000 so'm", self)
        self.gilosga.setGeometry(15,335,100,50)
        self.gilosga.setFont(QFont("Poppins",7))
        self.gilosga.setStyleSheet("color: rgb(0,0,0)")
        self.forgilos=QLineEdit(self)
        self.forgilos.setGeometry(140,330,40,30)
        self.forgilos.setFont(QFont("Cosolas",12))
        
        self.gusht=QLabel(self)
        self.gusht.setGeometry(200,40,250,50)
        self.gusht.setFont(QFont("Consolas",15))
        self.gusht.setText("Go'sht mahsulotlari")
        self.gusht.setStyleSheet("color: rgb(0,0,0)")
        
        self.mol=QCheckBox("Mol go'shti", self)
        self.mol.setGeometry(200,90,150,50)
        self.mol.setFont(QFont("Poppins",14))
        self.mol.setStyleSheet("color: rgb(0,0,0)")
        self.molga=QLabel("79.000 so'm", self)
        self.molga.setGeometry(200,115,100,50)
        self.molga.setFont(QFont("Poppins",7))
        self.molga.setStyleSheet("color: rgb(0,0,0)")
        self.formol=QLineEdit(self)
        self.formol.setGeometry(350,100,40,30)
        self.formol.setFont(QFont("Cosolas",12))
        
        self.quy=QCheckBox("Qo'y go'shti", self)
        self.quy.setGeometry(200,150,150,50)
        self.quy.setFont(QFont("Poppins",14))
        self.quy.setStyleSheet("color: rgb(0,0,0)")
        self.quyga=QLabel("89.000 so'm (dona)", self)
        self.quyga.setGeometry(200,175,100,50)
        self.quyga.setFont(QFont("Poppins",7))
        self.quyga.setStyleSheet("color: rgb(0,0,0)")
        self.forquy=QLineEdit(self)
        self.forquy.setGeometry(350,165,40,30)
        self.forquy.setFont(QFont("Cosolas",12))
        
        self.tovuq=QCheckBox("Tovuq go'shti", self)
        self.tovuq.setGeometry(200,200,250,50)
        self.tovuq.setFont(QFont("Poppins",14))
        self.tovuq.setStyleSheet("color: rgb(0,0,0)")
        self.tovuqga=QLabel("49.000 so'm", self)
        self.tovuqga.setGeometry(200,225,100,50)
        self.tovuqga.setFont(QFont("Poppins",7))
        self.tovuqga.setStyleSheet("color: rgb(0,0,0)")
        self.fortovuq=QLineEdit(self)
        self.fortovuq.setGeometry(350,215,40,30)
        self.fortovuq.setFont(QFont("Cosolas",12))
        
        self.baliq=QCheckBox("Baliq ", self)
        self.baliq.setGeometry(200,250,300,50)
        self.baliq.setFont(QFont("Poppins",14))
        self.baliq.setStyleSheet("color: rgb(0,0,0)")
        self.baliqga=QLabel("49.000 so'm", self)
        self.baliqga.setGeometry(200,275,100,50)
        self.baliqga.setFont(QFont("Poppins",7))
        self.baliqga.setStyleSheet("color: rgb(0,0,0)")
        self.forbaliq=QLineEdit(self)
        self.forbaliq.setGeometry(350,270,40,30)
        self.forbaliq.setFont(QFont("Cosolas",12))
        
        self.qazi=QCheckBox("Qazi", self)
        self.qazi.setGeometry(200,305,250,50)
        self.qazi.setFont(QFont("Poppins",14))
        self.qazi.setStyleSheet("color: rgb(0,0,0)")
        self.qaziga=QLabel("99.000 so'm", self)
        self.qaziga.setGeometry(200,330,100,50)
        self.qaziga.setFont(QFont("Poppins",7))
        self.qaziga.setStyleSheet("color: rgb(0,0,0)")
        self.forqazi=QLineEdit(self)
        self.forqazi.setGeometry(350,325,40,30)
        self.forqazi.setFont(QFont("Cosolas",12))
        
        self.ichimlik=QLabel(self)
        self.ichimlik.setGeometry(440,40,250,50)
        self.ichimlik.setFont(QFont("Consolas",18))
        self.ichimlik.setText("Ichimliklar: ")
        self.ichimlik.setStyleSheet("color: rgb(0,0,0)")

        
        self.fanta=QCheckBox("Fanta 1l", self)
        self.fanta.setGeometry(440,90,200,50)
        self.fanta.setFont(QFont("Poppins",14))
        self.fanta.setStyleSheet("color: rgb(0,0,0)")
        self.fantaga=QLabel("8.000 so'm", self)
        self.fantaga.setGeometry(440,115,100,50)
        self.fantaga.setFont(QFont("Poppins",7))
        self.fantaga.setStyleSheet("color: rgb(0,0,0)")
        self.forfanta=QSpinBox(self)
        self.forfanta.setGeometry(545,100,40,30)
        self.forfanta.setFont(QFont("Consolas",15))
        
        
        self.pepsi=QCheckBox("Pepsi", self)
        self.pepsi.setGeometry(440,150,100,50)
        self.pepsi.setFont(QFont("Poppins",14))
        self.pepsi.setStyleSheet("color: rgb(0,0,0)")
        self.pepsiga=QLabel("10.000 so'm/litr", self)
        self.pepsiga.setGeometry(440,175,100,50)
        self.pepsiga.setFont(QFont("Poppins",7))
        self.pepsiga.setStyleSheet("color: rgb(0,0,0)")
        self.forpepsi=QSpinBox(self)
        self.forpepsi.setGeometry(545,165,40,30)
        self.forpepsi.setFont(QFont("Consolas",15))
        
        
        self.cola=QCheckBox("Coca-Cola", self)
        self.cola.setGeometry(440,200,250,50)
        self.cola.setFont(QFont("Poppins",14))
        self.cola.setStyleSheet("color: rgb(0,0,0)")
        self.colaga=QLabel("10.000 so'm/litr", self)
        self.colaga.setGeometry(440,225,100,50)
        self.colaga.setFont(QFont("Poppins",7))
        self.colaga.setStyleSheet("color: rgb(0,0,0)")
        self.forcola=QSpinBox(self)
        self.forcola.setGeometry(545,215,40,30)
        self.forcola.setFont(QFont("Consolas",15))
        
        
        self.flash=QCheckBox("Flash", self)
        self.flash.setGeometry(440,250,300,50)
        self.flash.setFont(QFont("Poppins",14))
        self.flash.setStyleSheet("color: rgb(0,0,0)")
        self.flashga=QLabel("7.000 so'm 450mg", self)
        self.flashga.setGeometry(440,275,100,50)
        self.flashga.setFont(QFont("Poppins",7))
        self.flashga.setStyleSheet("color: rgb(0,0,0)")
        self.forflash=QSpinBox(self)
        self.forflash.setGeometry(545,270,40,30)
        self.forflash.setFont(QFont("Consolas",15))
        
        
        self.saber=QCheckBox("7Saber", self)
        self.saber.setGeometry(440,305,250,50)
        self.saber.setFont(QFont("Poppins",14))
        self.saber.setStyleSheet("color: rgb(0,0,0)")
        self.saberga=QLabel("8.000 so'm 450mg", self)
        self.saberga.setGeometry(440,330,100,50)
        self.saberga.setFont(QFont("Poppins",7))
        self.saberga.setStyleSheet("color: rgb(0,0,0)")
        self.forsaber=QSpinBox(self)
        self.forsaber.setGeometry(545,325,40,30)
        self.forsaber.setFont(QFont("Consolas",15))
        
        
        self.uni=QLabel(self)
        self.uni.setGeometry(640,40,250,50)
        self.uni.setFont(QFont("Consolas",18))
        self.uni.setText("Un Mahsulotlari: ")
        self.uni.setStyleSheet("color: rgb(0,0,0)") 
        
        self.un=QCheckBox("Un Turon", self)
        self.un.setGeometry(640,90,200,50)
        self.un.setFont(QFont("Poppins",14))
        self.un.setStyleSheet("color: rgb(0,0,0)")
        self.unga=QLabel("10.800 so'm/kg", self)
        self.unga.setGeometry(640,115,100,50)
        self.unga.setFont(QFont("Poppins",7))
        self.unga.setStyleSheet("color: rgb(0,0,0)")
        self.forun=QSpinBox(self)
        self.forun.setGeometry(750,100,40,30)
        self.forun.setFont(QFont("Consolas",15))
        
        
        self.makaron=QCheckBox("Makaron ", self)
        self.makaron.setGeometry(640,150,100,50)
        self.makaron.setFont(QFont("Poppins",14))
        self.makaron.setStyleSheet("color: rgb(0,0,0)")
        self.makaronga=QLabel("Makfa 13.000 so'm/kg", self)
        self.makaronga.setGeometry(640,175,100,50)
        self.makaronga.setFont(QFont("Poppins",7))
        self.makaronga.setStyleSheet("color: rgb(0,0,0)")
        self.formakaron=QSpinBox(self)
        self.formakaron.setGeometry(750,170,40,30)
        self.formakaron.setFont(QFont("Consolas",15))
         
        self.lagman=QCheckBox("Makaron", self)
        self.lagman.setGeometry(640,200,250,50)
        self.lagman.setFont(QFont("Poppins",12))
        self.lagman.setStyleSheet("color: rgb(0,0,0)")
        self.lagmanga=QLabel("Makfa solomka uzun 400g\n20.000 so'm/kg", self)
        self.lagmanga.setGeometry(640,225,100,50)
        self.lagmanga.setFont(QFont("Poppins",7))
        self.lagmanga.setStyleSheet("color: rgb(0,0,0)")
        self.forlagman=QSpinBox(self)
        self.forlagman.setGeometry(750,215,40,30)
        self.forlagman.setFont(QFont("Consolas",15))
        
        self.chuchvara=QCheckBox("Chuchvara ", self)
        self.chuchvara.setGeometry(640,250,300,50)
        self.chuchvara.setFont(QFont("Poppins",14))
        self.chuchvara.setStyleSheet("color: rgb(0,0,0)")
        self.chuchvaraga=QLabel("15.000 so'm", self)
        self.chuchvaraga.setGeometry(640,275,100,50)
        self.chuchvaraga.setFont(QFont("Poppins",7))
        self.chuchvaraga.setStyleSheet("color: rgb(0,0,0)")
        self.forchuchvara=QSpinBox(self)
        self.forchuchvara.setGeometry(750,270,40,30)
        self.forchuchvara.setFont(QFont("Consolas",15))
        
        
        self.manti=QCheckBox("Manti", self)
        self.manti.setGeometry(640,305,250,50)
        self.manti.setFont(QFont("Poppins",14))
        self.manti.setStyleSheet("color: rgb(0,0,0)")
        self.mantiga=QLabel("20.000 so'm/kg", self)
        self.mantiga.setGeometry(640,330,100,50)
        self.mantiga.setFont(QFont("Poppins",7))
        self.mantiga.setStyleSheet("color: rgb(0,0,0)")
        self.formanti=QSpinBox(self)
        self.formanti.setGeometry(750,325,40,30)
        self.formanti.setFont(QFont("Consolas",15))
        
        self.tugma=QPushButton("Sotib olish",self)
        self.tugma.setGeometry(140,500,200,50)
        self.tugma.setFont(QFont("Consolas",20))
        self.tugma.setStyleSheet("""
                        background-color: rgb(0,255,0);
                        border-width: 3px;
                        border-style: solid;
                        border-color: rgb(255,160,122);
                        border-radius: 10px;
                        """)
        self.tugma.clicked.connect(self.hisob_kitob)

        self.chekol=QPushButton("Chekni olish",self)
        self.chekol.setGeometry(360,500,200,50)
        self.chekol.setFont(QFont("Consolas",20))
        self.chekol.setStyleSheet("""
                        background-color: rgb(0,255,0);
                        border-width: 3px;
                        border-style: solid;
                        border-color: rgb(255,160,122);
                        border-radius: 10px;
                        """)
        self.chekol.clicked.connect(self.push)
    
    
    def hisob_kitob(self):        
        with open("Natija.txt", "wt") as f:
            ol=0
            an=0
            ban=0
            gil=0
            qul=0
            mg=0
            qg=0
            tg=0
            bg=0
            qg=0
            fan=0
            pep=0
            col=0
            fla=0
            sab=0
            uni=0
            lag=0
            chuch=0
            man=0
            mak=0
           
            if self.olma.isChecked():
                ol=30000*float(self.forolma.text())
                f.write(f"Olma..........{ol}\n")
                
            if self.anor.isChecked():
                an=25000*float(self.foranor.text())
                f.write(f"Anor..........{an}\n")
                
            if self.banan.isChecked():
                ban=28000*float(self.forbanan.text())
                f.write(f"Banan..........{ban}\n")
                
            if self.qulpinay.isChecked():
                qul=100000*float(self.forqulipnay.text())
                f.write(f"Qulpinay..........{qul}\n")
            
            if self.gilos.isChecked():
                gil=549000*float(self.forgilos.text())
                f.write(f"Gilos..........{gil}\n")
                
            
            
            if self.mol.isChecked():
                mg=80000*float(self.formol.text())
                f.write(f"Mol go'shti..........{mg}\n")
            if self.quy.isChecked():
                qg=89000*float(self.forquy.text())
                f.write(f"Qo'y go'shti..........{qg}\n")
            if self.tovuq.isChecked():
                tg=49000*float(self.fortovuq.text())
                f.write(f"Tovuq go'shti..........{tg}\n")
            if self.baliq.isChecked():
                bg=49000*float(self.forbaliq.text())
                f.write(f"Baliq go'shti..........{bg}\n")
            if self.qazi.isChecked():
                qg=99000*float(self.forqazi.text())
                f.write(f"Qazi..........{qg}\n")
            
            if self.fanta.isChecked():
                fan=8000*float(self.forfanta.text())
                f.write(f"Fanta..........{fan}\n")
            if self.pepsi.isChecked():
                pep=10000*float(self.forpepsi.text())
                f.write(f"Pepsi..........{pep}\n")
            if self.cola.isChecked():
                col=10000*float(self.forfanta.text())
                f.write(f"Cola..........{col}\n")
            if self.flash.isChecked():
                fla=7000*float(self.forflash.text())
                f.write(f"Flash..........{fla}\n")               
            if self.saber.isChecked():
                sab=8000*float(self.forsaber.text())
                f.write(f"7Saber..........{sab}\n")
            
            if self.un.isChecked():
                uni=10800*float(self.forun.text())
                f.write(f"Un..........{uni}\n")
                
            if self.makaron.isChecked():
                mak=13000*float(self.formakaron.text())
                f.write(f"Makaron..........{mak}\n")
            if self.lagman.isChecked():
                lag=20000*float(self.forlagman.text())
                f.write(f"Makaron Makfa solomka\n uzun 400g..........{lag}\n")
            if self.chuchvara.isChecked():
                chuch=15000*float(self.forchuchvara.text())
                f.write(f"Chuchvara..........{chuch}\n")
                
            if self.manti.isChecked():
                man=20000*float(self.formanti.text())
                f.write(f"Manti 450mg..........{man}\n")
                
                hisob=ol+an+ban+gil+qul+mg+qg+tg+bg+fan+col+pep+fla+sab+man+chuch+uni+lag+mak
                f.write(f"Jami:..........{hisob}\n")
                f.write("\n\tKorzinka.uz!!!")
                f.write("\nXARIDINGIZ UCHUN TASHAKKUR")
            
    def push(self):
        os.system("C:\\Users\\Oybek\\python\\Natija.txt") 
                    
if __name__=="__main__":
    app=QApplication(sys.argv)
    project=dastur()
    project.show()
    sys.exit(app.exec_())