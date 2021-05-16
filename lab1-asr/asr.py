from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys
import threading
import recognizer


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def clickButton():
    application.ui.gif.start()
    t1 = threading.Thread(target=recognizer.recognizeSpeech, args=(application,))
    t1.setDaemon(True)
    t1.start()


app = QtWidgets.QApplication([])
application = myWindow()

application.show()

application.ui.button.clicked.connect(clickButton)
sys.exit(app.exec())
