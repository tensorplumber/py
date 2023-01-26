import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel
from PyQt5.QtCore import Qt #가운데 정렬

class myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cbox = QCheckBox('체크박스1', self)
        self.cbox.move(40,30)

        self.cbox.stateChanged.connect(self.changeBox1)

        self.cbox2 = QCheckBox('체크박스2', self)
        self.cbox2.move(150,30)

        self.cbox2.stateChanged.connect(self.changeBox2)

        self.result = QLabel('체크박스 넛ㄴ택', self)
        self.result.setFixedWidth(300)
        self.result.move(40,100)

        self.cbox2.toggle() #변화되는 삳태는 논리적으로 뒤에
        # attribute
        # text() 체크박스의 라벨텍스트 반환
        # setText() 라벨텍스트 설정
        # isChecked() 상태반환 트루폴스
        # checkState() 체크 박스의 상태를 반환 2/1/0 선택/변경없음/해제
        # toggle() 상태변경
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('checkbox')
        self.show()

    def changeBox1(self,state):
        print(state)
        if state == 2:
            self.result.setText('체크박스1 선택')
        else:
            self.result.setText('체크박스 선택해')

    def changeBox2(self, state):
        if state == Qt.Checked:
            self.result.setText('체크박스2 선택')
        else:
            self.result.setText('체크박스 선택해')

프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = myapp()
프로그램무한반복.exec_()
