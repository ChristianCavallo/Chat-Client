# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(290, 388)
        LoginForm.setMinimumSize(QtCore.QSize(250, 278))
        LoginForm.setMaximumSize(QtCore.QSize(450, 400))
        self.centralwidget = QtWidgets.QWidget(LoginForm)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 271, 351))
        self.groupBox.setStyleSheet("background-color: rgba(111,111,111, 0.1);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(50, 140, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(40, 130, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("padding-left: 35px;\n"
"border-radius: 20px;\n"
"background-color: rgba(255,255,255, 0.8);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(40, 180, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("padding-left: 35px;\n"
"border-radius: 20px;\n"
"background-color: rgba(255,255,255, 0.8);")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(50, 190, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("background-color: rgba(255,255,255,0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(106, 0, 71, 71))
        self.toolButton_3.setStyleSheet("background-color: rgba(255,255,255,0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/user_contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(70, 70))
        self.toolButton_3.setObjectName("toolButton_3")
        self.pushButton_Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Login.setGeometry(QtCore.QRect(40, 230, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setStyleSheet("background-color: rgba(0,175, 206);\n"
"color: rgba(255,255,255);\n"
"border-radius: 10px;")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.pushButton_createAccount = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_createAccount.setGeometry(QtCore.QRect(40, 320, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_createAccount.setFont(font)
        self.pushButton_createAccount.setStyleSheet("background-color: rgba(0,175, 206);\n"
"color: rgba(255,255,255);\n"
"border-radius: 10px;")
        self.pushButton_createAccount.setObjectName("pushButton_createAccount")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgba(0,175, 206);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox.raise_()
        self.toolButton_3.raise_()
        self.label.raise_()
        self.pushButton_Login.raise_()
        self.pushButton_createAccount.raise_()
        self.lineEdit_password.raise_()
        self.lineEdit_email.raise_()
        self.toolButton_2.raise_()
        self.toolButton.raise_()
        LoginForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login to the chat!"))
        self.toolButton.setText(_translate("LoginForm", "..."))
        self.lineEdit_email.setPlaceholderText(_translate("LoginForm", "Email..."))
        self.lineEdit_password.setPlaceholderText(_translate("LoginForm", "Password..."))
        self.toolButton_2.setText(_translate("LoginForm", "..."))
        self.toolButton_3.setText(_translate("LoginForm", "..."))
        self.pushButton_Login.setText(_translate("LoginForm", "Login"))
        self.pushButton_createAccount.setText(_translate("LoginForm", "Create an account"))
        self.label.setText(_translate("LoginForm", "Sign in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QMainWindow()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())
