from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication
import sys

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn = QPushButton('그램 종료', self)
        btn.clicked.connect(self.close)
        btn.move(20,50)

        btn2 = QPushButton('에러발생', self)
        btn2.clicked.connect(self.critical)
        btn2.move(130,50)

        btn3 = QPushButton('경고발생', self)
        btn3.clicked.connect(self.warning)
        btn3.move(240,50)


        
        self.setWindowTitle('362546')
        self.setGeometry(300,300,720,500)
        self.show()

    def close(self):
        question = QMessageBox.question(self, '질문 메세짖창', '정말 종료?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if question == QMessageBox.Yes:
            super().close()

    def critical(self):
        critical = QMessageBox.critical(self, 'error', '에러가 ㅏㅂㄹ생?', QMessageBox.Help|QMessageBox.Reset, QMessageBox.Apply)
        

    def warning(self):
        warning = QMessageBox.warning(self, '경고', '위험?', QMessageBox.Ok|QMessageBox.Retry, QMessageBox.Ignore)
        

app = QApplication(sys.argv)
ex = myapp()
app.exec_()