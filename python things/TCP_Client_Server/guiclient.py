from PyQt4 import QtGui, QtCore, uic
import sys
import socket
from cwindow import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSend.clicked.connect(self.btnSend_clicked)
        
    def btnSend_clicked(self):
        self.ui.out.setText("hello")
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
