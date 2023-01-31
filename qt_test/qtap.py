import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        tabs = QTabWidget()

        tabs.addTab(self.tab1, '라이캣')
        tabs.addTab(self.tab2, '파이')
        tabs.addTab(self.tab3, '썬')

        tabs.setTabPosition(1)
        tabs.setTabShape(0)

        tabs.tabBarClicked.connect(self.clickedTab)

        vbox = QVBoxLayout()  
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def clickedTab(self, index):
        if index == 0:
            self.tab1.setStyleSheet('imge:url(20211026_150102.png)')
        elif index == 1:
            self.tab2.setStyleSheet('imge:url(20211026_150102.png)')
        else:
            self.tab3.setStyleSheet('imge:url(20211026_150102.png)')


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
