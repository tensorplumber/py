from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from pathlib import Path

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn1 = QPushButton('버튼1')
        self.btn2 = QPushButton('버튼2')

        self.btn1.clicked.connect(self.buttonClicked)
        self.btn2.clicked.connect(self.buttonClicked)

        self.label = QLabel('누가 시그널을 보냈을까ㅑ')

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.label.setText(sender.text()+'이 보냈습니다')


        
app = QApplication(sys.argv)
ex = myapp()
app.exec_()