import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        slide = QSlider(Qt.Vertical, self)
        slide.setGeometry(200,50,100,200)
        slide.setTickPosition(QSlider.TicksLeft)
        slide.valueChanged[int].connect(self.changeValue)
        
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap(''))
        self.img.adjustSize()
        self.img.move(30,70)

        self.label = QLabel(f'범위{slide.minimum()}~{slide.maximum()}',self)
        self.label.move(50,200)

        self.label2 = QLabel(self)
        self.label2.move(50,250)
        self.label2.setFixedWidth(30)
        
        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def changeValue(self,value):
        self.label2.setText(str(value))

        if value ==0:
            self.img.setPixmap(QPixmap(''))
        elif 0 < value <=30:
            self.img.setPixmap(QPixmap(''))
        elif 30 < value <=80:
            self.img.setPixmap(QPixmap(''))
        else:
            self.img.setPixmap(QPixmap(''))


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
