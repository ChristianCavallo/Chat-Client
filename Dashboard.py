# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Dashboard(object):
    def setupUi(self, Dialog_Dashboard):
        Dialog_Dashboard.setObjectName("Dialog_Dashboard")
        Dialog_Dashboard.resize(587, 392)
        self.label = QtWidgets.QLabel(Dialog_Dashboard)
        self.label.setGeometry(QtCore.QRect(210, 160, 211, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Dashboard)

    def retranslateUi(self, Dialog_Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Dashboard.setWindowTitle(_translate("Dialog_Dashboard", "Dialog"))
        self.label.setText(_translate("Dialog_Dashboard", "Programma strano"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Dashboard = QtWidgets.QDialog()
    ui = Ui_Dialog_Dashboard()
    ui.setupUi(Dialog_Dashboard)
    Dialog_Dashboard.show()
    sys.exit(app.exec_())
