import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QRadioButton, QCheckBox, QPushButton, QGridLayout, QVBoxLayout, QMenu, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        img = QPixmap('20211026_150102.png')
        label = QLabel()
        label.setPixmap(img)
        label.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        grid.addWidget(self.RadioGroup(),0,0)
        grid.addWidget(self.CheckGroup(),1,0)
        grid.addWidget(label,0,1,2,1)
        grid.addWidget(self.PushButtonGroup(),2,0,1,2)

        self.setLayout(grid)

              
        self.setGeometry(300,300,600,700)
        self.setWindowTitle('checkbox')
        self.show()

    def RadioGroup(self):
        RadioGroupBox = QGroupBox('라디오 버튼 그룹')

        radio1 = QRadioButton('라디오버튼1')
        radio2 = QRadioButton('라디오버튼2')
        radio3 = QRadioButton('라디오버튼3')
        radio2.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        RadioGroupBox.setLayout(vbox)

        return RadioGroupBox

    def CheckGroup(self):
        CheckBoxGroup = QGroupBox('체크박스그룹')
        CheckBoxGroup.setCheckable(True) #하위항목에서 체크를 허용할 것인가
        CheckBoxGroup.setChecked(False) #체크된 상태로 시작할 것인가

        checkbox1 = QCheckBox('체크박스1')
        checkbox1.setChecked(True)
        checkbox2 = QCheckBox('체크박스2')

        tristatebox = QCheckBox('체크박스3')
        tristatebox.setTristate(True) #체크형태  

        hbox = QHBoxLayout()

        hbox.addWidget(checkbox1)
        hbox.addWidget(checkbox2)
        hbox.addWidget(tristatebox)
        CheckBoxGroup.setLayout(hbox)

        return CheckBoxGroup

    def PushButtonGroup(self):
        PushButtonGroupBox = QGroupBox('푸시버튼 그룹')
        PushButtonGroupBox.setAlignment(Qt.AlignCenter)

        PushButton = QPushButton('기본버튼')
        PushButton.setStyleSheet('color:green;'
        'border-style:solide;''bordfer-width:3px;''background-color:beige;')

        CheckedBotton = QPushButton('체크표시버튼')
        CheckedBotton.setCheckable(True)
        CheckedBotton.setChecked(False)

        FlatButton = QPushButton('FLAT')
        FlatButton.setFlat(True)

        PopupButton = QPushButton('popCUP')
        menu = QMenu(self)
        menu.addAction('opt1')
        menu.addAction('opt2')
        PopupButton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(PushButton)
        vbox.addWidget(CheckedBotton)
        vbox.addWidget(FlatButton)
        vbox.addWidget(PopupButton)
        PushButtonGroupBox.setLayout(vbox)

        return PushButtonGroupBox


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
