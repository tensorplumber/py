from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton,QLabel,QHBoxLayout, QLineEdit, QGroupBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap, QFont
import sys


class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.합산 = QLabel('*5년 월급 합: -원, \n\n* 5년 실수령액 합: -원\n\n*실수령액과 집값과의 차 : -원')
        버튼 = QPushButton('계산하기')
        버튼.clicked.connect(self.btnClick)

        가로정렬 = QHBoxLayout()
        가로정렬.addWidget(self.사용자입력그룹박스())
        가로정렬.addWidget(self.월급그룹박스())
        가로정렬.addWidget(self.실수령액그룹박스())


        세로정렬 = QVBoxLayout()
        세로정렬.addLayout(가로정렬)
        세로정렬.addWidget(self.합산)
        세로정렬.addWidget(버튼)

        self.setLayout(세로정렬)
        

   
        self.setWindowTitle('재무보고서')
        self.setWindowIcon(QIcon('png_sample/20211026_150102.png'))
        self.setGeometry(300,300,1000,540)
        self.show()


    def 사용자입력그룹박스(self):
        self.월급_라벨 = QLabel('월급(만원)')
        self.월급_라인입력 = QLineEdit(self)
        self.월급_라인입력.setFixedWidth(200)

        self.세금_라벨 = QLabel('세금(%)')
        self.세금_라인입력 = QLineEdit(self)
        self.세금_라인입력.setFixedWidth(200)

        self.연인상율_라벨 = QLabel('연인상율(%)')
        self.연인상율_라인입력 = QLineEdit(self)
        self.연인상율_라인입력.setFixedWidth(200)

        self.집값_라벨 = QLabel('집값(억원)')
        self.집값_라인입력 = QLineEdit(self)
        self.집값_라인입력.setFixedWidth(200)


        self.그룹박스_사용자입력 = QGroupBox('사용자 입력 그룹박스')
        self.세로정렬_사용자입력 = QVBoxLayout()
        self.세로정렬_사용자입력.addWidget(self.월급_라벨)
        self.세로정렬_사용자입력.addWidget(self.월급_라인입력)
        self.세로정렬_사용자입력.addWidget(self.세금_라벨)
        self.세로정렬_사용자입력.addWidget(self.세금_라인입력)
        self.세로정렬_사용자입력.addWidget(self.연인상율_라벨)
        self.세로정렬_사용자입력.addWidget(self.연인상율_라인입력)
        self.세로정렬_사용자입력.addWidget(self.집값_라벨)
        self.세로정렬_사용자입력.addWidget(self.집값_라인입력)
        self.그룹박스_사용자입력.setLayout(self.세로정렬_사용자입력)
        self.그룹박스_사용자입력.setFixedWidth(330)

        return self.그룹박스_사용자입력

    def 월급그룹박스(self):
        self.월급_라벨하나 = QLabel('1년 : -원')
        self.월급_라벨둘 = QLabel('2년 : -원')
        self.월급_라벨셋 = QLabel('3년 : -원')
        self.월급_라벨넷 = QLabel('4년 : -원')
        self.월급_라벨다섯 = QLabel('5년 : -원')

        self.그룹박스_연봉 = QGroupBox('연봉')
        self.세로정렬_월급 = QVBoxLayout()
        self.세로정렬_월급.addWidget(self.월급_라벨하나)
        self.세로정렬_월급.addWidget(self.월급_라벨둘)
        self.세로정렬_월급.addWidget(self.월급_라벨셋)
        self.세로정렬_월급.addWidget(self.월급_라벨넷)
        self.세로정렬_월급.addWidget(self.월급_라벨다섯)
        self.그룹박스_연봉.setLayout(self.세로정렬_월급)

        return self.그룹박스_연봉

    def 실수령액그룹박스(self):
        self.실수령액_라벨하나 = QLabel('1년: -원')
        self.실수령액_라벨둘 = QLabel('2년: -원')
        self.실수령액_라벨셋 = QLabel('3년: -원')
        self.실수령액_라벨넷 = QLabel('4년: -원')
        self.실수령액_라벨다섯 = QLabel('5년: -원')

        self.그룹박스_실수령액 = QGroupBox('실수령액')
        self.세로정렬_실수령액 = QVBoxLayout()
        self.세로정렬_실수령액.addWidget(self.실수령액_라벨하나)
        self.세로정렬_실수령액.addWidget(self.실수령액_라벨둘)
        self.세로정렬_실수령액.addWidget(self.실수령액_라벨셋)
        self.세로정렬_실수령액.addWidget(self.실수령액_라벨넷)
        self.세로정렬_실수령액.addWidget(self.실수령액_라벨다섯)
        self.그룹박스_실수령액.setLayout(self.세로정렬_실수령액)

        return self.그룹박스_실수령액
        
    def btnClick(self):
        입력값 = []
        입력값.append(float(self.월급_라인입력.text()))
        입력값.append(float(self.세금_라인입력.text()))
        입력값.append(float(self.연인상율_라인입력.text()))
        입력값.append(float(self.집값_라인입력.text()))
        
        일년차_연봉 = 입력값[0]*12
        이년차_연봉 = 일년차_연봉*(입력값[2]+100)/100
        삼년차_연봉 = 일년차_연봉*(입력값[2]+100)/100
        사년차_연봉 = 일년차_연봉*(입력값[2]+100)/100
        오년차_연봉 = 일년차_연봉*(입력값[2]+100)/100

        self.월급_라벨하나.setText(f'1년 : {일년차_연봉}만원')
        self.월급_라벨둘.setText(f'1년 : {이년차_연봉}만원')
        self.월급_라벨셋.setText(f'1년 : {삼년차_연봉}만원')
        self.월급_라벨넷.setText(f'1년 : {사년차_연봉}만원')
        self.월급_라벨다섯.setText(f'1년 : {오년차_연봉}만원')
         
app = QApplication(sys.argv)
ex = myapp()
app.exec_()