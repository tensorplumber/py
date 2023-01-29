import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        btn_1 = QRadioButton(self)
        btn_1.setText('버튼1')
        btn_1.move(60,50)
        
        btn_2 = QRadioButton('&Button2',self)
        btn_2.setText('버튼2')
        btn_2.setChecked(True)
        btn_2.move(60,80)
        
        btn_3 = QRadioButton('버튼3',self)
        btn_3.move(50,120)
        btn_3.setAutoExclusive(False)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('checkbox')
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
