from PyQt5.QtWidgets import QMainWindow, QComboBox, QApplication

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"]) # items added in this order

        # Sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        widget.currentTextChanged.connect( self.text_changed )

        # To make editable: widget.setEditable(True)
            # can use a flag instead to control how the custom inserts occur (QComboBox.NoInsert, InsertAtTop, InsertAtCurrent, InsertAtBottom, InsertAfterCurrent, InsertBeforeCurrent, InsertALphabetically)
            # can also do widget.setMaxCount(10)

        self.setCentralWidget(widget)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()