import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!") 
        button.setCheckable(True) # to recognize pressed & released states
        button.clicked.connect(self.the_button_was_clicked) # clicked signal

        self.setCentralWidget(button)
    
    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()