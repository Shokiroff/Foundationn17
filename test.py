import sys
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class dastur(QWidget):
      score=0
      def __init__(self):
          QWidget.__init__(self) 
          self.setMaximumSize(1000,780)
          self.setMinimumSize(1000,780)
          self.setWindowTitle("Test")

          self.name=QLabel(self)
          self.name.setGeometry(250,5,600,50)
          self.name.setFont(QFont("Times New Roman",25))
          self.name.setText("Tests: ")
          self.name.setStyleSheet("color: rgb(220,20,60);")

          self.test1=QLabel(self)
          self.test1.setGeometry(30,50,800,60)
          self.test1.setFont(QFont("Calibri",18))
          self.test1.setText("1.If I want to pass the exam, I need to study _____ .")
          self.test1.setStyleSheet("color: rgb(0,0,205);")

          self.answer1=QRadioButton("a lot",self)
          self.answer1.setGeometry(60,100,250,50)
          self.answer1.setFont(QFont("Calibri",16))
          self.answer1.setStyleSheet("color: rgb(205,0,205);")

          self.answer2=QRadioButton("much",self)
          self.answer2.setGeometry(180,100,250,50)
          self.answer2.setFont(QFont("Calibri",16))
          self.answer2.setStyleSheet("color: rgb(205,0,205);")

          self.answer3=QRadioButton("a lot of",self)
          self.answer3.setGeometry(290,100,250,50)
          self.answer3.setFont(QFont("Calibri",16))
          self.answer3.setStyleSheet("color: rgb(205,0,205);")



          self.test2=QLabel(self)
          self.test2.setGeometry(30,140,800,60)
          self.test2.setFont(QFont("Calibri",18))
          self.test2.setText("2.There are not ____ things to do in this village.")
          self.test2.setStyleSheet("color: rgb(0,0,205);")

          self.answer4=QRadioButton("much",self)
          self.answer4.setGeometry(60,190,250,50)
          self.answer4.setFont(QFont("Calibri",16))
          self.answer4.setStyleSheet("color: rgb(205,0,205);")

          self.answer5=QRadioButton("many",self)
          self.answer5.setGeometry(180,190,250,50)
          self.answer5.setFont(QFont("Calibri",16))
          self.answer5.setStyleSheet("color: rgb(205,0,205);")

          self.answer6=QRadioButton("a lot of",self)
          self.answer6.setGeometry(290,190,250,50)
          self.answer6.setFont(QFont("Calibri",16))
          self.answer6.setStyleSheet("color: rgb(205,0,205);")



          self.test3=QLabel(self)
          self.test3.setGeometry(30,230,800,60)
          self.test3.setFont(QFont("Calibri",18))
          self.test3.setText("3.____ sugar do you take in your tea?")
          self.test3.setStyleSheet("color: rgb(0,0,205);")

          self.answer7=QRadioButton("How little",self)
          self.answer7.setGeometry(60,280,250,50)
          self.answer7.setFont(QFont("Calibri",16))
          self.answer7.setStyleSheet("color: rgb(205,0,205);")

          self.answer8=QRadioButton("How many",self)
          self.answer8.setGeometry(200,280,250,50)
          self.answer8.setFont(QFont("Calibri",16))
          self.answer8.setStyleSheet("color: rgb(205,0,205);")

          self.answer9=QRadioButton("How much",self)
          self.answer9.setGeometry(350,280,250,50)
          self.answer9.setFont(QFont("Calibri",16))
          self.answer9.setStyleSheet("color: rgb(205,0,205);")




          self.test4=QLabel(self)
          self.test4.setGeometry(30,330,800,60)
          self.test4.setFont(QFont("Calibri",18))
          self.test4.setText("4.There is ____ milk in the fridge. We need to buy some.")
          self.test4.setStyleSheet("color: rgb(0,0,205);")

          self.answer10=QRadioButton("no",self)
          self.answer10.setGeometry(60,380,250,50)
          self.answer10.setFont(QFont("Calibri",16))
          self.answer10.setStyleSheet("color: rgb(205,0,205);")

          self.answer11=QRadioButton("any",self)
          self.answer11.setGeometry(180,380,250,50)
          self.answer11.setFont(QFont("Calibri",16))
          self.answer11.setStyleSheet("color: rgb(205,0,205);")

          self.answer12=QRadioButton("none",self)
          self.answer12.setGeometry(290,380,250,50)
          self.answer12.setFont(QFont("Calibri",16))
          self.answer12.setStyleSheet("color: rgb(205,0,205);")




          self.test5=QLabel(self)
          self.test5.setGeometry(30,430,800,60)
          self.test5.setFont(QFont("Calibri",18))
          self.test5.setText("5. He does not have ____ hobbies.")
          self.test5.setStyleSheet("color: rgb(0,0,205);")

          self.answer13=QRadioButton("much",self)
          self.answer13.setGeometry(60,480,250,50)
          self.answer13.setFont(QFont("Calibri",16))
          self.answer13.setStyleSheet("color: rgb(205,0,205);")

          self.answer14=QRadioButton("any",self)
          self.answer14.setGeometry(180,480,250,50)
          self.answer14.setFont(QFont("Calibri",16))
          self.answer14.setStyleSheet("color: rgb(205,0,205);")

          self.answer15=QRadioButton("a lot of",self)
          self.answer15.setGeometry(290,480,250,50)
          self.answer15.setFont(QFont("Calibri",16))
          self.answer15.setStyleSheet("color: rgb(205,0,205);")



          self.show_answer=QPushButton('Show Answers',self)
          self.show_answer.resize(250,50)
          self.show_answer.move(390,540)
          self.show_answer.setFont(QFont("Consolas",18))
          self.show_answer.setStyleSheet("""
                                  color: rgb(0,0,0);   
                                  border-color: rgb(253,14,53);
                                  border-radius: 15px;
                                  border-width: 3px;
                                  border-style: outset;
                                  background-color: rgb(255,0,0);
                                  """)
          self.show_answer.clicked.connect(self.calculate_score)
          
          self.score1=QLabel(self)
          self.score1.move(480,600)
          self.score1.setVisible(False)
          self.show()

      def calculate_score(self):
        
        if self.answer1.isChecked():
            dastur.score += 1
        if self.answer5.isChecked():    
            dastur.score += 1         
        if self.answer9.isChecked():    
            dastur.score += 1
        if self.answer10.isChecked():    
            dastur.score += 1
        if self.answer14.isChecked():    
            dastur.score += 1

        self.score1.setText('Score: ' + str(dastur.score) + '/5')
        self.score1.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test=dastur()
    test.show()
    sys.exit(app.exec_())

 
 




