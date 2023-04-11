import os 
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.chdir(r"Your_file_location")
        
os.system("cls")
class dastur(QWidget):
    ovqat1=0
    ovqat2=0
    ichimliklar=0
    desertcha=0
    def __init__(self):
        super().__init__()
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        self.move(150,100)
        self.setWindowIcon(QIcon("C:\\Users\\Oybek\\Downloads\\Telegram Desktop\\Rayxon.png"))
        self.setWindowTitle("Rayxon Milliy Taomlari")
        
        self.menu=QLabel(self)
        self.menu.setGeometry(300,0,250,50)
        self.menu.setFont(QFont("Poppins",30))
        self.menu.setText("Menu: ")
        self.menu.setStyleSheet("color: rgb(0,0,0)")
        
   
        self.taom1=QLabel(self)
        self.taom1.setGeometry(20,50,250,50)
        self.taom1.setFont(QFont("Consolas",18))
        self.taom1.setText("1-taom: ")
        self.taom1.setStyleSheet("color: rgb(0,0,0)")
        
        self.osh=QCheckBox("Osh", self)
        self.osh.setGeometry(50,90,100,50)
        self.osh.setFont(QFont("Poppins",18))
        self.osh.setStyleSheet("color: rgb(0,0,0)")
        self.oshga=QLabel("30.000 so'm  \nnon choy salat", self)
        self.oshga.setGeometry(50,115,100,50)
        self.oshga.setFont(QFont("Poppins",7))
        self.oshga.setStyleSheet("color: rgb(0,0,0)")
        
        self.somsa=QCheckBox("Somsa", self)
        self.somsa.setGeometry(160,90,100,50)
        self.somsa.setFont(QFont("Poppins",18))
        self.somsa.setStyleSheet("color: rgb(0,0,0)")
        self.somsaga=QLabel("7.000 so'm", self)
        self.somsaga.setGeometry(160,115,100,50)
        self.somsaga.setFont(QFont("Poppins",7))
        self.somsaga.setStyleSheet("color: rgb(0,0,0)")
        
        self.lagman=QCheckBox("Lag'mon", self)
        self.lagman.setGeometry(320,90,250,50)
        self.lagman.setFont(QFont("Poppins",18))
        self.lagman.setStyleSheet("color: rgb(0,0,0)")
        self.lagmanga=QLabel("20.000 so'm", self)
        self.lagmanga.setGeometry(320,115,100,50)
        self.lagmanga.setFont(QFont("Poppins",7))
        self.lagmanga.setStyleSheet("color: rgb(0,0,0)")
        
        self.shashlik=QCheckBox("Shashlik", self)
        self.shashlik.setGeometry(480,90,250,50)
        self.shashlik.setFont(QFont("Poppins",18))
        self.shashlik.setStyleSheet("color: rgb(0,0,0)")
        self.shashlikga=QLabel("11.000 so'm", self)
        self.shashlikga.setGeometry(480,115,100,50)
        self.shashlikga.setFont(QFont("Poppins",7))
        self.shashlikga.setStyleSheet("color: rgb(0,0,0)")
        
        self.manti=QCheckBox("Manti", self)
        self.manti.setGeometry(640,90,250,50)
        self.manti.setFont(QFont("Poppins",18))
        self.manti.setStyleSheet("color: rgb(0,0,0)")
        self.mantiga=QLabel("7.000 so'm", self)
        self.mantiga.setGeometry(640,115,100,50)
        self.mantiga.setFont(QFont("Poppins",7))
        self.mantiga.setStyleSheet("color: rgb(0,0,0)")
        
        self.taom2=QLabel(self)
        self.taom2.setGeometry(20,150,250,50)
        self.taom2.setFont(QFont("Consolas",18))
        self.taom2.setText("2-taom: ")
        self.taom2.setStyleSheet("color: rgb(0,0,0)")
        
        self.shurva=QCheckBox("Sho'rva", self)
        self.shurva.setGeometry(50,185,100,50)
        self.shurva.setFont(QFont("Poppins",18))
        self.shurva.setStyleSheet("color: rgb(0,0,0)")
        self.shurvaga=QLabel("20.000 so'm", self)
        self.shurvaga.setGeometry(50,210,100,50)
        self.shurvaga.setFont(QFont("Poppins",7))
        self.shurvaga.setStyleSheet("color: rgb(0,0,0)")
        
        self.dolma=QCheckBox("Do'lma", self)
        self.dolma.setGeometry(160,185,100,50)
        self.dolma.setFont(QFont("Poppins",18))
        self.dolma.setStyleSheet("color: rgb(0,0,0)")
        self.dolmaga=QLabel("5.000 so'm (dona)", self)
        self.dolmaga.setGeometry(160,210,100,50)
        self.dolmaga.setFont(QFont("Poppins",7))
        self.dolmaga.setStyleSheet("color: rgb(0,0,0)")
        
        self.guja=QCheckBox("Guja", self)
        self.guja.setGeometry(320,185,250,50)
        self.guja.setFont(QFont("Poppins",18))
        self.guja.setStyleSheet("color: rgb(0,0,0)")
        self.gujaga=QLabel("20.000 so'm", self)
        self.gujaga.setGeometry(320,210,100,50)
        self.gujaga.setFont(QFont("Poppins",7))
        self.gujaga.setStyleSheet("color: rgb(0,0,0)")
        
        self.koza_shurva=QCheckBox("Ko'za sho'rva", self)
        self.koza_shurva.setGeometry(480,185,300,50)
        self.koza_shurva.setFont(QFont("Poppins",18))
        self.koza_shurva.setStyleSheet("color: rgb(0,0,0)")
        self.koza_shurvaga=QLabel("26.000 so'm", self)
        self.koza_shurvaga.setGeometry(480,210,100,50)
        self.koza_shurvaga.setFont(QFont("Poppins",7))
        self.koza_shurvaga.setStyleSheet("color: rgb(0,0,0)")
        
        self.mastava=QCheckBox("Mastava", self)
        self.mastava.setGeometry(650,185,250,50)
        self.mastava.setFont(QFont("Poppins",18))
        self.mastava.setStyleSheet("color: rgb(0,0,0)")
        self.mastavaga=QLabel("20.000 so'm", self)
        self.mastavaga.setGeometry(650,210,100,50)
        self.mastavaga.setFont(QFont("Poppins",7))
        self.mastavaga.setStyleSheet("color: rgb(0,0,0)")
        
        self.ichimlik=QLabel(self)
        self.ichimlik.setGeometry(20,250,250,50)
        self.ichimlik.setFont(QFont("Consolas",18))
        self.ichimlik.setText("Ichimliklar: ")
        self.ichimlik.setStyleSheet("color: rgb(0,0,0)")

        
        self.choy=QCheckBox("Choy", self)
        self.choy.setGeometry(50,285,200,50)
        self.choy.setFont(QFont("Poppins",18))
        self.choy.setStyleSheet("color: rgb(0,0,0)")
        self.choyga=QLabel("3.000 so'm", self)
        self.choyga.setGeometry(50,310,100,50)
        self.choyga.setFont(QFont("Poppins",7))
        self.choyga.setStyleSheet("color: rgb(0,0,0)")
        
        self.pepsi=QCheckBox("Pepsi", self)
        self.pepsi.setGeometry(160,285,100,50)
        self.pepsi.setFont(QFont("Poppins",18))
        self.pepsi.setStyleSheet("color: rgb(0,0,0)")
        self.pepsiga=QLabel("10.000 so'm/litr", self)
        self.pepsiga.setGeometry(160,310,100,50)
        self.pepsiga.setFont(QFont("Poppins",7))
        self.pepsiga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.cola=QCheckBox("Coca-Cola", self)
        self.cola.setGeometry(320,285,250,50)
        self.cola.setFont(QFont("Poppins",18))
        self.cola.setStyleSheet("color: rgb(0,0,0)")
        self.colaga=QLabel("10.000 so'm/litr", self)
        self.colaga.setGeometry(320,310,100,50)
        self.colaga.setFont(QFont("Poppins",7))
        self.colaga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.limon_choy=QCheckBox("Limon choy", self)
        self.limon_choy.setGeometry(480,285,300,50)
        self.limon_choy.setFont(QFont("Poppins",18))
        self.limon_choy.setStyleSheet("color: rgb(0,0,0)")
        self.limon_choyga=QLabel("10.000 so'm", self)
        self.limon_choyga.setGeometry(480,310,100,50)
        self.limon_choyga.setFont(QFont("Poppins",7))
        self.limon_choyga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.suv=QCheckBox("Suv", self)
        self.suv.setGeometry(650,285,250,50)
        self.suv.setFont(QFont("Poppins",18))
        self.suv.setStyleSheet("color: rgb(0,0,0)")
        self.suvga=QLabel("1.000 so'm/250mg", self)
        self.suvga.setGeometry(650,310,100,50)
        self.suvga.setFont(QFont("Poppins",7))
        self.suvga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.desert=QLabel(self)
        self.desert.setGeometry(20,340,250,50)
        self.desert.setFont(QFont("Consolas",18))
        self.desert.setText("Desert: ")
        self.desert.setStyleSheet("color: rgb(0,0,0)") 
        
        self.holva=QCheckBox("Holva", self)
        self.holva.setGeometry(50,385,200,50)
        self.holva.setFont(QFont("Poppins",18))
        self.holva.setStyleSheet("color: rgb(0,0,0)")
        self.holvaga=QLabel("5.000 so'm/dona", self)
        self.holvaga.setGeometry(50,410,100,50)
        self.holvaga.setFont(QFont("Poppins",7))
        self.holvaga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.paxlava=QCheckBox("Paxlava", self)
        self.paxlava.setGeometry(160,385,100,50)
        self.paxlava.setFont(QFont("Poppins",18))
        self.paxlava.setStyleSheet("color: rgb(0,0,0)")
        self.paxlavaga=QLabel("50.000 so'm/kg", self)
        self.paxlavaga.setGeometry(160,410,100,50)
        self.paxlavaga.setFont(QFont("Poppins",7))
        self.paxlavaga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.napalyon=QCheckBox("Napalyon", self)
        self.napalyon.setGeometry(320,385,250,50)
        self.napalyon.setFont(QFont("Poppins",18))
        self.napalyon.setStyleSheet("color: rgb(0,0,0)")
        self.napalyonga=QLabel("50.000 so'm/kg", self)
        self.napalyonga.setGeometry(160,410,100,50)
        self.napalyonga.setFont(QFont("Poppins",7))
        self.napalyonga.setStyleSheet("color: rgb(0,0,0)")
        
        self.gelato=QCheckBox("Gelato", self)
        self.gelato.setGeometry(480,385,300,50)
        self.gelato.setFont(QFont("Poppins",18))
        self.gelato.setStyleSheet("color: rgb(0,0,0)")
        self.gelatoga=QLabel("60.000 so'm/kg", self)
        self.gelatoga.setGeometry(480,410,100,50)
        self.gelatoga.setFont(QFont("Poppins",7))
        self.gelatoga.setStyleSheet("color: rgb(0,0,0)")
        
        
        self.cheesecake=QCheckBox("Cheesecake", self)
        self.cheesecake.setGeometry(650,385,250,50)
        self.cheesecake.setFont(QFont("Poppins",18))
        self.cheesecake.setStyleSheet("color: rgb(0,0,0)")
        self.cheesecakega=QLabel("65.000 so'm/kg", self)
        self.cheesecakega.setGeometry(650,410,100,50)
        self.cheesecakega.setFont(QFont("Poppins",7))
        self.cheesecakega.setStyleSheet("color: rgb(0,0,0)")
        
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
        with open("Hisob_kitob.txt", "wt") as f:
            
            f.write("Birinchi taom: ")
            if self.osh.isChecked():
                f.write("Osh")
                self.ovqat1+=30.000
            elif self.somsa.isChecked():
                f.write("Somsa")
                self.ovqat1+=7.000
            elif self.lagman.isChecked():
                f.write("Lagman")
                self.ovqat1+=20.000
            elif self.manti.isChecked():
                f.write("Manti")
                self.ovqat1+=7.000
            else:
                f.write("Shashlik")
                self.ovqat1+=11.000
            f.write(f"\t{self.ovqat1}00\n")
            
            
            f.write("Ikkinchi taom: ")
            if self.shurva.isChecked():
                f.write("Shurva")
                self.ovqat2+=20.000
            elif self.dolma.isChecked():
                f.write("Do'lma")
                self.ovqat2+=5.000
            elif self.guja.isChecked():
                f.write("Guja")
                self.ovqat2+=20.000
            elif self.koza_shurva.isChecked():
                f.write("Ko'za shurva")
                self.ovqat2+=26.000
            else:
                f.write("Mastava")
                self.ovqat1+=20.000
            f.write(f"\t{self.ovqat2}00\n")
            
            f.write("Ichimlik: ")
            if self.choy.isChecked():
                f.write("Choy")
                self.ichimliklar+=3.000
            elif self.pepsi.isChecked():
                f.write("Pepsi")
                self.ichimliklar+=10.000
            elif self.cola.isChecked():
                f.write("Cola")
                self.ichimliklar+=10.000
            elif self.limon_choy.isChecked():
                f.write("Limon choy")
                self.ichimliklar+=10.000
            else:
                f.write("Suv")
                self.ichimliklar+=1.000
            f.write(f"\t{self.ichimliklar}00\n")
            
            f.write("Desert: ")
            if self.holva.isChecked():
                f.write("Holva")
                self.desertcha+=5.000
            elif self.paxlava.isChecked():
                f.write("Paxlava")
                self.desertcha+=50.000
            elif self.gelato.isChecked():
                f.write("Gealito")
                self.desertcha+=60.000
            elif self.cheesecake.isChecked():
                f.write("Cheesecake")
                self.desertcha+=65.000
            else:
                f.write("Napalyon")
                self.desertcha+=60.000
            f.write(f"\t{self.desertcha}00\n")
            hisob=((self.ovqat1+self.ovqat2+self.ichimliklar+self.desertcha)//10)
            f.write(f"\n\nShundan xizmat haqqi: {hisob}00\n")
            f.write(f"Jami: {self.ovqat1+self.ovqat2+self.ichimliklar+self.desertcha+hisob}00\n")
            f.write("\tYoqimli ishtaha!!!")
            
    def push(self):
        os.system("C:\\Users\\Oybek\\python\\Hisob_kitob.txt") 
            
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    project=dastur()
    project.show()
    sys.exit(app.exec_())