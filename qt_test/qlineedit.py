import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit
from PyQt5.QtCore import Qt
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.label = QLabel(self)
        self.label.move(30,20)

        self.inputText = QLineEdit(self)
        self.inputText.move(30,50)
        self.inputText.textChanged[str].connect(self.changed1)
        self.inputText.returnPressed.connect(self.changeText)

        self.label2 = QLabel(self)
        self.label2.move(30,100)

        self.inputText2 = QLineEdit(self)
        self.inputText2.move(30,150)
        self.inputText2.setEchoMode(2)
        self.inputText2.textChanged[str].connect(self.changed2)
        
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('checkbox')
        self.show()

    def changed1(self):
        # print(t
        # ext)
        self.label.setText('편집중 엔터키')
        self.label.adjustSize()


    def changeText(self):
        # print(self.inputText.text())
        self.label.setText(self.inputText.text())

    def changed2(self, text):
        print(text)
        self.label2.setText(text)
        self.label.adjustSize()
        

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
