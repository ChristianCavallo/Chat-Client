import sys

from PyQt5.uic.properties import QtWidgets

import Login
import Registration
import client
import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainWindow


#SocketClient = client.SocketClient(('localhost', 15000))
login = Login
app = login.QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
print("bella minchiata")

#SocketClient.sendMessage("ciao")


