import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QDoubleSpinBox, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.label1 = QLabel('qspin')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(10000000)
        self.spinbox.setSingleStep(1000)
        self.label2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.valueChange)

        self.label3 = QLabel('qdoublepsinbox')
        self.dSpinbox = QDoubleSpinBox()
        self.dSpinbox.setSingleStep(.5)
        self.dSpinbox.setSuffix('dooloow')
        self.dSpinbox.setDecimals(1)
        self.label4 = QLabel('0')

        self.dSpinbox.valueChanged.connect(self.valueChange2)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.dSpinbox)
        vbox.addWidget(self.label4)

        self.setLayout(vbox)
              
        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def valueChange(self):
        self.label2.setText(str(self.spinbox.value())+'원 ->'+
        str(round(self.spinbox.value()/1191,2))+'달러')
        


    def valueChange2(self):
        self.label2.setText(f'{self.dSpinbox.value()}원 ->'+
        f'{round(self.dSpinbox.value()*1991,2)}달러')

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
