import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
class MyForm(QtWidgets.QDialog):
	def __init__(self, parent = None):
		QtWidgets.QDialog.__init__(self, parent)
        # super(self).__init__()
		self.ui = uic.loadUi('vision.ui',self)#self 안주면 attribute error
		self.ui.label.setText('input data')
		self.ui.show()

# AttributeError: 'QDialog' object has no attribute 'slot_save' save함수가 없으니 정의하라는 말
	def slot_save(self): 
		msg = self.ui.lineEdit.text()
		with open('data.txt','at') as f:
			f.write(msg+'\n')
		self.ui.label.setText('saved input data')
		self.ui.lineEdit.setText('')

	def slot_clear(self): 
		self.ui.label.setText('clear input data')
		self.ui.lineEdit.setText('')
	def slot_exit(self): 
		print('bye')
		sys.exit()

app = QtWidgets.QApplication(sys.argv)
w = MyForm()
sys.exit(app.exec())
