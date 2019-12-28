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
        Dialog_Registration.resize(211, 256)
        Dialog_Registration.setMinimumSize(QtCore.QSize(200, 234))
        Dialog_Registration.setMaximumSize(QtCore.QSize(500, 5000))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_Registration)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEdit_email.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        self.lineEdit_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_surname.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEdit_surname.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;")
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.verticalLayout.addWidget(self.lineEdit_surname)
        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(161, 20))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_password.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.lineEdit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(161, 21))
        self.lineEdit_name.setStyleSheet("border-radius: 10px;\n"
"padding-left: 10px;")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.Signup_toolButton = QtWidgets.QToolButton(Dialog_Registration)
        self.Signup_toolButton.setGeometry(QtCore.QRect(15, 190, 181, 71))
        self.Signup_toolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Signup_toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/register_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Signup_toolButton.setIcon(icon)
        self.Signup_toolButton.setIconSize(QtCore.QSize(400, 100))
        self.Signup_toolButton.setObjectName("Signup_toolButton")

        self.retranslateUi(Dialog_Registration)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Registration)

    def retranslateUi(self, Dialog_Registration):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Registration.setWindowTitle(_translate("Dialog_Registration", "Register a new account"))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog_Registration", "Email..."))
        self.lineEdit_surname.setPlaceholderText(_translate("Dialog_Registration", "Surname..."))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog_Registration", "Password..."))
        self.lineEdit_name.setPlaceholderText(_translate("Dialog_Registration", "Name..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Registration = QtWidgets.QDialog()
    ui = Ui_Dialog_Registration()
    ui.setupUi(Dialog_Registration)
    Dialog_Registration.show()
    sys.exit(app.exec_())
