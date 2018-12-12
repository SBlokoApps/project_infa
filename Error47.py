# -*- coding: utf-8 -*-
# Version 1.1
# Form implementation generated from reading ui file 'Error#47.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.B_OK = QtWidgets.QDialogButtonBox(Dialog)
        self.B_OK.setGeometry(QtCore.QRect(30, 180, 211, 32))
        self.B_OK.setOrientation(QtCore.Qt.Horizontal)
        self.B_OK.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.B_OK.setObjectName("B_OK")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 271, 101))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.B_OK.rejected.connect(Dialog.reject)
        self.B_OK.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ОШИБКА"))
        self.label_2.setText(_translate("Dialog", "№47"))
