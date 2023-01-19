from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QVBoxLayout, QLabel, QSlider, QLCDNumber
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPixmap
import sys
from pathlib import Path

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)

        self.slider.valueChanged.connect(lcd.display)
        self.slider.valueChanged.connect(self.setValue)

        btn1 = QPushButton('초기화')
        btn2 = QPushButton('종료')

        btn1.clicked.connect(self.changeValue)
        btn2.clicked.connect(self.exitProgram)



        vbox = QVBoxLayout(self)
        vbox.addWidget(lcd)
        vbox.addWidget(self.slider, alignment=Qt.AlignCenter)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def changeValue(self):
        self.slider.setValue(0)
        self.label.setText(str(self.slider.value()))


    def setValue(self):
        self.label.setText(str(self.slider.value()))

    def exitProgram(self):
        QCoreApplication.instance().quit()
        

app = QApplication(sys.argv)
ex = myapp()
app.exec_()