import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QBasicTimer
class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.bar1 = QProgressBar(self)
        self.bar1.setOrientation(Qt.Vertical)
        self.bar1.setGeometry(50,50,80,300) #x,y,width, height
        
        
        self.bar2 = QProgressBar(self)
        self.bar2.setGeometry(250,200,250,30) #x,y,width, height
        self.bar2.setRange(0,50)

        self.label1 = QLabel(f'이 바의 범위는 {self.bar2.minimum()}부터ㅕ {self.bar2.maximum()}까지',self)
        self.label1.move(130,300)

        self.label2 = QLabel('이 첫번째 바의 값 ',self)
        self.label2.move(50,240)

        self.btn = QPushButton('시작',self)
        self.btn.move(50,390)
        self.btn.clicked.connect(self.runTimer)

        self.value = 0
        self.timer = QBasicTimer()
        self.bar1.valueChanged.connect(self.changeValue)

        
        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def runTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('시작')

        else:
            self.timer.start(self.bar1.maximum(),self)
            self.btn.setText('중지')

    def timerEvent(self, event):
        if self.value >= self.bar1.maximum():
            self.timer.stop()
            self.btn.setText('완료')
            return

        self.value +=1
        self.bar1.setValue(self.value)

    def changeValue(self):
        self.label2.setText(str(self.bar1.value()))


        

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
