import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

os.system("cls")
class Dastur(QWidget):
    a = str()
    b = str()
    c = str()
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1000, 900)
        self.setMaximumSize(1000, 900)

        self.btn = QPushButton("Rangni tallang", self)
        self.btn.setStyleSheet("""
                            border-color: rgb(0, 0, 0);
                            border: 3px;
                            color: rgb(0, 0, 0);
                            background-color: rgb(240,234,214);""")
        self.btn.setFont(QFont("Consolas", 16))
        self.btn.move(200, 50)
        self.btn.resize(600, 150)
        self.btn.clicked.connect(self.select_color)

        self.btn_1 = QPushButton("Rangni tallang", self)
        self.btn_1.setStyleSheet("""
                            border-color: rgb(0, 0, 0);
                            border: 3px;
                            background-color: rgb(240,234,214);
                            color: rgb(0, 0, 0);""")
        self.btn_1.setFont(QFont("Consolas", 16))
        self.btn_1.move(200, 200)
        self.btn_1.resize(600, 150)
        self.btn_1.clicked.connect(self.select_color1)

        self.btn_2 = QPushButton("Rangni tallang", self)
        self.btn_2.setStyleSheet("""
                            border-color: rgb(0, 0, 0);
                            border: 3px;
                            color: rgb(0, 0, 0);
                            background-color: rgb(240,234,214);""")
        self.btn_2.setFont(QFont("Consolas", 16))
        self.btn_2.move(200, 350)
        self.btn_2.resize(600, 150)
        self.btn_2.clicked.connect(self.select_color2)

        self.click_Btn = QPushButton("Click", self)
        self.click_Btn.setFont(QFont("Calibri", 18))
        self.click_Btn.setStyleSheet("""
                                    border-radius: 25px;
                                    background-color: rgb(0, 0, 0);
                                    color: rgb(115, 235, 85);""")
        self.click_Btn.move(650, 530)
        self.click_Btn.resize(150, 60)
        self.click_Btn.clicked.connect(self.click_Btn_function)

        self.click_Btn_clear = QPushButton("Clear", self)
        self.click_Btn_clear.setFont(QFont("Calibri", 18))
        self.click_Btn_clear.setStyleSheet("""
                                    border-radius: 25px;
                                    background-color: rgb(0, 0, 0);
                                    color: rgb(115, 235, 85);""")
        self.click_Btn_clear.move(450, 530)
        self.click_Btn_clear.resize(150, 60)
        self.click_Btn_clear.clicked.connect(self.click_Btn_clear_function)

        self.output = QLabel(self)
        self.output.setFont(QFont("Calibri", 20))
        self.output.move(500, 620)
        self.output.resize(500,60)


    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            self.btn.setStyleSheet(f"background-color: {color.name()};")
            Dastur.a = color.name()
            self.btn.setText("")
        else:
            print("Siz rang tallamadingiz")

    def select_color1(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            self.btn_1.setStyleSheet(f"background-color: {color.name()};")
            Dastur.b = color.name()
            self.btn_1.setText("")
        else:
            print("Siz rang tallamadingiz")

    def select_color2(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            self.btn_2.setStyleSheet(f"background-color: {color.name()};")
            Dastur.c = color.name()
            self.btn_2.setText("")
        else:
            print("Siz rang tallamadingiz")
    def click_Btn_clear_function(self):
        self.btn.setText("Rangni tallang")
        self.btn.setStyleSheet("""
                            border-color: rgb(0, 0, 0);
                            border: 3px;
                            background-color: rgb(240,234,214);""")

        self.btn_1.setText("Rangni tallang")
        self.btn_1.setStyleSheet("""
                            border-color: rgb(0, 0, 0);
                            border: 3px;
                            background-color: rgb(240,234,214);""")

        self.btn_2.setText("Rangni tallang")
        self.btn_2.setStyleSheet("""
                            border-color: rgb(0, 0, 0);
                            border: 3px;
                            background-color: rgb(240,234,214);""")
        self.output.setText("")

    def click_Btn_function(self):
              
        if Dastur.a == "#ffffff" and Dastur.b == "#5500ff" and Dastur.c == "#aa0000":
            self.output.setText("The flag of Russia")
        elif Dastur.a == "#00aaff" and Dastur.b == "#ffffff" and Dastur.c == "#00aa00":
            self.output.setText("The flag of Uzbekistan")
        elif Dastur.a == "#ffaa00" and Dastur.b == "#ffffff" and Dastur.c == "#00aa00":
            self.output.setText("The flag of India")
        elif Dastur.a == "#55aaff" and Dastur.b == "#ffffff" and Dastur.c == "#55aaff":
            self.output.setText("The flag of Argentina")
        elif Dastur.a == "#000000" and Dastur.b == "#aa0000" and Dastur.c == "#ffff7f":
            self.output.setText("The flag of Germany")
        elif Dastur.a == "#55aaff" and Dastur.b == "#000000" and Dastur.c == "#ffffff":
            self.output.setText("The flag of Estonia")
        else:
            self.output.setText("There is no the flag")
            




if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = Dastur()
    project.show()
    sys.exit(app.exec_())