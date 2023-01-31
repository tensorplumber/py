import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

class 기본위치(QWidget):
    def __init__(self):
        super().__init__()
        self.UI초기화()

    def UI초기화(self):

        테스트버튼 = QPushButton('버튼', self)
        # 테스트버튼.setGeometry(50,100,100,40)
        테스트버튼.move(30,30)
        테스트버튼.resize(100,50)
        # 테스트버튼.setFixedSize(w,h)
        # 테스트버튼.setFixedWidth(w)
        # 테스트버튼.setFixedHeight(w)
        
        파이라벨 = QLabel('나는 파이',self)
        파이라벨.move(60,20)
        썬라벨 = QLabel('나는 썬', self)
        썬라벨.move(230,60)

        파이이미지 = QLabel(self)
        파이이미지.setPixmap(QPixmap('C:/Users/dksw/Desktop/soomin/hd_autocam/20211026_150102.jpg'))
        파이이미지.move(40,40)

        썬이미지 = QLabel(self)
        썬이미지.setPixmap(QPixmap('C:/Users/dksw/Desktop/soomin/hd_autocam/20211026_150102.jpg'))
        썬이미지.move(200,80)

        파이버튼 = QPushButton('파이',self)
        파이버튼.move(70,230)

        
        썬버튼 = QPushButton('썬',self)
        썬버튼.move(230,230)

        self.setWindowTitle('기본위치')
        self.setWindowIcon(QIcon('C:/Users/dksw/Desktop/soomin/hd_autocam/20211026_150102.jpg'))
        self.setGeometry(400,400,500,500)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 기본위치()
프로그램무한반복.exec_()
