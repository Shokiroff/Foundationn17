import os
import sys
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ilova(QMainWindow):
      def __init__(self):
          QMainWindow.__init__(self) 
          self.setMaximumSize(840,650)
          self.setMinimumSize(840,650)
          self.setFont(QFont("Times New Roman",18))
          self.setWindowIcon(QIcon("/home/aziza/Downloads/mmm.png"))

          self.menyu=self.menuBar()
          self.menyu.setFont(QFont("Calibri",18))
          self.menu=self.menyu.addMenu("&File")
          self.menu.setFont(QFont("Consolas",18))
          
          self.txt=QLineEdit(self)
          self.txt.setGeometry(150,100,600,400)
          self.txt.setFont(QFont("Calibri",18))
          self.txt.setStyleSheet("""color: rgb(0,255,0)   
                                  border-color: rgb(255,0,0);
                                  border-radius: 30px;
                                  border_style: solid
                                  border-width: 3px;
                                  background-color: rgb(0,0,0);    
                                  """)

          self.action1=QAction(QIcon("/home/aziza/Downloads/mmm.png"),'Open file',self)
          self.action1.setShortcut("Ctrl+O")
          self.action1.triggered.connect(self.action_1)

          self.action2=QAction(QIcon("/home/aziza/Downloads/mmm.png"),'Save file',self)
          self.action2.setShortcut("Ctrl+S")
          
          self.action3=QAction(QIcon("/home/aziza/Downloads/mmm.png"),'Exit file',self)
          self.action3.setShortcut("Ctrl+S")
          self.action3.triggered.connect(self.yopish)

          self.menu.addAction(self.action1)
          self.menu.addAction(self.action2)
          self.menu.addAction(self.action3)

          self.menu1=self.menu.addMenu("Edit Code")
          self.menu1.setFont(QFont("Consolas",18))
 

          self.font=QAction(QIcon("/home/aziza/Downloads/mmm.png"),'Edit Font',self)
          self.font.setShortcut("Ctrl+F")
          self.font.triggered.connect(self.select_font)

          self.color=QAction(QIcon("/home/aziza/Downloads/mmm.png"),'Edit Text Color',self)
          self.color.setShortcut("Ctrl+C")
          self.color.triggered.connect(self.select_color)

          self.menu1.addActions([self.font,self.color])

      def action_1(self):
          file=QFileDialog().getOpenFileName(self,"Fayl")
          f=open(file,'rt')
          data=f.read()
          print(data)
          self.txt.setText(data)
      def yopish(self):
          message=QMessageBox(self)
          message.setWindowIcon(QIcon("/home/aziza/Downloads/mmm.png"),'Exit file',self)
          message.setWindowTitle("EXIT")
          message.setFont(QFont("Consolas",18))
          message.setText("Dasturdan chiqasizmi? ")
          message.setIcon(QMessageBox.Information)
          message.setStandartButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Close)
          natija=message.exec_()
          if natija==message.OK:
             self.close()
          else:
             print("Bekor qilindi.")

      def select_font(self):
          fontdialog=QFontDialog()
          font,ok=fontdialog.getFont()
          if ok==True:
             self.txt.setFont(font)
          else:
             print("Siz bekor qildingiz")


      def select_color(self):
          color=QColorDialog().getColor()
          if color.isValid():
             print(color.name())
             self.txt.setStyleSheet(f"color: {color.name()}")


app=QApplication(sys.argv)
project=ilova()
project.show()
sys.exit(app.exec_())
