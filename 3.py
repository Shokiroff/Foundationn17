import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Dastur(QWidget):
    sch_ol = 0
    sch_chek = 0
    Umumiy = 0
    def __init__(self):
        QWidget.__init__(self)
        self.setMaximumSize(1080, 760)
        self.setMinimumSize(1080, 760)

        self.Mahsulotlar = QLabel(self)
        self.Mahsulotlar.setText("Restoranimizga hush kelibsiz!!!")
        self.Mahsulotlar.setStyleSheet("""
                                    color: rgb(0, 0, 0);""")
        self.Mahsulotlar.setFont(QFont("Calibri", 20))
        self.Mahsulotlar.setGeometry(200, 10, 700, 50)

        self.Mahsulotlar_Meva = QLabel(self)
        self.Mahsulotlar_Meva.setText("Ovqat va Kaboblar")
        self.Mahsulotlar_Meva.setFont(QFont("Calibri", 18))
        self.Mahsulotlar_Meva.setGeometry(10, 50, 700, 50)

        self.Mahsulotlar_1 = QCheckBox(self)
        self.Mahsulotlar_1.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_1.setGeometry(70, 90, 250, 50)
        self.Mahsulotlar_1.setText("Osh: 25000 so'm")

        self.Mahsulotlar_2 = QCheckBox(self)
        self.Mahsulotlar_2.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_2.setGeometry(330, 90, 280, 50)
        self.Mahsulotlar_2.setText("Lag'man: 35000 so'm")

        self.Mahsulotlar_3 = QCheckBox(self)
        self.Mahsulotlar_3.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_3.setGeometry(630, 90, 280, 50)
        self.Mahsulotlar_3.setText("Sho'rva: 20000 so'm")

        self.Mahsulotlar_4 = QCheckBox(self)
        self.Mahsulotlar_4.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_4.setGeometry(70, 130, 250, 50)
        self.Mahsulotlar_4.setText("Shashlik: 10000 so'm")

        self.Mahsulotlar_5 = QCheckBox(self)
        self.Mahsulotlar_5.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_5.setGeometry(330, 130, 280, 50)
        self.Mahsulotlar_5.setText("Qiyma_Shashlik: 15000 so'm")

        self.Mahsulotlar_6 = QCheckBox(self)
        self.Mahsulotlar_6.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_6.setGeometry(630, 130, 280, 50)
        self.Mahsulotlar_6.setText("Somsa: 5000 so'm")

        self.Mahsulotlar_Gosht = QLabel(self)
        self.Mahsulotlar_Gosht.setText("Choylar")
        self.Mahsulotlar_Gosht.setFont(QFont("Calibri", 18))
        self.Mahsulotlar_Gosht.setGeometry(10, 190, 700, 50)

        self.Mahsulotlar_7 = QCheckBox(self)
        self.Mahsulotlar_7.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_7.setGeometry(70, 230, 250, 50)
        self.Mahsulotlar_7.setText("Ko'k_choy: 6000 so'm")

        self.Mahsulotlar_8 = QCheckBox(self)
        self.Mahsulotlar_8.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_8.setGeometry(330, 230, 280, 50)
        self.Mahsulotlar_8.setText("Qora_choy: 7000 so'm")

        self.Mahsulotlar_9 = QCheckBox(self)
        self.Mahsulotlar_9.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_9.setGeometry(630, 230, 280, 50)
        self.Mahsulotlar_9.setText("Qora_Limon_Choy: 12000 so'm")

        self.Mahsulotlar_Fast_Food =  QLabel(self)
        self.Mahsulotlar_Fast_Food.setText("Fast Food Mahsulotlar")
        self.Mahsulotlar_Fast_Food.setFont(QFont("Calibri", 20))
        self.Mahsulotlar_Fast_Food.setGeometry(10, 290, 800, 50)

        self.Mahsulotlar_10 = QCheckBox(self)
        self.Mahsulotlar_10.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_10.setGeometry(70, 330, 250, 50)
        self.Mahsulotlar_10.setText("Lavash: 28000 so'm")

        self.Mahsulotlar_11 = QCheckBox(self)
        self.Mahsulotlar_11.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_11.setGeometry(330, 330, 280, 50)
        self.Mahsulotlar_11.setText("Hod_Dog: 15000 so'm")

        self.Mahsulotlar_12 = QCheckBox(self)
        self.Mahsulotlar_12.setFont(QFont("Calibri", 15))
        self.Mahsulotlar_12.setGeometry(630, 330, 280, 50)
        self.Mahsulotlar_12.setText("Hamburger: 30000 so'm")

        self.click = QPushButton("Olish" ,self)
        self.click.setFont(QFont("Consalas", 20))
        self.click.setGeometry(200, 400, 180, 60)
        self.click.setStyleSheet("""
                        color: rgb(80,200,120);
                        background-color: rgb(0, 0, 75);
                        border-width: 3px;
                        border-radius: 25px;
                        border-color:  rgb(80,200,120);""")
        self.click.clicked.connect(self.click_ON)

        self.olish = QLabel(self)
        self.olish.setFont(QFont("Calibri", 18))
        self.olish.setGeometry(100, 475, 700, 50)

        self.chek = QPushButton(self)

        self.chek.clicked.connect(self.click_chek)
        self.chek_txt = QLabel(self)
        self.chek_txt.setFont(QFont("Calibri", 18))
        self.chek_txt.setGeometry(100, 630, 700, 50)
        
        

    def click_ON(self):
        if Dastur.sch_ol > 0:
            return
        self.olish.setText("Haridingiz uchun Tashakkur")
        self.chek.setText("Check")
        self.chek.setFont(QFont("Calibri", 18))
        self.chek.setGeometry(200, 540, 180, 60)
        self.chek.setStyleSheet("""
                        color: rgb(80,200,120);
                        background-color: rgb(0, 0, 75);
                        border-width: 3px;
                        border-radius: 25px;
                        border-color:  rgb(80,200,120);""")
        Dastur.sch_ol += 1
    def click_chek(self):
        if Dastur.sch_chek > 0:
            return
        self.chek_txt.setText("Chek Tayyor")
        f = open("D:\\Menu_chek.txt", "wt")

        f.write("   ****Chek****\n")

        if self.Mahsulotlar_1.isChecked():
            a = self.Mahsulotlar_1.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_1.text()}\n")
        if self.Mahsulotlar_2.isChecked():
            a = self.Mahsulotlar_2.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_2.text()}\n")
        if self.Mahsulotlar_3.isChecked():
            a = self.Mahsulotlar_3.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_3.text()}\n")
        if self.Mahsulotlar_4.isChecked():
            a = self.Mahsulotlar_4.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_4.text()}\n")
        if self.Mahsulotlar_5.isChecked():
            a = self.Mahsulotlar_5.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_5.text()}\n")
        if self.Mahsulotlar_6.isChecked():
            a = self.Mahsulotlar_6.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_6.text()}\n")
        if self.Mahsulotlar_7.isChecked():
            a = self.Mahsulotlar_7.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_7.text()}\n")
        if self.Mahsulotlar_8.isChecked():
            a = self.Mahsulotlar_8.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_8.text()}\n")
        if self.Mahsulotlar_9.isChecked():
            a = self.Mahsulotlar_9.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_9.text()}\n")
        if self.Mahsulotlar_10.isChecked():
            a = self.Mahsulotlar_10.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_10.text()}\n")
        if self.Mahsulotlar_11.isChecked():
            a = self.Mahsulotlar_11.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_11.text()}\n")
        if self.Mahsulotlar_12.isChecked():
            a = self.Mahsulotlar_12.text().split()
            Dastur.Umumiy += int(a[1])
            f.write(f"{self.Mahsulotlar_12.text()}\n")
        f.write(f"Hizmat uchun: {Dastur.Umumiy * 0.1} so'm\n")
        Dastur.Umumiy = Dastur.Umumiy + Dastur.Umumiy * 0.1
        f.write(f"Umumiy summa: {Dastur.Umumiy} so'm\n")

        Dastur.sch_chek += 1
        

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    Eng_test = Dastur()
    Eng_test.show()
    sys.exit(app.exec_())