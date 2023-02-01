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

        self.count = 0
        btn = QPushButton('클릭')
        btn.clicked.connect(self.changeLabel)

        self.label = QLabel(f'{self.count}번 누름')
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        
        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def changeLabel(self):
        self.count += 1
        self.label.setText(f'{self.count}번 누름')

        
app = QApplication(sys.argv)
ex = myapp()
app.exec_()