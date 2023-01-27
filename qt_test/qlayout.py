import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

class 기본위치(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1_img = QLabel()
        label1_img.setPixmap(QPixmap(''))
        label1 = QLabel('내이름 라벨')

        label2_img = QLabel()
        label2_img.setPixmap(QPixmap(''))
        label2 = QLabel('내이름 라벨2')

        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()

        vbox1.addWidget(label1_img)
        vbox1.addWidget(label1)

        vbox1.addWidget(label2_img)
        vbox1.addWidget(label2)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)


        self.setWindowTitle('기본위치')
        self.setGeometry(400,400,500,500)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 기본위치()
프로그램무한반복.exec_()
