from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton,QLabel,QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal, QObject
import sys

class Signal(QObject):
    closeProgram = pyqtSignal()
    addText = pyqtSignal()


class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.signal1 = Signal()    
        self.signal1.closeProgram.connect(self.close)

        self.label1 = QLabel('시그널을 알아보자', self)
        self.label1.setFixedSize(300,20)
        self.label1.move(40,100)

        self.signal2 = Signal()
        self.signal2.addText.connect(self.changelabel)
        
        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def mouseDoubleClickEvent(self, event):
        self.signal1.closeProgram.emit()

    def mousePressEvent(self, event):
        self.signal2.addText.emit()


    def changelabel(self):
        self.label1.setText('마우스가 눌림')

    def close(self):
        super().close()
        

app = QApplication(sys.argv)
ex = myapp()
app.exec_()