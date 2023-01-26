import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QDial
from PyQt5.QtCore import Qt
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
                
        self.dial = QDial(self)
        self.dial.move(30,20)

        self.dial2 = QDial(self)
        self.dial2.move(200,20)
        self.dial2.setRange(0,50)
        self.dial2.setNotchesVisible(True)

        self.label1 = QLabel('다이얼 1',self)
        self.label1.move(40,130)
        self.label2 = QLabel('다이얼 2',self)
        self.label2.move(210,130)

        btn = QPushButton('기본값',self)
        btn.move(115,200)

        self.dial.valueChanged.connect(self.changeValue)
        self.dial2.valueChanged.connect(self.changeValue)

        btn.clicked.connect(self.btn_clicked)        
        
        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def btn_clicked(self):
        self.dial.setValue(0)
        self.dial2.setValue(0)

    def changeValue(self):
        self.label1.setText(str(self.dial.value()))
        self.label2.setText(str(self.dial2.value()))

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
