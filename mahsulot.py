import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.chdir(r"C:\\Users\\Oybek\\python")
import mysql.connector        
os.system("cls")
class dastur(QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(0,0,800,600)
        self.setMaximumSize(1000,600)
        self.setMinimumSize(1000,600)
        self.move(150,100)
        self.setWindowIcon(QIcon("C:\\Users\\Oybek\\Downloads\\Telegram Desktop\\membership.ico"))
        self.setWindowTitle("Mahsulot")
        
        self.con=mysql.connector.connect(user="root",password='root',host='localhost',database='bozor')
        if self.con.is_connected():
            print("Baza bilan Bog'landi")
        
        self.kur=self.con.cursor()
        self.kur.execute("""create table if not exists mahsulot (id int primary key auto_increment,name char(50),country char(50),price int)""")
        self.con.commit()
        
        
        self.name=QLabel(self)
        self.name.setGeometry(30,50,250,50)
        self.name.setFont(QFont("Consolas",18))
        self.name.setText("Mahsulot nomi: ")
        self.name.setStyleSheet("color: rgb(0,0,205);")
        
        self.Name=QLineEdit(self)
        self.Name.setGeometry(230,50,200,50)
        self.Name.setFont(QFont("Consolas",18))
        self.Name.setStyleSheet("""
                        color: rgb(0,0,205);
                        border-color: rgb(220,208,255);
                        border-width:3px;
                        border-radius:15px;
                        border-style:outset;""")
        self.Name.setAlignment(Qt.AlignCenter)
        
        self.country=QLabel(self)
        self.country.setGeometry(30,130,250,50)
        self.country.setFont(QFont("Consolas",18))
        self.country.setText("Davlat nomi: ")
        self.country.setStyleSheet("color: rgb(0,0,205);")
        
        self.Country=QLineEdit(self)
        self.Country.setGeometry(230,130,200,50)
        self.Country.setFont(QFont("Consolas",18))
        self.Country.setStyleSheet("""
                        color: rgb(0,0,205);
                        border-color: rgb(220,208,255);
                        border-width:3px;
                        border-radius:15px;
                        border-style:outset;""")
        self.Country.setAlignment(Qt.AlignCenter)
        
        self.price=QLabel(self)
        self.price.setGeometry(30,200,250,50)
        self.price.setFont(QFont("Consolas",18))
        self.price.setText("Mahsulot narxi: ")
        self.price.setStyleSheet("color: rgb(0,0,205);")
        
        self.Price=QLineEdit(self)
        self.Price.setGeometry(230,200,200,50)
        self.Price.setFont(QFont("Consolas",18))
        self.Price.setStyleSheet("""
                        color: rgb(0,0,205);
                        border-color: rgb(220,208,255);
                        border-width:3px;
                        border-radius:15px;
                        border-style:outset;""")
        self.Price.setAlignment(Qt.AlignCenter)
        
        self.register=QPushButton("Register",self)
        self.register.setGeometry(230,300,200,50)
        self.register.setFont(QFont("Consolas",20))
        self.register.setStyleSheet("""
                        color: rgb(255,255,255);
                        border-color: rgb(220,220,220);
                        border-radius: 15px;
                        border-width: 3px;
                        border-style: outset;
                        background-color: rgb(70,130,180);
                        """)
        self.register.clicked.connect(self.save_data)
        
        
        self.search=QLineEdit(self)
        self.search.setGeometry(480,30,200,35)
        self.search.setFont(QFont("Consolas",18))
        self.search.setStyleSheet("""
                        color: rgb(0,0,205);
                        border-color: rgb(220,208,255);
                        border-width:3px;
                        border-radius:9px;
                        border-style:outset;""")
        self.search.setAlignment(Qt.AlignLeft)
        
        self.search_click=QPushButton("Search",self)
        self.search_click.setGeometry(700,30,150,30)
        self.search_click.setFont(QFont("Consolas",20))
        self.search_click.setStyleSheet("""
                        color: rgb(255,255,255);
                        border-color: rgb(220,220,220);
                        border-radius: 7px;
                        border-width: 3px;
                        border-style: outset;
                        background-color: rgb(70,130,180);
                        """)
        self.search_click.clicked.connect(self.search_data)
    
    
    def save_data(self):
        name = self.Name.text()
        Country = self.Country.text()
        Price = self.Price.text()
        

        if not name or not Country or not Price:
            QMessageBox.warning(self, "Xatolik", "Iltimos, barcha maydonlarni to'ldiring.")
            return

        sql = """INSERT INTO mahsulot(name, country,price) VALUES(%s, %s, %s)"""
        tpl = (name, Country, Price)

        try:
            self.kur.execute(sql, tpl)
            self.con.commit()
            QMessageBox.information(self, "Ma'lumot saqlandi", "Ma'lumotlar bazaga muvaffaqiyatli saqlandi.")
        except:
            QMessageBox.critical(self, "Xatolik", "Ma'lumotlar saqlashda xatolik yuz berdi.")
   
        self.Name.setText("")
        self.Country.setText("")
        self.Price.setText("")
    
    def search_data(self):
        pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    project=dastur()
    project.show()
    sys.exit(app.exec_())