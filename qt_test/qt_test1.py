import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random

class 대표선출프로그램(QWidget):
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):
        self.이미지()
        self.버튼()
        self.툴팁()
        self.대리인번호()
        self.setWindowTitle('대표선출')
        self.setWindowIcon(QIcon('20211026_150102.png'))
        self.setGeometry(500,500,400,400)
        self.show()

    def 이미지(self):
        self.대표이미지 = QLabel(self)
        self.대표이미지.setPixmap(QPixmap('20211026_150102.png').scaled(35,44))
        self.대표이미지.move(100, 10)

    def 버튼(self):
        self.대표선출버튼 = QPushButton('대표선출', self)
        self.대표선출버튼.setFixedSize(340, 40)
        self.대표선출버튼.move(30, 290)
        self.대표선출버튼.clicked.connect(self.choice)

        self.종료버튼 = QPushButton('종료', self)
        self.종료버튼.setFixedSize(340, 40)
        self.종료버튼.move(30, 340)
        self.종료버튼.clicked.connect(self.close)

    def 툴팁(self):
        self.대표선출버튼.setToolTip('이버튼을 누르면 대표선출함\n주의하세요 되돌릴수 없습니다')
        self.종료버튼.setToolTip('이버튼은 종료')
        self.대표이미지.setToolTip('대표이미지')
        self.setToolTip('작업을 선택하십시오')


    def 대리인번호(self):
        self.대리인번호라벨 = QLabel('000', self)
        self.대리인번호라벨.setFont(QFont('Helvetica', pointSize=75, weight=2))
        self.대리인번호라벨.move(100,100)


    def choice(self):
        s = str(random.randint(1,1000))
        print(s)
        self.대리인번호라벨.setText(s)

    def close(self):
        return QCoreApplication.instance().quit()
        
프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 대표선출프로그램()
프로그램무한반복.exec_()