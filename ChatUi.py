# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(592, 520)
        Form.setMinimumSize(QtCore.QSize(592, 520))
        Form.setMaximumSize(QtCore.QSize(592, 520))
        Form.setStyleSheet("background-color: rgb(237, 237, 237);")
        self.mediaToolButton = QtWidgets.QToolButton(Form)
        self.mediaToolButton.setGeometry(QtCore.QRect(7, 472, 40, 41))
        self.mediaToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.mediaToolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/OpenCamera1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mediaToolButton.setIcon(icon)
        self.mediaToolButton.setIconSize(QtCore.QSize(50, 50))
        self.mediaToolButton.setAutoRaise(False)
        self.mediaToolButton.setObjectName("mediaToolButton")
        self.sendToolButton = QtWidgets.QToolButton(Form)
        self.sendToolButton.setGeometry(QtCore.QRect(520, 480, 61, 26))
        self.sendToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.sendToolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/send3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendToolButton.setIcon(icon1)
        self.sendToolButton.setIconSize(QtCore.QSize(50, 50))
        self.sendToolButton.setObjectName("sendToolButton")
        self.labelChatName = QtWidgets.QLabel(Form)
        self.labelChatName.setGeometry(QtCore.QRect(60, 5, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelChatName.setFont(font)
        self.labelChatName.setWordWrap(True)
        self.labelChatName.setObjectName("labelChatName")
        self.iconToolButton = QtWidgets.QToolButton(Form)
        self.iconToolButton.setGeometry(QtCore.QRect(5, 5, 41, 41))
        self.iconToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.iconToolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconToolButton.setIcon(icon2)
        self.iconToolButton.setIconSize(QtCore.QSize(50, 50))
        self.iconToolButton.setCheckable(False)
        self.iconToolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.iconToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.iconToolButton.setObjectName("iconToolButton")
        self.statusToolButton = QtWidgets.QToolButton(Form)
        self.statusToolButton.setGeometry(QtCore.QRect(35, 30, 15, 15))
        self.statusToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.statusToolButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/green_dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statusToolButton.setIcon(icon3)
        self.statusToolButton.setIconSize(QtCore.QSize(50, 50))
        self.statusToolButton.setObjectName("statusToolButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 591, 411))
        self.listWidget.setStyleSheet("background-color: rgb(229, 221, 213);\n"
"")
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        self.labelStatus = QtWidgets.QLabel(Form)
        self.labelStatus.setGeometry(QtCore.QRect(60, 30, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelStatus.setFont(font)
        self.labelStatus.setStyleSheet("text-color: \"red\"")
        self.labelStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.textLine = QtWidgets.QLineEdit(Form)
        self.textLine.setGeometry(QtCore.QRect(50, 477, 521, 31))
        self.textLine.setStyleSheet("border-radius: 15px;\n"
"padding-left: 10px;\n"
"padding-right: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.textLine.setObjectName("textLine")
        self.iconToolButton.raise_()
        self.labelChatName.raise_()
        self.statusToolButton.raise_()
        self.listWidget.raise_()
        self.labelStatus.raise_()
        self.textLine.raise_()
        self.mediaToolButton.raise_()
        self.sendToolButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Chat"))
        self.labelChatName.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:400;\">Christian Cavallo</span></p></body></html>"))
        self.labelStatus.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:normal; color:#7e7e7e;\">online now</span></p></body></html>"))
        self.textLine.setText(_translate("Form", "Some text to send here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
