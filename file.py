# -*- coding: utf-8 -*-
# Version 1.31
# Form implementation generated from reading ui file 'proj1_1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(10, 0, 791, 91))
        self.columnView_2.setObjectName("columnView_2")
        # Сначала делаются кнопки
        self.copy = QtWidgets.QPushButton(self.centralwidget) # Копировать
        self.copy.setGeometry(QtCore.QRect(30, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        self.move = QtWidgets.QPushButton(self.centralwidget) # Переместить
        self.move.setGeometry(QtCore.QRect(30, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.move.setFont(font)
        self.move.setObjectName("move")
        self.dele = QtWidgets.QPushButton(self.centralwidget) # Удалить
        self.dele.setGeometry(QtCore.QRect(280, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.dele.setFont(font)
        self.dele.setObjectName("dele")
        self.open = QtWidgets.QPushButton(self.centralwidget) # Переместить
        # Да, название переводится "Открыть", но так получилось
        self.open.setGeometry(QtCore.QRect(570, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.open.setFont(font)
        self.open.setObjectName("open")
        self.cmd = QtWidgets.QPushButton(self.centralwidget) # Открыть cmd
        self.cmd.setGeometry(QtCore.QRect(610, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.cmd.setFont(font)
        self.cmd.setObjectName("cmd")
        self.new_dir = QtWidgets.QPushButton(self.centralwidget) # Новая папка
        self.new_dir.setGeometry(QtCore.QRect(230, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.new_dir.setFont(font)
        self.new_dir.setObjectName("new_dir")
        self.new_file = QtWidgets.QPushButton(self.centralwidget) # Новый файл
        self.new_file.setGeometry(QtCore.QRect(430, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.new_file.setFont(font)
        self.new_file.setObjectName("new_file")
        self.left_table = QtWidgets.QTableWidget(self.centralwidget) # Таблица
        # Слева
        self.left_table.setGeometry(QtCore.QRect(10, 130, 391, 421))
        self.left_table.setObjectName("left_table")
        self.left_table.setColumnCount(0)
        self.left_table.setRowCount(0)
        self.right_table = QtWidgets.QTableWidget(self.centralwidget)
        # Таблица справа
        self.right_table.setGeometry(QtCore.QRect(410, 130, 391, 421))
        self.right_table.setObjectName("right_table")
        self.right_table.setColumnCount(0)
        self.right_table.setRowCount(0)
        self.n_left = QtWidgets.QPushButton(self.centralwidget) # Назад
        # У левой таблицы
        self.n_left.setGeometry(QtCore.QRect(10, 100, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.n_left.setFont(font)
        self.n_left.setObjectName("n_left")
        self.n_right = QtWidgets.QPushButton(self.centralwidget) # Назад
        # У правой таблицы
        self.n_right.setGeometry(QtCore.QRect(410, 100, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.n_right.setFont(font)
        self.n_right.setObjectName("n_right")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "InFA - Individual File Assistant"))
        self.copy.setText(_translate("MainWindow", "Копировать"))
        self.move.setText(_translate("MainWindow", "Переместить"))
        self.dele.setText(_translate("MainWindow", "Удалить"))
        self.open.setText(_translate("MainWindow", "Переименовать"))
        self.cmd.setText(_translate("MainWindow", "Открыть  CMD"))
        self.new_dir.setText(_translate("MainWindow", "Новая папка"))
        self.new_file.setText(_translate("MainWindow", "Новый файл"))
        self.n_left.setText(_translate("MainWindow", ".....НАЗАД....."))
        self.n_right.setText(_translate("MainWindow", ".....НАЗАД....."))
