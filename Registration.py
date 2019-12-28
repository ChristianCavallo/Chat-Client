# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import time
from PyQt5 import QtCore, QtGui, QtWidgets
from events import Events

ut =[]

class Ui_Dialog_Registration(object):

    def setupUi(self, Dialog_Registration):
        self.events = Events(("onRegistrationDone")) #Registro l'evento "onRegistrationDone" (a registrazione finita)
        Dialog_Registration.setObjectName("Dialog_Registration")
        Dialog_Registration.resize(546, 401)
        self.widget = QtWidgets.QWidget(Dialog_Registration)
        self.widget.setGeometry(QtCore.QRect(180, 90, 189, 207))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2_surname = QtWidgets.QLabel(self.widget)
        self.label_2_surname.setObjectName("label_2_surname")
        self.horizontalLayout_2.addWidget(self.label_2_surname)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.lineEdit_surname = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.horizontalLayout_2.addWidget(self.lineEdit_surname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_nickname = QtWidgets.QLabel(self.widget)
        self.label_nickname.setObjectName("label_nickname")
        self.horizontalLayout_6.addWidget(self.label_nickname)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.lineEdit_nickname = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_nickname.setObjectName("lineEdit_nickname")
        self.horizontalLayout_6.addWidget(self.lineEdit_nickname)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_password = QtWidgets.QLabel(self.widget)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_4.addWidget(self.label_password)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_4.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_email = QtWidgets.QLabel(self.widget)
        self.label_email.setObjectName("label_email")
        self.horizontalLayout_5.addWidget(self.label_email)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_5.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.pushButton_SingUp = QtWidgets.QPushButton(self.widget)
        self.pushButton_SingUp.setObjectName("pushButton_SingUp")
        self.verticalLayout.addWidget(self.pushButton_SingUp)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)

        self.retranslateUi(Dialog_Registration)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Registration)

        # Collegamenti: Azioni con bottoni
        self.dialog = Dialog_Registration #Riferimento alla finestra di dialog
        self.pushButton_SingUp.clicked.connect(self.disperazione)


    def retranslateUi(self, Dialog_Registration):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Registration.setWindowTitle(_translate("Dialog_Registration", "Dialog"))
        self.label_name.setText(_translate("Dialog_Registration", "Name"))
        self.label_2_surname.setText(_translate("Dialog_Registration", "Surname"))
        self.label_nickname.setText(_translate("Dialog_Registration", "nickname"))
        self.label_password.setText(_translate("Dialog_Registration", "Password"))
        self.label_email.setText(_translate("Dialog_Registration", "Email"))
        self.pushButton_SingUp.setText(_translate("Dialog_Registration", "Sing up"))



    def disperazione(self):
        #questo funziona xk ho provato a stamparli e li stampa corretti ma come passo il vettore ut nel main per mandarlo?
        ut.append(self.lineEdit_name.text())
        ut.append(self.lineEdit_surname.text())
        ut.append(self.lineEdit_nickname.text())
        ut.append(self.lineEdit_email.text())
        ut.append(self.lineEdit_password.text())
        print(ut[0])
        message = {"id" : 10,
                   "name" :self.lineEdit_name.text() } # ecc ecc
        self.events.onRegistrationDone(message) #Richiamo l'evento passando anche un messaggio. Ci sei fino a qui?si

        #time.sleep(1)  # Delays for 5 seconds. You can also use a float value.
        #self.dialog.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Registration = QtWidgets.QDialog()
    ui = Ui_Dialog_Registration()
    ui.setupUi(Dialog_Registration)
    Dialog_Registration.show()
    sys.exit(app.exec_())
