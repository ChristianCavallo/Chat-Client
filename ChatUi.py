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
        Form.resize(1024, 768)
        Form.setMinimumSize(QtCore.QSize(592, 520))
        Form.setMaximumSize(QtCore.QSize(2000, 2000))
        Form.setStyleSheet("background-color: rgb(237, 237, 237);\n"
"background-color: rgb(229, 221, 213);")
        self.messagesList = QtWidgets.QListWidget(Form)
        self.messagesList.setGeometry(QtCore.QRect(314, 70, 711, 640))
        self.messagesList.setStyleSheet("background-color: rgb(229, 221, 213);\n"
"")
        self.messagesList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.messagesList.setSelectionRectVisible(True)
        self.messagesList.setObjectName("messagesList")
        self.headerChatFrame = QtWidgets.QFrame(Form)
        self.headerChatFrame.setGeometry(QtCore.QRect(315, 0, 711, 71))
        self.headerChatFrame.setStyleSheet("background-color: rgb(237, 237, 237);")
        self.headerChatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerChatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerChatFrame.setObjectName("headerChatFrame")
        self.labelStatus = QtWidgets.QLabel(self.headerChatFrame)
        self.labelStatus.setGeometry(QtCore.QRect(89, 35, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelStatus.setFont(font)
        self.labelStatus.setStyleSheet("text-color: \"red\"")
        self.labelStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.statusToolButton = QtWidgets.QToolButton(self.headerChatFrame)
        self.statusToolButton.setGeometry(QtCore.QRect(50, 40, 20, 20))
        self.statusToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.statusToolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/green_dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statusToolButton.setIcon(icon)
        self.statusToolButton.setIconSize(QtCore.QSize(50, 50))
        self.statusToolButton.setObjectName("statusToolButton")
        self.labelChatName = QtWidgets.QLabel(self.headerChatFrame)
        self.labelChatName.setGeometry(QtCore.QRect(85, 5, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelChatName.setFont(font)
        self.labelChatName.setWordWrap(True)
        self.labelChatName.setObjectName("labelChatName")
        self.iconToolButton = QtWidgets.QToolButton(self.headerChatFrame)
        self.iconToolButton.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.iconToolButton.setFont(font)
        self.iconToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.iconToolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/user_contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconToolButton.setIcon(icon1)
        self.iconToolButton.setIconSize(QtCore.QSize(50, 50))
        self.iconToolButton.setCheckable(False)
        self.iconToolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.iconToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.iconToolButton.setObjectName("iconToolButton")
        self.removeChatToolButton = QtWidgets.QToolButton(self.headerChatFrame)
        self.removeChatToolButton.setGeometry(QtCore.QRect(650, 10, 51, 51))
        self.removeChatToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.removeChatToolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/remove_chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeChatToolButton.setIcon(icon2)
        self.removeChatToolButton.setIconSize(QtCore.QSize(80, 80))
        self.removeChatToolButton.setObjectName("removeChatToolButton")
        self.labelStatus.raise_()
        self.labelChatName.raise_()
        self.iconToolButton.raise_()
        self.removeChatToolButton.raise_()
        self.statusToolButton.raise_()
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 316, 771))
        self.frame_2.setStyleSheet("background-color: rgb(237, 237, 237);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(315, 0, 3, 768))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.userIconButton = QtWidgets.QToolButton(self.frame_2)
        self.userIconButton.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.userIconButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.userIconButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/user-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userIconButton.setIcon(icon3)
        self.userIconButton.setIconSize(QtCore.QSize(50, 50))
        self.userIconButton.setCheckable(False)
        self.userIconButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.userIconButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.userIconButton.setObjectName("userIconButton")
        self.userLabel = QtWidgets.QLabel(self.frame_2)
        self.userLabel.setGeometry(QtCore.QRect(70, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userLabel.setFont(font)
        self.userLabel.setWordWrap(True)
        self.userLabel.setObjectName("userLabel")
        self.searchContactLabel = QtWidgets.QLineEdit(self.frame_2)
        self.searchContactLabel.setGeometry(QtCore.QRect(20, 100, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchContactLabel.setFont(font)
        self.searchContactLabel.setStyleSheet("border-radius: 15px;\n"
"padding-left: 10px;\n"
"padding-right: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.searchContactLabel.setText("")
        self.searchContactLabel.setObjectName("searchContactLabel")
        self.addContactToolButton = QtWidgets.QToolButton(self.frame_2)
        self.addContactToolButton.setGeometry(QtCore.QRect(260, 100, 41, 41))
        self.addContactToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Resources/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addContactToolButton.setIcon(icon4)
        self.addContactToolButton.setIconSize(QtCore.QSize(28, 28))
        self.addContactToolButton.setObjectName("addContactToolButton")
        self.chatList = QtWidgets.QListWidget(self.frame_2)
        self.chatList.setGeometry(QtCore.QRect(0, 150, 316, 541))
        self.chatList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chatList.setObjectName("chatList")
        self.addGroupToolButton = QtWidgets.QToolButton(self.frame_2)
        self.addGroupToolButton.setGeometry(QtCore.QRect(120, 700, 71, 61))
        self.addGroupToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Resources/create_group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addGroupToolButton.setIcon(icon5)
        self.addGroupToolButton.setIconSize(QtCore.QSize(40, 40))
        self.addGroupToolButton.setObjectName("addGroupToolButton")
        self.logoutToolButton = QtWidgets.QToolButton(self.frame_2)
        self.logoutToolButton.setGeometry(QtCore.QRect(270, 10, 41, 41))
        self.logoutToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Resources/shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutToolButton.setIcon(icon6)
        self.logoutToolButton.setIconSize(QtCore.QSize(32, 32))
        self.logoutToolButton.setObjectName("logoutToolButton")
        self.confirmGroupToolButton = QtWidgets.QToolButton(self.frame_2)
        self.confirmGroupToolButton.setEnabled(True)
        self.confirmGroupToolButton.setGeometry(QtCore.QRect(220, 700, 51, 61))
        self.confirmGroupToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Resources/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirmGroupToolButton.setIcon(icon7)
        self.confirmGroupToolButton.setIconSize(QtCore.QSize(34, 34))
        self.confirmGroupToolButton.setObjectName("confirmGroupToolButton")
        self.cancelGroupToolButton = QtWidgets.QToolButton(self.frame_2)
        self.cancelGroupToolButton.setGeometry(QtCore.QRect(270, 700, 41, 61))
        self.cancelGroupToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Resources/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelGroupToolButton.setIcon(icon8)
        self.cancelGroupToolButton.setIconSize(QtCore.QSize(40, 40))
        self.cancelGroupToolButton.setObjectName("cancelGroupToolButton")
        self.groupNameText = QtWidgets.QLineEdit(self.frame_2)
        self.groupNameText.setGeometry(QtCore.QRect(20, 710, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupNameText.setFont(font)
        self.groupNameText.setStyleSheet("border-radius: 20px;\n"
"padding-left: 10px;\n"
"padding-right: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.groupNameText.setText("")
        self.groupNameText.setObjectName("groupNameText")
        self.chatList.raise_()
        self.line.raise_()
        self.userIconButton.raise_()
        self.userLabel.raise_()
        self.searchContactLabel.raise_()
        self.addContactToolButton.raise_()
        self.addGroupToolButton.raise_()
        self.logoutToolButton.raise_()
        self.confirmGroupToolButton.raise_()
        self.cancelGroupToolButton.raise_()
        self.groupNameText.raise_()
        self.sendBarFrame = QtWidgets.QFrame(Form)
        self.sendBarFrame.setEnabled(True)
        self.sendBarFrame.setGeometry(QtCore.QRect(310, 710, 721, 61))
        self.sendBarFrame.setStyleSheet("")
        self.sendBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sendBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sendBarFrame.setObjectName("sendBarFrame")
        self.removeMediaToolButton = QtWidgets.QToolButton(self.sendBarFrame)
        self.removeMediaToolButton.setEnabled(False)
        self.removeMediaToolButton.setGeometry(QtCore.QRect(53, 30, 31, 31))
        self.removeMediaToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Resources/cancel_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeMediaToolButton.setIcon(icon9)
        self.removeMediaToolButton.setIconSize(QtCore.QSize(20, 20))
        self.removeMediaToolButton.setObjectName("removeMediaToolButton")
        self.sendToolButton = QtWidgets.QToolButton(self.sendBarFrame)
        self.sendToolButton.setGeometry(QtCore.QRect(640, 10, 41, 41))
        self.sendToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.sendToolButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Resources/send3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendToolButton.setIcon(icon10)
        self.sendToolButton.setIconSize(QtCore.QSize(50, 50))
        self.sendToolButton.setObjectName("sendToolButton")
        self.mediaToolButton = QtWidgets.QToolButton(self.sendBarFrame)
        self.mediaToolButton.setGeometry(QtCore.QRect(10, 0, 51, 61))
        self.mediaToolButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.mediaToolButton.setText("")

        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Resources/OpenCamera1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mediaToolButton.setIcon(icon11)
        self.mediaToolButton.setIconSize(QtCore.QSize(50, 50))
        self.mediaToolButton.setAutoRaise(False)
        self.mediaToolButton.setObjectName("mediaToolButton")
        self.messageText = QtWidgets.QLineEdit(self.sendBarFrame)
        self.messageText.setGeometry(QtCore.QRect(90, 10, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageText.setFont(font)
        self.messageText.setStyleSheet("border-radius: 20px;\n"
"padding-left: 10px;\n"
"padding-right: 40px;\n"
"background-color: rgb(255, 255, 255);")
        self.messageText.setText("")
        self.messageText.setObjectName("messageText")
        self.mediaToolButton.raise_()
        self.messageText.raise_()
        self.sendToolButton.raise_()
        self.removeMediaToolButton.raise_()
        self.headerChatFrame.raise_()
        self.sendBarFrame.raise_()
        self.messagesList.raise_()
        self.frame_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelStatus.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:normal; color:#7e7e7e;\">online now</span></p></body></html>"))
        self.labelChatName.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:400;\">Christian Cavallo</span></p></body></html>"))
        self.userLabel.setText(_translate("Form", "Noemi Buggea"))
        self.searchContactLabel.setPlaceholderText(_translate("Form", "Search a new contact by email..."))
        self.addContactToolButton.setText(_translate("Form", "..."))
        self.addGroupToolButton.setText(_translate("Form", "..."))
        self.logoutToolButton.setText(_translate("Form", "..."))
        self.confirmGroupToolButton.setText(_translate("Form", "..."))
        self.cancelGroupToolButton.setText(_translate("Form", "..."))
        self.groupNameText.setPlaceholderText(_translate("Form", "Group\'s name..."))
        self.removeMediaToolButton.setText(_translate("Form", "..."))
        self.messageText.setPlaceholderText(_translate("Form", "Write a message..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
