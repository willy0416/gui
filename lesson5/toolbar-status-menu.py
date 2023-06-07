import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QCheckBox,
    QLabel, QToolBar, QAction, QStatusBar
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("../icons/icons/abacus.png"), "your button", self) # 2nd parameter is the parent for the action
        button_action.setStatusTip("this is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True) # makes the QAction toggleable

        # keyboard shortcut
        button_action.setShortcut(QKeySequence("Ctrl+k"))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('../icons/icons/bug.png'), '2nd button', self)
        button_action2.setStatusTip("This is your second button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True) 
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        # will only output false if the button is CHECKED (not nec. clicked)
        print("click", s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()