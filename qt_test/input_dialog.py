from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton, QInputDialog
from PyQt5.QtCore import Qt
import sys

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.day = ['월','화','수','목','금']
        self.initUI()

    def initUI(self):

        self.btn1 = QPushButton('이름입력',self)
        self.btn1.move(30,30)
        self.btn1.clicked.connect(self.showDialog)

        self.btn2 = QPushButton('요일선택',self)
        self.btn2.move(30,80)
        self.btn2.clicked.connect(self.showDialog2)

        self.btn3 = QPushButton('일자 선택',self)
        self.btn3.move(30,130)
        self.btn3.clicked.connect(self.showDialog3)

        self.label1 = QLabel('이곳에 이름표시',self)
        self.label1.move(130,35)
        self.label1.setFixedSize(150,20)

        self.label2 = QLabel('요일',self)
        self.label2.move(130,85)
        self.label2.setFixedSize(150,20)

        self.label3 = QLabel('날짜',self)
        self.label3.move(130,135)
        self.label3.setFixedSize(150,20)
        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def showDialog(self):
        text, flag = QInputDialog.getText(self, '입력창', '이름을 입력하세요')
        if flag:
            self.label1.setText(str(text))

    def showDialog2(self):
        text, flag = QInputDialog.getItem(self, '리스트호출', '요일선택', self.day)
        if flag:
            self.label1.setText(str(text))
        

    def showDialog3(self):
        number, flag = QInputDialog.getInt(self, '요일선택창', '날짜선택', min=1,max=31)
        if flag:
            self.label1.setText(str(number)+'일')
        
        

app = QApplication(sys.argv)
ex = myapp()
app.exec_()