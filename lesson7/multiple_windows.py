from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

# If you need toolbars or menus on the second window, use QMainWindow (otherwise any subclass of QWidget)

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        # must keep reference to window in an instance variable for window to persist
        if self.w is None: # a.k.a. window has not yet been created
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None # Discard reference


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()