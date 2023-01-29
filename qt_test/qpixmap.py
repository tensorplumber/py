import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import urllib.request

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.img = QPixmap()
        url = 'https://paullab.co.kr/images/message_licat.png'
        webImg = urllib.request.urlopen(url).read()
        # print(webImg)
        self.img.loadFromData(webImg)

        self.label_img = QLabel()
        self.label_img.setPixmap(self.img)
        self.label_img.setAlignment(Qt.AlignCenter)
        self.label_size = QLabel(f'가로{self.img.width()}/세로{self.img.height()}')

        loadBtn = QPushButton('이미지변경')
        loadBtn.clicked.connect(self.changeImage)

        saveBtn = QPushButton('저장')
        saveBtn.clicked.connect(self.saveImage)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_img)
        vbox.addWidget(self.label_size)
        vbox.addWidget(loadBtn)
        vbox.addWidget(saveBtn)
        self.setLayout(vbox)

        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def changeImage(self):
        self.img.load('20211026_150102.png')
        self.label_img.setPixmap(self.img)
        self.label_size.setText(f'가로:{self.img.width()}/세로:{self.img.height()}')

    def saveImage(self):
        self.img = self.label_img.pixmap()
        self.img.save('저장된 이미지.png')

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
