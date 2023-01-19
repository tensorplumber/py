import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.s = '1=3'

        self.one = QPushButton('1')
        self.one.clicked.connect(lambda :self.clickedNum('1'))

        self.one = QPushButton('1')
        self.one.clicked.connect(lambda :self.clickedNum('1'))

        self.three = QPushButton('3')
        self.three.clicked.connect(lambda :self.clickedNum('3'))

        self.plus = QPushButton('+')
        self.plus.clicked.connect(lambda :self.clickedNum('+'))

        self.one = QPushButton('=')
        self.one.clicked.connect(self.calc)

        hbox = QHBoxLayout()
        hbox.addWidget(self.one)
        hbox.addWidget(self.plus)
        hbox.addWidget(self.three)
        hbox.addWidget(self.calc)

        self.setLayout(hbox)

        self.setWindowTitle('계산기')
        self.show()

    def clickedNum(self, text):
        self.s += text
        print(self.s)

    def calc(self):
        print(eval(self.s))
        self.s = ''


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = myapp()
    app.exec_()