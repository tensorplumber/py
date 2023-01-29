import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout
from PyQt5.QtGui import QColor, QIcon

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        btn_1 = QPushButton(self)
        btn_1.setText('버튼1')
        btn_1.setEnabled(True)
        
        btn_2 = QPushButton('&Button2',self)
        btn_2.setText('버튼2')
        btn_2.setEnabled(True)
        
        btn_3 = QPushButton('버튼3',self)
        btn_3.setIcon(QIcon(''))
        btn_3.move(50,200)
        btn_3.setFixedSize(200,50)

        btn_2.toggle()

        hbox = QHBoxLayout()
        hbox.addWidget(btn_1)
        hbox.addWidget(btn_2)
        hbox.addWidget(btn_3)

        self.setLayout(hbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('checkbox')
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
