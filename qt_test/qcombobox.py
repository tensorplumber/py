import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QComboBox

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.label = QLabel('옵션선택', self)
        self.label.move(20,80)
        self.label.setFixedSize(300,20)

        self.cbox = QComboBox(self)
        self.cbox.addItem('op1')
        self.cbox.addItem('op2')
        self.cbox.addItem('op3')
        self.cbox.addItem('op4')

        self.cbox.move(40,40)
        self.cbox.activated[str].connect(self.clicked)


        self.setGeometry(300,300,300,150)
        self.setWindowTitle('checkbox')
        self.show()

    def clicked(self):
        index = str(self.cbox.currentIndex())
        print(index)
        text = str(self.cbox.currentText())
        print(text)
        self.label.setText(f'아이템의 {index}번째 {text}을 선택')
        self.adjustSize()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
