# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Dashboard import Ui_Dialog_Dashboard
from Registration import Ui_Dialog_Registration


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 170, 210, 161))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_Login = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Login.setObjectName("pushButton_Login")

        self.verticalLayout.addWidget(self.pushButton_Login)
        self.pushButton_createAccount = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_createAccount.setObjectName("pushButton_createAccount")
        self.verticalLayout.addWidget(self.pushButton_createAccount)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Collegamenti: Azioni con bottoni
        #self.pushButton_Login.clicked.connect(self.openWindowDashboard)
        self.pushButton_createAccount.clicked.connect(self.openWindowRegistration)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Singin"))
        self.label.setText(_translate("MainWindow", "UserName"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        self.pushButton_createAccount.setText(_translate("MainWindow", "Create an account"))



    def openWindowRegistration(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_Dialog_Registration()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setWindowModality(QtCore.Qt.WindowModal)

        self.main.hide()
        self.dialog.exec_()
        self.main.show()
        print("ciao")

    def openWindowDashboard(self):
        #lg.append(self.lineEdit_email.text())
        #lg.append(self.lineEdit_password.text())
        message = {"id": 21,
                   "name": self.lineEdit_email.text(),
                   "email": self.lineEdit_password.text()}  # ecc ecc
        self.events.onLoginDone(message)

        #Allora quello che vuoi fare tu... nn funziona
        #la cosa che potresti fare è questa

        self.Dialog = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog_Dashboard()
        self.ui2.setupUi(self.Dialog)
        self.Dialog.show()
        self.main.close()
        #cmq in ogni caso nn va bene... ste chiamate devono essere fatte dal main, altrimenti nn abbiamo controllo sui risultati...
        #cioè non possiamo ascoltare un evento di un form a cui nn possiamo accedere dal main... nn so se mi stai capendo,, avevo intuito una cosa del genere
        #cioè se self.ui2 la sto creando qua... dal main nn posso fare self.ui2.onLoginDone per esempio... capito?

    def Avvio(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
