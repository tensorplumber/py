import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt #가운데 정렬

class 기본위치(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        insert = QPushButton('insert')
        home = QPushButton('home')
        pageup = QPushButton('pageup')
        deltete = QPushButton('deltete')
        end = QPushButton('end')
        down = QPushButton('down')
        keyboard = QPushButton('keyboard')

        grid = QGridLayout()
        grid.setSpacing(15) #서로 간격

        grid.addWidget(insert,0,0) #0row, 0col
        grid.addWidget(home,0,1)
        grid.addWidget(pageup,0,2)

        grid.addWidget(deltete,1,0) #0row, 0col
        grid.addWidget(end,1,1)
        grid.addWidget(down,1,2)

        grid.addWidget(keyboard, 2,0,2,3,alignment=Qt.AlignHCenter)
        #키보드 라벨 위젯은 2개로우의 0칼럼부터 2개로우 3칼럼까지 있다

        self.setLayout(grid)


        self.setWindowTitle('기본위치')
        self.setGeometry(400,400,500,500)
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = 기본위치()
프로그램무한반복.exec_()
