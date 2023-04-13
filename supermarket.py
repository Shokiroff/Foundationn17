import os
import sys
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.chdir("/home/aziza/Downloads/AZIZA1")

class products(QWidget):
      hisob1=0
      hisob2=0
      hisob3=0
      hisob4=0
      def __init__(self):
           
          super().__init__()
          self.setMaximumSize(1120,760)
          self.setMinimumSize(1120,760)
          self.move(150,100)
          self.setWindowTitle("SUPERMARKET")


          self.name=QLabel(self)
          self.name.setGeometry(400,5,600,50)
          self.name.setFont(QFont("Times New Roman",30))
          self.name.setText("SUPERMARKET")
          self.name.setStyleSheet("color: rgb(50,205,50);")

          self.price=QLabel(self)
          self.price.setGeometry(430,50,100,50)
          self.price.setFont(QFont("Times New Roman",18))
          self.price.setText("Narxi: ")
          self.price.setStyleSheet("color: rgb(220,20,60);")

          self.meat=QLabel(self)
          self.meat.setGeometry(10,150,250,60)
          self.meat.setFont(QFont("Calibri",20))
          self.meat.setText("   Go'sht\nmaxsuloti: ")
          self.meat.setStyleSheet("color: rgb(255,0,0);")

          self.meat1=QCheckBox("Tovuq Go'shti",self)
          self.meat1.setGeometry(160,80,250,50)
          self.meat1.setFont(QFont("Calibri",16))
          self.meat1.setStyleSheet("color: rgb(65,74,76);")

          self.cost=QLabel(self)
          self.cost.setGeometry(430,80,250,50)
          self.cost.setFont(QFont("Calibri",16))
          self.cost.setText("50000 ")
          self.cost.setStyleSheet("color: rgb(139,0,0);")


          self.meat2=QCheckBox("Qo'y Go'shti",self)
          self.meat2.setGeometry(160,120,250,50)
          self.meat2.setFont(QFont("Calibri",16))
          self.meat2.setStyleSheet("color: rgb(65,74,76);")

          self.cost1=QLabel(self)
          self.cost1.setGeometry(430,120,250,50)
          self.cost1.setFont(QFont("Calibri",16))
          self.cost1.setText("80000 ")
          self.cost1.setStyleSheet("color: rgb(139,0,0);")


          self.meat3=QCheckBox("Mol Go'shti",self)
          self.meat3.setGeometry(160,160,250,50)
          self.meat3.setFont(QFont("Calibri",16))
          self.meat3.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost2=QLabel(self)
          self.cost2.setGeometry(430,160,250,50)
          self.cost2.setFont(QFont("Calibri",16))
          self.cost2.setText("85000 ")
          self.cost2.setStyleSheet("color: rgb(139,0,0);")

          self.meat4=QCheckBox("Baliq Go'shti",self)
          self.meat4.setGeometry(160,200,250,50)
          self.meat4.setFont(QFont("Calibri",16))
          self.meat4.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost3=QLabel(self)
          self.cost3.setGeometry(430,200,250,50)
          self.cost3.setFont(QFont("Calibri",16))
          self.cost3.setText("70000 ")
          self.cost3.setStyleSheet("color: rgb(139,0,0);")

          self.meat5=QCheckBox("Qiyma",self)
          self.meat5.setGeometry(160,240,250,50)
          self.meat5.setFont(QFont("Calibri",16))
          self.meat5.setStyleSheet("color: rgb(65,74,76);")

          self.cost4=QLabel(self)
          self.cost4.setGeometry(430,240,250,50)
          self.cost4.setFont(QFont("Calibri",16))
          self.cost4.setText("65000 ")
          self.cost4.setStyleSheet("color: rgb(139,0,0);")

          self.fruit=QLabel(self)
          self.fruit.setGeometry(600,160,250,50)
          self.fruit.setFont(QFont("Calibri",20))
          self.fruit.setText("Mevalar: ")
          self.fruit.setStyleSheet("color: rgb(255,0,0);")

          self.price1=QLabel(self)
          self.price1.setGeometry(950,50,100,50)
          self.price1.setFont(QFont("Times New Roman",18))
          self.price1.setText("Narxi: ")
          self.price1.setStyleSheet("color: rgb(220,20,60);")


          self.fruit1=QCheckBox("Apelsin",self)
          self.fruit1.setGeometry(730,80,250,50)
          self.fruit1.setFont(QFont("Calibri",16))
          self.fruit1.setStyleSheet("color: rgb(65,74,76);")

          self.cost5=QLabel(self)
          self.cost5.setGeometry(950,80,250,50)
          self.cost5.setFont(QFont("Calibri",16))
          self.cost5.setText("35000 ")
          self.cost5.setStyleSheet("color: rgb(139,0,0);")

          self.fruit2=QCheckBox("Banan",self)
          self.fruit2.setGeometry(730,120,250,50)
          self.fruit2.setFont(QFont("Calibri",16))
          self.fruit2.setStyleSheet("color: rgb(65,74,76);")

          self.cost6=QLabel(self)
          self.cost6.setGeometry(950,120,250,50)
          self.cost6.setFont(QFont("Calibri",16))
          self.cost6.setText("24000 ")
          self.cost6.setStyleSheet("color: rgb(139,0,0);")

          self.fruit3=QCheckBox("Kivi",self)
          self.fruit3.setGeometry(730,160,250,50)
          self.fruit3.setFont(QFont("Calibri",16))
          self.fruit3.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost7=QLabel(self)
          self.cost7.setGeometry(950,160,250,50)
          self.cost7.setFont(QFont("Calibri",16))
          self.cost7.setText("22000 ")
          self.cost7.setStyleSheet("color: rgb(139,0,0);")

          self.fruit4=QCheckBox("Ananas",self)
          self.fruit4.setGeometry(730,200,250,50)
          self.fruit4.setFont(QFont("Calibri",16))
          self.fruit4.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost8=QLabel(self)
          self.cost8.setGeometry(950,200,250,50)
          self.cost8.setFont(QFont("Calibri",16))
          self.cost8.setText("65000 ")
          self.cost8.setStyleSheet("color: rgb(139,0,0);")

          self.fruit5=QCheckBox("Gilos",self)
          self.fruit5.setGeometry(730,240,250,50)
          self.fruit5.setFont(QFont("Calibri",16))
          self.fruit5.setStyleSheet("color: rgb(65,74,76);")

          self.cost9=QLabel(self)
          self.cost9.setGeometry(950,240,250,50)
          self.cost9.setFont(QFont("Calibri",16))
          self.cost9.setText("70000 ")
          self.cost9.setStyleSheet("color: rgb(139,0,0);")

          self.price2=QLabel(self)
          self.price2.setGeometry(430,300,100,50)
          self.price2.setFont(QFont("Times New Roman",18))
          self.price2.setText("Narxi: ")
          self.price2.setStyleSheet("color: rgb(220,20,60);")

          self.vegetable=QLabel(self)
          self.vegetable.setGeometry(10,380,250,60)
          self.vegetable.setFont(QFont("Calibri",20))
          self.vegetable.setText("Sabzavotlar: ")
          self.vegetable.setStyleSheet("color: rgb(255,0,0);")

          self.vegetable1=QCheckBox("Bodring",self)
          self.vegetable1.setGeometry(190,340,250,50)
          self.vegetable1.setFont(QFont("Calibri",16))
          self.vegetable1.setStyleSheet("color: rgb(65,74,76);")

          self.cost10=QLabel(self)
          self.cost10.setGeometry(430,340,250,50)
          self.cost10.setFont(QFont("Calibri",16))
          self.cost10.setText("32000 ")
          self.cost10.setStyleSheet("color: rgb(139,0,0);")

          self.vegetable2=QCheckBox("Pamidor",self)
          self.vegetable2.setGeometry(190,370,250,50)
          self.vegetable2.setFont(QFont("Calibri",16))
          self.vegetable2.setStyleSheet("color: rgb(65,74,76);")

          self.cost11=QLabel(self)
          self.cost11.setGeometry(430,370,250,50)
          self.cost11.setFont(QFont("Calibri",16))
          self.cost11.setText("22000 ")
          self.cost11.setStyleSheet("color: rgb(139,0,0);")

          self.vegetable3=QCheckBox("Sabzi",self)
          self.vegetable3.setGeometry(190,400,250,50)
          self.vegetable3.setFont(QFont("Calibri",16))
          self.vegetable3.setStyleSheet("color: rgb(65,74,76);")
    
          self.cost12=QLabel(self)
          self.cost12.setGeometry(430,400,250,50)
          self.cost12.setFont(QFont("Calibri",16))
          self.cost12.setText("10000 ")
          self.cost12.setStyleSheet("color: rgb(139,0,0);")

          self.vegetable4=QCheckBox("Piyoz",self)
          self.vegetable4.setGeometry(190,430,250,50)
          self.vegetable4.setFont(QFont("Calibri",16))
          self.vegetable4.setStyleSheet("color: rgb(65,74,76);")

          self.cost13=QLabel(self)
          self.cost13.setGeometry(430,430,250,50)
          self.cost13.setFont(QFont("Calibri",16))
          self.cost13.setText("20000 ")
          self.cost13.setStyleSheet("color: rgb(139,0,0);")

          self.vegetable5=QCheckBox("Kartoshka",self)
          self.vegetable5.setGeometry(190,460,250,50)
          self.vegetable5.setFont(QFont("Calibri",16))
          self.vegetable5.setStyleSheet("color: rgb(65,74,76);")

          self.cost14=QLabel(self)
          self.cost14.setGeometry(430,460,250,50)
          self.cost14.setFont(QFont("Calibri",16))
          self.cost14.setText("15000 ")
          self.cost14.setStyleSheet("color: rgb(139,0,0);")


          self.dairy=QLabel(self)
          self.dairy.setGeometry(580,380,250,70)
          self.dairy.setFont(QFont("Calibri",20))
          self.dairy.setText("      Sut\nmahsulotlari:")
          self.dairy.setStyleSheet("color: rgb(255,0,0);")

          self.price3=QLabel(self)
          self.price3.setGeometry(950,300,100,50)
          self.price3.setFont(QFont("Times New Roman",18))
          self.price3.setText("Narxi: ")
          self.price3.setStyleSheet("color: rgb(220,20,60);")

          self.dairy1=QCheckBox("Sut",self)
          self.dairy1.setGeometry(760,340,250,50)
          self.dairy1.setFont(QFont("Calibri",16))
          self.dairy1.setStyleSheet("color: rgb(65,74,76);")

          self.cost15=QLabel(self)
          self.cost15.setGeometry(950,340,250,50)
          self.cost15.setFont(QFont("Calibri",16))
          self.cost15.setText("20000 ")
          self.cost15.setStyleSheet("color: rgb(139,0,0);")

          self.dairy2=QCheckBox("Qaymoq",self)
          self.dairy2.setGeometry(760,370,250,50)
          self.dairy2.setFont(QFont("Calibri",16))
          self.dairy2.setStyleSheet("color: rgb(65,74,76);")

          self.cost16=QLabel(self)
          self.cost16.setGeometry(950,370,250,50)
          self.cost16.setFont(QFont("Calibri",16))
          self.cost16.setText("30000 ")
          self.cost16.setStyleSheet("color: rgb(139,0,0);")

          self.dairy3=QCheckBox("Tvarog",self)
          self.dairy3.setGeometry(760,400,250,50)
          self.dairy3.setFont(QFont("Calibri",16))
          self.dairy3.setStyleSheet("color: rgb(65,74,76);")

          self.cost17=QLabel(self)
          self.cost17.setGeometry(950,400,250,50)
          self.cost17.setFont(QFont("Calibri",16))
          self.cost17.setText("18000 ")
          self.cost17.setStyleSheet("color: rgb(139,0,0);")

          self.dairy4=QCheckBox("Brinza",self)
          self.dairy4.setGeometry(760,430,250,50)
          self.dairy4.setFont(QFont("Calibri",16))
          self.dairy4.setStyleSheet("color: rgb(65,74,76);")
 
          self.cost18=QLabel(self)
          self.cost18.setGeometry(950,430,250,50)
          self.cost18.setFont(QFont("Calibri",16))
          self.cost18.setText("50000 ")
          self.cost18.setStyleSheet("color: rgb(139,0,0);")
    
          self.dairy5=QCheckBox("Kefir",self)
          self.dairy5.setGeometry(760,460,250,50)
          self.dairy5.setFont(QFont("Calibri",16))
          self.dairy5.setStyleSheet("color: rgb(65,74,76);")

          self.cost19=QLabel(self)
          self.cost19.setGeometry(950,460,250,50)
          self.cost19.setFont(QFont("Calibri",16))
          self.cost19.setText("12000 ")
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
          f=open("hisobla.txt","wt")
          f.write("\t\t***************HISOB**************\n")
          if self.meat1.isChecked():
              f.write(f"Go'sht mahsuloti: {self.meat1.text()}     {self.cost.text()}\n")
              products.hisob1+=50000
          elif self.meat2.isChecked():
              f.write(f"Go'sht mahsuloti: {self.meat2.text()}     {self.cost1.text()}\n")
              products.hisob1+=80000
          elif self.meat3.isChecked():
              f.write(f"Go'sht mahsuloti: {self.meat3.text()}     {self.cost2.text()}\n")
              products.hisob1+=85000
          elif self.meat4.isChecked():
              f.write(f"Go'sht mahsuloti: {self.meat4.text()}     {self.cost3.text()}\n")
              products.hisob1+=70000
          else: 
              f.write(f"Go'sht mahsuloti: {self.meat5.text()}     {self.cost4.text()}\n")
              products.hisob1+=65000
              f.write(f"\t{self.hisob1}\n")
          if self.fruit1.isChecked():
              f.write(f"Mevalar: {self.fruit1.text()}     {self.cost5.text()}\n")
              products.hisob2+=35000
          elif self.fruit2.isChecked():
              f.write(f"Mevalar: {self.fruit2.text()}     {self.cost6.text()}\n")
              products.hisob2+=24000
          elif self.fruit3.isChecked():
              f.write(f"Mevalar: {self.fruit3.text()}     {self.cost7.text()}\n")
              products.hisob2+=22000
          elif self.fruit4.isChecked():
              f.write(f"Mevalar: {self.fruit4.text()}     {self.cost8.text()}\n")
              products.hisob2+=65000
          else: 
              f.write(f"Mevalar: {self.fruit5.text()}     {self.cost9.text()}\n")
              products.hisob2+=7000
              f.write(f"\t{self.hisob2}\n")

          if self.vegetable1.isChecked():
             f.write(f"Sabzavotlar: {self.vegetable1.text()}     {self.cost10.text()}\n")
             products.hisob3+=32000
          elif self.vegetable2.isChecked():
             f.write(f"Sabzavotlar: {self.vegetable2.text()}     {self.cost11.text()}\n")
             products.hisob3+=22000
          elif self.vegetable3.isChecked(): 
             f.write(f"Sabzavotlar: {self.vegetable3.text()}     {self.cost12.text()}\n")
             products.hisob3+=10000
          elif self.vegetable4.isChecked():
             f.write(f"Sabzavotlar: {self.vegetable4.text()}     {self.cost13.text()}\n")
             products.hisob3+=20000
          else:  
             f.write(f"Sabzavotlar: {self.vegetable5.text()}     {self.cost14.text()}\n")
             products.hisob3+=15000
             f.write(f"\t{self.hisob3}\n")


          if self.dairy1.isChecked():
             f.write(f"Sut mahsulotlari: {self.dairy1.text()}    {self.cost15.text()}\n")
             products.hisob4+=20000
          elif self.dairy2.isChecked():
             f.write(f"Sut mahsulotlari: {self.dairy2.text()}    {self.cost16.text()}\n")
             products.hisob4+=30000
          elif self.dairy3.isChecked():
             f.write(f"Sut mahsulotlari: {self.dairy3.text()}    {self.cost17.text()}\n") 
             products.hisob4+=18000
          elif self.dairy4.isChecked():
             f.write(f"Sut mahsulotlari: {self.dairy4.text()}    {self.cost18.text()}\n")
             products.hisob4+=50000
          else:  
             f.write(f"Sut mahsulotlari: {self.dairy5.text()}    {self.cost19.text()}\n")
             products.hisob4+=12000
             f.write(f"\t{self.hisob4}\n")
    
          f.write(f"Umumiy hisob:{products.hisob1+products.hisob2+products.hisob3+products.hisob4}\n")
          f.write("Data: 12/04/2023    12:32:23\n")
          f.write("To'lov shakli: plastik karta\n")
          f.write("Kassir: NIgmatov Nuriddin\n")
          f.write("Xaridingiz uchun rahmat!\n")
          f.write("FM: UZ210398765573\n")
          f.write("FB: 002687651359\n")

if __name__=="__main__":
   app=QApplication(sys.argv)
   project=products()
   project.show()
   sys.exit(app.exec_())
