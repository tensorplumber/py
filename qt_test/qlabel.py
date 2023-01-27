import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        label_1 = QLabel(self)
        label_1.setText('라벨1')
        label_1.setAlignment(Qt.AlignLeft)

        label_2 = QLabel('자벨2',self)
        label_2.setAlignment(Qt.AlignLeft)

        label_3 = QLabel('라벨3',self)
        label_3.setAlignment(Qt.AlignLeft)

        font_1 = label_1.font()
        font_1.setPointSize(15)
        font_1.setItalic(True)

        font_2 = label_2.font()
        font_2.setPointSize(15)
        font_2.setBold(True)

        font_3 = label_3.font()
        font_3.setPointSize(15)
        font_3.setFamily('Helvetica')

        label_1.setFont(font_1)
        label_2.setFont(font_2)
        label_3.setFont(font_3)

        vbox = QVBoxLayout()
        vbox.addWidget(label_1)
        vbox.addWidget(label_2)
        vbox.addWidget(label_3, alignment=Qt.AlignCenter)

        self.setLayout(vbox)
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('checkbox')
        self.show()

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
