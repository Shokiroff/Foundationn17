import os
import sys
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ilova(QMainWindow):
      def __init__(self):
          QMainWindow.__init__(self) 
          self.setMaximumSize(1270,670)
          self.setMinimumSize(1270,670)
          self.setWindowIcon(QIcon(QPixmap("/home/aziza/Downloads/AZIZA1/home.png")))

          self.name=QLabel(self)
          self.name.setGeometry(70,5,1000,50)
          self.name.setFont(QFont("Times New Roman",16))
          self.name.setText("Siz davlatlardan 1-Rassiya, 2-Ispaniya, 3-Tojikiston, 4-Hindiston, 5-Germaniya bayrog'larni bo'yay olasiz.")
          self.name.setStyleSheet("color: rgb(50,205,50);")


          self.btn=QPushButton(self)
          self.btn.setFont(QFont("Consolas",18))
          self.btn.move(20,60)
          self.btn.resize(350,80)
          self.btn.clicked.connect(self.select_color1)

          self.btn1=QPushButton(self)
          self.btn1.setFont(QFont("Consolas",18))
          self.btn1.move(20,140)
          self.btn1.resize(350,80)
          self.btn1.clicked.connect(self.select_color2)

          self.btn2=QPushButton(self)
          self.btn2.setFont(QFont("Consolas",18))
          self.btn2.move(20,220)
          self.btn2.resize(350,80)
          self.btn2.clicked.connect(self.select_color3)

          self.btn3=QPushButton(self)
          self.btn3.setFont(QFont("Consolas",18))
          self.btn3.move(470,60)
          self.btn3.resize(350,80)
          self.btn3.clicked.connect(self.select_color4)

          self.btn4=QPushButton(self)
          self.btn4.setFont(QFont("Consolas",18))
          self.btn4.move(470,140)
          self.btn4.resize(350,80)
          self.btn4.clicked.connect(self.select_color5)

          self.btn5=QPushButton(self)
          self.btn5.setFont(QFont("Consolas",18))
          self.btn5.move(470,220)
          self.btn5.resize(350,80)
          self.btn5.clicked.connect(self.select_color6)

          self.btn6=QPushButton(self)
          self.btn6.setFont(QFont("Consolas",18))
          self.btn6.move(900,60)
          self.btn6.resize(350,80)
          self.btn6.clicked.connect(self.select_color7)

          self.btn7=QPushButton(self)
          self.btn7.setFont(QFont("Consolas",18))
          self.btn7.move(900,140)
          self.btn7.resize(350,80)
          self.btn7.clicked.connect(self.select_color8)

          self.btn8=QPushButton(self)
          self.btn8.setFont(QFont("Consolas",18))
          self.btn8.move(900,220)
          self.btn8.resize(350,80)
          self.btn8.clicked.connect(self.select_color9)

          self.btn9=QPushButton(self)
          self.btn9.setFont(QFont("Consolas",18))
          self.btn9.move(250,370)
          self.btn9.resize(350,80)
          self.btn9.clicked.connect(self.select_color10)

          self.btn10=QPushButton(self)
          self.btn10.setFont(QFont("Consolas",18))
          self.btn10.move(250,440)
          self.btn10.resize(350,80)
          self.btn10.clicked.connect(self.select_color11)

          self.btn11=QPushButton(self)
          self.btn11.setFont(QFont("Consolas",18))
          self.btn11.move(250,510)
          self.btn11.resize(350,80)
          self.btn11.clicked.connect(self.select_color12)

          self.btn12=QPushButton(self)
          self.btn12.setFont(QFont("Consolas",18))
          self.btn12.move(700,370)
          self.btn12.resize(350,80)
          self.btn12.clicked.connect(self.select_color13)

          self.btn13=QPushButton(self)
          self.btn13.setFont(QFont("Consolas",18))
          self.btn13.move(700,440)
          self.btn13.resize(350,80)
          self.btn13.clicked.connect(self.select_color13)

          self.btn14=QPushButton(self)
          self.btn14.setFont(QFont("Consolas",18))
          self.btn14.move(700,510)
          self.btn14.resize(350,80)
          self.btn14.clicked.connect(self.select_color13)


          self.tx=QPushButton(self)
          self.tx.setText("Push")
          self.tx.setStyleSheet("""
                                  color: rgb(255,0,0);   
                                  border-color: rgb(255,0,0);
                                  border-radius: 30px;
                                  border_style: solid
                                  border-width: 3px;
                                  background-color: rgb(0,0,0);    
                                  """)
          self.tx.setFont(QFont("Consolas",18))
          self.tx.move(160,310)
          self.tx.resize(100,40)
          self.tx.clicked.connect(self.show_message1)

          self.tx1=QPushButton(self)
          self.tx1.setText("Push")
          self.tx1.setStyleSheet("""
                                  color: rgb(255,0,0);   
                                  border-color: rgb(255,0,0);
                                  border-radius: 30px;
                                  border_style: solid
                                  border-width: 3px;
                                  background-color: rgb(0,0,0);    
                                  """)
          self.tx1.setFont(QFont("Consolas",18))
          self.tx1.move(600,310)
          self.tx1.resize(100,40)
          self.tx1.clicked.connect(self.show_message2)


          self.tx2=QPushButton(self)
          self.tx2.setText("Push")
          self.tx2.setStyleSheet("""   
                                  border-color: rgb(255,0,0);
                                  border-radius: 30px;
                                  border_style: solid
                                  border-width: 3px;
                                  background-color: rgb(0,0,0);    
                                  """)
          self.tx2.setFont(QFont("Consolas",18))
          self.tx2.move(1030,310)
          self.tx2.resize(100,40)
          self.tx2.clicked.connect(self.show_message3)


          self.tx3=QPushButton(self)
          self.tx3.setText("Push")
          self.tx3.setStyleSheet("""
                                  color: rgb(255,0,0);   
                                  border-color: rgb(255,0,0);
                                  border-radius: 30px;
                                  border_style: solid
                                  border-width: 3px;
                                  background-color: rgb(0,0,0);    
                                  """)
          self.tx3.setFont(QFont("Consolas",18))
          self.tx3.move(380,600)
          self.tx3.resize(100,40)
          self.tx3.clicked.connect(self.show_message4)


          self.tx4=QPushButton(self)
          self.tx4.setText("Push")
          self.tx4.setStyleSheet("""   
                                  border-color: rgb(255,0,0);
                                  border-radius: 30px;
                                  border_style: solid
                                  border-width: 3px;
                                  background-color: rgb(0,0,0);    
                                  """)
          self.tx4.setFont(QFont("Consolas",18))
          self.tx4.move(830,600)
          self.tx4.resize(100,40)
          self.tx4.clicked.connect(self.show_message5)



      def select_color1(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn.setStyleSheet(f"background-color: {color.name()}")

      def select_color2(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn1.setStyleSheet(f"background-color: {color.name()}")

      def select_color3(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn2.setStyleSheet(f"background-color: {color.name()}")

      def select_color4(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn3.setStyleSheet(f"background-color: {color.name()}")

      def select_color5(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn4.setStyleSheet(f"background-color: {color.name()}")

      def select_color6(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn5.setStyleSheet(f"background-color: {color.name()}")

      def select_color7(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn6.setStyleSheet(f"background-color: {color.name()}")

      def select_color8(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn7.setStyleSheet(f"background-color: {color.name()}")

      def select_color9(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn8.setStyleSheet(f"background-color: {color.name()}")

      def select_color10(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn9.setStyleSheet(f"background-color: {color.name()}")

      def select_color11(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn10.setStyleSheet(f"background-color: {color.name()}")

      def select_color12(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn11.setStyleSheet(f"background-color: {color.name()}")

      def select_color13(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn12.setStyleSheet(f"background-color: {color.name()}")

      def select_color14(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn13.setStyleSheet(f"background-color: {color.name()}")

      def select_color15(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.btn14.setStyleSheet(f"background-color: {color.name()}")


      def show_message1(self):
          xabar=QMessageBox()
          xabar.setFont(QFont("Times Nw Roman",18))
          xabar.setText(f"Rassiya bayrog'i")
          xabar.setWindowTitle("MessageBox")
          xabar.setIcon(QMessageBox.Information)
          xabar.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close)
          print(xabar.exec_())

      def show_message2(self):
          xabar=QMessageBox()
          xabar.setFont(QFont("Times Nw Roman",18))
          xabar.setText(f"Ispaniya bayrog'i")
          xabar.setWindowTitle("MessageBox")
          xabar.setIcon(QMessageBox.Information)
          xabar.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close)
          print(xabar.exec_())

      def show_message3(self):
          xabar=QMessageBox()
          xabar.setFont(QFont("Times Nw Roman",18))
          xabar.setText(f"Tojikiston bayrog'i")
          xabar.setWindowTitle("MessageBox")
          xabar.setIcon(QMessageBox.Information)
          xabar.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close)
          print(xabar.exec_())

      def show_message4(self):
          xabar=QMessageBox()
          xabar.setFont(QFont("Times Nw Roman",18))
          xabar.setText(f"Hindiston bayrog'i")
          xabar.setWindowTitle("MessageBox")
          xabar.setIcon(QMessageBox.Information)
          xabar.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close)
          print(xabar.exec_())

      def show_message5(self):
          xabar=QMessageBox()
          xabar.setFont(QFont("Times Nw Roman",18))
          xabar.setText(f"Germaniya")
          xabar.setWindowTitle("MessageBox")
          xabar.setIcon(QMessageBox.Information)
          xabar.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close)
          print(xabar.exec_())

app=QApplication(sys.argv)
project=ilova()
project.show()
sys.exit(app.exec_())

     


