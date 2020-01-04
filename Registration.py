# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Registration(object):
    def setupUi(self, Dialog_Registration):
        Dialog_Registration.setObjectName("Dialog_Registration")
        Dialog_Registration.resize(262, 278)
        Dialog_Registration.setMinimumSize(QtCore.QSize(200, 234))
        Dialog_Registration.setMaximumSize(QtCore.QSize(1000, 5000))
        self.groupBox = QtWidgets.QGroupBox(Dialog_Registration)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 200, 241))
        self.groupBox.setStyleSheet("background-color: rgba(111,111,111, 0.1);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Signup_toolButton = QtWidgets.QToolButton(self.groupBox)
        self.Signup_toolButton.setGeometry(QtCore.QRect(16, 170, 161, 61))
        self.Signup_toolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Signup_toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/register_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Signup_toolButton.setIcon(icon)
        self.Signup_toolButton.setIconSize(QtCore.QSize(300, 90))
        self.Signup_toolButton.setObjectName("Signup_toolButton")
        self.toolButton = QtWidgets.QToolButton(Dialog_Registration)
        self.toolButton.setGeometry(QtCore.QRect(80, 0, 100, 61))
        self.toolButton.setStyleSheet("background-color: rgba(255,255,255, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/register-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog_Registration)
        self.lineEdit_name.setGeometry(QtCore.QRect(50, 70, 161, 21))
        self.lineEdit_name.setMinimumSize(QtCore.QSize(161, 21))
        self.lineEdit_name.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;\n"
"background-color: rgba(255,255,255, 0.8);")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_surname = QtWidgets.QLineEdit(Dialog_Registration)
        self.lineEdit_surname.setGeometry(QtCore.QRect(50, 100, 161, 20))
        self.lineEdit_surname.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEdit_surname.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;\n"
"background-color: rgba(255,255,255, 0.8);")
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.lineEdit_email = QtWidgets.QLineEdit(Dialog_Registration)
        self.lineEdit_email.setGeometry(QtCore.QRect(50, 130, 161, 20))
        self.lineEdit_email.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEdit_email.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;\n"
"background-color: rgba(255,255,255, 0.8);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog_Registration)
        self.lineEdit_password.setGeometry(QtCore.QRect(50, 160, 161, 20))
        self.lineEdit_password.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_password.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;\n"
"background-color: rgba(255,255,255, 0.8);")
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.retranslateUi(Dialog_Registration)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Registration)

    def retranslateUi(self, Dialog_Registration):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Registration.setWindowTitle(_translate("Dialog_Registration", "Register a new account"))
        self.toolButton.setText(_translate("Dialog_Registration", "..."))
        self.lineEdit_name.setPlaceholderText(_translate("Dialog_Registration", "Name..."))
        self.lineEdit_surname.setPlaceholderText(_translate("Dialog_Registration", "Surname..."))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog_Registration", "Email..."))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog_Registration", "Password..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Registration = QtWidgets.QDialog()
    ui = Ui_Dialog_Registration()
    ui.setupUi(Dialog_Registration)
    Dialog_Registration.show()
    sys.exit(app.exec_())
