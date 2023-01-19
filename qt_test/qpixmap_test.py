import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot
import numpy as np
class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(800,300)
        cap = cv2.VideoCapture(0)
        self.change_pixmap_signal = pyqtSignal(np.ndarray)

        while True:
            ret, frame = cap.read()
            
            if ret:
                self.change_pixmap_signal.emit(frame)

            if not 1:
                break

        # url = "http://cafefiles.naver.net/data21/2006/12/6/291/12801024-1-badpark.jpg"
        # image = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(frame)
        self.lbl.setPixmap(pixmap)

        self.resize(800,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = test()
    sys.exit(app.exec_())