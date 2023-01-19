from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QFontDialog, QColorDialog, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.label = QLabel('제주베이스',self)
        self.label.setAlignment(Qt.AlignCenter)

        btn1 = QPushButton('퐅느선택',self)
        btn1.clicked.connect(self.showFont)

        color = QColor(Qt.black)

        self.colorFrame = QFrame(self)
        self.colorFrame.setStyleSheet(f'background-color:{color.name()};')

        btn2 = QPushButton('색상선택',self)
        btn2.clicked.connect(self.showColor)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn1)
        vbox.addWidget(self.colorFrame)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()
        

    def showFont(self):
        font, flag = QFontDialog.getFont()
        if flag:
            self.label.setFont(font)
        else:
            self.label.setText('폰트 선택')

    def showColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.colorFrame.setStyleSheet(f'background-color:{color.name()};')
        else:
            self.colorFrame.setStyleSheet('image:url(png_sample/20211026_150102.png);')

app = QApplication(sys.argv)
ex = myapp()
app.exec_()