from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
from pathlib import Path

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit('이곳ㅇ데 파일내용')
        self.label = QLabel('그림')
        
        btn_open = QPushButton('파일불러오기')
        btn_open.clicked.connect(self.loadFile)

        btn_img = QPushButton('이미지불러오기')
        btn_img.clicked.connect(self.loadImg)

        vbox = QVBoxLayout()
        vbox.addWidget(self.textEdit)
        vbox.addWidget(btn_open)
        vbox.addWidget(self.label, alignment=Qt.AlignCenter)
        vbox.addWidget(btn_img)

        self.setLayout(vbox)

        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()
        
    def loadFile(self):
        openfile = QFileDialog.getOpenFileName(self, '파일열기','./',filter='Python Files(*.py)')
        if openfile[0]:
            f = open(openfile[0], 'r', encoding='utf-8')
            with f:
                data = f.read()
                self.textEdit.setText(data)
        
    def loadImg(self):
        home_dir = str(Path.home())
        openfile = QFileDialog.getOpenFileName(self, '이미지열기',directory=home_dir,filter='Python Files(*.png)')
        self.label.setPixmap(QPixmap(openfile[0]))

app = QApplication(sys.argv)
ex = myapp()
app.exec_()