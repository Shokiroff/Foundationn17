import os
import sys
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.chdir("/home/aziza/Downloads/AZIZA1")

class menu(QWidget):
     hisob1=0
     hisob2=0
     hisob3=0
     hisob4=0
     def __init__(self):
           
          super().__init__()
          self.setMaximumSize(1080,760)
          self.setMinimumSize(1080,760)
          self.move(150,100)
          self.setWindowTitle("MENU")


          self.name=QLabel(self)
          self.name.setGeometry(260,5,600,50)
          self.name.setFont(QFont("Times New Roman",30))
          self.name.setText("EFENDI RESTAURANT MENU: ")
          self.name.setStyleSheet("color: rgb(220,20,60);")

          self.price=QLabel(self)
          self.price.setGeometry(430,50,100,50)
          self.price.setFont(QFont("Times New Roman",18))
          self.price.setText("Narxi: ")
          self.price.setStyleSheet("color: rgb(220,20,60);")

          self.first_meal=QLabel(self)
          self.first_meal.setGeometry(30,150,250,60)
          self.first_meal.setFont(QFont("Calibri",20))
          self.first_meal.setText("Birinchi\n taom: ")
          self.first_meal.setStyleSheet("color: rgb(139,0,0);")

          self.meal1=QCheckBox("Chechevichniy sup",self)
          self.meal1.setGeometry(160,80,250,50)
          self.meal1.setFont(QFont("Calibri",16))
          self.meal1.setStyleSheet("color: rgb(65,74,76);")

          self.cost=QLabel(self)
          self.cost.setGeometry(430,80,250,50)
          self.cost.setFont(QFont("Calibri",16))
          self.cost.setText("35000 ")
          self.cost.setStyleSheet("color: rgb(139,0,0);")


          self.meal2=QCheckBox("Kurinniy bulyon",self)
          self.meal2.setGeometry(160,120,250,50)
          self.meal2.setFont(QFont("Calibri",16))
          self.meal2.setStyleSheet("color: rgb(65,74,76);")

          self.cost1=QLabel(self)
          self.cost1.setGeometry(430,120,250,50)
          self.cost1.setFont(QFont("Calibri",16))
          self.cost1.setText("40000 ")
          self.cost1.setStyleSheet("color: rgb(139,0,0);")


          self.meal3=QCheckBox("Sup Ezogelin",self)
          self.meal3.setGeometry(160,160,250,50)
          self.meal3.setFont(QFont("Calibri",16))
          self.meal3.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost2=QLabel(self)
          self.cost2.setGeometry(430,160,250,50)
          self.cost2.setFont(QFont("Calibri",16))
          self.cost2.setText("30000 ")
          self.cost2.setStyleSheet("color: rgb(139,0,0);")

          self.meal4=QCheckBox("Sup Kalapacha",self)
          self.meal4.setGeometry(160,200,250,50)
          self.meal4.setFont(QFont("Calibri",16))
          self.meal4.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost3=QLabel(self)
          self.cost3.setGeometry(430,200,250,50)
          self.cost3.setFont(QFont("Calibri",16))
          self.cost3.setText("35000 ")
          self.cost3.setStyleSheet("color: rgb(139,0,0);")

          self.meal5=QCheckBox("Ikshembe",self)
          self.meal5.setGeometry(160,240,250,50)
          self.meal5.setFont(QFont("Calibri",16))
          self.meal5.setStyleSheet("color: rgb(65,74,76);")

          self.cost4=QLabel(self)
          self.cost4.setGeometry(430,240,250,50)
          self.cost4.setFont(QFont("Calibri",16))
          self.cost4.setText("32000 ")
          self.cost4.setStyleSheet("color: rgb(139,0,0);")

          self.main_dishes=QLabel(self)
          self.main_dishes.setGeometry(600,160,250,50)
          self.main_dishes.setFont(QFont("Calibri",20))
          self.main_dishes.setText("Ikkinchi\n taom: ")
          self.main_dishes.setStyleSheet("color: rgb(139,0,0);")

          self.price1=QLabel(self)
          self.price1.setGeometry(950,50,100,50)
          self.price1.setFont(QFont("Times New Roman",18))
          self.price1.setText("Narxi: ")
          self.price1.setStyleSheet("color: rgb(220,20,60);")


          self.dish1=QCheckBox("Efendi Kebab",self)
          self.dish1.setGeometry(730,80,250,50)
          self.dish1.setFont(QFont("Calibri",16))
          self.dish1.setStyleSheet("color: rgb(65,74,76);")

          self.cost5=QLabel(self)
          self.cost5.setGeometry(950,80,250,50)
          self.cost5.setFont(QFont("Calibri",16))
          self.cost5.setText("70000 ")
          self.cost5.setStyleSheet("color: rgb(139,0,0);")

          self.dish2=QCheckBox("Beyti Kebab",self)
          self.dish2.setGeometry(730,120,250,50)
          self.dish2.setFont(QFont("Calibri",16))
          self.dish2.setStyleSheet("color: rgb(65,74,76);")

          self.cost6=QLabel(self)
          self.cost6.setGeometry(950,120,250,50)
          self.cost6.setFont(QFont("Calibri",16))
          self.cost6.setText("50000 ")
          self.cost6.setStyleSheet("color: rgb(139,0,0);")

          self.dish3=QCheckBox("Efendi Kofte",self)
          self.dish3.setGeometry(730,160,250,50)
          self.dish3.setFont(QFont("Calibri",16))
          self.dish3.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost7=QLabel(self)
          self.cost7.setGeometry(950,160,250,50)
          self.cost7.setFont(QFont("Calibri",16))
          self.cost7.setText("45000 ")
          self.cost7.setStyleSheet("color: rgb(139,0,0);")

          self.dish4=QCheckBox("Adana Kebab",self)
          self.dish4.setGeometry(730,200,250,50)
          self.dish4.setFont(QFont("Calibri",16))
          self.dish4.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost8=QLabel(self)
          self.cost8.setGeometry(950,200,250,50)
          self.cost8.setFont(QFont("Calibri",16))
          self.cost8.setText("55000 ")
          self.cost8.setStyleSheet("color: rgb(139,0,0);")

          self.dish5=QCheckBox("Iskandar Kebab",self)
          self.dish5.setGeometry(730,240,250,50)
          self.dish5.setFont(QFont("Calibri",16))
          self.dish5.setStyleSheet("color: rgb(65,74,76);")

          self.cost9=QLabel(self)
          self.cost9.setGeometry(950,240,250,50)
          self.cost9.setFont(QFont("Calibri",16))
          self.cost9.setText("48000 ")
          self.cost9.setStyleSheet("color: rgb(139,0,0);")

          self.price2=QLabel(self)
          self.price2.setGeometry(430,300,100,50)
          self.price2.setFont(QFont("Times New Roman",18))
          self.price2.setText("Narxi: ")
          self.price2.setStyleSheet("color: rgb(220,20,60);")

          self.desserts=QLabel(self)
          self.desserts.setGeometry(30,380,250,60)
          self.desserts.setFont(QFont("Calibri",20))
          self.desserts.setText("Dessertlar: ")
          self.desserts.setStyleSheet("color: rgb(139,0,0);")

          self.dessert1=QCheckBox("Shokoladli keks",self)
          self.dessert1.setGeometry(190,340,250,50)
          self.dessert1.setFont(QFont("Calibri",16))
          self.dessert1.setStyleSheet("color: rgb(65,74,76);")

          self.cost10=QLabel(self)
          self.cost10.setGeometry(430,340,250,50)
          self.cost10.setFont(QFont("Calibri",16))
          self.cost10.setText("25000 ")
          self.cost10.setStyleSheet("color: rgb(139,0,0);")

          self.dessert2=QCheckBox("Turetskiy paxlava",self)
          self.dessert2.setGeometry(190,370,250,50)
          self.dessert2.setFont(QFont("Calibri",16))
          self.dessert2.setStyleSheet("color: rgb(65,74,76);")

          self.cost11=QLabel(self)
          self.cost11.setGeometry(430,370,250,50)
          self.cost11.setFont(QFont("Calibri",16))
          self.cost11.setText("30000 ")
          self.cost11.setStyleSheet("color: rgb(139,0,0);")

          self.dessert3=QCheckBox("Baklava Prinses",self)
          self.dessert3.setGeometry(190,400,250,50)
          self.dessert3.setFont(QFont("Calibri",16))
          self.dessert3.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost12=QLabel(self)
          self.cost12.setGeometry(430,400,250,50)
          self.cost12.setFont(QFont("Calibri",16))
          self.cost12.setText("33000 ")
          self.cost12.setStyleSheet("color: rgb(139,0,0);")

          self.dessert4=QCheckBox("Turetskiy puding",self)
          self.dessert4.setGeometry(190,430,250,50)
          self.dessert4.setFont(QFont("Calibri",16))
          self.dessert4.setStyleSheet("color: rgb(65,74,76);")

          self.cost13=QLabel(self)
          self.cost13.setGeometry(430,430,250,50)
          self.cost13.setFont(QFont("Calibri",16))
          self.cost13.setText("25000 ")
          self.cost13.setStyleSheet("color: rgb(139,0,0);")

          self.dessert5=QCheckBox("Revaniye",self)
          self.dessert5.setGeometry(190,460,250,50)
          self.dessert5.setFont(QFont("Calibri",16))
          self.dessert5.setStyleSheet("color: rgb(65,74,76);")

          self.cost14=QLabel(self)
          self.cost14.setGeometry(430,460,250,50)
          self.cost14.setFont(QFont("Calibri",16))
          self.cost14.setText("25000 ")
          self.cost14.setStyleSheet("color: rgb(139,0,0);")


          self.drinks=QLabel(self)
          self.drinks.setGeometry(600,380,250,50)
          self.drinks.setFont(QFont("Calibri",20))
          self.drinks.setText("Ichimliklar: ")
          self.drinks.setStyleSheet("color: rgb(139,0,0);")

          self.price3=QLabel(self)
          self.price3.setGeometry(950,300,100,50)
          self.price3.setFont(QFont("Times New Roman",18))
          self.price3.setText("Narxi: ")
          self.price3.setStyleSheet("color: rgb(220,20,60);")

          self.drink1=QCheckBox("Moxito",self)
          self.drink1.setGeometry(760,340,250,50)
          self.drink1.setFont(QFont("Calibri",16))
          self.drink1.setStyleSheet("color: rgb(65,74,76);")

          self.cost15=QLabel(self)
          self.cost15.setGeometry(950,340,250,50)
          self.cost15.setFont(QFont("Calibri",16))
          self.cost15.setText("18000 ")
          self.cost15.setStyleSheet("color: rgb(139,0,0);")

          self.drink2=QCheckBox("Aysti",self)
          self.drink2.setGeometry(760,370,250,50)
          self.drink2.setFont(QFont("Calibri",16))
          self.drink2.setStyleSheet("color: rgb(65,74,76);")

          self.cost16=QLabel(self)
          self.cost16.setGeometry(950,370,250,50)
          self.cost16.setFont(QFont("Calibri",16))
          self.cost16.setText("16000 ")
          self.cost16.setStyleSheet("color: rgb(139,0,0);")

          self.drink3=QCheckBox("Sok",self)
          self.drink3.setGeometry(760,400,250,50)
          self.drink3.setFont(QFont("Calibri",16))
          self.drink3.setStyleSheet("color: rgb(65,74,76);")

          self.cost17=QLabel(self)
          self.cost17.setGeometry(950,400,250,50)
          self.cost17.setFont(QFont("Calibri",16))
          self.cost17.setText("13000 ")
          self.cost17.setStyleSheet("color: rgb(139,0,0);")

          self.drink4=QCheckBox("Kofe",self)
          self.drink4.setGeometry(760,430,250,50)
          self.drink4.setFont(QFont("Calibri",16))
          self.drink4.setStyleSheet("color: rgb(65,74,76);")
 
          self.cost18=QLabel(self)
          self.cost18.setGeometry(950,430,250,50)
          self.cost18.setFont(QFont("Calibri",16))
          self.cost18.setText("15000 ")
          self.cost18.setStyleSheet("color: rgb(139,0,0);")
    
          self.drink5=QCheckBox("Limonad",self)
          self.drink5.setGeometry(760,460,250,50)
          self.drink5.setFont(QFont("Calibri",16))
          self.drink5.setStyleSheet("color: rgb(65,74,76);")

          self.cost19=QLabel(self)
          self.cost19.setGeometry(950,460,250,50)
          self.cost19.setFont(QFont("Calibri",16))
          self.cost19.setText("20000 ")
          self.cost19.setStyleSheet("color: rgb(139,0,0);")

          self.cheque=QPushButton("Hisobni to'lash",self)
          self.cheque.resize(250,50)
          self.cheque.move(390,540)
          self.cheque.setFont(QFont("Consolas",18))
          self.cheque.setStyleSheet("""
                                  color: rgb(255,255,102);   
                                  border-color: rgb(178,236,93);
                                  border-radius: 15px;
                                  border-width: 3px;
                                  border-style: outset;
                                  background-color: rgb(50,205,50);
                                  """)
          self.cheque.clicked.connect(self.hisob)


     def hisob(self):
          f=open("hisoblash.txt","wt")
          f.write("\t\t***************HISOB**************\n")
          if self.meal1.isChecked():
             f.write(f"Birinchi taom: {self.meal1.text()}     {self.cost.text()}\n")
             self.hisob1+=35000
          elif self.meal2.isChecked():
             f.write(f"Birinchi taom: {self.meal2.text()}     {self.cost1.text()}\n")
             self.hisob1+=40000
          elif self.meal3.isChecked():
             f.write(f"Birinchi taom: {self.meal3.text()}     {self.cost2.text()}\n")
             self.hisob1+=30000
          elif self.meal4.isChecked():
             f.write(f"Birinchi taom: {self.meal4.text()}     {self.cost3.text()}\n")
             self.hisob1+=35000
          else: 
             f.write(f"Birinchi taom: {self.meal5.text()}     {self.cost4.text()}\n")
             self.hisob1+=32000
             f.write(f"\t{self.hisob1}\n")
          if self.dish1.isChecked():
             f.write(f"Ikkinchi taom: {self.dish1.text()}     {self.cost5.text()}\n")
               self.hisob2+=70000
          elif self.dish2.isChecked():
             f.write(f"Ikkinchi taom: {self.dish2.text()}     {self.cost6.text()}\n")
              self.hisob2+=50000
          elif self.dish3.isChecked():
             f.write(f"Ikkinchi taom: {self.dish3.text()}     {self.cost7.text()}\n")
              self.hisob2+=45000
          elif self.dish4.isChecked():
             f.write(f"Ikkinchi taom: {self.dish4.text()}     {self.cost8.text()}\n")
              self.hisob2+=55000
          else: 
             f.write(f"Ikkinchi taom: {self.dish5.text()}     {self.cost9.text()}\n")
             self.hisob2+=48000
             f.write(f"\t{self.hisob2}\n")

          if self.dessert1.isChecked():
             f.write(f"Dessert: {self.dessert1.text()}     {self.cost10.text()}\n")
             self.hisob3+=25000
          elif self.dessert2.isChecked():
             f.write(f"Dessert: {self.dessert2.text()}     {self.cost11.text()}\n")
             self.hisob3+=30000
          elif self.dessert3.isChecked(): 
             f.write(f"Dessert: {self.dessert3.text()}     {self.cost12.text()}\n")
             self.hisob3+=33000
          elif self.dessert4.isChecked():
             f.write(f"Dessert: {self.dessert4.text()}     {self.cost13.text()}\n")
             self.hisob3+=25000
          else:  
             f.write(f"Dessert: {self.dessert5.text()}     {self.cost14.text()}\n")
             self.hisob3+=25000
             f.write(f"\t{self.hisob3}\n")


          if self.drink1.isChecked():
             f.write(f"Ichimliklar: {self.drink1.text()}    {self.cost15.text()}\n")
             self.hisob4+=18000
          elif self.drink2.isChecked():
             f.write(f"Ichimliklar: {self.drink2.text()}    {self.cost16.text()}\n")
             self.hisob4+=16000
          elif self.drink3.isChecked():
             f.write(f"Ichimlikalr: {self.drink3.text()}    {self.cost17.text()}\n") 
             self.hisob4+=13000
          elif self.drink4.isChecked():
             f.write(f"Ichimliklar: {self.drink4.text()}    {self.cost18.text()}\n")
             self.hisob4+=15000
          else:  
             f.write(f"Ichimliklar: {self.drink5.text()}    {self.cost19.text()}\n")
             self.hisob4+=20000
             f.write(f"\t{self.hisob4}\n")
           list=(self.hisob1+self.hisob2+self.hisob3+self.hisob4)
           f.write(f"UMumiy hisob:{self.hisob1+self.hisob2+self.hisob3+self.hisob4}\n")
if __name__=="__main__":
   app=QApplication(sys.argv)
   project=menu()
   project.show()
   sys.exit(app.exec_())
