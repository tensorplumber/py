import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QTimeEdit, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime
# from PyQt5.QtGui import QPixmap
import urllib.request

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label = QLabel('QTimeEdit')
        label.setAlignment(Qt.AlignCenter)

        time = QTimeEdit(self)
        time.setTime(QTime.currentTime())
        time.setTimeRange(QTime(00,00,00), QTime.currentTime())
        time.setDisplayFormat('a:hh:mm:ss.zzz')

        label2 = QLabel('QDateEdit')
        label2.setAlignment(Qt.AlignCenter)

        date_edit = QDateEdit(self)
        date_edit.setDate(QDate.currentDate())
        date_edit.setDateRange(QDate(2000,1,1), QDate.currentDate())
        date_edit.dateChanged.connect(self.dateChange)

        label3 = QLabel('이곳에서 dateedit에서 선택된값')
        label3.setAlignment(Qt.AlignCenter)

        label4 = QLabel('qdateimeedit')
        label4.setAlignment(Qt.AlignCenter)

        label5 = QLabel('qdateimeedit')
        label5.setAlignment(Qt.AlignCenter)
        label5.setText(f'qdatetime \n 현재시간은 {QDateTime.currentDateTime().toString("yyyy년 mmm ㅇdnjf ㄴㄴ.zzz")}')

        dt_edit = QDateTimeEdit(self)

        dt_edit.setDateTimeRange(QDateTime(2020,1,1,00,00,00),
        QDateTime(20201,1,1,00,00,00))
        dt_edit.setDisplayFormat('yyyy.mm.dd hh:mm.:ss')
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(time)
        vbox.addWidget(label2)
        vbox.addWidget(date_edit)
        vbox.addWidget(label3)
        vbox.addWidget(label5)
        vbox.addWidget(dt_edit)

        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def dateChange(self):
        self.label3.setText(self.date_edit.date().toString('yyyy년 mmmm d일'))

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
