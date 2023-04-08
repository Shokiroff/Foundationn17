import os
import sys
os.system("cls")
from  PyQt5 import QtWidgets,QtGui,QtCore
def show(x,y):
    x=int(x)
    y=int(y)
    return x+y
def ilova():
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    widget.setMinimumSize(350,525)
    widget.setMaximumSize(350,525)
    widget.move(300,200)
    
    #QLabel bu textni yoki rasmni chiqarish uchun komponenta 

    
    tugma=QtWidgets.QPushButton("ON",widget)
    tugma.setGeometry(0,95,175,70)
    tugma.setFont(QtGui.QFont("Consolas",28))
    tugma.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(127,255,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma2=QtWidgets.QPushButton("C",widget)
    tugma2.setGeometry(175,95,175,70)
    tugma2.setFont(QtGui.QFont("Consolas",28))
    tugma2.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(0,206,209);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma3=QtWidgets.QPushButton("1",widget)
    tugma3.setGeometry(0,165,116,88)
    tugma3.setFont(QtGui.QFont("Consolas",28))
    tugma3.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugm4=QtWidgets.QPushButton("2",widget)
    tugm4.setGeometry(116,165,116,88)
    tugm4.setFont(QtGui.QFont("Consolas",28))
    tugm4.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugm5=QtWidgets.QPushButton("3",widget)
    tugm5.setGeometry(232,165,118,88)
    tugm5.setFont(QtGui.QFont("Consolas",28))
    tugm5.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma6=QtWidgets.QPushButton("4",widget)
    tugma6.setGeometry(0,253,116,88)
    tugma6.setFont(QtGui.QFont("Consolas",28))
    tugma6.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma7=QtWidgets.QPushButton("5",widget)
    tugma7.setGeometry(116,253,118,88)
    tugma7.setFont(QtGui.QFont("Consolas",28))
    tugma7.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma8=QtWidgets.QPushButton("6",widget)
    tugma8.setGeometry(232,253,118,88)
    tugma8.setFont(QtGui.QFont("Consolas",28))
    tugma8.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma9=QtWidgets.QPushButton("7",widget)
    tugma9.setGeometry(0,341,118,88)
    tugma9.setFont(QtGui.QFont("Consolas",28))
    tugma9.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma10=QtWidgets.QPushButton("8",widget)
    tugma10.setGeometry(116,341,118,88)
    tugma10.setFont(QtGui.QFont("Consolas",28))
    tugma10.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma11=QtWidgets.QPushButton("9",widget)
    tugma11.setGeometry(232,341,118,88)
    tugma11.setFont(QtGui.QFont("Consolas",28))
    tugma11.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(255,140,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma12=QtWidgets.QPushButton("O",widget)
    tugma12.setGeometry(0,429,175,88)
    tugma12.setFont(QtGui.QFont("Consolas",28))
    tugma12.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(127,255,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    tugma13=QtWidgets.QPushButton("=",widget)
    tugma13.setGeometry(175,429,175,88)
    tugma13.setFont(QtGui.QFont("Consolas",28))
    tugma13.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color: rgb(127,255,0);
                        border-width: 2px;
                        border-style: inset;
                        border-color:  rgb(0,0,0);""")
    
    txtbox3=QtWidgets.QLineEdit(widget)
    txtbox3.setGeometry(0,0,350,100)
    txtbox3.setFont(QtGui.QFont("Consolas",28))
    txtbox3.setStyleSheet("""color: rgb(49,140,231);
                         border-width: 3px;
                         border-style: solid;
                         border-color:  rgb(75,15,75);""")
    txtbox3.setAlignment(QtCore.Qt.AlignRight)
    widget.show()
    
    sys.exit(app.exec_())
if __name__=="__main__":
    ilova()