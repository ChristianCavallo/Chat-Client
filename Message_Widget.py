# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Message_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowMedia(object):
    def setupUi(self, ShowMedia):
        ShowMedia.setObjectName("ShowMedia")
        ShowMedia.setWindowModality(QtCore.Qt.WindowModal)
        ShowMedia.resize(806, 554)
        ShowMedia.setMinimumSize(QtCore.QSize(806, 554))
        ShowMedia.setMaximumSize(QtCore.QSize(806, 554))
        self.verticalLayoutWidget = QtWidgets.QWidget(ShowMedia)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 110, 271, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton.setMaximumSize(QtCore.QSize(50, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ShowMedia)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 210, 171, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.toolButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/download_media.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_2.addWidget(self.toolButton_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.retranslateUi(ShowMedia)
        QtCore.QMetaObject.connectSlotsByName(ShowMedia)

    def retranslateUi(self, ShowMedia):
        _translate = QtCore.QCoreApplication.translate
        ShowMedia.setWindowTitle(_translate("ShowMedia", "Form"))
        self.toolButton.setText(_translate("ShowMedia", "..."))
        self.label.setText(_translate("ShowMedia", "Christian Cavallo"))
        self.label_2.setText(_translate("ShowMedia", "10"))
        self.toolButton_2.setText(_translate("ShowMedia", "..."))
        self.label_3.setText(_translate("ShowMedia", "Get Media!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowMedia = QtWidgets.QWidget()
    ui = Ui_ShowMedia()
    ui.setupUi(ShowMedia)
    ShowMedia.show()
    sys.exit(app.exec_())
