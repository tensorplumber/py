from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QVBoxLayout, QLabel, QSlider, QLCDNumber
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap, QFont
import sys
from pathlib import Path

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0
        self.location = f'x좌표는 {x}, y좌표는 {y}'
        self.label1 = QLabel(self.location, self)
        self.label1.setFont(QFont('Decorative',20))
       
        self.label2 = QLabel('마우스클릭 혹은 더블클릭')

        self.setMouseTracking(True)


        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.setLayout(self.vbox)

        # vbox.addWidget(lcd)
        # vbox.addWidget(btn1)
        # vbox.addWidget(btn2)
        
        # self.setLayout(vbox)
        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def mousePressEvent(self, event):
        self.label2.setText('마우스 클릭')

    def mouseDoubleClickEvent(self, event):
        self.label2.setText('마우스 더블클릭')

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        
        location = f'x좌표는 {x} y좌표는 {y}'
        self.label1.setText(location)

            

        

app = QApplication(sys.argv)
ex = myapp()
app.exec_()