from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # super(MainWindow, self).__init__(*args, **kwargs) # always do this
        super().__init__() # or this when __init__ does not take arguments
        self.setWindowTitle("My Awesome App")

        label = QLabel("THIS IS AWESOME!!!") # text
        label.setAlignment(Qt.AlignCenter) # horizontal alignment
        self.setFixedSize(QSize(500, 400))
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()