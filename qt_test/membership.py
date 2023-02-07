import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
from PyQt5 import uic

class MyForm(QMainWindow):
    def __init__(self, parent =None):
        super().__init__(parent)
        self.ui = uic.loadUi('membership.ui', self)
        self.userInput = {'name': self.lineEdit_2,
        'id': self.lineEdit,
        'pw1': self.lineEdit_4,
        'pw2': self.lineEdit_3}
        self.lenInfo = {'name':{'minLne':2,'maxlne':20}, 'id':{'minLne':3,'maxlne':20},'pw1':{'minLne':8,'maxlne':20}}
        self.errMsg = {'title': '오류메시지','name':f'이름 길이 {self.lenInfo.name.minLne}~{self.lenInfo.name.maxlne}글자', 'id':f'이름 길이 {self.lenInfo.id.minLne}~{self.lenInfo.id.maxlne}글자', 'pw1':f'이름 길이 {self.lenInfo.pw1.minLne}~{self.lenInfo.pw1.maxlne}글자'}


        self.signupButton.setEnabled(False)
        self.signupButton.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.lineEdit_2.returnPressed.connect(self.lineEdit_3.setFocus)
        # self.lineEdit_3.returnPressed.connect(self.lineEdit_4.setFocus)
        # self.lineEdit_4.returnPressed.connect(self.lineEdit.setFocus)
        # self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)

        for x in self.userInput.values():
            x.returnPressed.connect(self.focusNextChild)

        self.currInfo = dict.fromkeys(('name','ikd','pw1','pw2'),None)
        self.newMemberInfo = dict.fromkeys(('name','ikd','pw1','pw2'),None)
        # self.lineEdit_2.returnPressed.connect(self.focusNextChild)
        # self.lineEdit_3.returnPressed.connect(self.focusNextChild)
        # self.lineEdit_4.returnPressed.connect(self.focusNextChild)
        # self.lineEdit.returnPressed.connect(self.focusNextChild)
        self.ui.show()

    def check_twice_enter(self, target):
        value = self.userInput[target].text()
        if value == self.currInfo[target] : return None #변경되지 않은 경우
        print('value_step2')
        self.currInfo[target] = value
        return value


    def slot_checkName(slef): 
        print('name')
        target = 'name'
        value = self.check_twice_enter('name')
        if value == None: return
        if len(value) >= self.lenInfo.target.minlne and len(value) <= self.lenInfo.target.maxlne:
            self.newMember.target = value
        else:
            QMessageBox.critical(self, self.errMsg.title,self.errMsg.target)

        # value = self.check_twice_enter()
        # if value == None : return
        # name = self.lineEdit_2.text()
        # if name == self.currInfo['name'] : return #변경되지 않은 경우
        # print('name_step2')
        # self.currInfo['name'] = name

    def slot_checkId(slef): print('id')
    def slot_checkpw1(slef): print('pw1')
    def slot_checkpw2(slef): print('pw2')
    def slot_membership(slef): print('member')

app = QApplication(sys.argv)
w = MyForm()
sys.exit(app.exec_())